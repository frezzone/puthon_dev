print ( "bienvenu chez credit mituel bank , veuillez introduire votre identité SVP  " )
action1 = input( "souhaitez vous faire une nouvelle transaction aujrd8 ? oui(o) ou non (n) : "  ).strip()
while action1== "o" :
    print ( "-" * 80)

    print ( "bienvenu chez credit mituel bank , veuillez introduire votre identité SVP  " )

    print ( "-" * 80)
    transaction =[]
    N_transaction = 1005
    login = (input('entrez votre nom ')).strip().capitalize
    password = int(input('entrez votre numero bancaire '))
    print ( "-" * 80)
    somme_transmisie = int(input('veuillez introduire la somme que vous souhaitez transmettre   '))
    destinataie  = int(input('entrez le numero de carte de la personne destinataie  :   '))
    destinataie_name = (input('entrez le nom de votre destinataire '))
    vvt_number= int(input('entrez le numero vvt : '))
    print ( "-" * 80)
    action = input( "etes vous sur de vouloir continuer ? oui(o) ou non (n) : "  ).strip()
    print ( "-" * 80)
    if action == "o" :
       print ( "-" * 80)
       N_transaction = N_transaction + 1 
       transaction =[[N_transaction,destinataie_name,destinataie,vvt_number,somme_transmisie,"EUR"]]
       print ( "-" * 80)
       print ( f"Une somme de {somme_transmisie } EURO à bien été transmise a MR/Mme {destinataie_name } sous le Numero de transaction {N_transaction }" )
       print ( transaction)
    else :
        action = input( "que souhaiter vous faire  ? modifiler (m) ou annuler (n) : "  ).strip()
        if action == "m" :
            new_somme_transmisie = int(input('veuillez introduire la nouvelle somme que vous souhaitez transmettre   '))
            transaction =[[N_transaction,destinataie_name,destinataie,vvt_number,new_somme_transmisie,"EUR"]]
            print ( "-" * 80)
            print ( f"Une somme de {new_somme_transmisie } EURO à bien été transmise a MR/Mme {destinataie_name } sous le Numero de transaction {N_transaction }" )
            print ( transaction)
        else :
            print ( "la credit mituel bank vous souhaite une exelante journée " )
else :
 block =[[transaction]]
 print (block)
       