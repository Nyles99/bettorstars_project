from django.http import HttpResponse
from django.shortcuts import render


# Главная страница
def index(request):
    # Адрес шаблона сохраним в переменную, это не обязательно, но удобно
    template = 'tournaments/index.html'
    # Строку, которую надо вывести на страницу, тоже сохраним в переменную
    title = 'Турниры для прогнозистов'
    # Словарь с данными принято называть context
    context = {
        # В словарь можно передать переменную
        'title': title,
        # А можно сразу записать значение в словарь. Но обычно так не делают
        'text': 'Главная страница',
    }
    # Третьим параметром передаём словарь context
    return render(request, template, context)


# Страница со списком турниров
def tournaments_list(request):
    template = 'tournaments/tournaments_list.html'
    title = 'Все турниры'
    context = {
        # В словарь можно передать переменную
        'title': title,
        # А можно сразу записать значение в словарь. Но обычно так не делают
        'text': 'Здесь должен быть список турниров!',
    }
    # Третьим параметром передаём словарь context
    return render(request, template, context)


# Страница с информацией об одном турнире;
# view-функция принимает параметр pk из path()
def tournaments_detail(request, pk):
    return HttpResponse(f'Турнир номер {pk}')
