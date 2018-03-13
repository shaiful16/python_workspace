from django.http import HttpResponse
import json

def index(request):
    return HttpResponse("Hello, world. You're at the hridoy index.")


def getInfo(request):
    print(request)
    return HttpResponse("Hello, world. You're at the hridoy index.")


def myview(request):
    if request.method == 'POST':
        print('POST')
        print(request.body)
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        print(body)
        id = body['id']
        print(id)

    dict = {'status': 'success', 'id': 123}
    return HttpResponse(json.dumps(dict))


'''
student object
{
	"id":2,
	"name":"hridoy",
	"age":28
}


[
    {
        "id":1,
        "name":"hiya",
        "age":20
    },
    {
        "id":2,
        "name":"hridoy",
        "age":28
    }
]

'''