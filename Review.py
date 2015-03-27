

class Mathe(object):
    def getDescription(self):
        t = "Mathe"
        print (str(t))
        return t
    def Zeit(self):
        zeit = 30
        print ("Benoetigte Zeit:" + str(zeit))
        return zeit

class Mathe_decorator(object):
    def __init__(self, decoratee):
        self._decoratee = decoratee
    def AddPruefungen(self):
        y=self._decoratee.getDescription()
        print (str(y) + ", Pruefungen")
    def AddPruefungZeit(self):
        q= 20
        x=self._decoratee.Zeit()
        z = x+q
        print ("Neue Benoetigte Zeit: " + str(z))
    def __getattr__(self, name):
        return getattr(self._decoratee, name)

u = Mathe()
v = Mathe_decorator(u)
v.AddPruefungen()
v.AddPruefungZeit()
