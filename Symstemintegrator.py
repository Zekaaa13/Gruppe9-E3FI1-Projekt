from unicodedata import name


class Systemintegrator():
    def __init__(self, name, alter, jahreErfahrung):
        self.name = name
        self.alter = alter
        self.jahreErfahrung = jahreErfahrung
    def __str__(self):
        return "" % (self.name,)
    
    def getName__(self, name: str):
        pass
    def setName__(self, name: str):
        self.__name = name
    def getAlter__(self, alter: int):
        pass
    def setAlter_(self, alter: int):
        self.__alter = alter
    def setJahreErfahrung__(self, jahreErfahrung: int):
        self.__jahreErfahrung = jahreErfahrung
    def getJahreErfahrung__():
        pass
    def __str__(self) -> str:
        pass