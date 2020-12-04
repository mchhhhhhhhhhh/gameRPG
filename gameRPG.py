class hero:
    def __init__(self,name,health,attack,geo_x,geo_y):
        self.name=name
        self.health=health
        self.attack=attack
        self.geo_x=geo_x
        self.geo_y=geo_y
    def attack_to_hero(self,damage):
        self.health=self.health-damage
        return self.health
    def forward(self):
        self.geo_x=self.geo_x+1
    def backward(self):
        self.geo_x=self.geo_x-1
    def upward(self):
        self.geo_y=self.geo_y+1
    def downward(self):
        self.geo_y=self.geo_y-1

class monster:
    def __init__(self,name,health,attack,geo_x,geo_y):
        self.name=name
        self.health=health
        self.attack=attack
        self.geo_x=geo_x
        self.geo_y=geo_y
    def attack_to_hero(self,damage):
        self.health=self.health-damage
        return self.health

class sund:
    def __init__(self,geo_x,geo_y):
        self.geo_x=geo_x
        self.geo_y=geo_y

print("Введите здоровье Коляна:")
h_Kolyan=int(input())
print("Введите атаку Коляна:")
A_Kolyan=int(input())

Kolyan=hero('Kolyan',h_Kolyan,A_Kolyan,0,0)
ushlepok=monster('ushlepok',9,7,2,4)
sund=sund(3,5)
while(1):
    print("Шагай")
    a=input()
    if(a=='d'):
        Kolyan.forward()
        print("Координаты Коляна:", Kolyan.geo_x, Kolyan.geo_y)
    if(a=='a'):
        Kolyan.backward()
        print("Координаты Коляна:",Kolyan.geo_x, Kolyan.geo_y)
    if(a=='w'):
        Kolyan.upward()
        print("Координаты Коляна:",Kolyan.geo_x, Kolyan.geo_y)
    if(a=='s'):
        Kolyan.downward()
        print("Координаты Коляна:",Kolyan.geo_x, Kolyan.geo_y)
    if((Kolyan.geo_x==ushlepok.geo_x)and(Kolyan.geo_y==ushlepok.geo_y)):
        break
    if((Kolyan.geo_x==sund.geo_x)and(Kolyan.geo_y==sund.geo_y)):
        print("В сундуке ничё нет. Разочарование((((((((((((")
print("Драка")
while((Kolyan.health>0)or(ushlepok.health>0)):
    if(Kolyan.health>ushlepok.health):
        print("Бьёт Колян")
        ushlepok.attack_to_hero(8)
        print("Здоровье ушлёпка:", ushlepok.health)
        if((Kolyan.health<1)or(ushlepok.health<1)):
                          break
        print("Бьёт ушлепок")
        Kolyan.attack_to_hero(7)
        print("Здоровье Коляна:",Kolyan.health)
        if((Kolyan.health<1)or(ushlepok.health<1)):
                          break
    if(Kolyan.health<ushlepok.health):
        print("Бьёт ушлепок")
        Kolyan.attack_to_hero(7)
        print("Здоровье Коляна:",Kolyan.health)
        if((Kolyan.health<1)or(ushlepok.health<1)):
                          break
        print("Бьёт Колян")
        ushlepok.attack_to_hero(8)
        print("Здоровье ушлёпка:", ushlepok.health)
        if((Kolyan.health<1)or(ushlepok.health<1)):
                          break
    if(Kolyan.health==ushlepok.health):
        if(Kolyan.attack>ushlepok.attack):
            print("Бьёт Колян")
            ushlepok.attack_to_hero(8)
            print("Здоровье ушлёпка:", ushlepok.health)
            if((Kolyan.health<1)or(ushlepok.health<1)):
                          break
            print("Бьёт ушлепок")
            Kolyan.attack_to_hero(7)
            print("Здоровье Коляна:",Kolyan.health)
            if((Kolyan.health<1)or(ushlepok.health<1)):
                          break
        if(Kolyan.attack<ushlepok.attack):
            print("Бьёт ушлепок")
            Kolyan.attack_to_hero(7)
            print("Здоровье Коляна:",Kolyan.health)
            if((Kolyan.health<1)or(ushlepok.health<1)):
                          break
            print("Бьёт Колян")
            ushlepok.attack_to_hero(8)
            print("Здоровье ушлёпка:", ushlepok.health)
            if((Kolyan.health<1)or(ushlepok.health<1)):
                          break
    if((Kolyan.health<1)or(ushlepok.health<1)):
                          break
if(Kolyan.health<1):
        print("Колян проиграл")
if(ushlepok.health<1):
        print("ушлёпок проиграл")
