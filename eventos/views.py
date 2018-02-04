from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, get_object_or_404

from eventos.models import Evento, EventoForm, UserForm


def index(request):
    if request.user.is_authenticated():
        list_eventos = Evento.objects.all().order_by('-fec_creacion').filter(user=request.user)
    else:
        list_eventos = None
    context = {'list_eventos': list_eventos}
    return render(request, 'eventos/index.html', context)

def add_evento(request):
    if request.method == 'POST' :
        form = EventoForm(request.POST, request.FILES)
        if form.is_valid():
            new_evento = Evento(txt_evento=request.POST.get('txt_evento'),
                                txt_direccion=request.POST.get('txt_direccion'),
                                ind_categoria=request.POST.get('ind_categoria'),
                                txt_lugar= request.POST.get('txt_lugar'),
                                fec_inicio=request.POST.get('fec_inicio'),
                                fec_final=request.POST.get('fec_final'),
                                ind_modalidad=request.POST.get('ind_modalidad'),
                                user=request.user)
            new_evento.save()

            return HttpResponseRedirect(reverse('eventos:index'))

    else:
        form = EventoForm()

    return render(request, 'eventos/evento_form.html', {'form':form})


def edit_eventoj(request):
    if request.method == 'POST':
        evento_id = request.POST.get('evento_id')
        evento = Evento.objects.filter(ind_estado=True).get(pk=evento_id)
        evento.txt_evento = request.POST.get('edit_nombre_evento')
        evento.txt_direccion = request.POST.get('edit_direccion_evento')
        evento.txt_lugar = request.POST.get('edit_lugar_evento')
        evento.ind_categoria = request.POST.get('edit_categoria_evento')
        evento.ind_modalidad = request.POST.get('edit_modalidad_evento')
        evento.fec_inicio = request.POST.get('edit_inicio_evento')
        evento.fec_final = request.POST.get('edit_final_evento')
        evento.save()

        return HttpResponseRedirect(reverse('eventos:index'))

    else:
        form = EventoForm()
        evento_id = request.GET.get('evento_id')
        evento = Evento.objects.filter(ind_estado=True).get(pk=evento_id)
        form.data(Evento)
        return render(request, 'eventos/evento_form.html', {'form': form})


def evento_update(request, pk, template_name='eventos/evento_form.html'):
    evento = get_object_or_404(Evento, pk=pk)
    form = EventoForm(request.POST or None, instance=evento)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('eventos:index'))
    return render(request, template_name, {'form': form})

def evento_delete(request, pk, template_name='eventos/evento_confirm_delete.html'):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method=='POST':
        evento.delete()
        return redirect('eventos:index')
    return render(request, template_name, {'object':evento})


def add_user_view(request):
    if request.method=='POST':
        form = UserForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            #username = cleaned_data.get('username')
            email = cleaned_data.get('email')
            #first_name = cleaned_data.get('first_name')
            #last_name = cleaned_data.get('last_name')
            password = cleaned_data.get('password')

            user_model = User.objects.create_user(username=email, password=password)
            #user_model.first_name = first_name
            #user_model.last_name = last_name
            user_model.email = email
            user_model.save()

            return HttpResponseRedirect(reverse('eventos:index'))
    else:
        form = UserForm()

    context = {'form':form}
    return render(request, 'eventos/registro.html', context)


def login_view(request):
    if request.user.is_authenticated():
        return redirect(reverse('eventos:index'))

    mensaje = ''

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None :
            login(request, user)
            return redirect(reverse('eventos:index'))
        else:
            mensaje ='Nombre de usuario o clave no válido'

    return render(request, 'eventos/login.html', {'mensaje':mensaje})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('eventos:index'))