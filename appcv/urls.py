from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.trombinoscope, name='trombinoscope'),

    path('create_personne/', views.create_or_edit_personne, name='create_personne'),
    path('boite/', views.boite, name='boite'),
    path('create_experience/', views.create_or_edit_experience, name='create_experience'),
    path('create_formation/', views.create_or_edit_formation, name='create_formation'),
    path('create_competence/', views.create_or_edit_competence, name='create_competence'),
    path('create_langue/', views.create_or_edit_langue, name='create_langue'),
    path('create_loisir/', views.create_or_edit_loisir, name='create_loisir'),
    path('create_cv/', views.create_or_edit_cv, name='create_cv'),
    path('create_contact/', views.create_contact, name='create_contact'),
    path('view_cv/<int:cv_id>/', views.view_cv, name='view_cv'),
    
    # Ajoutez une route par défaut pour la page de formulaire d'authentification
    path('connexion', views.formulaire, name='formulaire'),
    
    # Réécrivez les routes pour créer ou éditer les autres tables
    path('create_or_edit_personne/', views.create_or_edit_personne, name='create_or_edit_personne'),
    path('boite/', views.boite, name='boite'),
    path('create_or_edit_experience/', views.create_or_edit_experience, name='create_or_edit_experience'),
    path('create_or_edit_formation/', views.create_or_edit_formation, name='create_or_edit_formation'),
    path('create_or_edit_competence/', views.create_or_edit_competence, name='create_or_edit_competence'),
    path('create_or_edit_langue/', views.create_or_edit_langue, name='create_or_edit_langue'),
    path('create_or_edit_loisir/', views.create_or_edit_loisir, name='create_or_edit_loisir'),
    path('create_or_edit_cv/', views.create_or_edit_cv, name='create_or_edit_cv'), 
    path('register/', views.register, name='register'),
    path('create_contact/', views.create_contact, name='create_contact'),






    path('view_experiences/', views.view_experiences, name='view_experiences'),
    path('view_formations/', views.view_formations, name='view_formations'),
    path('view_competences/', views.view_competences, name='view_competences'),
    path('view_langues/', views.view_langues, name='view_langues'),
    path('view_loisirs/', views.view_loisirs, name='view_loisirs'),
     # Personne
    path('view_personne/', views.view_personne, name='view_personne'),
    # Contact
    path('view_contact/', views.view_contact, name='view_contact'),
    # CVs
    path('view_cvs/', views.view_cvs, name='view_cvs'),

    path('trombinoscope/', views.trombinoscope, name='trombinoscope'),
    path('cv/<int:pk>/', views.cv_detail, name='cv_detail'),  # Vue pour afficher le CV
   # pour rediriger vers la vue qui permet de modifier
    path('cv/<int:cv_id>/edit/', views.edit_cv, name='edit_cv'),
# pour rediriger vers la vue qui permet de surprimer
    path('cv/<int:cv_id>/delete/', views.delete_cv, name='delete_cv'),
#liens pour envoyer par mail
    path("cv/<int:cv_id>/send_email/", views.send_cv_email, name="send_cv_email"),

]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
