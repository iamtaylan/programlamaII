from django.contrib import admin
from acıktın.models import *

# Register your models here.

class RestoranAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',) }
    list_filter = ('genres','language',)
    search_fields = ('title','description',)

class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name','gender','duty_type')
    list_filter = ('gender','duty_type')
    search_fields = ('first_name','last_name')

admin.site.register(Restoran, RestoranAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Contact)
admin.site.register(Genre)
admin.site.register(Video)
