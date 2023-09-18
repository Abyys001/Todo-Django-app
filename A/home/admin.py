from django.contrib import admin

"""
for register any model:

1. improt model form your model file in this app
2. register it: admin.site.registet(ModelName)

"""


# local models 
from .models import (
    Todo, 
)


admin.site.register(Todo)
