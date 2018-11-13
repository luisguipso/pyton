from django.contrib import admin
#importar os modelos
from .models import *

# Register your models here.
admin.site.register(Cidade)
admin.site.register(Pessoa)
