from django.db import models
from django import forms
from django.core.urlresolvers import reverse

# Create your models here.
from django.forms.models import ModelForm


class Evento(models.Model):
    CATEGORIAS_CHOICES = (
        ('CONF', 'Conferencia'),
        ('SEMI', 'Seminario'),
        ('CONG', 'Congreso'),
        ('CURS', 'Curso')
    )
    MODALIDADES_CHOICES = (
        ('P', 'Presencial'),
        ('V', 'Virtual')
    )
    txt_evento = models.CharField(max_length=200, verbose_name='Nombre', help_text='Nombre del evento')
    ind_categoria = models.CharField(
        max_length=4,
        choices=CATEGORIAS_CHOICES
    )
    txt_lugar = models.CharField(max_length=100, verbose_name='Lugar', help_text='Lugar')
    txt_direccion = models.CharField(max_length=100, verbose_name='Dirección', help_text='Dirección')
    fec_inicio = models.DateField(auto_now_add=False, help_text='Fecha de inicio')
    fec_final = models.DateField(auto_now_add=False, help_text='Fecha de final')
    ind_modalidad = models.CharField(
        max_length=1,
        choices=MODALIDADES_CHOICES
    )

    def get_absolute_url(self):
        return reverse('edit_evento', kwargs={'pk': self.pk})


class EventoForm(ModelForm):
    class Meta:
        model = Evento
        fields = ['txt_evento', 'ind_categoria', 'txt_lugar', 'txt_direccion', 'fec_inicio', 'fec_final', 'ind_modalidad']
        labels = {'txt_evento': 'Evento', 'ind_categoria': 'Categoria', 'txt_lugar': 'Lugar', 'txt_direccion' : 'Dirección', 'fec_inicio': 'Fecha Inicial', 'fec_final':'Fecha Final', 'ind_modalidad': 'Modalidad'}
        widgets = {'txt_evento': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '200'}),
                   'txt_lugar': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '100'}),
                   'txt_direccion': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '100'}),}