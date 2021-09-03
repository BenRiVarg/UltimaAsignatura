from django.shortcuts import render,HttpResponse
from .models import MaterialesPractica
from .forms import MaterialesForm
from django.shortcuts import get_object_or_404
# Create your views here.



def principal(request):
    return render(request,"paginas/index.html")

def dash(request):
    registros=MaterialesPractica.objects.all()
    return render(request,"paginas/practicasDshbd.html",{'registros':registros})

def crear(request):
    if request.method=='POST':
        form= MaterialesForm(request.POST)
        if form.is_valid():   #Si los datos recibidos son correctos
            form.save()
            registros=MaterialesPractica.objects.all()
        return render(request,"paginas/practicasDshbd.html",{'registros':registros})
    return render(request,"paginas/crear.html")

def editar(request,id):
     practica = get_object_or_404(MaterialesPractica, id=id)
     if request.method=='POST':
        form = MaterialesForm(request.POST,instance=practica)
        #print(form)
        if form.is_valid():
            form.save()
            registros=MaterialesPractica.objects.all()
            return render(request,"paginas/practicasDshbd.html",{'registros':registros})
     return render(request,"paginas/editar.html",{'practica':practica})

def ver(request,id):
    practica = get_object_or_404(MaterialesPractica, id=id)
    
    return render(request,"paginas/ver.html",{'practica':practica})    


def borrar(request,id):
    practica=get_object_or_404(MaterialesPractica, id=id)
    practica.delete()
    registros=MaterialesPractica.objects.all()
    return render(request,"paginas/practicasDshbd.html",{'registros':registros})