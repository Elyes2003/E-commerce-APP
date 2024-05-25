import control_saisie
# Module biblio.py
# Un dictionnaire qui stocke les informations sur les étudiants
etudiants = {}
# Un dictionnaire qui stocke les informations sur les livres
livres = {}
# Un dictionnaire qui stocke les informations sur les emprunts
emprunts = {}

# Une fonction pour ajouter un étudiant au dictionnaire etudiants
def ajouter_etudiant(num, nom, prenom, date, adresse, mail, telephone, section, niveau):
    if (num != "")and (nom != "")and (prenom != "")and (date != "")and (adresse != "")and (mail != "")and (telephone != "")and (section != "")and(niveau != "") :
        if (control_saisie.control_chaine_chiffres(num)):
            if (control_saisie.control_chaine_lettres(nom)): 
                if (control_saisie.control_chaine_lettres(prenom)):
                    if (control_saisie.control_date(date)):
                        if (control_saisie.control_email(mail)):
                            if (control_saisie.control_numero(telephone)):
                                if num in etudiants:
                                    return("Ce numéro d'étudiant existe déjà.")
                                else:
                                    etudiant = {"nom": nom, "prenom": prenom, "date de naissance": date,"adresse": adresse,"mail": mail,"telephone":telephone, "section": section, "niveau etude": niveau}
                                    etudiants[num] = etudiant
                                    return("L'étudiant a été ajouté.")
                            else:
                                return("verifier le telephone")
                        else:
                            return("verifier le mail")
                    else:
                        return("verifier la date de naissance de format JJ/MM/AAAA")
                else:
                    return("verifier le prenom")
            else:
                return("verifier le nom")
        else:
            return("verifier le numero d'inscription")
    else:
        return("remplir les donnees")

# Une fonction pour supprimer un étudiant du dictionnaire etudiants
def supprimer_etudiant(num):
    if (control_saisie.control_chaine_chiffres(num)):
        if num in etudiants:
            del etudiants[num]
            return("L'étudiant a été supprimé.")
        else:
            return("Ce numéro d'étudiant n'existe pas.")
    else:
        return("verifier le numero d'inscription")
    
def supprimer_etudiants_section(section):
    a_supprimer = []
    test = False
    for num in etudiants:
        etudiant = etudiants[num]
        if etudiant["section"] == section:
            a_supprimer.append(num)
            test = True
    for num in a_supprimer:
        del etudiants[num]
    a_supprimer.clear()
    if test:
        return(f"Les étudiants de section {section} ont été supprimés.")
    else:
        return("ce niveau n'existe pas")    
    
    
def supprimer_etudiants_niveau(niveau):
    a_supprimer = []
    test = False
    for num in etudiants:
        etudiant = etudiants[num]
        if etudiant["niveau etude"] == niveau:
            a_supprimer.append(num)
            test = True
    for num in a_supprimer:
        del etudiants[num]
    a_supprimer.clear()
    if test:
        return(f"Les étudiants de niveau d'etude {niveau} ont été supprimés.")
    else: 
        return("ce niveau n'existe pas")
    
    
def supprimer_etudiants_section_niveau(section,niveau):
    a_supprimer = []
    test = False
    for num in etudiants:
        etudiant = etudiants[num]
        if (etudiant["section"] == section) and (etudiant["niveau etude"] == niveau):
            a_supprimer.append(num)
            test = True
    for num in a_supprimer:
        del etudiants[num]
    a_supprimer.clear()
    if test:
        return(f"Les étudiants de section {section} et de niveau d'etude {niveau} ont été supprimés.")
    else:
        return("ces données n'existe pas ")
    
        
# Une fonction pour modifier les informations d'un étudiant dans le dictionnaire etudiants
def modifier_etudiant_adresse(num, telephone=None, mail=None, adresse=None):

    if (control_saisie.control_chaine_chiffres(num)):
        if num in etudiants:
            etudiant = etudiants[num]
            if adresse is not None:
                etudiant["adresse"] = adresse
                etudiants[num] = etudiant
                return("Adresse d'étudiant a été modifié.")
            else:
                return("donner l'adresse a modifier")
        else:
            return("Ce numéro d'étudiant n'existe pas.")
    else:
        return("verifier le numero d'inscription")
    
