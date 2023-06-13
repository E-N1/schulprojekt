
"""
Diese Datei ist ein Teil des Spiels, Tik Tak Toe. Um das Spiel nutzen zu können, benötigt
man alle Dateien.

"""

from TikTakToe import Spiel

#Klasse der Spieler (bei Tik Tak Toe gibts nur zwei Spieler).
class Spieler():


    def __init__(self):
        self.nameSpieler1 = ""
        self.nameSpieler2 = ""
        self.spieleraktuell = self.nameSpieler1



    #Aktuelle Spieler
    def aktuellerSpieler(self):
        return self.spieleraktuell
    
    #Eine Methode in dieser die Spielernamen erstellt werden:
    def spielernameEins(self):
        spielernameEins = input("Bitte geben Sie denn Namen für die Erstellung des Spielernamens Eins ein: ")
       
        #Falls die Benutzer des Spieles keinen Namen eingeben, wird ein Standardname erstellt.
        if spielernameEins == "":
            spielernameEins = "Spieler_1"
            spielernameEins = self.nameSpieler1
            return spielernameEins
        
        #Festlegen dass der eingebene Name in die Klasse wiederspiegelt.
        spielernameEins = self.nameSpieler1
        return spielernameEins   


    def spielernameZwei(self):
        spielernameZwei = input("Bitte geben Sie denn Namen für die Erstellung des Spielernamens Zwei ein: ")
        
        #Falls die Benutzer des Spieles keinen Namen eingeben, wird ein Standardname erstellt.
        if spielernameZwei == "":
            spielernameZwei = "Spieler_2"
            spielernameZwei = self.nameSpieler2
            return spielernameZwei
        
        #Festlegen dass der eingebene Name in die Klasse wiederspiegelt.
        spielernameZwei = self.nameSpieler2
        return spielernameZwei


    def spielerWechseln(self):
        global spieleraktuell
        if self.spieleraktuell == self.spielernameEins:
            self.spieleraktuell = self.spielernameZwei
        else:
            self.spieleraktuell = self.spielernameEins



    

        
