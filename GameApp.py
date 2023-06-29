
import tkinter as tk #GUI
from tkinter import messagebox #Warnungen,Infos Ploppups
from db import DatenbankManager
from inGame import Game

class Login():

    def __init__(self):
        self.spieler1loggedIn = False
        self.spieler2loggedIn = False
        self.spielStarten = False
        self.datenbank = DatenbankManager()
        self.root = tk.Tk()
        self.rootWidget()



    def rootWidget(self):
        self.root.config(background="white")
        self.root.geometry("1000x500")
        self.root.title("Tic Tac Toe, Project by Enver")
        self.windowInMiddle(self.root)

        #Button zum öffnen des Registrierfenster
        self.ButtonRegistrieren = tk.Button(self.root,text = "Hier",command=self.clickButtonRegister, width= 7, height= 1)
        self.ButtonRegistrieren.place(x = 470,y= 250)
        self.ButtonRegistrieren.config(font = ("Arial",11))


        #Schließt das Fenster
        self.ButtonEnd = tk.Button(self.root,text = "Spiel beenden",command = lambda: self.closeConnectionWithWindow(self.root,DatenbankManager.disconnect),  width= 11, height= 1)
        self.ButtonEnd.place(x = 805, y = 430)
        self.ButtonEnd.config(font = ("Arial",11))


        #Anmeldung von Spieler 1, Daten werden von der Datenbank genommen
        self.ButtonSpieler1 = tk.Button(self.root, text = "Anmelden", command = self.anmeldenSpieler1, width= 11 , height= 1)
        self.ButtonSpieler1.place(x = 100, y = 300)
        self.ButtonSpieler1.config(font = ("Arial",11))

        self.labelSpieler1 = tk.Label(self.root,text= "Spieler 1 Login:")
        self.labelSpieler1.config(font = ("Arial",11),background="white")
        self.labelSpieler1.place(x = 95, y = 85)

        self.labelSpieler1Name = tk.Label(self.root,text= "Name:")
        self.labelSpieler1Name.place(x = 130,y = 130)
        self.labelSpieler1Name.config(font = ("Arial",11),background="white")

        self.entrySpieler1Name = tk.Entry(self.root,background= "white")
        self.entrySpieler1Name.place(x= 95, y = 160)

        self.labelSpieler1Passwort = tk.Label(self.root,text= "Passwort:")
        self.labelSpieler1Passwort.place(x = 120,y = 200)
        self.labelSpieler1Passwort.config(font = ("Arial",11),background="white")

        self.entrySpieler1Passwort = tk.Entry(self.root,background= "white")
        self.entrySpieler1Passwort.place(x= 95, y = 230)
        self.entrySpieler1Passwort.config(show= "*")


        #Anmeldung von Spieler 2, Daten werden von der Datenbank genommen
        self.labelSpieler2 = tk.Label(self.root,text= "Spieler 2 Login:")
        self.labelSpieler2.config(font = ("Arial",11),background="white")
        self.labelSpieler2.place(x = 795, y = 85)

        self.labelSpieler2Name = tk.Label(self.root,text= "Name:")
        self.labelSpieler2Name.place(x = 830,y = 130)
        self.labelSpieler2Name.config(font = ("Arial",11),background="white")

        self.entrySpieler2Name = tk.Entry(self.root,background= "white")
        self.entrySpieler2Name.place(x= 795, y = 160)

        self.labelSpieler2Passwort = tk.Label(self.root,text= "Passwort:")
        self.labelSpieler2Passwort.place(x = 820,y = 200)
        self.labelSpieler2Passwort.config(font = ("Arial",11),background="white")

        self.entrySpieler2Passwort = tk.Entry(self.root,background= "white")
        self.entrySpieler2Passwort.place(x= 795, y = 230)
        self.entrySpieler2Passwort.config(show= "*")

        self.ButtonSpieler2 = tk.Button(self.root, text = "Anmelden", command = self.anmeldenSpieler2, width= 11 , height= 1)
        self.ButtonSpieler2.place(x = 805, y = 300)
        self.ButtonSpieler2.config(font = ("Arial",11))

        #Anmeldetext in der Mitte des Bildschirms
        self.labelRegistrierenMitte = tk.Label(self.root, text = "Bitte melden Sie sich an.\n\nSollten Sie sich nicht registriert haben, bitte klicken Sie:")
        self.labelRegistrierenMitte.config(font = ("Arial",11),background="white")
        self.labelRegistrierenMitte.place(x = 330,y=170)

        self.ButtonSpielStarten = tk.Button(self.root, text = "Spiel starten", command = self.spielstarten, width= 11 , height= 1)
        self.ButtonSpielStarten.place(x = 460 , y = 430)

        self.ButtonSpieler2.config(font = ("Arial",11))
        self.root.mainloop()

    #Platziert das Spiel in der Mitte des Bildschirms
    def windowInMiddle(self,window):
        windowWidth = 1000
        windowHeight = 500
        screenHeight = window.winfo_screenwidth()
        screenWidth = window.winfo_screenheight()
        xcoordinate = int((screenHeight /2) - (windowWidth / 2))
        ycoordinate = int((screenWidth / 2) - (windowHeight / 2))
        window.geometry(f"{windowWidth}x{windowHeight}+{xcoordinate}+{ycoordinate}")

    
    def closeConnectionWithWindow(self,window,connectionDB):
        connectionDB = self.datenbank.disconnect()
        print(connectionDB)
        return connectionDB, window.destroy()


    #Beendet das Spiel
    def closeWindow(self,window):
        w = window
        return w.destroy()

    def spielstarten(self):

        if self.spieler1loggedIn == True and self.spieler2loggedIn == True:
            
            #newWindow = Game()

            Game( self.entrySpieler1Name.get() , self.entrySpieler2Name.get() )

            return True
                    
        elif self.spieler1loggedIn == True and self.spieler2loggedIn == False:
            labelNotLogin = tk.Label(self.root, text = "Es sind nicht alle Spieler angemeldet.",background= "white")
            labelNotLogin.place(x=380, y=340)
            labelNotLogin.config(font = ("Arial",11))

        elif self.spieler2loggedIn == True and self.spieler1loggedIn == False:
            labelNotLogin = tk.Label(self.root, text = "Es sind nicht alle Spieler angemeldet.",background= "white")
            labelNotLogin.place(x=380, y=340)
            labelNotLogin.config(font = ("Arial",11))

        else:
            labelNotLogin = tk.Label(self.root, text = "Es sind nicht alle Spieler angemeldet.",background= "white")
            labelNotLogin.place(x=380, y=340)
            labelNotLogin.config(font = ("Arial",11))


       


    def anmeldenSpieler1(self):
        
        #Liste aller vorherigen Labels
        listeLabelAusgaben = []

        #Vorherige Labels löschen oder ausblenden, weil sie sich sonst aufeinanderstapeln
        for label in listeLabelAusgaben:
            if label is not None:
                label.config(text ="")

        #Abfragen ob Anmeldename1 und Anmeldename2 nicht identisch sind        
        if self.entrySpieler1Name.get() == self.entrySpieler2Name.get():
            labelanmeldeinfoP26 = tk.Label(self.root,background= "white")
            labelanmeldeinfoP26.config(font = ("Arial",11),foreground="red",text="Dein Gegenspieler nutzt diesen Account bereits.")
            labelanmeldeinfoP26.pack()
            print("Dieser Account wurde bereits angemeldet! Achtung")
            listeLabelAusgaben.append(labelanmeldeinfoP26)
            return True
        
        #Checkt in der Datenbank ab, ob der eingegebene Eintrag übereinstimmt.
        elif self.datenbank.checkLogin(self.entrySpieler1Name.get(),self.entrySpieler1Passwort.get()):
            labelanmeldeinfoP1 = tk.Label(self.root, text="[Spieler 1]\nDu hast dich erfolgreich angemeldet!",background= "white")
            labelanmeldeinfoP1.config(font = ("Arial",11),foreground="green")

            #Boolean von Spieler1 wird auf True gesetzt
            self.spieler1loggedIn = True
            #Muss noch genacht werden
            # datenbank.setLoginStatus(entrySpieler1Name,True)
            listeLabelAusgaben.append(labelanmeldeinfoP1)
            labelanmeldeinfoP1.pack()
            print("Spieler 1 eingeloggt!")
            return True

        #Abfrage ob beide Felder leer gelassen wurden.
        elif self.entrySpieler1Name.get() == "" and self.entrySpieler1Passwort.get() == "":
            labelanmeldeinfoP15 = tk.Label(self.root, text="Nutzername und Passwort eingeben!",background= "white")
            labelanmeldeinfoP15.config(font = ("Arial",11),foreground="red")
            listeLabelAusgaben.append(labelanmeldeinfoP15)
            labelanmeldeinfoP15.pack()

        #Abfrage ob der Spielname nicht eingegeben wurde.
        elif self.entrySpieler1Name.get() == "":
            labelanmeldeinfoP14 = tk.Label(self.root, text="Nutzername wird für die Anmeldung benötigt!",background= "white")
            labelanmeldeinfoP14.config(font = ("Arial",11),foreground="red")
            listeLabelAusgaben.append(labelanmeldeinfoP14)
            labelanmeldeinfoP14.pack()

        #Abfrage ob das Passwort ausgelassen wurde.
        elif self.entrySpieler1Passwort.get() == "":
            labelanmeldeinfoP13 = tk.Label(self.root, text="Passwort wird für die Anmeldung benötigt!",background= "white")
            labelanmeldeinfoP13.config(font = ("Arial",11),foreground="red")
            listeLabelAusgaben.append(labelanmeldeinfoP13)
            labelanmeldeinfoP13.pack()

        #Sollte Nutzername oder Passwort nicht wie in der Datenbank übereinstimmen, wird eine Meldung ausgegeben, dass etwas nicht richtig eingegeben wurde.
        else:
            labelanmeldeinfoP12 = tk.Label(self.root, text="Nutzername oder Passwort falsch, \nÜberprüfe deine Eingabe.",background= "white")
            labelanmeldeinfoP12.config(font = ("Arial",11),foreground="red")
            listeLabelAusgaben.append(labelanmeldeinfoP12)
            labelanmeldeinfoP12.pack()
    

    def anmeldenSpieler2(self):
        #Liste aller vorherigen Labels
        listeLabelAusgaben = []
    

        #Vorherige Labels löschen oder ausblenden, weil sie sich sonst aufeinanderstapeln
        for label in listeLabelAusgaben:
            if label is not None:
                label.config(text = "")

        #Abfragen ob Anmeldename2 und Anmeldename1 nicht identisch sind      
        if self.entrySpieler2Name.get() == self.entrySpieler1Name.get():
            labelanmeldeinfoP21 = tk.Label(self.root,background= "white")
            labelanmeldeinfoP21.config(font = ("Arial",11),foreground="red",text="Dein Gegenspieler nutzt diesen Account bereits.")
            labelanmeldeinfoP21.pack()
            listeLabelAusgaben.append(labelanmeldeinfoP21)
            return True

        #Checkt in der Datenbank ab, ob der eingegebene Eintrag übereinstimmt.
        elif self.datenbank.checkLogin(self.entrySpieler2Name.get(),self.entrySpieler2Passwort.get()):
            labelanmeldeinfoP22 = tk.Label(self.root, text="[Spieler 2]\nDu hast dich erfolgreich angemeldet!",background= "white")
            labelanmeldeinfoP22.config(font = ("Arial",11),foreground="green")
            self.spieler2loggedIn = True
            Spieler2loggedin = True
            #muss noch gemacht werden
            # datenbank.setLoginStatus(entrySpieler2Name,True)
            listeLabelAusgaben.append(labelanmeldeinfoP22)
            labelanmeldeinfoP22.pack()
            print("Spieler 2 eingeloggt!")
            return True


        #Abfrage ob beide Felder leer gelassen wurden.
        elif self.entrySpieler2Name.get() == "" and self.entrySpieler2Passwort.get() == "":
            labelanmeldeinfoP23 = tk.Label(self.root, text="Nutzername und Passwort eingeben!",background= "white")
            labelanmeldeinfoP23.config(font = ("Arial",11),foreground="red")
            listeLabelAusgaben.append(labelanmeldeinfoP23)
            labelanmeldeinfoP23.pack()


        #Abfrage ob der Spielname nicht eingegeben wurde.
        elif self.entrySpieler2Name.get() == "":
            labelanmeldeinfoP24 = tk.Label(self.root, text="Nutzername wird für die Anmeldung benötigt!",background= "white")
            labelanmeldeinfoP24.config(font = ("Arial",11),foreground="red")
            listeLabelAusgaben.append(labelanmeldeinfoP24)
            labelanmeldeinfoP24.pack()


        #Abfrage ob das Passwort ausgelassen wurde.
        elif self.entrySpieler2Passwort.get() == "":
            labelanmeldeinfoP25 = tk.Label(self.root, text="Passwort wird für die Anmeldung benötigt!",background= "white")
            labelanmeldeinfoP25.config(font = ("Arial",11),foreground="red")
            listeLabelAusgaben.append(labelanmeldeinfoP25)
            labelanmeldeinfoP25.pack()


        #Sollte Nutzername oder Passwort nicht wie in der Datenbank übereinstimmen, wird eine Meldung ausgegeben, dass etwas nicht richtig eingegeben wurde.
        else:
            labelanmeldeinfoP26 = tk.Label(self.root, text="Nutzername oder Passwort falsch, \nÜberprüfe deine Eingabe.",background= "white")
            labelanmeldeinfoP26.config(font = ("Arial",11),foreground="red")
            listeLabelAusgaben.append(labelanmeldeinfoP26)
            labelanmeldeinfoP26.pack()

   

    #Wird ausgeführt bei Klicken des Registrierbutton 
    def clickButtonRegister(self):
        def testEntry(name,passwort,passwortwdh):

            #Mindeslänge des Passwortes
            mindlaenge = 8

            maxNickName = 18

            #Abfragen ob die Felder alle ausgefüllt sind.
            if name == "" or passwort == "" or passwortwdh == "":
                messagebox.showwarning("Warnung","Fehler, Bitte fülle alle Felder aus.")
                registerFenster.focus_set()
                
            #Abfragen ob Passwort und Passwortwiederholen das gleiche ist.
            elif not passwort == passwortwdh:
                messagebox.showwarning("Warnung","Passwörter sind nicht identisch eingeben, bitte wiederhole!")
                registerFenster.focus_set()

            #Abfragen ob die Mindestläenge bei Passwort erfüllt ist.
            elif len(passwort) < mindlaenge:
                messagebox.showwarning("Warnung",f"Das Passwort sollte mindestens {mindlaenge} Zeichen lang sein!")
                registerFenster.focus_set()

            #Abfangen wenn Nickname länger als 18 Zeichen hat.
            elif len(name) > maxNickName:
                messagebox.showwarning("Warnung",f"Nickname sollte maximal {maxNickName} Zeichen lang sein!")
                registerFenster.focus_set()

            #Ist alles eingehalten, können die Einträge in folgende Datenbank eingetragen werden
            #Eventuell mit einer Externen Datei, wo man die Datenbank anbindung verbinden kann
            else:
                if self.datenbank.checkEntryExists(name):

                    messagebox.showwarning("Warnung",f"{name} ist bereits registriert.\nWähle einen anderen Namen!")
                else:
                    self.datenbank.insertQuery(name,passwort)
                    self.closeWindow(registerFenster)
                    messagebox.showinfo("Info", "Registrierung erfolgreich.\n\nViel spaß beim Spielen!")

        
        registerFenster = tk.Toplevel(self.root,background= "white")
        registerFenster.title("2.Fenster, Registrierung")
        self.windowInMiddle(registerFenster)
        #Text von Registrieren
        labelRegisterEins = tk.Label(registerFenster, text ="Fülle das Formular aus, um ein Konto anzulegen.\n\nNutzername(Max 18 Zeichen) und Passwort(Mind. 8 Zeichen) eingeben.",background="white")
        labelRegisterEins.config(font = ("Arial",11))
        labelRegisterEins.place(x = 290,y=70)

        #Text und Eingabefeld für Nutzername
        labelName = tk.Label(registerFenster,text="Nutzername:",background= "white")
        labelName.config(font = ("Arial",11))
        labelName.place(x = 450,y=170)
        entryName = tk.Entry(registerFenster,background="white")
        entryName.place(x = 450,y=200)

        #Text und Eingabefeld für Passwort
        labelPasswort = tk.Label(registerFenster,text="Passwort:",background= "white")
        labelPasswort.config(font = ("Arial",11))
        labelPasswort.place(x = 450,y=240)
        entryPasswort = tk.Entry(registerFenster,background="white",show = "*")
        entryPasswort.place(x = 450,y=270)
        
        #Text und Eingabefeld für Passwort Wiederholung
        labelPasswortWdh = tk.Label(registerFenster,text="Passwort wiederholen:",background= "white")
        labelPasswortWdh.config(font = ("Arial",11))
        labelPasswortWdh.place(x = 435,y=310)
        entryPasswortWiederholung = tk.Entry(registerFenster,background="white",show = "*")
        entryPasswortWiederholung.place(x = 450,y=340)

        #Text für Datenbankinformation
        labelDB = tk.Label(registerFenster, text="Angaben werden anschließend in der Datenbank vermerkt.",background="white")
        labelDB.config(font = ("Arial",9))
        labelDB.place(x = 350,y=380)

        #Button für Speicherung der Eingaben in die Datenbank
        ButtonRegistrierenFenster2 = tk.Button(registerFenster, text="Registrieren", width= 10, height= 1,
                                            command= lambda: testEntry(entryName.get(),entryPasswort.get(),entryPasswortWiederholung.get() ),)
        ButtonRegistrierenFenster2.config(font =("Arial",11))
        ButtonRegistrierenFenster2.place(x= 460, y = 420)

        #Fenster schließen
        ButtonSchliessen = tk.Button(registerFenster, text="Fenster schließen", width= 14, height= 1,command = lambda: self.closeWindow(registerFenster) )
        ButtonSchliessen.config(font =("Arial",11))
        ButtonSchliessen.place(x = 840, y = 430)
        return True
    

LoginScreen = Login()