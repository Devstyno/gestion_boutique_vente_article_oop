import datetime
from modele.article import Article

class Vente:
    """Classe de vente. Une vente est definie par un article, une quantite d'achat et un prix total de vente."""

    effectif = 0

    # constructor
    def __init__(self, article : Article, quantite_achetee : int):
        self.__article = article
        self.__quantite_achetee = quantite_achetee
        
        self.__created_date = datetime.datetime.now()
        self.__is_active = True

        Vente.effectif += 1
        self.__id = Vente.effectif

    # id property
    def get_id(self):
        return self.__id

    id = property(get_id)

    # article property
    def get_article(self):
        return self.__article
    
    def set_article(self, value : Article):
        self.__article = value

    article = property(get_article, set_article)

    # quantite_achetee property
    def get_quantite_achetee(self):
        return self.__quantite_achetee
    
    def set_quantite_achetee(self, value : int):
        self.__quantite_achetee = value

    quantite_achetee = property(get_quantite_achetee, set_quantite_achetee)

    # prix_total property
    def get_prix_total(self):
        return self.__article.prix_unitaire * self.__quantite_achetee

    prix_total = property(get_prix_total)

    # created_date property
    def get_created_date(self):
        return self.__created_date

    created_date = property(get_created_date)

    # is_active property
    def get_is_active(self):
        return self.__is_active
    
    def set_is_active(self):
        self.__is_active = not self.__is_active

    is_active = property(get_is_active, set_is_active)

    def details(self):
        return f"{self.id}\t\t\t{self.article.libelle}\t\t\t{self.article.prix_unitaire}\t\t\t{self.quantite_achetee}\t\t\t{self.prix_total}"