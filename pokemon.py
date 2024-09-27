import time

class pokemones:

    def __init__(self, nom, poid = float, pattes = int, freq_card = int, taille = float, heure_tv = int, nageoires = int,vitesse = float) :
        self.__nom = nom
        self.__poid = poid
        self.__pattes = pattes
        self.__freq_card = freq_card
        self.__taille = taille
        self.__heure_tv = heure_tv
        self.__nageoires = nageoires
        self.__vitesse = vitesse

    def poke_sport(self,):
        self.__vitesse = self.__pattes * 3
        
    def poke_carn(self,):
        self.__vitesse = self.__pattes * self.__taille * 3
    
    def poke_mers(self,):
        self.__vitesse = (self.__poid / 25) * self.__nageoires
    
    def poke_crois(self,):
        self.__vitesse = (self.__poid / 25 * self.__nageoires) / 2
    

    def 