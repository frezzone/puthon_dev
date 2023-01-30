ouverture = int(input('entrez votre heure d\'ouverture '))
fermeture = int(input('entrez votre heure de fermeture '))
crenau = [ ]
if fermeture < ouverture :
    print ( f"erreur l\'heure d\'ouveture : {ouverture} H ne peut pas etre superieure a l\'heure de fermeture {fermeture} H  " )
    new_hour = input( "voulez vous maittre a nouveau creneau  ? oui(o) ou non (n) " ).strip().capitalize
    if new_hour == "o" :
      ouverture = int(input('entrez votre nouvelle heure d\'ouverture ')) 
      crenau = [ouverture ,fermeture ]
      crenaux_aprem = (input('avez vous un crenaux de plus dans la journée oui(o) ou non (n) ?')).strip().capitalize 
      if crenaux_aprem == "o" :
        ouvertur_aprem = int(input('entrez votre heure d\'ouverture '))  
        fermeture_aprem = int(input('entrez votre heure de fermeture '))
        heure_finale = [[crenau ],[ouvertur_aprem ,fermeture_aprem ] ]
      elif crenaux_aprem == "n" :
        crenau = [ouverture ,fermeture ]
        print ( "a la prochaine :) " )
    else :
        print ( "a la prochaine :) " )
else:
    crenaux_aprem =(input('avez vous un crenaux de plus dans la journée oui(o) ou non (n) ?')).strip().capitalize 
    if crenaux_aprem == "o" :
        ouvertur_aprem = int(input('entrez votre heure d\'ouverture '))    
        fermeture_aprem = int(input('entrez votre heure de fermeture '))
        heure_finale = [[crenau ],[ouvertur_aprem ,fermeture_aprem ] ]
    elif crenaux_aprem == "n" :
        
       print ( "a la prochaine :) " )