# create a class 'pets' from a class 'Animal' and further create a class 'Dog' from 'Pets' . Add
# a method 'bark' to class 'Dog'.
class animal:
    pass
class pets(animal):
    pass
class dog(pets):
    @staticmethod
    def bark():
        print("Barking")

a = dog()
a.bark()