def modifier_etudiant_telephone(num, telephone=None):

    if (control_saisie.control_chaine_chiffres(num)):
        if num in etudiants:
            etudiant = etudiants[num]
            if telephone is not None:
                if (control_saisie.control_numero(telephone)):
                    etudiant["telephone"] = telephone
                    etudiants[num] = etudiant
                    return("Telephone d'étudiant a été modifié.")
                else:
                    ("verifer le numero telephone")
            else:
                return("donner le telephone a modifier")
        else:
            return("Ce numéro d'étudiant n'existe pas.")
    else:
        return("verifier le numero d'inscription")
    
def modifier_etudiant_mail(num, mail=None):

    if (control_saisie.control_chaine_chiffres(num)):
        if num in etudiants:
            etudiant = etudiants[num]
            if mail is not None:
                if (control_saisie.control_email(mail)):
                    etudiant["mail"] = mail
                    etudiants[num] = etudiant
                    return("Mail d'étudiant a été modifié.")
                else:
                    return("verifier le mail")
            else:
                return("donner le mail a modifier")
        else:
            return("Ce numéro d'étudiant n'existe pas.")
    else:
        return("verifier le numero d'inscription")

# Une fonction pour afficher les informations de tous les étudiants dans le dictionnaire etudiants
def afficher_etudiants():
    
    if not etudiants:
        return ({})
    else:
        res = {}
        for num in sorted(etudiants):
            res[num] = etudiants[num]
        return (res)
              
      
def afficher_etudiants_num(numero):    

    if not etudiants:
        return ({})
    else:
        res = {}
        for num in sorted(etudiants):
            if num == numero:
                res[num] = etudiants[num]
        return (res)

def afficher_etudiants_section(section):
    if not etudiants:
        return ({})
    else:
        res = {}
        for num in sorted(etudiants):
            if etudiants[num]["section"] == section:
                res[num] = etudiants[num]
        return (res)
    
def afficher_etudiants_niveau(niveau):
    if not etudiants:
        return ({})
    else:
        res = {}
        for num in sorted(etudiants):
            if etudiants[num]["niveau etude"] == niveau:
                res[num] = etudiants[num]
        return (res)
def afficher_etudiants_section_niveau(section,niveau):
    if not etudiants:
        return ({})
    else:
        res = {}
        for num in sorted(etudiants):
            if (etudiants[num]["section"] == section) and (etudiants[num]["niveau etude"] == niveau) :
                res[num] = etudiants[num]
        return (res)
        


# Une fonction pour ajouter un livre au dictionnaire livres
def ajouter_livre(reference, titre, auteur, annee):
    if (control_saisie.control_chaine_lettres(auteur)):
        if (control_saisie.control_chaine_chiffres(annee)):
            if reference in livres:
                return("Ce livre existe déjà.")
            else:
                livre = {"titre": titre, "auteur": auteur, "annee edition": annee}
                livres[reference] = livre
                return("Le livre a été ajouté.")
        else: 
            return("verifier l'annee d'édition")
    else: 
        return("verifier le nom d'auteur")

# Une fonction pour supprimer un livre du dictionnaire livres
def supprimer_livre(reference):
    if reference in livres:
        del livres[reference]
        return("Le livre a été supprimé.")
    else:
        return("Ce livre n'existe pas.")
        
def supprimer_livre_auteur(auteur):
    if (control_saisie.control_chaine_lettres(auteur)):
        a_supprimer = []
        test = False
        for reference in livres:
            if livres[reference]["auteur"] == auteur:
                a_supprimer.append(reference)
                test = True
        for reference in a_supprimer:
            del livres[reference]
        a_supprimer.clear()
        if test:
            return(f"Les livres de l'auteur {auteur} ont été supprimés.")
        else:
            return("le nom d'auteur n'existe pas")
    else: 
        return("verifier le nom d'auteur")
    
    
def supprimer_livre_annee(annee):
    if (control_saisie.control_chaine_chiffres(annee)):
        a_supprimer = []
        test = False
        for reference in livres:
            if livres[reference]["annee edition"] == annee:
                a_supprimer.append(reference)
                test = True
        for reference in a_supprimer:
                del livres[reference]
        a_supprimer.clear()
        if test:
            return(f"Les livres de l'annee {annee} ont été supprimés.")
        else:
            return("cette année n'existe pas")
    else: 
        return("verifier l'annee d'édition")




def afficher_livres():
    if not livres:
        return ({})
    else:
        res = {}
        for reference in sorted(livres):
            res[reference] = livres[reference]
        return (res)
            
def afficher_livres_reference(ref):
    if not livres:
        return ({})
    else:
        res = {}
        for reference in sorted(livres):
            if reference == ref :
                res[reference] = livres[reference]
        return (res)
        
