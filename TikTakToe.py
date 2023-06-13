"""
Programmierung des Spieles Tic Tac Toe,mit der Sprache Python. Dies ist ein Schulprojekt, womit ich 4 Wochen zeit habe es fertigzustellen.
Die Anforderungen und Aufgaben hab ich selbst geplant. Zum Projekt:
Das Spielfeld wird unter 3x3 Felder gespielt. Abwechselnd setzt jeder Spieler seine Marke (X oder O) in ein freies Feld.
Wer als erstes 3 Felder belegt, die in einer Reihe oder Spalte oder in der Diagonale liegen, gewinnt.
Das Spiel wird mit mehreren Python Dateien, Klassen miteinander verknüpft.
Um das Spiel mit der Datenbank Richtig nutzen zu können, muss man
die Datenbankverbindung eingeben und abschließen.
Autor: Enver 
Beginndatum: 12.06.2023
Beendet am: - - -
"""


#Die Klasse Spiel, wodrin beinhaltet wird: Funktionen, Interaktionen einzelner Spielzugs, erstellung des Spielfelds und vieles mehr.
class Spiel():
    
    def __init__(self):
        #Erstellung des 3x3 Feldes
        #Eine Methode erstellen, die das Spielfeld in der Konsole anzeigt.
        #Die Position 0 der Liste wird für die leichtere Eingaben, überflüssig gemacht.
        self.spielfeldListe = ["",
                                "1","2","3",
                                "4","5","6",
                                "7","8","9"]
        self.spielerEins = False
        self.spielerZwei = False
        self.spielAktiv = True


        #Ausgabe des Spielfeldes in einer überschaubaren Ansicht
    def spielfeldAusgeben(self):


        print(self.spielfeldListe[1],"|",self.spielfeldListe[2],"|",self.spielfeldListe[3])
        print(self.spielfeldListe[4],"|",self.spielfeldListe[5],"|",self.spielfeldListe[6])
        print(self.spielfeldListe[7],"|",self.spielfeldListe[8],"|",self.spielfeldListe[9])


        self.spielfeldListe = self.spielfeldListe
        

    def aktualisiereSpielfeld(self, neue_spielfeld):
        self.spielfeld = neue_spielfeld



    def spielzug(self):
        spielzuge = input("Bitte Feld (1 bis 9) eingeben, 'b' für vorzeitiges beenden: ")

        #Abfrage falls zahlen von 1-9 nicht eingeben werden.
        if not int(spielzuge) <= 9 and int(spielzuge) >=1:
            print("Bitte nur Zahlen von 1 bis 9 eingeben!")
        elif spielzuge == "b":
            print("Das Spiel wurde soeben beendet. Bis zum nächsten mal!")
            return spielzuge
        else:
            #Gibt die eingebene Zahl wieder.
            return spielzuge
    


    def spielerEingabe(self):
        global spiel_aktiv
        while True:
            self.spielzug()


            #Die Abfrage beendet das spiel, b => beenden.
            if self.spielzug.spielzug == "b":
                spiel_aktiv = False
                break
            
            #Die Try , except Methode verhindert das Abstürzen, Fehlermeldung des Programms.
            try:
                if self.spielzug.spielzuge <= 9 and self.spielzug.spielzuge >= 1:
                    return self.spielzug.spielzuge

            except ValueError:
                print("Bitte nur gültige Zahlen von 1 bis 9 eingeben, b => beenden!")

    
#Ausgaben für das Spielen.

