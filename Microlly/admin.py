from django.contrib import admin
from Microlly.models import *

class PublicationAdmin(admin.ModelAdmin):
	list_display = ('title', )
	search_fields = ('title', )

admin.site.register(Publication, PublicationAdmin)

