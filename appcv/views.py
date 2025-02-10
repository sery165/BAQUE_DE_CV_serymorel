from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.mail import EmailMessage  # Import ajouté
from smtplib import SMTPException
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from .forms import (
    PersonneForm,
    ExperienceForm,
    FormationForm,
    CompetenceForm,
    LangueForm,
    ContactForm,
    CVForm,
    LoisirForm,
    CustomUserCreationForm
)
from .models import (
    Personne,
    Experience,
    Formation,
    Competence,
    Langue,
    Contact,
    CV,
    Loisir,
)
from django.contrib.auth.models import User


# Vue pour la page d'authentification de l'utilisateur.
# Si l'utilisateur est authentifié, on tente de récupérer ses informations personnelles.
def formulaire(request):
    error_message = None
    user_authenticated = False
    personne = None
    user_not_found = False  # Ajouter la variable pour indiquer si l'utilisateur est non trouvé

    if request.method == 'POST':
        username = request.POST.get('username')  # Récupérer le nom d'utilisateur
        password = request.POST.get('password')  # Récupérer le mot de passe

        # Authentifier l'utilisateur avec le nom d'utilisateur et le mot de passe
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # L'utilisateur est authentifié, connectez-le
            login(request, user)
            user_authenticated = True
            try:
                # Essayer de récupérer l'objet Personne associé à l'utilisateur
                personne = Personne.objects.get(user=user)
            except Personne.DoesNotExist:
                # Si l'utilisateur n'a pas d'objet Personne associé, gérer l'exception
                personne = None
                error_message = "Aucune information personnelle trouvée pour vous."
        else:
            # Si l'utilisateur n'est pas trouvé ou mot de passe incorrect
            error_message = "Mot de passe incorrect ou utilisateur non trouvé."
            user_not_found = True  # Utilisateur non trouvé

    return render(request, 'formulaire.html', {
        'error_message': error_message,
        'user_authenticated': user_authenticated,
        'personne': personne,
        'user_not_found': user_not_found,  # Passer la variable pour afficher le bouton
    })


# Vue pour créer ou modifier les informations personnelles de l'utilisateur
@login_required
def create_or_edit_personne(request):
    try:
        personne = Personne.objects.get(user=request.user)
    except Personne.DoesNotExist:
        personne = None

    if request.method == "POST":
        form = PersonneForm(request.POST, request.FILES, instance=personne)
        if form.is_valid():
            personne = form.save(commit=False)
            personne.user = request.user
            personne.save()
            return redirect("create_or_edit_experience")
    else:
        form = PersonneForm(instance=personne)

    return render(request, "create_personne.html", {"form": form})


def boite(request):
    try:
        personne = Personne.objects.get(user=request.user)
    except Personne.DoesNotExist:
        personne = None

    if request.method == "POST":
        form = PersonneForm(request.POST, request.FILES, instance=personne)
        if form.is_valid():
            personne = form.save(commit=False)
            personne.user = request.user
            personne.save()
            return redirect("create_or_edit_experience")
    else:
        form = PersonneForm(instance=personne)

    return render(request, "boite.html", {"form": form})


# Vue pour créer ou modifier les expériences professionnelles de l'utilisateur
@login_required
def create_or_edit_experience(request):
    experiences = Experience.objects.filter(user=request.user)

    if request.method == "POST":
        form = ExperienceForm(request.POST)
        if form.is_valid():
            experience = form.save(commit=False)
            experience.user = request.user
            experience.save()
            return redirect("create_or_edit_experience")
    else:
        form = ExperienceForm()

    return render(request, "create_experience.html", {"form": form, "experiences": experiences})


# Vue pour créer ou modifier les formations de l'utilisateur
@login_required
def create_or_edit_formation(request):
    formations = Formation.objects.filter(user=request.user)

    if request.method == "POST":
        form = FormationForm(request.POST)
        if form.is_valid():
            formation = form.save(commit=False)
            formation.user = request.user
            formation.save()
            return redirect("create_or_edit_formation")
    else:
        form = FormationForm()

    return render(request, "create_formation.html", {"form": form, "formations": formations})


