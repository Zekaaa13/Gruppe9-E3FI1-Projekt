class Anwendungsentwickler:
    def __init__(self, name, alter, lieblingsSprache, jahreErfahrung):
        self.name = name,
        self.alter = alter,
        self.lieblingsSprache = lieblingsSprache,
        self.jahreErfahrung = jahreErfahrung

    def getName(self):
        return self.name
    
    def setName(self,name):
        self.name = name

    def getAlter(self):
        return self.alter
    
    def setAlter(self,alter):
        self.alter = alter
    
    def getLieblingsSprache(self):
        return self.lieblingsSprache
    
    def setLieblingsSprache(self,lieblingsSprache):
        self.lieblingsSprache = lieblingsSprache
    
    def getJahreErfahrung(self):
        return self.jahreErfahrung
    
    def setJahreErfahrung(self, jahreErfahrung):
        self.jahreErfahrung = jahreErfahrung
    
    def __str__(self) -> str:
        "Name" + str(self.getName) + "Alter" + str(self.getAlter) + "Lieblingssprache" + str(self.lieblingsSprache)

    # Yodi mit der Klasse bin ich schon fertig, wie siehts bei dir aus