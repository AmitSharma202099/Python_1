# Gaming Program

class Game:
    membership = True  # Class (Game) Attribute ,not dynamic not modified ,doesn't change across instances

    def __init__(self, name='anonymymous', age=1):
        #        if (self.membership):
        #if (Game.membership):
        if(age>=18):
            self.name = name
            self.age = age

    def play(self):
        print(f'{self.name} you are an an Authorised Member {self.membership} & Paid fees {self.payment()}' '\n'
              f'Lets Play! You are Energitc & Young Age {self.age} is just a number and  {self.result()}')
        return "Its Fun...."

    def result(self):
        #print("You Won!")
        return "You Won Congrats!"

    def payment(self):
        #print("Money Paid")
        return "Money Paid Continue..."
    @classmethod
    def add_objects(cls,num1,num2):
        return num1+num2
    @staticmethod
    def add_static_objects(num1,num2):
        return num1+num2


player1 = Game("Amit", 39)
player2 = Game("Saumya", 35)
player1.program= "Python!"
player2.program = "Java!"

player3: Game=Game('Vaanya',4)

print(player1.add_objects(1,2))
print(Game.add_objects(1,2))
print(player1.add_static_objects(5,9))

#print(f'Player Name is {player1.name} and Player Age is  {player1.age}',end=":\n")  # calling Attribute of a class from Gamme(Class) Object player1
print(player1.play())
#print(player2.name, end=":\n")
print(player2.play())
print(player3.play())
#print(player1.program)
#print(player2.program)

# player1.play('Saumya')
#print(player2.membership)
