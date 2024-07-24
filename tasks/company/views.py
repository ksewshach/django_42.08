from django.shortcuts import render

# Create your views here.

def main(request):
        return render(request=request, template_name='company/main.html')


def contacts(request):
        return render(request=request, template_name='company/contacts.html')


def about_company(request):
        return render(request=request, template_name='company/about_company.html')


def management_company(request):
        return render(request=request, template_name='company/management_company.html')


def news(request):
        return render(request=request, template_name='company/news.html')

