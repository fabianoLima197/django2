from django.shortcuts import render

# Create your views here.
def index(reguest):
    return render(reguest, 'index.html')

def contato(request):
    form = ContatoForm()

    context = {
        'form': form
    }
    return render(request, 'contato.html', context)

def produto(request):
    return render(request, 'produto.html')

