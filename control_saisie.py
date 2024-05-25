# Module control_saisie.py
from datetime import datetime
import re

def control_date(date):
  # Définit le format de la date comme JJ/MM/AAAA
  format_date = "%d/%m/%Y"
  try:
    datetime.strptime(date, format_date)
    return True
  except ValueError:
    return False

def control_chaine_chiffres(ch):
  chaine_sans_espaces = ch.strip()
  return chaine_sans_espaces.isnumeric()

def control_numero(ch):
  chaine_sans_espaces = ch.strip()
  return (chaine_sans_espaces.isnumeric() and (len(chaine_sans_espaces)==8))

def control_chaine_lettres(ch):
  chaine_sans_espaces = ch.replace(" ", "")  
  return chaine_sans_espaces.isalpha()

def control_email(email):
  regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
  match = re.fullmatch(regex, email)
  return bool(match)

def compare_dates(date1, date2):

    date1_obj = datetime.strptime(date1, "%d/%m/%Y")
    date2_obj = datetime.strptime(date2, "%d/%m/%Y")
    if date1_obj <= date2_obj:
        return 0
    else:
        return 1