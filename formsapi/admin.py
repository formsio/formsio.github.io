from django.contrib import admin
from .models import User,Form,Question,Answer,Response

# Register your models here.
admin.site.register(User)
admin.site.register(Form)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Response)