def afficher_livres_titre(titre):
    if not livres:
        return ({})
    else:
        res = {}
        for reference in sorted(livres):
            if livres[reference]["titre"] == titre :
                res[reference] = livres[reference]
        return (res)
    
def afficher_livres_annee(annee):
        if not livres:
            return ({})
        else:
            res = {}
            for reference in sorted(livres):
                if livres[reference]["annee edition"] == annee :
                     res[reference] = livres[reference]
            return (res)

def afficher_livres_auteur(auteur):
        if not livres:
            return ({})
        else:
            res = {}
            for reference in sorted(livres):
                if livres[reference]["auteur"] == auteur :
                    res[reference] = livres[reference]
            return (res)
       
def afficher_livres_par_titre_alphabetique():
    if not livres:
        return ({})
    else:
        dictionnaire_livre_tries = sorted (livres.items(), key= lambda x:x[1]['titre'].lower() )
        
        return (dictionnaire_livre_tries)
    
def emprunter_livre(num, reference, datem):
    if (control_saisie.control_chaine_chiffres(num)):
        if (control_saisie.control_date(datem)):
            if num in etudiants:
                if reference in livres:
                    if reference in emprunts:
                        return("Ce livre est déjà emprunté.")
                    else:
                        emprunt = {"num": num, "date d'emprunt": datem, "date retour": '--'}
                        emprunts[reference] = emprunt
                        return("Le livre a été emprunté.")
                else:
                    return("Ce livre n'existe pas.")
            else:
                return("Ce numéro d'étudiant n'existe pas.")
        else:
            return("verifier la date de format JJ/MM/AAAA")
    else:
        return("verifier le numéro d'inscription")

def rendre_livre(num,reference,date):
    if (control_saisie.control_chaine_chiffres(num)):
        if (control_saisie.control_date(date)):
            if num in etudiants:
                if reference in livres:
                    if reference in emprunts:
                        if control_saisie.compare_dates(emprunts[reference]["date d'emprunt"],date)==0 :
                            emprunts[reference]["date retour"] = date
                            return("Le livre a été rendu.")
                        else:
                            date_emprunt = emprunts[reference]["date d'emprunt"]
                            return(f"la date doit étre superieur à {date_emprunt}.")
                    else:
                        return("Ce livre n'est pas emprunté.")
                else:
                    return("Ce livre n'existe pas.")
            else:
                return("Ce numéro d'étudiant n'existe pas.")
        else:
            return("verifier la date de format JJ/MM/AAAA")
    else:
        return("verifier le numéro d'inscription")


def supprimer_emprunt(num,reference):
    if (control_saisie.control_chaine_chiffres(num)):
        if num in etudiants:
            if reference in livres:
                if reference in emprunts:
                    del emprunts[reference]
                    return("l'emprunt a été supprimé.")
                else:
                    return("Ce livre n'est pas emprunté.")
            else:
                return("Ce livre n'existe pas.")
        else:
            return("Ce numéro d'étudiant n'existe pas.")
    else:
        return("verifier le numéro d'inscription")

def modifier_emprunt_date(reference,datem=None):
    if (control_saisie.control_date(datem)):
        if reference in emprunts:
            emprunt = emprunts[reference]
            if datem is not None:
                emprunt["date d'emprunt"] = datem
                emprunts[reference] = emprunt
                return("emprunt a été modifié.")
            else:
                return(" donner la date emprunt")
        else:
            return("Ce emprunt n'existe pas.")
    else:
        return("verifier la date de format JJ/MM/AAAA")

def modifier_retour_date(reference,dateretour=None):
    if (control_saisie.control_date(dateretour)):
        if reference in emprunts:
            emprunt = emprunts[reference]
            if dateretour is not None:
                emprunt["date retour"] = dateretour
                emprunts[reference] = emprunt
                return("date retour a été modifié.")
            else:
                return(" donner la date retour")
        else:
            return("Ce emprunt n'existe pas.")
    else:
        return("verifier la date de format JJ/MM/AAAA")

def afficher_emprunts():
    if not emprunts:
        return ({})
    else:
        res = {}
        for reference in sorted(emprunts):

            num = emprunts[reference]["num"]
            datem = emprunts[reference]["date d'emprunt"]
            dateretour = emprunts[reference]["date retour"]

            nom = etudiants[num]["nom"]
            prenom = etudiants[num]["prenom"]

            titre = livres[reference]["titre"]
            
            emprunt  = {"Titre": titre, "Numéro": num, "Nom": nom,"Prénom": prenom,"date emprunt": datem,"date retour":dateretour}
            res[num] = emprunt 
        return (res)
    
