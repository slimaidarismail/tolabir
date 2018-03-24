from django.contrib import admin

# Register your models here.
from tafaha.models import Test, Answer

admin.site.register(Test)
admin.site.register(Answer)