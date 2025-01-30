from django.contrib import admin
from .models import Personne, Experience, Formation, Competence, Langue, CV, Loisir, Contact

@admin.register(CV)
class CVAdmin(admin.ModelAdmin):
    # Champs affichés dans la liste des CVs
    list_display = ['title', 'personne', 'user', 'design']
    # Champs pour filtrer
    list_filter = ['design']
    # Champs éditables directement depuis la liste
    list_editable = ['design']
    # Champs de recherche
    search_fields = ['title', 'personne__nom', 'personne__prenom']

# Enregistrement des autres modèles sans personnalisation
admin.site.register(Personne)
admin.site.register(Experience)
admin.site.register(Formation)
admin.site.register(Competence)
admin.site.register(Langue)
admin.site.register(Loisir)

# Enregistrer le modèle Contact
admin.site.register(Contact)
