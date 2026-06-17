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
# class Country:
#     def __init__(self, name, pop, lang, area = None):
#         self.__name = name
#         self.__population = pop
#         self.__area = area
#         self.__language = lang
#     def print_info(self):
#         print(f"\nI {self.__name} bor det {self.__population} personer och arean är {self.__area} kvadrat KM, Språk som talas i landet är")
#         for lang in self.__language:
#             print(lang + ",", end=" ")
#
#
#
#
# # se = Country("Sverige", round(10.5,1) )
# IS = Country("Island",round(383726,0),["Islandic"])
# IS.print_info()
# den = Country("Danmark",round(5961249,0),["Gröt", "Engelska"], 25.5, )
# den.print_info()

#3
#Banken
class bank_account():
    def __init__(self):
        self.balance = 0
        self.interest = 1.4

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} har satt in ditt nuvaranda saldo är", self.balance)
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        print(f"{amount} har tagits ut, ditt nuvarande saldo är", self.balance)
        return amount

    def check_saldo(self):
        print(f"{self.balance} är ditt nuvarande saldo")
        return self.balance

    def check_interest(self):
        self.balance += self.interest / 12 * self.balance
        print(f"Värdet på kontot efter applicerad ränta blir {self.balance}")
        return self.balance

    def faktura_betalning(self, amount):
        if amount >= self.balance:
            return False
        else:
            return True

#4
# Webbshop
class webshop():
    def __init__(self):
        self.kundvagn = kundvagn() # Vi deklarer att classen innehåller kundvagn, produkter och Id
        self. produkter = []
        self.id = 0
    def remove_to_cart(self, id): # I denna klass har vi en funktion som tillåter oss att plocka varor från shoppen till kundvagnen.
        for i in self.produkter:# Här kör vi en loop som letar efter alla produkter, om produktens id matchar id vi letar efter flyttas den till kundvagn.
            if i.id == id:
                self.kundvagn.add_to_cart(i)
                i.quantity -= 1 # För att inte varan ska försvinna helt har vi deklarerat hur många av samma vara vi har när vi lägger in den och att den minskar med en för varje gång vi tar ut den.
                break
    def print_all_products(self):
        for i in self.produkter:
            print(i.name, i.pris,":-", "id:",i.id) # Här har vi en funktion som printar ut alla produkter i webshoppen

    def add_produkt(self, produkt):
        self.produkter.append(produkt) # Här har vi en funktion som tillåter användaren att lägga till produkter till webshoppen.
        self.id += 1 # Varje gång en produkt läggs till adderas ID med 1.
        produkt.id = self.id


class produkt():
    def __init__(self, pris, name,quantity ): # Här skappar vi klassen för produkten
        self.pris = pris # Den innehåller pris som använder sätter
        self.id = None # Den innehåller ID som automatiskt sätt i funktionen när den läggs till i shoppen
        self.name = name # Namn på produkten sätts av användaren
        self.quantity = quantity # Och kvantitet på produkten

class kundvagn(): # Här skapar vi klassen för kundvagn
    def __init__(self):
        self.varor =[] # Den har en variabel vid namn varor som är tom

    def add_to_cart(self, produkt): # Till detta har vi en funktion för att lägga till varor till sin varukorg
       self.varor.append(produkt)

    def print_all_cart_products(self): # Sist en funktion för att pringa alla varor i korgen
        for i in self.varor:
            print(i.name, i.pris,":-", "id:",i.id)


shop = webshop() # Här skapar vi objeket för webshop()

skruvmejsel = produkt(199, "skruvmejsel", 10) # Här skapar vi en massa objekt för klassen produkt
saw = produkt(250,"saw", 10)
skifnyckel = produkt(400,"skifnyckel", 10)
kattstrypare = produkt(99,"kattstrypare", 10)
tumstock = produkt(229,"tumstock",10)
skruvar = produkt(89, "Skruvar",10)
vattenpass_long = produkt(799,"långt vattenpass",10)
vattenpass_kort = produkt(399,"kort vattenpass",10)
snickarbord = produkt (2999,"Snickarbord",10)
Skruvdragare = produkt (1999, "Kärcher skruvdragare",10)

shop.add_produkt(skruvmejsel)
shop.add_produkt(saw)
shop.add_produkt(kattstrypare)
shop.add_produkt(tumstock)
shop.add_produkt(skruvar)
shop.add_produkt(vattenpass_long)
shop.add_produkt(vattenpass_kort)
shop.add_produkt(snickarbord)
shop.add_produkt(Skruvdragare)


shop.remove_to_cart(skruvmejsel.id)
shop.remove_to_cart(Skruvdragare.id)
shop.remove_to_cart(snickarbord.id)
shop.print_all_products()
print("\n")

shop.kundvagn.print_all_cart_products()