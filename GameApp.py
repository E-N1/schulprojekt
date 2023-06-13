"""
Diese Datei ist ein Teil des Spiels ebenso des Projektes, Tik Tak Toe. Um das Spiel nutzen zu können, benötigt
man alle Dateien. Diese Sind folgender:
TikTakToe.py, User.py.

"""

from TikTakToe import Spiel
from User import Spieler

spielTTT = Spieler()



weiterspielen = True
Spieler.spielernameEins
Spieler.spielernameZwei

#Spielschleife führt solange aus bis "q" eingeben oder Programm wird. 
while weiterspielen == True:
    
    if Spiel.spielerEingabe == "q":
        weiterspielen = False

    #Beendet das Spiel
    if weiterspielen == False:
        break


    #Ausgeben welcher Spieler denn aktueller am Zug ist.
    print("Spieler",spielTTT.aktuellerSpieler(),"am Zug")

