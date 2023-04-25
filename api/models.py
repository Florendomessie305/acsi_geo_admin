from django.db import models


# Create your models here.
class Localite(models.Model):
    nom_localite = models.CharField(max_length=200, unique=True)
    superficie = models.FloatField()
    description = models.TextField(default='description')

    def __str__(self):
        return self.nom_localite


class CategorieCimetiere(models.Model):
    nom_categorie = models.CharField(max_length=200, null=False, unique=True)
    description = models.CharField(max_length=200, default='description de la categorie')

    def __str__(self):
        return self.nom_categorie


class Cimetiere(models.Model):
    nom_cimetiere = models.CharField(max_length=200, unique=True)
    superficie = models.FloatField()
    description = models.TextField()
    categorie = models.ForeignKey(CategorieCimetiere, on_delete=models.SET_NULL, related_name='cimetieres', null=True)
    localite = models.ForeignKey(Localite, on_delete=models.SET_NULL, related_name='cimetieres', null=True)

    def __str__(self):
        return self.nom_cimetiere


class Tombe(models.Model):
    numero_tombe = models.CharField(max_length=200)
    lat = models.FloatField(default=0.0)
    lon = models.FloatField(default=0.0)
    cimetiere = models.ForeignKey(Cimetiere, on_delete=models.SET_NULL, related_name='tombes', null=True)

    def __str__(self):
        return self.numero_tombe


class Defunt(models.Model):
    matricule = models.CharField(max_length=200)
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200, null=True, blank=True)
    genre_tye = models.TextChoices('genre_type', 'Monsieur Madame Mademoiselle')
    genre = models.CharField(choices=genre_tye.choices, max_length=15, blank=True)
    nationalite = models.CharField(max_length=200)
    date_naiss = models.DateField()
    date_deces = models.DateField()
    date_inhumation = models.DateField()
    tombe = models.OneToOneField(Tombe, on_delete=models.CASCADE, related_name="defunt")
    statut = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.nom} {self.prenom}'


class Exhumation(models.Model):
    date_exhumation = models.DateField()
    last_cimetiere = models.ForeignKey(Cimetiere, on_delete=models.SET_NULL, related_name='exhumations', null=True)
    new_cimetiere = models.ForeignKey(Cimetiere, on_delete=models.SET_NULL, related_name='new_r_inhumations', null=True)
    defunt = models.ForeignKey(Defunt, on_delete=models.CASCADE, related_name="exhumations")

    def __str__(self):
        return f'{self.date_exhumation}'