@login_required
def create_contact(request):
    try:
        contact = Contact.objects.get(user=request.user)
    except Contact.DoesNotExist:
        contact = None

    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            return redirect("create_contact")  # Rediriger vers la vue des informations de contact
    else:
        form = ContactForm(instance=contact)

    return render(request, "create_contact.html", {"form": form})


# Vue pour créer ou modifier les compétences de l'utilisateur
@login_required
def create_or_edit_competence(request):
    competences = Competence.objects.filter(user=request.user)

    if request.method == "POST":
        form = CompetenceForm(request.POST)
        if form.is_valid():
            competence = form.save(commit=False)
            competence.user = request.user
            competence.save()
            return redirect("create_or_edit_competence")
    else:
        form = CompetenceForm()

    return render(request, "create_competence.html", {"form": form, "competences": competences})


# Vue pour créer ou modifier les langues parlées par l'utilisateur
@login_required
def create_or_edit_langue(request):
    langues = Langue.objects.filter(user=request.user)

    if request.method == "POST":
        form = LangueForm(request.POST)
        if form.is_valid():
            langue = form.save(commit=False)
            langue.user = request.user
            langue.save()
            return redirect("create_or_edit_langue")
    else:
        form = LangueForm()

    return render(request, "create_langue.html", {"form": form, "langues": langues})


# Vue pour créer ou modifier les loisirs de l'utilisateur
@login_required
def create_or_edit_loisir(request):
    loisirs = Loisir.objects.filter(user=request.user)

    if request.method == "POST":
        form = LoisirForm(request.POST)
        if form.is_valid():
            loisir = form.save(commit=False)
            loisir.user = request.user
            loisir.save()
            return redirect("create_or_edit_loisir")
    else:
        form = LoisirForm()

    return render(request, "create_loisir.html", {"form": form, "loisirs": loisirs})


# Vue pour créer ou modifier le CV de l'utilisateur


# Vue pour afficher le CV de l'utilisateur
@login_required
def view_cv(request, cv_id, *args, **kwargs):
    # Récupération du CV et des données associées
    cv = get_object_or_404(CV, id=cv_id, user=request.user)
    experiences = cv.experiences.all()  # Toutes les expériences liées
    formations = cv.formations.all()  # Toutes les formations liées
    competences = cv.competences.all()  # Toutes les compétences liées
    langues = cv.langues.all()  # Toutes les langues liées
    loisirs = cv.loisirs.all()  # Tous les loisirs liés
    # Récupération de la personne et du contact associés au CV
    personne = cv.personne
    contact = cv.contact
   # Choisir le design
    if cv.design == 'design1':
        template_name = 'cv_design1.html'
    elif cv.design == 'design2':
        template_name = 'cv_design2.html'
    elif cv.design == 'design3':
        template_name = 'cv_design3.html'
    else:
        template_name = 'cv_design4.html'

    return render(request, template_name, {
        "cv": cv,
        "personne": personne,
        "contact": contact,
        "experiences": experiences,
        "formations": formations,
        "competences": competences,
        "langues": langues,
        "loisirs": loisirs,
    })


# Fonction pour créer une personne si elle n'existe pas déjà
def create_personne(request):
    if request.method == 'POST':
        form = PersonneForm(request.POST, request.FILES)
        if form.is_valid():
            personne = form.save(commit=False)
            personne.user = request.user
            personne.save()
            return redirect('home')  # Redirigez vers une page d'accueil ou autre.
    else:
        form = PersonneForm()
    return render(request, 'create_personne.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Sauvegarder l'utilisateur
            messages.success(request, 'Votre compte a été créé avec succès.')
            return redirect('formulaire')  # Rediriger vers la page de connexion
        else:
            # Si le formulaire n'est pas valide, afficher les erreurs
            messages.error(request, 'Il y a des erreurs dans le formulaire.')
            for field, errors in form.errors.items():
                for error in errors:
                    print(f"Erreur dans {field}: {error}")
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})



