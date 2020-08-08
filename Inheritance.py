class All_User:
    def sign_in(self):
        print("Logged in ")

class Cricketer(All_User):
    def __init__(self,name,century,award):
        self.name=name
        self.century=century
        self.award=award

    def Award(self):
         print(f'Player got the Team Awards {self.award}')


class Tennis(All_User):
    def __init__(self,name,holes,award):
        self.name=name
        self.holes=holes
        self.award=award

    def Award(self):
         print(f'Player got the IC Awards {self.award}')

cricket1 = Cricketer('Amit',100,72)
print(cricket1.sign_in())
tennis1= Tennis('Saumya',200,88)

cricket1.Award()
tennis1.Award()

print(isinstance(cricket1,Cricketer))
print(isinstance(cricket1,All_User))
print(isinstance(cricket1,object))

for char in [cricket1,tennis1]:   #polymorphish example
    char.Award()