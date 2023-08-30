from django.contrib import admin
from Report.models import School,Student,Dropout

admin.site.register([School,Student,Dropout])
admin.site.site_header='Control Panel'
