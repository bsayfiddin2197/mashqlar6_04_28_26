class Shaxs:
    def __init__(self, ism):
        self.ism = ism

    def salom(self):
        print(f"Ism: {self.ism}")

class Oqtuvchi(Shaxs):
    def __init__(self, ism, fan):
        super().__init__(ism)
        self.fan = fan

    def salom(self):
        super().salom()
        print(f"fan: {self.fan}")

oq = Oqtuvchi("Diloza", "Matematika")
oq.salom()