@login_required
def view_experiences(request):
    """
    Affiche les expériences professionnelles de l'utilisateur.
    """
    experiences = Experience.objects.filter(user=request.user)

    return render(request, "view_experiences.html", {"experiences": experiences})

@login_required
def view_formations(request):
    """
    Affiche les formations de l'utilisateur.
    """
    formations = Formation.objects.filter(user=request.user)

    return render(request, "view_formations.html", {"formations": formations})

@login_required
def view_competences(request):
    """
    Affiche les compétences de l'utilisateur.
    """
    competences = Competence.objects.filter(user=request.user)

    return render(request, "view_competences.html", {"competences": competences})


@login_required
def view_langues(request):
    """
    Affiche les langues de l'utilisateur.
    """
    langues = Langue.objects.filter(user=request.user)

    return render(request, "view_langues.html", {"langues": langues})

@login_required
def view_loisirs(request):
    """
    Affiche les loisirs de l'utilisateur.
    """
    loisirs = Loisir.objects.filter(user=request.user)

    return render(request, "view_loisirs.html", {"loisirs": loisirs})
 
@login_required
def view_personne(request):
    """
    Affiche les informations personnelles de l'utilisateur.
    """
    personne = Personne.objects.filter(user=request.user).first()
    return render(request, "view_personne.html", {"personne": personne})

@login_required
def view_contact(request):
    """
    Affiche les informations de contact de l'utilisateur.
    """
    contact = Contact.objects.filter(user=request.user).first()
    return render(request, "view_contact.html", {"contact": contact})


@login_required
def view_cvs(request):
    """
    Affiche tous les CVs créés par l'utilisateur.
    """
    cvs = CV.objects.filter(user=request.user)
    return render(request, "view_cvs.html", {"cvs": cvs})

@login_required
def create_or_edit_cv(request):
    personnes = Personne.objects.filter(user=request.user)
    contacts = Contact.objects.filter(user=request.user)
    experiences = Experience.objects.filter(user=request.user)
    formations = Formation.objects.filter(user=request.user)
    competences = Competence.objects.filter(user=request.user)
    langues = Langue.objects.filter(user=request.user)
    loisirs = Loisir.objects.filter(user=request.user)

    if request.method == "POST":
        form = CVForm(request.POST or None, user=request.user)
        if form.is_valid():
            cv = form.save(commit=False)
            cv.user = request.user
            cv.save()
            form.save_m2m()
            return redirect("view_cvs")
        else:
            # Si le formulaire est invalide, ajoutez un message d'erreur dans le contexte
            return render(request, "create_cv.html", {
                "form": form,
                "personnes": personnes,
                "contacts": contacts,
                "experiences": experiences,
                "formations": formations,
                "competences": competences,
                "langues": langues,
                "loisirs": loisirs,
                "errors": form.errors,  # Ajout des erreurs
            })

    else:  # Si c'est une requête GET
        form = CVForm(user=request.user)

    return render(request, "create_cv.html", {
        "form": form,
        "personnes": personnes,
        "contacts": contacts,
        "experiences": experiences,
        "formations": formations,
        "competences": competences,
        "langues": langues,
        "loisirs": loisirs,
    })

def trombinoscope(request):
    personnes = Personne.objects.all()  # Récupère toutes les personnes
    data = []
    for personne in personnes:
        # Récupère le premier CV de la personne si disponible
        premier_cv = CV.objects.filter(personne=personne).first()
        data.append({
            'personne': personne,
            'premier_cv': premier_cv,
        })
    return render(request, 'trombinoscope.html', {'data': data})

