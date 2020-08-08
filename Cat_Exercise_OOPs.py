# Given the below class:


class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age




# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('White', 3)
cat2 = Cat('Black', 2)
cat3 = Cat('Green', 1)

# 2 Create a function that finds the oldest cat
#def cat_age(self):
def cat_age(*args):
    #if (cat1.age > cat2.age and cat2.age > cat3.age):
        #print(f'cat age is {self.age}')
        return max(args)

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

print(f"The Oldest cat is {cat_age(cat1.age,cat2.age,cat3.age)} Year Old!")

#print(cat1.cat_age())
#print(cat2.cat_age())
#print(cat3.cat_age())
# cat1.age
