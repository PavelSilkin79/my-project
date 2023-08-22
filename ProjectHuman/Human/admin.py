from django.contrib import admin
from .models import Human, Profession

class HumanAdmin(admin.ModelAdmin):
    list_display = ('id', 'profession', 'name', 'surname', 'age', 'content', 'address', 'photo')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')
    list_filter = ('name', 'id')
    list_editable = ['profession']

class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


admin.site.register(Human, HumanAdmin)
admin.site.register(Profession, ProfessionAdmin)