# Gestion des activités d'une boutique de vente d'articles

# Importations
from vue.index import faire_choix_menu

# VARIABLES
welcome = "Bienvenue dans votre Systeme de Gestion d'articles et de ventes d'articles."

menu = "MENU :\n\
Gestion des articles :\n\
\ta- Saisie des articles\n\
\tb- Liste des articles\n\
\tc- Recherche d'un article\n\
Gestion des ventes :\n\
\td- Enregistrement d'une vente\n\
\te- Liste des ventes\n\
\tf- Montant total des ventes"

liste_articles : list = []
liste_ventes : list = []


## Fonction main du programme
def main(liste_articles : list, liste_ventes : list):
    print(welcome)
    quitter = False
    while not quitter:
        print(menu)
        faire_choix_menu(liste_articles, liste_ventes)
        choix = input("Revoir le menu, oui ? ")
        if choix.lower() != "oui":
            quitter = True
    print("Merci, a la prochaine !")


# EXECUTION DE LA FONCTION DU PROGRAMME
if __name__ == "__main__":
    main(liste_articles, liste_ventes)