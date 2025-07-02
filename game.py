import random
from jarre import Jarre

class JarreGame:
    def __init__(self):
        self.compteur = 0
        self.jarres = []
        self.serpents = []
        self.bonus = None
        self.malus = None
        self.reset_game()

    def reset_game(self):
        self.compteur = 0
        self.jarres = [Jarre(i, (i % 5) * 150, (i // 5) * 150) for i in range(20)]

        self.serpents = random.sample(range(20), 2)
        restants = list(set(range(20)) - set(self.serpents))
        self.malus = random.choice(restants)
        restants.remove(self.malus)
        self.bonus = random.choice(restants)

    def click_jarre(self, index):
        if index < 0 or index >= 20:
            return {"error": "index invalide"}

        jarre = self.jarres[index]

        if jarre.state != "hidden":
            return {"message": "déjà cliquée", "state": jarre.state}

        if index in self.serpents:
            jarre.set_state("serpent")
        elif index == self.malus:
            jarre.set_state("malus")
            self.compteur *= 2
        elif index == self.bonus:
            jarre.set_state("bonus")
        else:
            jarre.set_state("beer")
            self.compteur += 1

        return {
            "index": index,
            "new_state": jarre.state,
            "compteur": self.compteur
        }

    def get_state(self):
        return {
            "jarres": [j.state for j in self.jarres],
            "compteur": self.compteur
        }
