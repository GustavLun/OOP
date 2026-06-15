# 1 Läs och förstå
#1A
class SafeStorage:
    __data = None
    def get(self):
        return self.__data
    def put(self, data):
        self.__data = data

safe = SafeStorage()
safe.put("Anakonda")
x = safe.get()
safe.put("Boaorm")
y = safe.get()
print(x, y)
# Den skapar en klass för safestorage som är tom ==None
# Vi har två funktioner i klassen som tillåter användaren att lägga till och ta bort saker i safestorage
# först ger vi variablen safe samma som safestorage()
# Vi lägger till genom att ta sage.storge och vi lägger till en Anakonda
# Samma sak igen med vi lägger till en boaorm
