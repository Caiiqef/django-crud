from django.shortcuts import render, redirect
from user.forms import UsuarioForm
from user.models import Usuario

def usr(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = UsuarioForm()
    return render(request, 'index.html', {'form':form})

def show(request):
    usuarios = Usuario.objects.all()
    return render(request, "show.html", {'usuarios':usuarios})

# def edit(request, teste):
#     usuario = Usuario.objects.user_id(teste=teste)
#     return render(request, 'edit.html', {'usuario':usuario})

def update(request, user_id):
    usuario = Usuario.objects.get(id=user_id)
    form = UsuarioForm(request.POST, instance = usuario)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'usuario':usuario})

def destroy(request, user_id):
    usuario = Usuario.objects.get(id=user_id)
    usuario.delete()
    return redirect("/show")