#print('Hi')

#OOPs Example



class Player:
    membership=True #Class Object Atrribute ,not Dynamic , All objects have access

    def __init__(self,name='Anonymys',age=0):  #Default Parameters
#        if self.membership:
         if Player.membership:
             if age>= 18:
                self.name = name #These are Attributes
                self.age=age

    # def shout(self,study):
    #     print(f'My name is {self.name}')
    #     print('f I want to study')
    #     return 'self'

    def run(self):
        print('run')
        return 'done'


player1=Player('Amit',39)
player2=Player('Saumya',34)


#player1=Player()
#player2=Player()

player3=Player('Vaanya',4)

#print(player1) #<__main__.Player object at 0x0000024930137400>  -- tells memory loc of object player1
print(player1.name,end=":") #Amit will come
print(player1.age,end= "!\n")

print(player2.name,end=":") #Saumya  will come
print(player2.age,end= "!\n")

#print(player3.name)
#print(player3.age)  #AttributeError: 'Player' object has no attribute 'name



#player2.attack=50
#print(player2.attack)
#help(player1)
#help(list)
#print(player1.membership)
#print(player1.shout('Study'))