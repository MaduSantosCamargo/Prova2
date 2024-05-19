from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def producao(request):
    return render(request, 'producao.html')

def engenharia(request):
    return render(request, 'engenharia.html')

def controle_qualidade(request):
    return render(request, 'controle_qualidade.html')

def expedicao(request):
    return render(request, 'expedicao.html')