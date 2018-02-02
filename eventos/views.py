from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, get_object_or_404

from eventos.models import Evento, EventoForm


def index(request):
    list_eventos = Evento.objects.all()
    context = {'list_eventos': list_eventos}
    return render(request, 'eventos/index.html', context)

def add_evento(request):
    if request.method == 'POST' :
        form = EventoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

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