def afficher_emprunts_dateemprunt(date):
        if not emprunts:
            return ({})
        else:
            res =  {}
            for reference in sorted(emprunts):
                if emprunts[reference]["date d'emprunt"] == date :
                    num = emprunts[reference]["num"]
                    datem = emprunts[reference]["date d'emprunt"]
                    dateretour = emprunts[reference]["date retour"]
                    nom = etudiants[num]["nom"]
                    prenom = etudiants[num]["prenom"]
                    titre = livres[reference]["titre"]
                    emprunt  = {"Titre": titre, "Numéro": num, "Nom": nom,"Prénom": prenom,"date emprunt": datem,"date retour":dateretour}
                    res[reference] = emprunt 
            return (res)

    
def afficher_emprunts_reference(referencedonnee):
    if not emprunts:
        return ({})
    else:
        res = {}
        for reference in sorted(emprunts):
            if reference == referencedonnee :
                num = emprunts[reference]["num"]
                datem = emprunts[reference]["date d'emprunt"]
                dateretour = emprunts[reference]["date retour"]
                nom = etudiants[num]["nom"]
                prenom = etudiants[num]["prenom"]
                titre = livres[reference]["titre"]
                emprunt  = {"Titre": titre, "Numéro": num, "Nom": nom,"Prénom": prenom,"date emprunt": datem,"date retour":dateretour}
                res[reference] = emprunt 
        return (res)
    
def afficher_emprunts_num(num):
        if not emprunts:
            return ({})
        else:
            res = {}
            for reference in sorted(emprunts):
                if emprunts[reference]["num"] == num :
                    num = emprunts[reference]["num"]
                    datem = emprunts[reference]["date d'emprunt"]
                    dateretour = emprunts[reference]["date retour"]
                    nom = etudiants[num]["nom"]
                    prenom = etudiants[num]["prenom"]
                    titre = livres[reference]["titre"]
                    emprunt  = {"Titre": titre, "Numéro": num, "Nom": nom,"Prénom": prenom,"date emprunt": datem,"date retour":dateretour}
                    res[reference] = emprunt 
            return (res)

    
def afficher_emprunts_dateretour(date):
        if not emprunts:
            return ({})
        else:
            res = {}
            for reference in sorted(emprunts):
                if emprunts[reference]["date retour"] == date :
                    num = emprunts[reference]["num"]
                    datem = emprunts[reference]["date d'emprunt"]
                    dateretour = emprunts[reference]["date retour"]
                    nom = etudiants[num]["nom"]
                    prenom = etudiants[num]["prenom"]
                    titre = livres[reference]["titre"]
                    emprunt  = {"Titre": titre, "Numéro": num, "Nom": nom,"Prénom": prenom,"date emprunt": datem,"date retour":dateretour}
                    res[reference] = emprunt 
            return (res)

    
def afficher_emprunts_2dateemprunt(date1, date2):
            if not emprunts:
                return ({})
            else:
                res = {}
                for reference in sorted(emprunts):
                    num = emprunts[reference]["num"]
                    datem = emprunts[reference]["date d'emprunt"]
                    dateretour = emprunts[reference]["date retour"]
                    nom = etudiants[num]["nom"]
                    prenom = etudiants[num]["prenom"]
                    titre = livres[reference]["titre"]
                    annee1 = int(date1[6:])
                    mois1 = int(date1[3:5])
                    jour1 = int(date1[:2])
                    annee2 = int(date2[6:])
                    mois2 = int(date2[3:5])
                    jour2 = int(date2[:2])
                    datecmp = emprunts[reference]["date d'emprunt"]
                    annee = int(datecmp[6:])
                    mois = int(datecmp[3:5])
                    jour = int(datecmp[:2])
                    if (annee1<=annee<=annee2) :
                        if(annee1==annee2):
                            if(mois1<=mois<=mois2):
                                if(mois1==mois2):
                                    if(jour1<=jour<=jour2):
                                        emprunt  = {"Titre": titre, "Numéro": num, "Nom": nom,"Prénom": prenom,"date emprunt": datem,"date retour":dateretour}
                                        res[reference] = emprunt 
                                else:
                                    emprunt  = {"Titre": titre, "Numéro": num, "Nom": nom,"Prénom": prenom,"date emprunt": datem,"date retour":dateretour}
                                    res[reference] = emprunt 

                        else:
                             emprunt  = {"Titre": titre, "Numéro": num, "Nom": nom,"Prénom": prenom,"date emprunt": datem,"date retour":dateretour}
                             res[reference] = emprunt 
                return (res)

    
