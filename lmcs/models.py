from django.db import models

class Projet(models.Model):
    id_projet=models.AutoField(primary_key=True)
    chercheur_role=models.CharField(max_length=50)
    start_date=models.CharField(max_length=50)
    end_date=models.CharField(max_length=50)


class Chercheur(models.Model):
    id_chercheur=models.AutoField(primary_key=True)
    nom_chercheur=models.CharField(max_length=50,null=False)
    prenom_chercheur=models.CharField(max_length=50,null=False)
    genre=models.CharField(max_length=50)
    date_naiss=models.CharField(max_length=50)
    etablissement=models.CharField(max_length=50)
    diplome=models.CharField(max_length=100)
    grade_recherche=models.CharField(max_length=50 , null=True)
    mail=models.EmailField(unique=True)
    tel=models.CharField(max_length=50)
    dblp_lien=models.CharField(max_length=50)
    bureau=models.CharField(max_length=50)
    role_eq=models.CharField(max_length=50)
    fonction_etbl=models.CharField(max_length=50)
    photo=models.ImageField(upload_to='photos/')
    # Define a foreign key relationship with Projet table 
    id_projet = models.ForeignKey(Projet, on_delete=models.CASCADE, null=True,db_column='id_projet')
    class Meta:
        db_table = 'Chercheurs'


class Publication(models.Model):
    id_publication=models.AutoField(primary_key=True)
    acronyme=models.CharField(max_length=50)
    descrp_acronyme=models.CharField(max_length=50)
    titre=models.CharField(max_length=50)
    classification=models.CharField(max_length=50)

    type_choices =[
        ('Journaux','Journaux'),
        ('Conference','Conference'),
        ('Autre','Autre'),
    ]
    ptype=models.CharField(max_length=50 , choices=type_choices)
    class Meta:
        db_table = 'publications'
    

class Etudiants(models.Model) : 
    id_etudiant=models.AutoField(primary_key=True)
    nom_etd=models.CharField(max_length=50)
    prenom_etd=models.CharField(max_length=50)
    etablissement_etd=models.CharField(max_length=50)
    class Meta:
        db_table = 'etudiants'


class Encadrement (models.Model) : 
     # Define the foreign keys relationship with chercheur and etudiant table 

    id_chercheur = models.ForeignKey(Chercheur, on_delete=models.CASCADE, null=True,db_column='id_chercheur')
    id_etudiant = models.ForeignKey(Etudiants, on_delete=models.CASCADE, null=True , db_column='id_etudiant')
    type_choices = [
        ('PFE','PFE'),
        ('Master','Master'),
        ('Doctorat','Doctorat'),
        ('Autre','Autre'),
    ]
    type_encadrement=models.CharField(max_length=50 , choices=type_choices)
    intitule=models.CharField(max_length=50)
    start_date=models.CharField(max_length=50)
    end_date=models.CharField(max_length=50)
    class Meta:
        # Define the composite primary key using unique_together
        unique_together = ('id_chercheur', 'id_etudiant')
        db_table = 'encadrements'


class PubliePublication(models.Model):
    id_chercheur = models.ForeignKey(Chercheur, on_delete=models.CASCADE)
    id_publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    p_date = models.CharField(max_length=50)
    volume = models.CharField(max_length=50)
    domaine = models.CharField(max_length=50)
    prolongement_page = models.CharField(max_length=50)
    ordre_chercheur = models.IntegerField(unique=True)
    class Meta:
        # Define the composite primary key using unique_together
        unique_together = ('id_chercheur', 'id_publication')
        db_table = 'publie_publication'





# Create your models here.