def cv_detail(request, pk):
    cv = get_object_or_404(CV, pk=pk)
    return render(request, 'cv_detail.html', {'cv': cv})

#pour la modification

def edit_cv(request, cv_id):
    # Récupérer l'instance du CV à modifier
    cv = get_object_or_404(CV, id=cv_id, user=request.user)

    # Récupérer les données pour les sélections (Personne, Contact, etc.)
    personnes = Personne.objects.filter(user=request.user)
    contacts = Contact.objects.filter(user=request.user)
    experiences = Experience.objects.filter(user=request.user)
    formations = Formation.objects.filter(user=request.user)
    competences = Competence.objects.filter(user=request.user)
    langues = Langue.objects.filter(user=request.user)
    loisirs = Loisir.objects.filter(user=request.user)

    if request.method == "POST":
        # Initialiser le formulaire avec les données POST et l'instance existante
        form = CVForm(request.POST, instance=cv, user=request.user)
        if form.is_valid():
            form.save()  # Sauvegarder les modifications
            return redirect("view_cvs")  # Rediriger vers la liste des CVs après modification
        else:
            # Ajouter les erreurs au contexte en cas de problème
            return render(request, "edit_cv.html", {
                "form": form,
                "personnes": personnes,
                "contacts": contacts,
                "experiences": experiences,
                "formations": formations,
                "competences": competences,
                "langues": langues,
                "loisirs": loisirs,
                "errors": form.errors,  # Ajout des erreurs
            })

    else:
        # Pré-remplir le formulaire avec les données de l'instance
        form = CVForm(instance=cv, user=request.user)

    return render(request, "edit_cv.html", {
        "form": form,
        "personnes": personnes,
        "contacts": contacts,
        "experiences": experiences,
        "formations": formations,
        "competences": competences,
        "langues": langues,
        "loisirs": loisirs,
    })



def delete_cv(request, cv_id):
    cv = get_object_or_404(CV, id=cv_id)  # Récupérer le CV correspondant à l'ID
  
    if request.method == 'POST':
        cv.delete()  # Supprimer le CV
        return redirect('view_cvs')  # Rediriger vers la liste des CVs
    return render(request, 'delete_cv_confirm.html', {'cv': cv})

def send_cv_email(request, cv_id):
    # Récupération du CV et de la personne associée
    cv = get_object_or_404(CV, id=cv_id, user=request.user)
    personne = cv.personne

    loisirs = cv.loisirs.all() 
    experiences = cv.experiences.all() 
    langues = cv.langues.all() 
    formations= cv.formations.all()
    competences= cv.competences.all()

    #photo_url = request.build_absolute_uri(personne.photo.url)
    photo_url = "https://www.univ-na.ci/storage/settings/March2021/q7ebFVlLpG3BnHZWV47N.png"

    if request.method == 'POST':
        recipient_email = request.POST.get('email')

        if not recipient_email:
            messages.error(request, "Veuillez fournir une adresse e-mail valide.")
            return render(request, 'email_cv.html', {'cv': cv})

        # Préparation de l'email
        subject = f"CV de {personne.nom} {personne.prenom}"
        message = render_to_string('cv_email_template.html', context={
            'cv': cv,  
            'loisirs': loisirs,  
            'experiences': experiences,
            'langues': langues,
            'competences': competences,
            'formations': formations,
            'photo_url': photo_url   
        })

        email = EmailMessage(
            subject=subject,
            body=message,
            from_email='animanalfred@gmail.com',
            to=[recipient_email],
        )
        email.content_subtype = 'html'  # Spécifie que le contenu est en HTML

        try:
            email.send()  # Envoi de l'email
            messages.success(request, "Le CV a été envoyé avec succès.")
        except Exception as e:
            messages.error(request, f"Une erreur s'est produite lors de l'envoi de l'email : {e}")

        return redirect('view_cvs')

    return render(request, 'email_cv.html', {'cv': cv})