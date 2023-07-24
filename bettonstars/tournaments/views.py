from django.http import HttpResponse


# Главная страница
def index(request):    
    return HttpResponse('Главная страница')


# Страница со списком турниров
def tournaments_list(request):
    return HttpResponse('Список турниров')


# Страница с информацией об одном турнире;
# view-функция принимает параметр pk из path()
def tournaments_detail(request, pk):
    return HttpResponse(f'Турнир номер {pk}')
