from django.http import HttpResponse

ICE_CREAM = chr(127846)


def ice_cream_detail(request, pk):
    return HttpResponse(f'Мороженое номер {pk}')


def ice_cream_list(request):
    return HttpResponse(f'Каталог мороженого')