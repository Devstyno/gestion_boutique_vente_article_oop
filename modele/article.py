import datetime

class Article:
    """Classe d'article. Un article est defini par un libelle, un prix unitaire et une quantite en stock."""

    effectif = 0

    # constructor
    def __init__(self, libelle : str, prix_unitaire : float, quantite_en_stock : int):
        self.__libelle = libelle
        self.__prix_unitaire = prix_unitaire
        self.__quantite_en_stock = quantite_en_stock
        
        self.__created_date = datetime.datetime.now()
        self.__is_active = True

        Article.effectif += 1
        self.__id = Article.effectif

    # id property
    def get_id(self):
        return self.__id

    id = property(get_id)

    # libelle property
    def get_libelle(self):
        return self.__libelle
    
    def set_libelle(self, value : str):
        self.__libelle = value

    libelle = property(get_libelle, set_libelle)

    # prix_unitaire property
    def get_prix_unitaire(self):
        return self.__prix_unitaire
    
    def set_prix_unitaire(self, value : float):
        self.__prix_unitaire = value

    prix_unitaire = property(get_prix_unitaire, set_prix_unitaire)

    # quantite_en_stock property
    def get_quantite_en_stock(self):
        return self.__quantite_en_stock
    
    def set_quantite_en_stock(self, value : int):
        self.__quantite_en_stock = value

    quantite_en_stock = property(get_quantite_en_stock, set_quantite_en_stock)

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

    def decrease_qtte_stock(self, value):
        self.quantite_en_stock -= value

    def details(self):
        return f"{self.id}\t\t\t{self.libelle}\t\t\t{self.prix_unitaire}\t\t\t{self.quantite_en_stock}"