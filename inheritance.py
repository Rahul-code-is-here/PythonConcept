class Mamals:
    def walk(self):
        print("walk")


class Dog(Mamals):
    #pass      dog object ne empty rakhva pass use thai
    def bark(self):
        print("dogs bark")


class cat(Mamals):
    #pass  empty rakhvu hoy tyare pass
    def annoying(self):
        print("cat's are annoying")


dog1=Dog()
dog1.walk()
dog1.bark()

cat1=cat()
cat1.walk()
cat1.annoying()