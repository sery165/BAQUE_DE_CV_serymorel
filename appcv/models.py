from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    telephone = models.CharField(max_length=20, null=True, blank=True)
    adresse = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Contact de {self.user.username}"

from django.db import models
from django.contrib.auth.models import User

class Personne(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)  # Correction de 'maxlength' en 'max_length'
    date_naissance = models.DateField()
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    email = models.EmailField()
    telephone = models.CharField(max_length=20, null=True, blank=True)  # Correction de 'maxlength' en 'max_length'
    adresse = models.TextField(null=True, blank=True)
    cv = models.FileField(upload_to='cv/', null=True, blank=True)  # Ajout du champ pour le CV

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    titre = models.CharField(maxlength=100)
    entreprise = models.CharField(maxlength=100)
    date_debut = models.DateField()
    date_fin = models.DateField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.titre} chez {self.entreprise}"

class Formation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    diplome = models.CharField(maxlength=100)
    institution = models.CharField(maxlength=100)
    date_debut = models.DateField()
    date_fin = models.DateField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.diplome} à {self.institution}"

class Competence(models.Model):
    NIVEAU_CHOICES = [
        ('Débutant', 'Débutant'),
        ('Intermédiaire', 'Intermédiaire'),
        ('Avancé', 'Avancé'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nom = models.CharField(maxlength=100)
    niveau = models.CharField(maxlength=50)

    def __str__(self):
        return f"{self.nom} - {self.niveau}"

class Langue(models.Model):
    NIVEAU_CHOICES = [
        ('Débutant', 'Débutant'),
        ('Intermédiaire', 'Intermédiaire'),
        ('Avancé', 'Avancé'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    langue = models.CharField(maxlength=50)
    niveau = models.CharField(maxlength=50)

    def __str__(self):
        return f"{self.langue} - {self.niveau}"

class Loisir(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nom = models.CharField(maxlength=100)
    description = models.TextField()

    def __str__(self):
        return self.nom

class CV(models.Model):
    DESIGN_CHOICES = [
        ('design1', 'Design 1'),
        ('design2', 'Design 2'),
        ('design3', 'Design 3'),
        ('design4', 'Design 4'),
    ]
    design = models.CharField(maxlength=10, choices=DESIGN_CHOICES, default='design1')
    title = models.CharField(maxlength=100, default='CV sans titre')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    personne = models.ForeignKey(Personne, on_delete=models.CASCADE)
    experiences = models.ManyToManyField(Experience, blank=True)
    formations = models.ManyToManyField(Formation, blank=True)
    competences = models.ManyToManyField(Competence, blank=True)
    langues = models.ManyToManyField(Langue, blank=True)
    loisirs = models.ManyToManyField(Loisir, blank=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"CV de {self.personne.prenom} {self.personne.nom}"
