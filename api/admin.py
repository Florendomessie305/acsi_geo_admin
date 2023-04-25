from django.contrib import admin

from api.models import *


# Register your models here.
class CategorieAdmin(admin.ModelAdmin):
    fields = ['nom_categorie', 'description']
    list_display = ('nom_categorie', 'description')
    list_per_page = 8


admin.site.register(CategorieCimetiere, CategorieAdmin)


class LocaliteAdmin(admin.ModelAdmin):
    fields = ['nom_localite', 'superficie', 'description']
    list_display = ('nom_localite', 'superficie', 'description')
    search_fields = ['nom_localite']
    list_per_page = 8


admin.site.register(Localite, LocaliteAdmin)


class CimetiereAdmin(admin.ModelAdmin):
    fields = ['nom_cimetiere', 'superficie', 'categorie', 'localite']
    list_display = ('nom_cimetiere', 'superficie', 'categorie', 'localite')
    search_fields = ['nom_cimetiere']
    list_filter = ['categorie', 'localite']
    list_per_page = 8


admin.site.register(Cimetiere, CimetiereAdmin)


class TombeAdmin(admin.ModelAdmin):
    fields = ['numero_tombe', 'lat', 'lon', 'cimetiere']
    list_display = ('numero_tombe', 'lat', 'lon', 'cimetiere')
    search_fields = ['numero_tombe']
    list_filter = ['cimetiere']
    list_per_page = 100


admin.site.register(Tombe, TombeAdmin)


# Admin gestion des dufun
class DefunAdmin(admin.ModelAdmin):
    fields = ['matricule', 'nom', 'prenom', 'genre', 'nationalite', 'date_naiss',
              'date_deces', 'date_inhumation', 'statut', 'tombe']

    list_display = ('nom', 'prenom', 'genre', 'nationalite',
                    'date_naiss', 'date_deces', 'date_inhumation', 'tombe', 'statut')
    search_fields = ['nom', 'prenom', 'matricule', 'date_deces']
    list_filter = ['statut', 'date_deces', 'date_inhumation']
    list_per_page = 100


admin.site.register(Defunt, DefunAdmin)


class ExhumationAdmin(admin.ModelAdmin):
    fields = ['date_exhumation', 'last_cimetiere',
              'new_cimetiere', 'defunt']
    list_display = ('date_exhumation', 'last_cimetiere',
                    'new_cimetiere', 'defunt')
    search_fields = ['date_exhumation']
    list_per_page = 100


admin.site.register(Exhumation, ExhumationAdmin)
