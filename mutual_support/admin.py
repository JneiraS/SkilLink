from django.contrib import admin

# Register your models here.


from .models import Competence
from .models import Profile
from .models import Creneau


admin.site.register(Competence)
admin.site.register(Profile)
admin.site.register(Creneau)

