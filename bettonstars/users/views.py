from django.http import HttpResponse


# Страница со списком пользователей
def users_list(request):
    return HttpResponse('Список пользователей')


# Страница с информацией об одном пользователе;
# view-функция принимает параметр pk из path()
def users_detail(request, pk):
    return HttpResponse(f'Пользователь номер {pk}')
