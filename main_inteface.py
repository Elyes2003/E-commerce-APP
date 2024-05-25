import sys
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QTableWidgetItem
import control_saisie
import biblio
from  ui_test import Ui_MainWindow

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        
        self.ui.stackedWidget.setCurrentWidget(self.ui.page)
        
        self.ui.actionAjouter_tudiant.triggered.connect(self.show_ajouter_etudiant)
        self.ui.actionSuppression_tudiant_donn.triggered.connect(self.show_supp_etudiant)
        self.ui.actionSuppression_des_tudiants_d_une_section_donn.triggered.connect(self.show_supp_etudiants_section)
        self.ui.actionSuppression_des_tudiants_d_un_niveau_donn.triggered.connect(self.show_supp_etudiants_niveau)
        self.ui.actionSuppression_des_tudiants_d_une_section_et_un_niveau.triggered.connect(self.show_supp_etudiants_section_niveau)
        self.ui.actionT_l_phone.triggered.connect(self.show_modifier_telephone_etudiant)
        self.ui.actionAdresse.triggered.connect(self.show_modifier_adresse_etudiant)
        self.ui.actionMail.triggered.connect(self.show_modifier_mail_etudiant)
        self.ui.actionContenu_du_dictionnnaire_tudiants.triggered.connect(self.show_afficher_etudiants)
        self.ui.actionRecherche_par_num_rp_inscription.triggered.connect(self.show_afficher_etudiant_num)
        self.ui.actionRecherche_par_section.triggered.connect(self.show_afficher_etudiant_section)
        self.ui.actionRecherche_par_niveau.triggered.connect(self.show_afficher_etudiant_niveau)
        self.ui.actionRecherche_par_section_et_niveau.triggered.connect(self.show_afficher_etudiant_section_niveau)
        
        
        self.ui.actionAjouter_un_nouvel_livre.triggered.connect(self.show_ajouter_livre)
        self.ui.actionSuppression_livre_donn.triggered.connect(self.show_supp_livre)
        self.ui.actionSuppression_livres_d_un_auteur_donn.triggered.connect(self.show_supp_livre_auteur)
        self.ui.actionSuppression_livres_d_une_ann_e_donn.triggered.connect(self.show_supp_livre_annee)
        self.ui.actionContenu_du_dictionnnaire_LIVRE.triggered.connect(self.show_afficher_livres)
        self.ui.actionRecherche_par_R_f_rence.triggered.connect(self.show_afficher_livre_reference)
        self.ui.actionRecherche_par_titre.triggered.connect(self.show_afficher_livre_titre)
        self.ui.actionRecherche_livres_par_ann_e_dition_donn_e.triggered.connect(self.show_afficher_livre_annee)
        self.ui.actionRecherche_livres_d_un_auteur_donn.triggered.connect(self.show_afficher_livre_auteur)
        
        
        self.ui.actionAjouter_un_nouvel_emprunt.triggered.connect(self.show_emprunter)
        self.ui.actionRetour_d_un_emprunt.triggered.connect(self.show_retourner)
        self.ui.actionSupprimer_d_un_emprunt.triggered.connect(self.show_supp_emprunt)
        self.ui.actionDate_emprunt.triggered.connect(self.show_modifier_emprunt_date)
        self.ui.actionDate_retour.triggered.connect(self.show_modifier_retour_date)
        self.ui.actionContenu_du_dictionnnaire_emprunt.triggered.connect(self.show_afficher_emprunts)
        self.ui.actionRecherche_emprunts_par_livre.triggered.connect(self.show_afficher_emprunt_livre)
        self.ui.actionRecherche_emprunts_par_tudiant.triggered.connect(self.show_afficher_emprunt_etudiant)
        self.ui.actionRecherche_livres_emprunt_s_une_date_donn_es.triggered.connect(self.show_afficher_emprunt_date)
        self.ui.actionRecherche_livres_retourn_s_une_date_donn_es.triggered.connect(self.show_afficher_retour_livre)
        self.ui.actionRecherche_livres_emprunt_s_entre_2_dates_donn_es.triggered.connect(self.show_afficher_emprunt_2dates)
        self.ui.actionRecherche_livres_retourn_s_entre_2_dates_donn_es.triggered.connect(self.show_afficher_retour_2dates)
        self.ui.actionAffichage_des_livres_par_ordre_alphab_tique.triggered.connect(self.show_livres_alphas)
        
        
    
        
        

    

        self.ui.ajouter_etudiant_botton.clicked.connect(self.add_stud)
        
        self.ui.Button_supprimer_etudiant.clicked.connect(self.del_stud_num)
        
        self.ui.Button_supprimer_section.clicked.connect(self.del_section)
        
        self.ui.Button_supprimer_niveau.clicked.connect(self.del_niveau)
        
        self.ui.Button_supprimer_sectionniveau.clicked.connect(self.del_niveau_section)
        
        self.ui.pushButton_modifer.clicked.connect(self.edit_stud_telephone)
        
        self.ui.pushButton_modifer_2.clicked.connect(self.edit_stud_adresse)

        self.ui.pushButton_modifer_3.clicked.connect(self.edit_stud_mail)
        
        self.ui.affiche_dictionnaire.clicked.connect(self.show_stud)
        
        self.ui.pushButton_recherchenum.clicked.connect(self.show_stud_num)
        
        self.ui.pushButton_recherchesection.clicked.connect(self.show_stud_section)
        
        self.ui.pushButton_rechercheniveau.clicked.connect(self.show_stud_niveau)
        
        self.ui.pushButton_recherchenivetsect.clicked.connect(self.show_stud_section_niveau)
        
        
        self.ui.ajouter_livre_botton.clicked.connect(self.add_livre)

        self.ui.Button_supprimer_livre.clicked.connect(self.del_livre)
        
        self.ui.Button_supprimer_auteur.clicked.connect(self.del_livres_auteur)
        
        self.ui.Button_supprimer_annee_edition.clicked.connect(self.del_livres_annee_edition)
        
        self.ui.affiche_dictionnaire_2.clicked.connect(self.show_livres)
        
        self.ui.pushButton_recherchereference.clicked.connect(self.show_livres_reference)
        
        self.ui.pushButton_recherchetitre.clicked.connect(self.show_livres_titre)
        
        self.ui.pushButton_rechercheauteur.clicked.connect(self.show_livres_auteur)
        
        self.ui.pushButton_rechercheanneeedition.clicked.connect(self.show_livres_annee_edition)
        
        
        
        self.ui.ajouter_emprunt_botton.clicked.connect(self.empruntlivre)
        
        self.ui.retour_emprunt_botton.clicked.connect(self.retourlivre)
    
        self.ui.supprimer_emprunt_botton.clicked.connect(self.supprimeremprunt)    
        
        self.ui.modifier_emprunt_botton.clicked.connect(self.modifier_emprunt_date)
    
        self.ui.modifier_emprunt_botton_2.clicked.connect(self.modifier_retour_date)
        
        self.ui.afficher_botton_dictionnaire_emprunt.clicked.connect(self.showemprunts)
        
        self.ui.pushButton_recherchereference_emprunt.clicked.connect(self.showemprunts_reference)
        
        self.ui.pushButton_rechercheetudiant_emprunt.clicked.connect(self.showemprunts_num)
        
        self.ui.pushButton_recherchedate_emprunt.clicked.connect(self.showemprunts_date_emprunt)
        
        self.ui.pushButton_recherchedate_retour.clicked.connect(self.showemprunts_date_retour)
        
        self.ui.pushButton_recherche_date1_emprunt.clicked.connect(self.showemprunts_2dates_emprunts)
        
        self.ui.pushButton_recherche_date2_emprunt.clicked.connect(self.showemprunts_2dates_retours)
        
        self.ui.affiche_dictionnaire_alphabetique.clicked.connect(self.show_livres_alpha)
        
        self.ui.actionEnregistrement_fichier_tudiants.triggered.connect(self.enregistrer_etudiants)
        self.ui.actionR_cup_ration_fichier_tudiants.triggered.connect(self.recuperer_etudiants)
        
        self.ui.actionEnregistrement_fichier_livres.triggered.connect(self.enregistrer_livres)
        self.ui.actionR_cup_ration_fichier_livres.triggered.connect(self.recuperer_livres)
        
        self.ui.actionEnregistrement_fichier_emprunts.triggered.connect(self.enregistrer_emprunts)
        self.ui.actionR_cup_ration_fichier_emprunts.triggered.connect(self.recuperer_emprunts)
        
    

                
    def show(self):
        self.main_win.show()    
    
    def enregistrer_etudiants(self):
        if biblio.enregistrer_donnees_etudiants()== True:
            message = "les données etudiants ont été enregistrer"
            QMessageBox.about(None,"message",message)
    def enregistrer_livres(self):
        if biblio.enregistrer_donnees_livres()== True:
            message = "les données livres ont été enregistrer"
            QMessageBox.about(None,"message",message)
    def enregistrer_emprunts(self):
        if biblio.enregistrer_donnees_emprunts()== True:
            message = "les données emprunts ont été enregistrer"
            QMessageBox.about(None,"message",message)
    def recuperer_etudiants(self):
        if biblio.recuperation_donnees_etudiants()== True:
            message = "les données etudiants ont été recuperer"
            QMessageBox.about(None,"message",message)
    def recuperer_livres(self):
        if biblio.recuperation_donnees_livres()== True:
            message = "les données livres ont été recuperer"
            QMessageBox.about(None,"message",message)
    def recuperer_emprunts(self):
        if biblio.recuperation_donnees_emprunts()== True:
            message = "les données emprunts ont été recuperer"
            QMessageBox.about(None,"message",message)
    
    
    
        
    def show_ajouter_etudiant(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_ajouter_etudiant)
    def show_supp_etudiant(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_supp_etudiant)
    def show_supp_etudiants_section(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_supp_etudiants_section)
    def show_supp_etudiants_niveau(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_supp_etudiants_niveau)   
    def show_supp_etudiants_section_niveau(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_supp_etudiants_section_niveau) 
    def show_modifier_telephone_etudiant(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_modifier_telephone_etudiant)
    def show_modifier_adresse_etudiant(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_modifier_adresse_etudiant)
    def show_modifier_mail_etudiant(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_modifier_mail_etudiant)
    def show_afficher_etudiants(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_afficher_etudiants)
    def show_afficher_etudiant_num(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_afficher_etudiant_num)
    def show_afficher_etudiant_section(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_afficher_etudiant_section)
    def show_afficher_etudiant_niveau(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_afficher_etudiant_niveau)
    def show_afficher_etudiant_section_niveau(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_afficher_etudiant_section_niveau)
        
        
    def show_ajouter_livre(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_ajouter_livre)
    def show_supp_livre(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_supp_livre)
    def show_supp_livre_auteur(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_supp_livre_auteur)
    def show_supp_livre_annee(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_supp_livre_annee)
    def show_afficher_livres(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_afficher_livres)
    def show_afficher_livre_reference(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_afficher_livre_reference)
    def show_afficher_livre_titre(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_afficher_livre_titre)
    def show_afficher_livre_auteur(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_afficher_livre_auteur)
    def show_afficher_livre_annee(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_afficher_livre_annee)
    def show_livres_alphas(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)
    
    
    def show_emprunter(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_emprunter)
    def show_retourner(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_retourner)
    def show_supp_emprunt(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_supp_emprunt)
    def show_modifier_emprunt_date(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_modifier_emprunt_date)
    def show_modifier_retour_date(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_modifier_retour_date)
    def show_afficher_emprunts(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_afficher_emprunts)
    def show_afficher_emprunt_livre(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_afficher_emprunt_livre)
    def show_afficher_emprunt_etudiant(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_afficher_emprunt_etudiant)
    def show_afficher_emprunt_date(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_afficher_emprunt_date)
    def show_afficher_retour_livre(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_afficher_retourner_livre)
    def show_afficher_emprunt_2dates(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_afficher_emprunt_2dates)
    def show_afficher_retour_2dates(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_afficher_retourner_2dates)




    def add_stud(self):
        num1 = self.ui.num_input.text()
        nom1= self.ui.nom_input.text()
        prenom1 = self.ui.prenom_input.text()   
        date_naissance1 = self.ui.date_naissance_input.text() 
        adresse1 = self.ui.adresse_input.text()
        mail1 = self.ui.mail_input.text()
        telephone1 = self.ui.telephone_input.text()
        section1 = self.ui.section_input.text()
        niveau_etude1 = self.ui.niveau_etude_input.text()
        res = biblio.ajouter_etudiant(num1,nom1,prenom1,date_naissance1,adresse1,mail1,telephone1,section1,niveau_etude1)
        QMessageBox.about(None,"message",res)
        if res == "L'étudiant a été ajouté." :
            self.ui.num_input.clear()
            self.ui.nom_input.clear()
            self.ui.prenom_input.clear()
            self.ui.adresse_input.clear()
            self.ui.date_naissance_input.clear()
            self.ui.mail_input.clear()
            self.ui.telephone_input.clear()
            self.ui.section_input.clear()
            self.ui.niveau_etude_input.clear()
        
    def del_stud_num(self):
        num1 = self.ui.num_input_supprimer.text()
        res = biblio.supprimer_etudiant(num1)
        QMessageBox.about(None,"message",res)
        if res == "L'étudiant a été supprimé." :
            self.ui.num_input_supprimer.clear()
    def del_section(self):
        section1 = self.ui.section_input_supprimer.text()
        res = biblio.supprimer_etudiants_section(section1)
        QMessageBox.about(None,"message",res)
        if res == f"Les étudiants de section {section1} ont été supprimés." :
            self.ui.section_input_supprimer.clear()
    def del_niveau(self):
        niveau1 = self.ui.niveau_input_supprimer.text()
        res = biblio.supprimer_etudiants_niveau(niveau1)
        QMessageBox.about(None,"message",res)
        if res == f"Les étudiants de niveau d'etude {niveau1} ont été supprimés." :
            self.ui.niveau_input_supprimer.clear()
    def del_niveau_section(self):
        section1 = self.ui.sectionmix_input_syupprimer.text()
        niveau1 = self.ui.niveau_etudemic_input_supprimer.text()      
        res = biblio.supprimer_etudiants_section_niveau(section1,niveau1)
        QMessageBox.about(None,"message",res)
        if res == f"Les étudiants de section {section1} et de niveau d'etude {niveau1} ont été supprimés." :
            self.ui.sectionmix_input_syupprimer.clear()
            self.ui.niveau_etudemic_input_supprimer.clear()
    def edit_stud_telephone(self):
        num1 = self.ui.num_modifier.text()
        telephone1 = self.ui.telephone_modifier.text()
        res = biblio.modifier_etudiant_telephone(num1,telephone1)
        QMessageBox.about(None,"message",res)
        if res == "Telephone d'étudiant a été modifié." :
            self.ui.num_modifier.clear()
            self.ui.telephone_modifier.clear()
    def edit_stud_adresse(self):
        num1 = self.ui.num_modifier_2.text()
        adresse1 = self.ui.adresse_modifer.text()
        res = biblio.modifier_etudiant_adresse(num1,adresse1)
        QMessageBox.about(None,"message",res)
        if res == "Adresse d'étudiant a été modifié." :
            self.ui.num_modifier_2.clear()
            self.ui.adresse_modifer.clear()
    def edit_stud_mail(self):
        num1 = self.ui.num_modifier_3.text()
        mail1 = self.ui.mail_modifer.text()
        res = biblio.modifier_etudiant_mail(num1,mail1)
        QMessageBox.about(None,"message",res)
        if res == "Mail d'étudiant a été modifié." :
            self.ui.num_modifier_3.clear()
            self.ui.mail_modifer.clear()
        
    def show_stud(self):

        res = biblio.afficher_etudiants()
        if len(res) == 0:
            message = "Il n'y a pas d'étudiants."
            QMessageBox.about(None,"message",message)
        else:
            self.remplir_table_etudiants(res,self.ui.tableWidget_etudiants)
            
    def show_stud_num(self):
        num1 = self.ui.num_input_recherche.text()
        if (control_saisie.control_chaine_chiffres(num1)):
            res = biblio.afficher_etudiants_num(num1)
            if len(res) == 0:
                message = "Il n'y a pas un etudiant de ce numéro."
                QMessageBox.about(None,"message",message)
            else:
                self.remplir_table_etudiants(res,self.ui.tableWidget_etudiants_num)
        else: 
            self.ui.num_input_recherche.clear()
            message = "verifier le numero"
            QMessageBox.about(None,"message",message)
            
    def show_stud_section(self):
        section1 = self.ui.section_input_recherche.text()
        res = biblio.afficher_etudiants_section(section1)
        if len(res) == 0:
            message = "Il n'y a pas des etudiants de cette section."
            QMessageBox.about(None,"message",message)
        else:
            self.remplir_table_etudiants(res,self.ui.tableWidget_etudiants_section)

    def show_stud_niveau(self):
        niveau1 = self.ui.niveau_input_recherche.text()
        res = biblio.afficher_etudiants_niveau(niveau1)
        if len(res) == 0:
            message = "Il n'y a pas des etudiants de ce niveau."
            QMessageBox.about(None,"message",message)
        else:
            self.remplir_table_etudiants(res,self.ui.tableWidget_etudiants_niveau)
    def show_stud_section_niveau(self):
        section1 = self.ui.sectionmix_input_recherche.text()
        niveau1 = self.ui.niveau_etudemix_input_recherche.text()
        res = biblio.afficher_etudiants_section_niveau(section1,niveau1)
        if len(res) == 0:
            message = "Il n'y a pas des etudiants."
            QMessageBox.about(None,"message",message)
        else:
            self.remplir_table_etudiants(res,self.ui.tableWidget_etudiants_mix)
  
        
    def add_livre(self):
        reference1 = self.ui.reference_input.text()
        titre1 = self.ui.titre_input.text()
        auteur1 = self.ui.auteur_input.text()
        annee_edition1 = self.ui.annee_edition_input.text()
        res = biblio.ajouter_livre(reference1,titre1,auteur1,annee_edition1)
        QMessageBox.about(None,"message",res)
        if res == "Le livre a été ajouté." :
            self.ui.reference_input.clear()
            self.ui.titre_input.clear()
            self.ui.auteur_input.clear()
            self.ui.annee_edition_input.clear()
    def del_livre(self):
        reference1 = self.ui.reference_input_supprimer.text()
        res = biblio.supprimer_livre(reference1)
        QMessageBox.about(None,"message",res)
        if res == "Le livre a été supprimé." :
            self.ui.reference_input_supprimer.clear()
    def del_livres_auteur(self):
        auteur1 = self.ui.auteur_input_supprimer.text()
        res = biblio.supprimer_livre_auteur(auteur1)
        QMessageBox.about(None,"message",res)
        if res == f"Les livres de l'auteur {auteur1} ont été supprimés." :
            self.ui.auteur_input_supprimer.clear()
    def del_livres_annee_edition(self):
        annee_edition1 = self.ui.annee_edition_input_supprimer.text()
        res = biblio.supprimer_livre_annee(annee_edition1)
        QMessageBox.about(None,"message",res)
        if res == f"Les livres de l'annee {annee_edition1} ont été supprimés." :
            self.ui.annee_edition_input_supprimer.clear()
            
    def show_livres(self):
        res = biblio.afficher_livres()
        if len(res) == 0:
            message = "Il n'y a pas de livres."
            QMessageBox.about(None,"message",message)
        else:
            self.remplir_table_livres(res,self.ui.tableWidget_livres)
            
    def show_livres_reference(self):
        reference1 = self.ui.reference_input_recherche.text()
        if (control_saisie.control_chaine_chiffres(reference1)):
            res = biblio.afficher_livres_reference(reference1)
            if len(res) == 0:
                message = "Il n'y a pas de livres de cette reference."
                QMessageBox.about(None,"message",message)
            else:
                self.remplir_table_livres(res,self.ui.tableWidget_livres_ref)
        else: 
            message = "verifier la reference"
            QMessageBox.about(None,"message",message)
            
    def show_livres_titre(self):
        titre1 = self.ui.titre_input_recherche.text()
        res = biblio.afficher_livres_titre(titre1)
        if len(res) == 0:
                message = "Il n'y a pas de livres de ce titre."
                QMessageBox.about(None,"message",message)
        else:
            self.remplir_table_livres(res,self.ui.tableWidget_livres_titre)
            
    def show_livres_auteur(self):
        auteur1 = self.ui.auteur_input_recherche.text()
        if (control_saisie.control_chaine_lettres(auteur1)):
            res = biblio.afficher_livres_auteur(auteur1)
            if len(res) == 0:
                message = "Il n'y a pas de livres de ce auteur."
                QMessageBox.about(None,"message",message)
            else:
                self.remplir_table_livres(res,self.ui.tableWidget_livres_auteur)
        else: 
            message = "verifier le nom d'auteur"
            QMessageBox.about(None,"message",message)
            
    def show_livres_annee_edition(self):
        annee_edition1 = self.ui.annee_edition_input_recherche.text()
        if (control_saisie.control_chaine_chiffres(annee_edition1)):
            res = biblio.afficher_livres_annee(annee_edition1)
            if len(res) == 0:
                message = "Il n'y a pas de livres de cette annee."
                QMessageBox.about(None,"message",message)
            else:
                self.remplir_table_livres(res,self.ui.tableWidget_livres_annee)
        else: 
            message = "verifier l'annee d'édition"
            QMessageBox.about(None,"message",message)
    def empruntlivre(self):
        num1 = self.ui.num_emprunt_input.text()
        reference1 = self.ui.reference_emprunt_input.text()
        date_emprunt1 = self.ui.date_emprunt_input.text()
        res = biblio.emprunter_livre(num1,reference1,date_emprunt1)
        QMessageBox.about(None,"message",res)
        if res == "Le livre a été emprunté." :
            self.ui.num_emprunt_input.clear()
            self.ui.reference_emprunt_input.clear()
            self.ui.date_emprunt_input.clear()
    def retourlivre(self):
        num1 = self.ui.num_retour_input.text()
        reference1 = self.ui.reference_retour_input.text()
        date_retour1 = self.ui.date_retour_input.text()
        res = biblio.rendre_livre(num1,reference1,date_retour1)
        QMessageBox.about(None,"message",res)
        if res == "Le livre a été rendu." :
            self.ui.num_retour_input.clear()
            self.ui.reference_retour_input.clear()
            self.ui.date_retour_input.clear()
    def supprimeremprunt(self):
        num1 = self.ui.num_emprunt_supprimer_input.text()
        reference1 = self.ui.reference_emprunt_supprimer_input.text()
        res = biblio.supprimer_emprunt(num1,reference1)
        QMessageBox.about(None,"message",res)
        if res == "l'emprunt a été supprimé." :
            self.ui.num_emprunt_supprimer_input.clear()
            self.ui.reference_emprunt_supprimer_input.clear()
    def modifier_emprunt_date(self):
        reference1 = self.ui.reference_emprunt_modifier_input.text()
        date_emprunt1 = self.ui.date_emprunt_modifier_input.text()
        res = biblio.modifier_emprunt_date(reference1,date_emprunt1)
        QMessageBox.about(None,"message",res)
        if res == "emprunt a été modifié." :
            self.ui.reference_emprunt_modifier_input.clear()
            self.ui.date_emprunt_modifier_input.clear()
    def modifier_retour_date(self):
        reference1 = self.ui.reference_emprunt_modifier_input_2.text()
        date_retour1 = self.ui.date_retour_modifier_input.text()
        res = biblio.modifier_retour_date(reference1,date_retour1)
        QMessageBox.about(None,"message",res)
        if res == "date retour a été modifié." :
            self.ui.reference_emprunt_modifier_input_2.clear()
            self.ui.date_retour_modifier_input.clear()
    def showemprunts(self):
        res = biblio.afficher_emprunts()
        if len(res) == 0:
            message = "Il n'y a pas des emprunts."
            QMessageBox.about(None,"message",message)
        else:
            self.remplir_table_emprunts(res,self.ui.tableWidget_emprunts)
    def showemprunts_reference(self):
        reference1 = self.ui.reference_emprunt_input_recherche.text()
        if (control_saisie.control_chaine_chiffres(reference1)):
            res = biblio.afficher_emprunts_reference(reference1)
            if len(res) == 0:
                message = "Il n'y a pas des emprunts de cette reference."
                QMessageBox.about(None,"message",message)
            else:
                self.remplir_table_emprunts(res,self.ui.tableWidget_emprunts_livre)
        else: 
            message = "verifier la reference"
            QMessageBox.about(None,"message",message)
            
    def showemprunts_num(self):
        num1 = self.ui.etudiant_emprunt_input_recherche.text()
        if (control_saisie.control_chaine_chiffres(num1)):
            res = biblio.afficher_emprunts_num(num1)
            if len(res) == 0:
                message = "Il n'y a pas des emprunts de ce numéro."
                QMessageBox.about(None,"message",message)
            else:
                self.remplir_table_emprunts(res,self.ui.tableWidget_emprunts_etudiant)
        else: 
            message = "verifier le numéro"
            QMessageBox.about(None,"message",message)
    def showemprunts_date_emprunt(self):
        date_emprunt1 = self.ui.date_emprunt_input_recherche.text()
        if (control_saisie.control_date(date_emprunt1)):
            res = biblio.afficher_emprunts_dateemprunt(date_emprunt1)
            if len(res) == 0:
                message = "Il n'y a pas des emprunts de cette date."
                QMessageBox.about(None,"message",message)
            else:
                self.remplir_table_emprunts(res,self.ui.tableWidget_emprunts_date)
        else: 
            message = "verifier la date"
            QMessageBox.about(None,"message",message)
    def showemprunts_date_retour(self):
        date_retour1 = self.ui.date_retour_input_recherche.text()
        if (control_saisie.control_date(date_retour1)):
            res = biblio.afficher_emprunts_dateretour(date_retour1)
            if len(res) == 0:
                message = "Il n'y a pas des emprunts de cette date."
                QMessageBox.about(None,"message",message)
            else:
                self.remplir_table_emprunts(res,self.ui.tableWidget_retour_date)
        else: 
            message = "verifier la date"
            QMessageBox.about(None,"message",message)   
    def showemprunts_2dates_emprunts(self):
        date_debut = self.ui.datedebut_emprunt_input_recherche.text()
        date_fin = self.ui.datefin_emprunt_input_recherche.text()
        if (control_saisie.control_date(date_fin)):
            if (control_saisie.control_date(date_debut)):
                res = biblio.afficher_emprunts_2dateemprunt(date_debut,date_fin)
                if len(res) == 0:
                    message = "Il n'y a pas des emprunts ."
                    QMessageBox.about(None,"message",message)
                else:
                    self.remplir_table_emprunts(res,self.ui.tableWidget_emprunts_2dates)
            else:
                message = "verifier la date de debut de format JJ/MM/AAAA"
                QMessageBox.about(None,"message",message)
        else: 
            message = "verifier la date de fin de format JJ/MM/AAAA"
            QMessageBox.about(None,"message",message)
    def showemprunts_2dates_retours(self):
        date_debut = self.ui.datedebut_retour_input_recherche_.text()
        date_fin = self.ui.datefin_retour_input_recherche.text()
        if (control_saisie.control_date(date_fin)):
            if (control_saisie.control_date(date_debut)):
                res = biblio.afficher_emprunts_2dateretour(date_debut,date_fin)
                if len(res) == 0:
                    message = "Il n'y a pas des emprunts ."
                    QMessageBox.about(None,"message",message)
                else:
                    self.remplir_table_emprunts(res,self.ui.tableWidget_retour_2dates)
            else:
                message = "verifier la date de debut de format JJ/MM/AAAA"
                QMessageBox.about(None,"message",message)
        else: 
            message = "verifier la date de fin format JJ/MM/AAAA"
            QMessageBox.about(None,"message",message)  
    def show_livres_alpha(self):
        res =biblio.afficher_livres_par_titre_alphabetique()
        if len(res) == 0:
            message = "Il n'y a pas de livres."
            QMessageBox.about(None,"message",message)
        else:
            self.ui.tableWidget_livres_alphabetique.setRowCount(len(res))    
            self.ui.tableWidget_livres_alphabetique.setColumnCount(4)
            self.ui.tableWidget_livres_alphabetique.setHorizontalHeaderLabels(("Reference","Titre","Auteur","Annee edition"))
            self.ui.tableWidget_livres_alphabetique.setColumnWidth(0,120)
            self.ui.tableWidget_livres_alphabetique.setColumnWidth(1,350)
            self.ui.tableWidget_livres_alphabetique.setColumnWidth(2,338)
            self.ui.tableWidget_livres_alphabetique.setColumnWidth(3,120)

            indice = 0
            for reference, livre in res:
                    self.ui.tableWidget_livres_alphabetique.setItem(indice, 0, QTableWidgetItem(str(reference)))
                    self.ui.tableWidget_livres_alphabetique.setItem(indice, 1, QTableWidgetItem(str(livre['titre'])))
                    self.ui.tableWidget_livres_alphabetique.setItem(indice, 2, QTableWidgetItem(str(livre['auteur'])))
                    self.ui.tableWidget_livres_alphabetique.setItem(indice, 3, QTableWidgetItem(str(livre['annee edition'])))
                    indice += 1
           
    def remplir_table_livres(self, livres, table):
        table.setRowCount(len(livres))    
        table.setColumnCount(4)
        table.setHorizontalHeaderLabels(("Reference","Titre","Auteur","Annee edition"))
        table.setColumnWidth(0,120)
        table.setColumnWidth(1,350)
        table.setColumnWidth(2,338)
        table.setColumnWidth(3,120)

        indice = 0
        for reference, livre in livres.items():
                table.setItem(indice, 0, QTableWidgetItem(str(reference)))
                table.setItem(indice, 1, QTableWidgetItem(str(livre['titre'])))
                table.setItem(indice, 2, QTableWidgetItem(str(livre['auteur'])))
                table.setItem(indice, 3, QTableWidgetItem(str(livre['annee edition'])))
                indice += 1
        
    def remplir_table_etudiants(self, etudiants, table):
        table.setRowCount(len(etudiants))    
        table.setColumnCount(9)
        table.setHorizontalHeaderLabels(("Numero inscri","Nom","Prenom","Date","Adresse","Mail","Telephone","Section","Niveau"))
        table.setColumnWidth(0,120)
        table.setColumnWidth(1,100)
        table.setColumnWidth(2,100)
        table.setColumnWidth(3,110)
        table.setColumnWidth(4,200)
        table.setColumnWidth(5,300)
        table.setColumnWidth(6,140)
        table.setColumnWidth(7,100)
        table.setColumnWidth(8,400)
        indice = 0
        for num, etudiant in etudiants.items():
                table.setItem(indice, 0, QTableWidgetItem(str(num)))
                table.setItem(indice, 1, QTableWidgetItem(str(etudiant['nom'])))
                table.setItem(indice, 2, QTableWidgetItem(str(etudiant['prenom'])))
                table.setItem(indice, 3, QTableWidgetItem(str(etudiant['date de naissance'])))
                table.setItem(indice, 4, QTableWidgetItem(str(etudiant['adresse'])))
                table.setItem(indice, 5, QTableWidgetItem(str(etudiant['mail'])))
                table.setItem(indice, 6, QTableWidgetItem(str(etudiant['telephone'])))
                table.setItem(indice, 7, QTableWidgetItem(str(etudiant['section'])))
                table.setItem(indice, 8, QTableWidgetItem(str(etudiant['niveau etude'])))
                indice += 1
                
    def remplir_table_emprunts(self, emprunts, table):
        table.setRowCount(len(emprunts))    
        table.setColumnCount(7)
        table.setHorizontalHeaderLabels(("Reference","Titre","Numero","Nom","Prénom","Date emprunt","Date retour"))
        table.setColumnWidth(0,120)
        table.setColumnWidth(1,200)
        table.setColumnWidth(2,100)
        table.setColumnWidth(3,100)
        table.setColumnWidth(4,100)
        table.setColumnWidth(5,100)
        table.setColumnWidth(6,100)
        indice = 0
        for reference, emprunt in emprunts.items():
                table.setItem(indice, 0, QTableWidgetItem(str(reference)))
                table.setItem(indice, 1, QTableWidgetItem(str(emprunt['Titre'])))
                table.setItem(indice, 2, QTableWidgetItem(str(emprunt['Numéro'])))
                table.setItem(indice, 3, QTableWidgetItem(str(emprunt['Nom'])))
                table.setItem(indice, 4, QTableWidgetItem(str(emprunt['Prénom'])))
                table.setItem(indice, 5, QTableWidgetItem(str(emprunt["date emprunt"])))
                table.setItem(indice, 6, QTableWidgetItem(str(emprunt['date retour'])))
                indice += 1            
    
            
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())

