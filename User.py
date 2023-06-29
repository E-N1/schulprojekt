class Spieler():


    def __init__(self):
        self.nrSpieler1 = "O"
        self.nrSpieler2 = "X"
        self.spieleraktuell = self.nrSpieler1

    #Definiert Spieler 1
    def SpielerNrEins(self):
        return self.nrSpieler1 

    #Definiert Spieler 2
    def SpielerNrZwei(self):
        return self.nrSpieler1 
    
    #Aktuelle Spieler
    def aktuellerSpieler(self):
        return self.spieleraktuell

    #Wechseln der Spieler
    def spielerWechseln(self):
        if self.spieleraktuell == self.nrSpieler1:
            self.spieleraktuell = self.nrSpieler2
        else:
            self.spieleraktuell = self.nrSpieler1



    

        
