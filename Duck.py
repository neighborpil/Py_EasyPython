class Duck:
    def Quack(self):

        print("ㄴQuaaaack!")

    def feathers(self):
        print("The duck has white and gray feathers.")

class Person:
    def Quack(self):
        print("The person imitates a duck.")
    def feathers(self):
        print("The person takes a feather from the ground and show it.")
    def name(self):
        print("John Smith")

def in_the_forest(duck): #in_the_forest에게 duck이란 Quack()와 feathers()를 가지고 잇는 것이다
    duck.Quack()
    duck.feathers()

def game():
    donald = Duck()
    john = Person()
    in_the_forest(donald)
    in_the_forest(john) #명확한 상속의 개념 없이 상속을 구

game()




    
