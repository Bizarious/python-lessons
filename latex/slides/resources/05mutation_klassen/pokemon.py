
class Pokemon:
    def __init__(self, name, max_hp, current_hp, attack_power):
        self.name = name
        self.max_hp = max_hp
        self.current_hp = current_hp
        self.attack_power = attack_power

    def attack(self, other_pokemon):
        if self.current_hp == 0:
            print(f"{self.name} kann nicht mehr länger kämpfen")
            return
        print(f"{self.name} greift {other_pokemon.name} an.")
        other_pokemon.take_attack(self.attack_power)

    def take_attack(self, amount):
        self.current_hp -= amount
        if self.current_hp <= 0:
            self.current_hp = 0
            print(f"{self.name} kann nicht mehr länger kämpfen")
        print(f"{self.name} hat noch {self.current_hp} / {self.max_hp} HP")
        
    def heal(self):
        self.current_hp = self.max_hp
        print(f"{self.name} wurde geheilt")

bisasam = Pokemon("Bisasam", 40, 40, 30)
glurak = Pokemon("Glurak", 40, 40, 10)

while True:
    action = input()
    if action == '0':
        break
    elif action == '1':
        bisasam.attack(glurak)
    elif action == '2':
        glurak.attack(bisasam)
