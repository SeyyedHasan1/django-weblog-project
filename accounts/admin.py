from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .froms import CustomCreationForm,CustomChangeForm
from .models import CustomUser
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form=CustomCreationForm   #add a new admin(form)
    form=CustomChangeForm       #change(edit & update) an admin(form)
    model=CustomUser
    list_display=['username','email','age','is_staff']
    fieldsets=UserAdmin.fieldsets + (       #set the age model in panel admin when login
        (None,{'fields':('age',)}),
    )

    add_fieldsets=UserAdmin.fieldsets + (    #set the age model in panel admin when signup
        (None,{'fields':('age',)}),
    )


admin.site.register(CustomUser,CustomUserAdmin) #register
