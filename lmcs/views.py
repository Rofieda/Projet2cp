from django.shortcuts import render ,redirect
from .models import Chercheur ,Etudiants
from django.db import IntegrityError
def create_chercheur(request) : 
    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        genre = request.POST.get('genre')
        date_naiss = request.POST.get('date_naiss')
        etabliss = request.POST.get('etabliss')
        mail = request.POST.get('mail')
        diplome = request.POST.get('diplome')
        photo = request.POST.get('photo')
        fonction_etbl = request.POST.get('fonction_etbl')
        role_eq = request.POST.get('role_eq')
        bureau = request.POST.get('bureau')
        dblp_lien = request.POST.get('dblp_lien')
        etablissement=request.POST.get('etablissement')
        tel=request.POST.get('tel')
        grade_recherche=request.POST.get('grade_recherche')
        # Ensure email field is not empty before proceeding
        if mail:
            try:
                if Chercheur.objects.filter(mail=mail).exists():
                    return render(request, 'create_chercheur.html', {'error_message': 'Email already exists'})
                else:
                    Cherch = Chercheur(
                        nom_chercheur=nom,
                        prenom_chercheur=prenom,
                        genre=genre,
                        date_naiss=date_naiss,
                        diplome=diplome,
                        photo=photo,
                        fonction_etbl=fonction_etbl,
                        role_eq=role_eq,
                        bureau=bureau,
                        dblp_lien=dblp_lien,
                        mail=mail  ,
                        etablissement=etablissement,
                        tel=tel,
                        grade_recherche=grade_recherche,

                    )
                    Cherch.save()

                    return redirect('the info add with success')
            except IntegrityError as e:
                return render(request, 'create_chercheur.html', {'error_message': str(e)})
        else:
            return render(request, 'create_chercheur.html', {'error_message': 'Email cannot be empty'})
    else:
        return render(request, 'create_chercheur.html')
        

        
def home_page(request): 
    return render(request, 'home.html')



def create_etudiant(request) :
    if request.method == 'POST':
        nom_etd=request.POST.get('nom_etd') 
        prenom_etd=request.POST.get('prenom_etd')
        etablissement_etd=request.POST.get('etablissement_etd')
       
        etud=Etudiants(
            nom_etd=nom_etd,
            prenom_etd=prenom_etd,
            etablissement_etd=etablissement_etd,
        )
        etud.save()
        return redirect('the etudiant added succecfuly')
    else : 
        return render(request , 'Add_etudiant.html')
    
# def create_etudiant(request):
  #   if request.method == 'POST':
   #     type_encadr=request.post.get('type_encadr')
    #    return redirect('the encadrement added succecfuly')
    #else: 
     #   return render(request , 'Add_etudiant.html') 
    
    

def search_chercheur(request):
    if request.method == 'GET':
        nom = request.GET.get('nom')
        prenom = request.GET.get('prenom')
        chercheur = Chercheur.objects.filter(nom_chercheur=nom,prenom_chercheur=prenom).first()
        return render(request, 'Affich_chercheur.html', {'key': chercheur})
        #chercheur is a variable contain the data returned from the BDD
    else:
        return render(request, 'Affich_chercheur.html')


# Create your views here.
