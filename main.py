# # 1 Läs och förstå
# #1A
# class SafeStorage:
#     __data = None
#     def get(self):
#         return self.__data
#     def put(self, data):
#         self.__data = data
#
# safe = SafeStorage()
# safe.put("Anakonda")
# x = safe.get()
# safe.put("Boaorm")
# y = safe.get()
# print(x, y)
# # Den skapar en klass för safestorage som är tom ==None
# # Vi har två funktioner i klassen som tillåter användaren att lägga till och ta bort saker i safestorage
# # först ger vi variablen safe samma som safestorage()
# # Vi lägger till genom att ta sage.storge och vi lägger till en Anakonda
# # Samma sak igen med vi lägger till en boaorm
#
# #2A & B
# #vad gör följande kod ?
# class Animal: # En klass vid namn animal.
#     def make_noise(self): # Klassen består av en funktion make noise som är sig själv
#         print("Detta djur har vi inget ljud för.")
#
# class Dog(Animal): # Här gör vi en klass för hund som definerar en funktion för hundens läte som använder klassen animal
#     def make_noise(self):
#         print("Voff!")
#
# class Cat(Animal): # Här gör vi en klass för katt där vi definerar en funktion för kattens läte som använder klassen animal
#     def make_noise(self):
#         print("Mjau!")
#
# class fish(Animal):
#     pass
#
# def sound_off(Animal): # Här gör vi en funktion som skall hämta klasser och deras inbyggda funktioner.
#     Animal.make_noise()
#
# class Rooster(Animal):
#     def make_noise(self):
#         print("Kockelku!")
#
# class cow(Animal):
#     def make_noise(self):
#         print("MUUUU")
#
# c = Cat()
# d = Dog()
# h = Rooster()
# f = fish()
# t = cow()
#
# sound_off (t)
# sound_off(d)
# sound_off(h)
# sound_off(f)

# 2 Länder
#1A
class Country:
    def __init__(self, name, pop, lang, area = None):
        self.__name = name
        self.__population = pop
        self.__area = area
        self.__language = lang
    def print_info(self):
        print(f"\nI {self.__name} bor det {self.__population} personer och arean är {self.__area} kvadrat KM, Språk som talas i landet är")
        for lang in self.__language:
            print(lang + ",", end=" ")




# se = Country("Sverige", round(10.5,1) )
IS = Country("Island",round(383726,0),["Islandic"])
IS.print_info()
den = Country("Danmark",round(5961249,0),["Gröt", "Engelska"], 25.5, )
den.print_info()