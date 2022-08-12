from django.http import HttpResponse, Http404, StreamingHttpResponse, FileResponse, JsonResponse
from django.shortcuts import render
from django.template.loader import get_template

from service.models import Product


def index(request):
    # template = get_template('index.html')
    return render(request, 'index.html')


def page(request, page_num):
    return HttpResponse(f'Page {page_num}')


def about(request, id):
    # a = int(request.GET.get('a'))
    # b = int(request.GET.get('b'))

    # return HttpResponse(HttpResponse(f'{request.scheme}').status_code)
    try:
        Product.objects.get(pk=id)
    except Product.DoesNotExist:
        raise Http404('NOT FOUND')

    return HttpResponse('OK')


def file_show(request):
    file = 'service/Screenshot_2022.01.13_20.44.34.956.png'
    return FileResponse(open(file, 'rb'))


def json_show(request):
    data = {'cost': 14, 'title': 'book'}
    return JsonResponse(data)
