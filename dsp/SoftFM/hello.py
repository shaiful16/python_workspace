
import types
import numpy
import numpy.fft
import numpy.linalg
import numpy.random
import scipy.signal



def lazyRawSamples(fname, blocklen):
    """Return generator over blocks of raw samples."""

    f = open(fname, 'rb')
    while 1:
        d = f.read(2 * blocklen)
        if len(d) < 2 * blocklen:
            break
        d = numpy.fromstring(d, dtype=numpy.uint8)
        d = d.astype(numpy.float64)
        d = (d - 128) / 128.0
        yield d[::2] + 1j * d[1::2]


def freqShiftIQ(d, freqshift):
    """Shift frequency by multiplication with complex phasor."""
    def g(d, freqshift):
        p = 0
        for b in d:
            n = len(b)
            w = numpy.exp((numpy.arange(n) + p) * (2j * numpy.pi * freqshift))
            p += n
            yield b * w

    if isinstance(d, types.GeneratorType):
        return g(d, freqshift)
    else:
        n = len(d)
        w = numpy.exp(numpy.arange(n) * (2j * numpy.pi * freqshift))
        return d * w



def firFilter(d, coeff):
    """Apply FIR filter to sample stream."""

    # lazy version
    def g(d, coeff):
        prev = None
        for b in d:
            if prev is None:
                yield scipy.signal.lfilter(coeff, 1, b)
                prev = b
            else:
                k = min(len(prev), len(coeff))
                x = numpy.concatenate((prev[-k:], b))
                y = scipy.signal.lfilter(coeff, 1, x)
                yield y[k:]
                if len(coeff) > len(b):
                    prev = x
                else:
                    prev = b

    if isinstance(d, types.GeneratorType):
        return g(d, coeff)
    else:
        return scipy.signal.lfilter(coeff, 1, d)


def quadratureDetector(d, fs):
    """FM frequency detector based on quadrature demodulation.
    Return an array of real-valued numbers, representing frequencies in Hz."""

    k = fs / (2 * numpy.pi)

    # lazy version
    def g(d):
        prev = None
        for b in d:
            if prev is not None:
                x = numpy.concatenate((prev[1:], b[:1]))
                yield numpy.angle(x * prev.conj()) * k
            prev = b
        yield numpy.angle(prev[1:] * prev[:-1].conj()) * k

    if isinstance(d, types.GeneratorType):
        return g(d)
    else:
        return numpy.angle(d[1:] * d[:-1].conj()) * k


def spectrum(d, fs=1, nfft=None, sortfreq=False):
    """Calculate Welch-style power spectral density.

    fs       :: sample rate, default to 1
    nfft     :: FFT length, default to block length
    sortfreq :: True to put negative freqs in front of positive freqs

    Use Hann window with 50% overlap.

    Return (freq, Pxx)."""

    if not isinstance(d, types.GeneratorType):
        d = [ d ]

    prev = None

    if nfft is not None:
        assert nfft > 0
        w = numpy.hanning(nfft)
        q = numpy.zeros(nfft)

    pos = 0
    i = 0
    for b in d:

        if nfft is None:
            nfft = len(b)
            assert nfft > 0
            w = numpy.hanning(nfft)
            q = numpy.zeros(nfft)

        while pos + nfft <= len(b):

            if pos < 0:
                t = numpy.concatenate((prev[pos:], b[:pos+nfft]))
            else:
                t = b[pos:pos+nfft]

            t *= w
            tq = numpy.fft.fft(t)
            tq *= numpy.conj(tq)
            q += numpy.real(tq)

            del t
            del tq

            pos += (nfft+(i%2)) // 2
            i += 1

        pos -= len(b)
        if pos + len(b) > 0:
            prev = b
        else:
            prev = numpy.concatenate((prev[pos+len(b):], b))

    if i > 0:
        q /= (i * numpy.sum(numpy.square(w)) * fs)

    f = numpy.arange(nfft) * (fs / float(nfft))
    f[nfft//2:] -= fs

    if sortfreq:
        f = numpy.concatenate((f[nfft//2:], f[:nfft//2]))
        q = numpy.concatenate((q[nfft//2:], q[:nfft//2]))

    return f, q



graw = lazyRawSamples('hello.dat', 1000000)
gtune = freqShiftIQ(graw, 0.25)
bfir = scipy.signal.firwin(20, 0.2, window='nuttall')
gfilt = firFilter(gtune, bfir)
gbase = quadratureDetector(gfilt, fs=1.0e6)
spectrum(gbase, fs=1.0e6)