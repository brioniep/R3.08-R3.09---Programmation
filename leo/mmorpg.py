import time



# 2. LE CONTEXTE

class Personnage:

    # Fonction constructeur
    def __init__(self, pseudo, niveau=1, life_points=None, initiative=None):
        self.pseudo = pseudo
        self.niveau = niveau

        # Si les points de vie et l'initiative ne sont pas spécifiés, ils sont égaux au niveau
        self.life_points = life_points if life_points is not None else niveau
        self.initiative = initiative if initiative is not None else niveau
    
    # Fonction pour afficher le profil d'un joueur
    def afficher_profil(self):
        print("Création du profil...")        
        time.sleep(1.5)
        print("--------------------------------------")
        print(f"Bienvenue à toi {self.pseudo}, voici ton profil")
        print(f" - Niveau : {self.niveau}")
        print(f" - Points de vie : {self.life_points}")
        print(f" - Initiative : {self.initiative}")
        print("--------------------------------------")
    
    # Méthode pour attaquer un autre personnage
    def attaquer(self, autre_personnage):
        if self.initiative > autre_personnage.initiative:
            autre_personnage.life_points -= self.niveau
            if autre_personnage.life_points > 0:
                self.life_points -= autre_personnage.niveau
        
        elif autre_personnage.initiative > self.initiative:
            self.life_points -= autre_personnage.niveau
            if self.life_points > 0:
                autre_personnage.life_points -= self.niveau
        
        else:
            self.life_points -= autre_personnage.niveau
            autre_personnage.life_points -= self.niveau


    # Méthode pour mener le combat jusqu'à la mort d'un des personnages
    def combat(self, autre_personnage):
        while self.life_points > 0 and autre_personnage.life_points > 0:
            self.attaquer(autre_personnage)
            if self.life_points <= 0 or autre_personnage.life_points <= 0:
                break


        if self.life_points > 0:
            print(f"{self.pseudo} a gagné le combat contre {autre_personnage.pseudo} !")
        elif autre_personnage.life_points > 0:
            print(f"{autre_personnage.pseudo} a gagné le combat contre {self.pseudo} !")
        else:
            print(f"Les deux personnages, {self.pseudo} et {autre_personnage.pseudo}, se sont entretués !")



    # Méthode pour soigner le personnage jusqu'à son niveau
    def soigner(self):
        if self.life_points < self.niveau:
            self.life_points = self.niveau
            print(f"{self.pseudo} a été soigné ! Points de vie restaurés à {self.life_points}.")
        else:
            print(f"{self.pseudo} a déjà tous ses points de vie.")




# 3. LA NOTION  D'HERITAGE

# Sous-classe Guerrier
class Guerrier(Personnage):

    def __init__(self, pseudo, niveau=1,):
        life_points = niveau * 8 + 4
        initiative = niveau * 4 + 4
        super().__init__(pseudo, niveau, life_points, initiative)
    
# Sous-classe Mage
class Mage(Personnage):

    def __init__(self, pseudo, niveau=1,):
        life_points = niveau *5 + 10
        initiative = niveau * 6 + 4
        self.mana = niveau * 5

        super().__init__(pseudo, niveau, life_points, initiative)

    def afficher_profil(self):
        super().afficher_profil()
        print(f" - Mana : {self.mana}")






def main():
    guerrier = Guerrier(pseudo="Léonard", niveau=3)
    mage = Mage(pseudo="Adel", niveau=1)
    
    guerrier.afficher_profil()
    mage.afficher_profil()

    # Passe l'instance de Mage, pas la classe
    guerrier.combat(mage)

    # Exemples supplémentaires
    # perso1 = Personnage(pseudo="Adel")
    # perso1.afficher_profil()

    # perso2 = Personnage(pseudo="Leonard", niveau=1)
    # perso2.afficher_profil()

    # perso1.combat(perso2)

    # perso1.soigner()
    # perso2.soigner()

if __name__ == "__main__":
    main()
