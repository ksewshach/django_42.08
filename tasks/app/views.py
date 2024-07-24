from django.shortcuts import render, HttpResponse
from app.datetime_func import show_date_time

# Create your views here.

def render_index_page(request):
    return render(request=request, template_name='index.html')

def show_time(request): # С созданием хтмл-ки
    show_date_time()
    return render(request=request, template_name='datetime.html')

def show_quote(request): # Тут реализация прямо здесь, без создания хтмл-ки
    if request.method == 'GET':
        quotes = [
            'Ученье – свет. А неученье – тень.',
            'Для всех хорошим не будешь. Будь собой.',
            'Никто не ценит того, чего слишком много.',
            'Улыбайся, не доставляй беде удовольствия.',
        ]
        import random
        return HttpResponse(random.choice(quotes))