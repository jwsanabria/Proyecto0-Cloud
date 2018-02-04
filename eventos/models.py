from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.forms import forms
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
    fec_creacion = models.DateTimeField(auto_now_add=True, blank=True)
    user = models.ForeignKey(User, null=True)

    def get_absolute_url(self):
        return reverse('edit_evento', kwargs={'pk': self.pk})


class DateInput(forms.DateInput):
    input_type = 'date'


class EventoForm(ModelForm):
    class Meta:
        model = Evento
        fields = ['txt_evento', 'ind_categoria', 'txt_lugar', 'txt_direccion', 'fec_inicio', 'fec_final', 'ind_modalidad']
        labels = {'txt_evento': 'Evento', 'ind_categoria': 'Categoria', 'txt_lugar': 'Lugar', 'txt_direccion' : 'Dirección', 'fec_inicio': 'Fecha Inicial', 'fec_final':'Fecha Final', 'ind_modalidad': 'Modalidad'}
        widgets = {'txt_evento': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '200'}),
                   'txt_lugar': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '100'}),
                   'txt_direccion': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '100'}),
                   'fec_inicio': DateInput(),
                   'fec_final' : DateInput(),}

class UserForm(ModelForm):
    #username = forms.CharField(max_length=50)
    #first_name = forms.CharField(max_length=20)
    #last_name = forms.CharField(max_length=20)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        #fields = ['username', 'first_name', 'last_name', 'email', 'password', 'password2']
        fields = ['email', 'password', 'password2']

    #def clean_username(self):
    #    username = self.cleaned_data['username']
    #    if User.objects.filter(username=username):
    #        raise forms.ValidationError('Nombre de usuario ya registrado')
    #    return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email):
            raise forms.ValidationError('Ya existe un usuario con el mismo email')
        return email

    def clean_password2(self):
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password!=password2:
            raise forms.ValidationError('Las claves no coinciden')
        return password2