def afficher_emprunts_2dateretour(date1, date2):
            if not emprunts:
                return ({})
            else:
                res = {}
                for reference in sorted(emprunts):
                    num = emprunts[reference]["num"]
                    datem = emprunts[reference]["date d'emprunt"]
                    dateretour = emprunts[reference]["date retour"]
                    nom = etudiants[num]["nom"]
                    prenom = etudiants[num]["prenom"]
                    titre = livres[reference]["titre"]
                    annee1 = int(date1[6:])
                    mois1 = int(date1[3:5])
                    jour1 = int(date1[:2])
                    annee2 = int(date2[6:])
                    mois2 = int(date2[3:5])
                    jour2 = int(date2[:2])
                    datecmp = emprunts[reference]["date retour"]
                    annee = int(datecmp[6:])
                    mois = int(datecmp[3:5])
                    jour = int(datecmp[:2])
                    if (annee1<=annee<=annee2) :
                        if(annee1==annee2):
                            if(mois1<=mois<=mois2):
                                if(mois1==mois2):
                                    if(jour1<=jour<=jour2):
                                        emprunt = {"Titre": titre, "Numéro": num, "Nom": nom,"Prénom": prenom,"date emprunt": datem,"date retour":dateretour}
                                        res[reference] = emprunt 
                                else:
                                    emprunt  = {"Titre": titre, "Numéro": num, "Nom": nom,"Prénom": prenom,"date emprunt": datem,"date retour":dateretour}
                                    res[reference] = emprunt 

                        else:
                            emprunt  = {"Titre": titre, "Numéro": num, "Nom": nom,"Prénom": prenom,"date emprunt": datem,"date retour":dateretour}
                            res[reference] = emprunt 
                return (res)
      
# les fonction pour enregistrer les données des dictionnaires etudiants, livres et emprunts dans des fichiers
def enregistrer_donnees_etudiants():
    with open("etudiants.txt", "w") as f:
        for num in sorted(etudiants):
            nom = etudiants[num]["nom"]
            prenom = etudiants[num]["prenom"]
            date = etudiants[num]["date de naissance"]
            adresse = etudiants[num]["adresse"]
            mail = etudiants[num]["mail"]
            telephone = etudiants[num]["telephone"]
            section = etudiants[num]["section"]
            niveau = etudiants[num]["niveau etude"]
            f.write(f"{num},{nom},{prenom},{date},{adresse},{mail},{telephone},{section},{niveau}\n")
    return True
            
def enregistrer_donnees_livres():
    with open("livres.txt", "w") as f:
        for reference in sorted(livres):
            titre = livres[reference]["titre"]
            auteur = livres[reference]["auteur"]
            annee = livres[reference]["annee edition"]
            f.write(f"{reference},{titre},{auteur},{annee}\n")
    return True       
def enregistrer_donnees_emprunts():
    with open("emprunts.txt", "w") as f:
        for reference in sorted(emprunts):
            num = emprunts[reference]["num"]
            datem = emprunts[reference]["date d'emprunt"]
            dateretour = emprunts[reference]["date retour"]
            f.write(f"{reference},{num},{datem},{dateretour}\n")
    return True


# les fonction pour la recupération les données des fichiers etudiants.txt, livres.txt et emprunts.txt dans les dictionnaires etudiants, livres et emprunts
def recuperation_donnees_etudiants():
    etudiants.clear() 
    with open("etudiants.txt", "r") as f:
        for line in f:
            line = line.strip()
            num, nom, prenom, date, adresse, mail, telephone, section, niveau= line.split(",")
            etudiant = {"nom": nom, "prenom": prenom, "date de naissance": date ,"adresse": adresse,"mail": mail,"telephone":telephone, "section": section, "niveau etude": niveau}
            etudiants[num] = etudiant
    return True        
def recuperation_donnees_livres():
    livres.clear()
    with open("livres.txt", "r") as f:
        for line in f:
            line = line.strip()
            reference, titre, auteur, annee = line.split(",")
            livre = {"titre": titre, "auteur": auteur, "annee edition": annee}
            livres[reference] = livre
    return True        
def recuperation_donnees_emprunts():
    emprunts.clear()
    with open("emprunts.txt", "r") as f:
        for line in f:
            line = line.strip()
            reference, num, datem, dateretour = line.split(",")
            emprunt = {"num": num, "date d'emprunt": datem, "date retour": dateretour}
            emprunts[reference] = emprunt
    return True        

