from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Student)
admin.site.register(Class)
admin.site.register(Marks)
admin.site.register(Subject)
admin.site.register(Exams)