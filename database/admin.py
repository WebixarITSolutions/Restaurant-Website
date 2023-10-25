from django.contrib import admin

from database.models import Contactd
from database.models import Feedbackd
from database.models import Reserved

class ContactAdmin(admin.ModelAdmin):

    list_display=('name','email','data')
admin.site.register(Contactd,ContactAdmin)

class FeedbackAdmin(admin.ModelAdmin):

    list_display=('name1','email1','num','feed')
admin.site.register(Feedbackd,FeedbackAdmin)

class ReservedAdmin(admin.ModelAdmin):

    list_display=('fname','lname','uname1','email2','num1','Time')
admin.site.register(Reserved,ReservedAdmin)
