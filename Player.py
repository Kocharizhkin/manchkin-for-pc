class Munchkin:
    level = 1
    gender = 'male'
    trust_level = 50
    race = []
    profession = []
    big_clothes = [0,1]
    shoes = [0,0]
    headdress = [0,0]
    armor = [0,0]
    non_hand_clothes = [0,0]
    hand = [0,0]
    def dmg_counter(self):
        dmg =Munchkin.big_clothes[1]+Munchkin.shoes[1]+Munchkin.shoes[1]+Munchkin.armor[1]+Munchkin.non_hand_clothes[1]+Munchkin.hand[1] + Munchkin.level
        print(dmg)
