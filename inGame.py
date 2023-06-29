import tkinter as tk
from User import Spieler
from db import DatenbankManager
class Game():

    def __init__(self,name1,name2):
        self.spielstarten = True
        self.spieler1loggedIn = True
        self.spieler2loggedIn = True
        self.spielAktiv = True

        self.spielername1 = name1
        self.spielername2 = name2

        self.datenbank = DatenbankManager()
        self.spieler = Spieler()

        self.rootIngame = tk.Tk()
        self.rootInGameWidget()
        
        
    def windowDestroy(self):
        window = self.rootIngame
        window.destroy()
        dbdc = DatenbankManager.disconnect
        return window,dbdc
    
    def windowInMiddle(self,window):
        windowWidth = 1000
        windowHeight = 500
        screenHeight = window.winfo_screenwidth()
        screenWidth = window.winfo_screenheight()
        xcoordinate = int((screenHeight /2) - (windowWidth / 2))
        ycoordinate = int((screenWidth / 2) - (windowHeight / 2))
        window.geometry(f"{windowWidth}x{windowHeight}+{xcoordinate}+{ycoordinate}")

    
    #Buttons,Spielfeld, Felder,..usw
    def rootInGameWidget(self):
        self.rootIngame.config(background="white")
        self.rootIngame.geometry("1000x500")
        self.rootIngame.title("Tic Tac Toe, Project by Enver")
        self.windowInMiddle(self.rootIngame)

        #Statistik, Gewinne, Niederlage und Quote werden von der Datenbank aufgerufe. Einsichtbar für beide Spieler.
        self.buttonStatistik = tk.Button(self.rootIngame, text ="Statistik", command = self.statistik ,width= 10, height = 1)
        self.buttonStatistik.place(x = 50, y = 430)
        self.buttonStatistik.config(font = ("Arial",11))

        #Label die angezeigt werden von den jeweiligen Gewinnern dann
        self.labelGewonnenS1 = tk.Label(self.rootIngame, text= "",background="white")
        self.labelGewonnenS1.place(x = 50, y = 250)
        self.labelGewonnenS1.config(font = ("Arial",14))

        self.labelGewonnenS2 = tk.Label(self.rootIngame, text= "",background="white")
        self.labelGewonnenS2.place(x=760,y = 250)
        self.labelGewonnenS2.config(font = ("Arial",14))

        self.labelUnentschieden = tk.Label(self.rootIngame,text ="",background="white")
        self.labelUnentschieden.place(x=830,y = 190)
        self.labelUnentschieden.config(font = ("Arial",14))

        #Schließt das Fenster
        self.ButtonEnd = tk.Button(self.rootIngame,text = "Spiel beenden",command = self.windowDestroy,  width= 11, height= 1)
        self.ButtonEnd.place(x = 810, y = 430)
        self.ButtonEnd.config(font = ("Arial",11))


        #Spiel neustarten Button, Felder werden zurückgesetzt
        self.restartButton = tk.Button(self.rootIngame, text ="Neu starten", command = self.restartGame, width= 11,height=1)
        self.restartButton.place(x = 810, y = 370)
        self.restartButton.config(font = ("Arial",11))


        #Label von Spieler 1
        self.labelSpieler1inGame = tk.Label(self.rootIngame, text = self.spielername1, background= "white")
        self.labelSpieler1inGame.config(font = ("Arial",14))
        self.labelSpieler1inGame.place(x = 95, y = 85)



        #Label von Spieler 2
        self.labelSpieler2inGame = tk.Label(self.rootIngame, text = self.spielername2, background= "white")
        self.labelSpieler2inGame.config(font = ("Arial",14))
        self.labelSpieler2inGame.place(x = 830,y = 85)


        #Label Spieler 1 _ O
        self.labelSpieler1X = tk.Label(self.rootIngame, text = "O", bd=2, background= "#F7F7F7",height= 2,width= 3) #Farbe Grau
        self.labelSpieler1X.config(font = ("Arial",18))
        self.labelSpieler1X.place(x = 110, y = 150)

        #Label Spieler 2 _ X
        self.labelSpieler2O = tk.Label(self.rootIngame, text = "X", bd=2, background= "#F7F7F7",height= 2,width= 3) #Farbe Grau
        self.labelSpieler2O.config(font = ("Arial",18))
        self.labelSpieler2O.place(x = 850, y = 150)

        #Die jeweiligen Felder in Buttons zum Drücken, interaktion des Spiels
        #Reihe1
        self.feld1 = tk.Button(self.rootIngame, text = "Feld 1",width= 7, height= 2,command= lambda: self.clickButtons(1))
        self.feld2 = tk.Button(self.rootIngame, text = "Feld 2",width= 7, height= 2,command= lambda: self.clickButtons(2))
        self.feld3 = tk.Button(self.rootIngame, text = "Feld 3",width= 7, height= 2,command= lambda: self.clickButtons(3))

        self.feld1.place(x = 400,y = 320)
        self.feld2.place(x = 470,y = 320)
        self.feld3.place(x = 540,y = 320)


        #Reihe 2 des Spielfelds
        self.feld4 = tk.Button(self.rootIngame, text = "Feld 4",width= 7, height= 2,command= lambda: self.clickButtons(4))
        self.feld5 = tk.Button(self.rootIngame, text = "Feld 5",width= 7, height= 2,command= lambda: self.clickButtons(5))
        self.feld6 = tk.Button(self.rootIngame, text = "Feld 6",width= 7, height= 2,command= lambda: self.clickButtons(6))

        self.feld4.place(x = 400,y = 370)
        self.feld5.place(x = 470,y = 370)
        self.feld6.place(x = 540,y = 370)


        #Reihe3 des Spielfelds
        self.feld7 = tk.Button(self.rootIngame, text = "Feld 7",width= 7, height= 2,command= lambda: self.clickButtons(7))
        self.feld8 = tk.Button(self.rootIngame, text = "Feld 8",width= 7, height= 2,command= lambda: self.clickButtons(8))
        self.feld9 = tk.Button(self.rootIngame, text = "Feld 9",width= 7, height= 2,command= lambda: self.clickButtons(9))
        self.feld7.place(x = 400,y = 420)
        self.feld8.place(x = 470,y = 420)
        self.feld9.place(x = 540,y = 420)


        #Zeigt das Label an: Am Spielzug ist SpielerNr:
        self.labelAktullerSpieler = tk.Label(self.rootIngame, text="Am Zug ist Spieler:",background= "white")
        self.labelAktullerSpieler.place(x = 405, y = 280)
        self.labelAktullerSpieler.config(font = ("Arial",11))

        self.labelSpielerNr = tk.Label(self.rootIngame, background= "#F7F7F7", width= 5, height= 2)
        self.labelSpielerNr.place(x = 545, y = 270)
        self.labelSpielerNr.config(font = ("Arial",11),text=f"{self.spieler.aktuellerSpieler()}")
        

        #Spielfeld in der Mitte ausgeben, leer.
        self.spielfeld1 = tk.Label(self.rootIngame, text = "", width=3, height = 2)
        self.spielfeld1.place(x = 410, y = 30)
        self.spielfeld1.config(font = ("Arial",17))

        self.spielfeld2 = tk.Label(self.rootIngame, text = "", width=3, height = 2)
        self.spielfeld2.place(x = 480, y = 30)
        self.spielfeld2.config(font = ("Arial",17))

        self.spielfeld3 = tk.Label(self.rootIngame, text = "", width=3, height = 2)
        self.spielfeld3.place(x = 550, y = 30)
        self.spielfeld3.config(font = ("Arial",17))

        self.spielfeld4 = tk.Label(self.rootIngame, text = "", width=3, height = 2)
        self.spielfeld4.place(x = 410, y = 110)
        self.spielfeld4.config(font = ("Arial",17))

        self.spielfeld5 = tk.Label(self.rootIngame, text = "", width=3, height = 2)
        self.spielfeld5.place(x = 480, y = 110)
        self.spielfeld5.config(font = ("Arial",17))

        self.spielfeld6 = tk.Label(self.rootIngame, text = "", width=3, height = 2)
        self.spielfeld6.place(x = 550, y = 110)
        self.spielfeld6.config(font = ("Arial",17))

        self.spielfeld7 = tk.Label(self.rootIngame, text = "", width=3, height = 2)
        self.spielfeld7.place(x = 410, y = 190)
        self.spielfeld7.config(font = ("Arial",17))

        self.spielfeld8 = tk.Label(self.rootIngame, text = "", width=3, height = 2)
        self.spielfeld8.place(x = 480, y = 190)
        self.spielfeld8.config(font = ("Arial",17))

        self.spielfeld9 = tk.Label(self.rootIngame, text = "", width=3, height = 2)
        self.spielfeld9.place(x = 550, y = 190)
        self.spielfeld9.config(font = ("Arial",17))
        
        #Fensterschleife, ermöglicht das Öffnet des Fensters.
        self.rootIngame.mainloop()


    #Methode für das klicken des Buttons Statistik. Wird für beide Spieler sichtbar gemacht, mit der Datenbank aufgerufen 
    def statistik(self):

        self.statistikSpieler1 = tk.Label(self.rootIngame, text= f"{self.spielername1} : {self.datenbank.checkPoints(self.spielername1)} Gewonnen | Verloren",background= "white")
        self.statistikSpieler1.place(x = 50, y = 360)
        self.statistikSpieler1.config(font = ("Arial",11))

        self.statistikSpieler2 = tk.Label(self.rootIngame, text= f"{self.spielername2} : {self.datenbank.checkPoints(self.spielername2)} Gewonnen | Verloren",background= "white")
        self.statistikSpieler2.place(x = 50, y = 390)
        self.statistikSpieler2.config(font = ("Arial",11))
        #Sollte die Verbindung zur Datenbank nicht funktionieren, wird ein Label ausgegeben, worin steht: DB-Verbindung aktuell nicht möglich.

        return True


    #Eine Methode die Zwischen O und X tauscht, über die self.feld1-9
    def spielzugSpielerNr(self):

        #Frägt nach ob der beinhaltende "text", ein X ist, wenn else:dann ist es ein O
        if self.labelSpielerNr.cget("text") == "X":
            #Ändert das X in ein O, genauso passiert es beim else andersrum.
            return self.labelSpielerNr.config(text="O")
        else:
            return self.labelSpielerNr.config(text="X")


    def gewonnen(self):
        #Wenn jemand Gewinnen sollte, wird einen Punkt in das dementsprechende Konto hinzugefügt.
        #Abfragen ob Reihenweise jemand gewonnen hat. Danach wird das Spielfeld als deaktiv eingestuft
        if self.spielfeld1.cget("text") == self.spielfeld2.cget("text") == self.spielfeld3.cget("text") != "":
            print("Der Gewinner ist:",self.spieler.aktuellerSpieler())
            if self.spieler.aktuellerSpieler() == "O":
                self.datenbank.insertPointsPlus1(self.spielername1,self.spielername2)
            else:
                self.datenbank.insertPointsPlus1(self.spielername2,self.spielername1)
            self.spielAktiv = False

        elif self.spielfeld4.cget("text") == self.spielfeld5.cget("text") == self.spielfeld6.cget("text")!= "":
            print("Der Gewinner ist:",self.spieler.aktuellerSpieler())
            if self.spieler.aktuellerSpieler() == "O":
                self.datenbank.insertPointsPlus1(self.spielername1,self.spielername2)
            else:
                self.datenbank.insertPointsPlus1(self.spielername2,self.spielername1)
            self.spielAktiv = False

        elif self.spielfeld7.cget("text") == self.spielfeld8.cget("text") == self.spielfeld9.cget("text")!= "":
            print("Der Gewinner ist:",self.spieler.aktuellerSpieler())
            if self.spieler.aktuellerSpieler() == "O":
                self.datenbank.insertPointsPlus1(self.spielername1,self.spielername2)
            else:
                self.datenbank.insertPointsPlus1(self.spielername2,self.spielername1)
            self.spielAktiv = False
        

        #Abfragen ob Spaltenweise jemand gewonnen hat. Danach wird das Spielfeld als deaktiv eingestuft
        elif self.spielfeld1.cget("text") == self.spielfeld4.cget("text") == self.spielfeld7.cget("text") != "":
            print("Der Gewinner ist:",self.spieler.aktuellerSpieler())
            if self.spieler.aktuellerSpieler() == "O":
                self.datenbank.insertPointsPlus1(self.spielername1,self.spielername2)
            else:
                self.datenbank.insertPointsPlus1(self.spielername2,self.spielername1)
            self.spielAktiv = False
        
        elif self.spielfeld2.cget("text") == self.spielfeld5.cget("text") == self.spielfeld8.cget("text") != "":
            print("Der Gewinner ist:",self.spieler.aktuellerSpieler())
            if self.spieler.aktuellerSpieler() == "O":
                self.datenbank.insertPointsPlus1(self.spielername1,self.spielername2)
            else:
                self.datenbank.insertPointsPlus1(self.spielername2,self.spielername1)
            self.spielAktiv = False

        elif self.spielfeld3.cget("text") == self.spielfeld6.cget("text") == self.spielfeld9.cget("text") != "":
            print("Der Gewinner ist:",self.spieler.aktuellerSpieler())
            if self.spieler.aktuellerSpieler() == "O":
                self.datenbank.insertPointsPlus1(self.spielername1,self.spielername2)
            else:
                self.datenbank.insertPointsPlus1(self.spielername2,self.spielername1)
            self.spielAktiv = False
        

        #Abfragen ob Diagonalerweise jemand gewonnen hat. Danach wird das Spielfeld als deaktiv eingestuft
        elif self.spielfeld1.cget("text") == self.spielfeld5.cget("text") == self.spielfeld9.cget("text") != "":
            print("Der Gewinner ist:",self.spieler.aktuellerSpieler())
            if self.spieler.aktuellerSpieler == "O":
                self.datenbank.insertPointsPlus1(self.spielername1,self.spielername2)
            else:
                self.datenbank.insertPointsPlus1(self.spielername2,self.spielername1)
            self.spielAktiv = False
        
        elif self.spielfeld3.cget("text") == self.spielfeld5.cget("text") == self.spielfeld7.cget("text") != "":
            print("Der Gewinner ist:",self.spieler.aktuellerSpieler())
            if self.spieler.aktuellerSpieler == "O":
                self.datenbank.insertPointsPlus1(self.spielername1,self.spielername2)
            else:
                self.datenbank.insertPointsPlus1(self.spielername2,self.spielername1)
            self.spielAktiv = False
        
        #Wenn das Spiel vorbei ist, wird der Sieger nominiert, hinzu kommt 1 Punkt in das Konto.
        #Das Ganze wird mit einem Label sichtbar gemacht und der Punkt in der Datenbank verzeichnet.
        if self.spielAktiv == False:

            if self.spieler.aktuellerSpieler() == "O":
                self.labelGewonnenS1 = tk.Label(self.rootIngame, text= f"Glückwunsch {self.spielername1}!\n Du hast gewonnen.\n+1 Punkt",background="white")
                self.labelGewonnenS1.place(x = 50, y = 250)
                self.labelGewonnenS1.config(font = ("Arial",14))
                return self.spieler.aktuellerSpieler
            else:
                self.labelGewonnenS2 = tk.Label(self.rootIngame, text= f"Glückwunsch {self.spielername2}!\n Du hast gewonnen!\n+1 Punkt",background="white")
                self.labelGewonnenS2.place(x=760,y = 250)
                self.labelGewonnenS2.config(font = ("Arial",14))
                return self.spieler.aktuellerSpieler

        

    #Nach jedem Clicken auf einem Button soll überprüft werden ob derjenige gewonnen hat, oder ein Unentschieden entstanden ist.
    #Hinzu kommt eine Benachrichtigung in die Console, Mit Feld , O oder X.
    def clickButtons(self,button):
        if self.spielAktiv == True:
            
            #Wenn Folgende Buttons gedrückt werden, wird der Spielerwechsel automatisch folgen, ebenso wie die SpielerzugNr. Das auf alle 9 Buttons
            #Gewinnen wird bei jedem platzieren abgefragt.Hinzu kommt ob das Spielfeld dann voll ist und dadurch ein unentschieden ist. Ebenso wird abgefragt ob das Spielfeld noch aktiv ist
            if button == 1:

                if self.spielfeld1.cget("text") == "":
                    self.spielfeld1.config(text = self.spieler.aktuellerSpieler())
                    print("Du hast auf Feld 1 mit einem","'",self.spieler.aktuellerSpieler(),"'","gehandelt.")
                    self.gewonnen()
                    self.unentschieden()
                    if self.spielzugSpielerNr():
                        self.spieler.spielerWechseln()
                    else:
                        self.spieler.spielerWechseln()
                else: 
                    print("Nicht möglich, da bereits belegt mit",self.spielfeld1.cget("text"))

            elif button == 2:
                if self.spielfeld2.cget("text") == "":
                    self.spielfeld2.config(text = self.spieler.aktuellerSpieler())
                    print("Du hast auf Feld 2 mit einem","'",self.spieler.aktuellerSpieler(),"'","gehandelt.")
                    self.gewonnen()
                    self.unentschieden()
                    if self.spielzugSpielerNr():
                        self.spieler.spielerWechseln()
                    else:
                        self.spieler.spielerWechseln()
                else: 
                    print("Nicht möglich, da bereits belegt mit",self.spielfeld2.cget("text"))

            elif button == 3:
                if self.spielfeld3.cget("text") == "":
                    self.spielfeld3.config(text = self.spieler.aktuellerSpieler())
                    print("Du hast auf Feld 3 mit einem","'",self.spieler.aktuellerSpieler(),"'","gehandelt.")
                    self.gewonnen()
                    self.unentschieden()
                    if self.spielzugSpielerNr():
                        self.spieler.spielerWechseln()
                    else:
                        self.spieler.spielerWechseln()
                    
                else: 
                    print("Nicht möglich, da bereits belegt mit",self.spielfeld3.cget("text"))

            elif button == 4:
                if self.spielfeld4.cget("text") == "":
                    self.spielfeld4.config(text = self.spieler.aktuellerSpieler())
                    print("Du hast auf Feld4 mit einem","'",self.spieler.aktuellerSpieler(),"'","gehandelt.")
                    self.gewonnen()
                    self.unentschieden()
                    if self.spielzugSpielerNr():
                        self.spieler.spielerWechseln()
                    else:
                        self.spieler.spielerWechseln()
                else: 
                    print("Nicht möglich, da bereits belegt mit",self.spielfeld4.cget("text"))

            elif button == 5:
                if self.spielfeld5.cget("text") == "":
                    self.spielfeld5.config(text = self.spieler.aktuellerSpieler())
                    print("Du hast auf Feld 5 mit einem","'",self.spieler.aktuellerSpieler(),"'","gehandelt.")
                    self.gewonnen()
                    self.unentschieden()
                    if self.spielzugSpielerNr():
                        self.spieler.spielerWechseln()
                    else:
                        self.spieler.spielerWechseln()
                else: 
                    print("Nicht möglich, da bereits belegt mit",self.spielfeld5.cget("text"))

            elif button == 6:
                if self.spielfeld6.cget("text") == "":
                    self.spielfeld6.config(text = self.spieler.aktuellerSpieler())
                    print("Du hast auf Feld 6 mit einem","'",self.spieler.aktuellerSpieler(),"'","gehandelt.")
                    self.gewonnen()
                    self.unentschieden()
                    if self.spielzugSpielerNr():
                        self.spieler.spielerWechseln()
                    else:
                        self.spieler.spielerWechseln()
                else: 
                    print("Nicht möglich, da bereits belegt mit",self.spielfeld6.cget("text"))

            elif button == 7:
                if self.spielfeld7.cget("text") == "":
                    self.spielfeld7.config(text = self.spieler.aktuellerSpieler())
                    print("Du hast auf Feld 7 mit einem","'",self.spieler.aktuellerSpieler(),"'","gehandelt.")
                    self.gewonnen()
                    self.unentschieden()
                    if self.spielzugSpielerNr():
                        self.spieler.spielerWechseln()
                    else:
                        self.spieler.spielerWechseln()
                else: 
                    print("Nicht möglich, da bereits belegt mit",self.spielfeld7.cget("text"))

            elif button == 8:
                if self.spielfeld8.cget("text") == "":
                    self.spielfeld8.config(text = self.spieler.aktuellerSpieler())
                    print("Du hast auf Feld 8 mit einem","'",self.spieler.aktuellerSpieler(),"'","gehandelt.")
                    self.gewonnen()
                    self.unentschieden()
                    if self.spielzugSpielerNr():
                        self.spieler.spielerWechseln()
                    else:
                        self.spieler.spielerWechseln()
                else: 
                    print("Nicht möglich, da bereits belegt mit",self.spielfeld8.cget("text"))

            elif button == 9:
            
                if self.spielfeld9.cget("text") == "":
                    self.spielfeld9.config(text = self.spieler.aktuellerSpieler())
                    print("Du hast auf Feld 9 mit einem","'",self.spieler.aktuellerSpieler(),"'","gehandelt.")
                    self.gewonnen()
                    self.unentschieden()
                    if self.spielzugSpielerNr():
                        self.spieler.spielerWechseln()
                    else:
                        self.spieler.spielerWechseln()
                else: 
                    print("Nicht möglich, da bereits belegt mit",self.spielfeld9.cget("text"))
            else:
                print("Ungültiges Feld!")
   
        else:
            print("Das Spiel ist aktuell nicht aktiv. Um spielen zu können, drücke auf Restart")
            return True


    def resetSpielfeld(self):
        #Eine Liste für die ganzen Felder. Dies wird dann einzeln mit einer Schleife zurückgesetzt, um das Spiel neu zu bespielen.
        spielfelder = [self.spielfeld1 , self.spielfeld2 , self.spielfeld3 ,
                       self.spielfeld4 , self.spielfeld5 , self.spielfeld6 , 
                       self.spielfeld7 , self.spielfeld8 , self.spielfeld9]
        
        for spielfeld in spielfelder:
            spielfeld.config(text ="")
        self.labelGewonnenS1.config(text = "")
        self.labelGewonnenS2.config(text = "")
        self.labelUnentschieden.config(text= "")
        return True
    #Restartbutton ausführung, resettet das Spielfeld komplett.
    def restartGame(self):
        #Wird bei aktiven sowie nicht aktiven Spiel restartet
        if self.spielAktiv == False:

            if self.spieler.aktuellerSpieler == "O":
                print("hallo O")
            if self.spieler.aktuellerSpieler == "X":
                print("hallo X")
            
            self.resetSpielfeld()
            self.spieler
            self.spielAktiv = True
            return True
            
        else:
            self.resetSpielfeld()
            self.spielAktiv = True
            return True

    def unentschieden(self):
        
        #Wird abgefragt wenn keiner gewonnen hat und alle Felder belegt sind. Eben so wird Label: LabelSpielerNr und den Text dazu entfernt
        if self.spielAktiv == True:

            if (self.spielfeld1.cget("text") == "X" or self.spielfeld1.cget("text") == "O") and (
                self.spielfeld2.cget("text") == "X" or self.spielfeld2.cget("text") == "O") and (
                self.spielfeld3.cget("text") == "X" or self.spielfeld3.cget("text") == "O") and (
                self.spielfeld4.cget("text") == "X" or self.spielfeld4.cget("text") == "O") and (
                self.spielfeld5.cget("text") == "X" or self.spielfeld5.cget("text") == "O") and (
                self.spielfeld6.cget("text") == "X" or self.spielfeld6.cget("text") == "O") and (
                self.spielfeld7.cget("text") == "X" or self.spielfeld7.cget("text") == "O") and (
                self.spielfeld8.cget("text") == "X" or self.spielfeld8.cget("text") == "O") and (
                self.spielfeld9.cget("text") == "X" or self.spielfeld9.cget("text") == "O"):

                print("Das Spiel ist mit einem unentschieden ausgegangen! Drücke Restart um erneut zu spielen.")


                self.labelAktullerSpieler.grid_forget()

                self.labelSpielerNr.grid_forget()
                
 
                self.labelUnentschieden = tk.Label(self.rootIngame,text ="Unentschieden! Spiel beendet.",background="white",height = 3)
                self.labelUnentschieden.place(x=400,y = 260)
                self.labelUnentschieden.config(font = ("Arial",11))
# spielen = Game("","")
        