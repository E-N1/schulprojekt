import mysql.connector
class DatenbankManager:

    def __init__(self, host="localhost", user="root", password= "hugo",database="tictactoe",port = "3306"):

        #Datenbank-Verbindung aufbauen
        self.connection = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database,
            port = port
            )
        #Cursor erstellen, um befehle auszuführen
        self.cursor = self.connection.cursor() 

    def tablenameSpieler(self):
        #Festlegen dass, Tabellenname "spieler" heißt.
        name = "spieler"
        return name


    def insertPointsPlus1(self, winname,losename):
        tablename = self.tablenameSpieler()
        # Wird bei Sieg einen Punkt in die Datenbank hinterlegt(gewinner)
        sqlselectWin = f"SELECT points FROM {tablename} WHERE name = %s"
        valuesselectWin = (winname,)

        # SELECT-Abfrage für den Verlierer
        sqlselectLoser = f"SELECT lose FROM {tablename} WHERE name = %s"
        valuesselectLoser = (losename,)


        try:
            # Gewinner-Daten abrufen
            self.cursor.execute(sqlselectWin, valuesselectWin)
            currentDataWinner = self.cursor.fetchone()

            # Verlierer-Daten abrufen
            self.cursor.execute(sqlselectLoser, valuesselectLoser)
            currentDataLoser = self.cursor.fetchone()

            if currentDataWinner is not None and currentDataWinner[0] is not None:
                # Gewinner-Punkte erhöhen
                points_winner = int(str(currentDataWinner[0])) + 1


                # Punkte und Verluste des Gewinners aktualisieren
                sqlupdate_winner = f"UPDATE {tablename} SET points = %s WHERE name = %s"
                updatevalues_winner = (points_winner, winname)
                self.cursor.execute(sqlupdate_winner, updatevalues_winner)
                self.connection.commit()
                print(winname, "hat einen Punkt hinzugefügt.")

            else:
                # Wenn der Gewinner-Eintrag nicht existiert, einen neuen Eintrag mit Punkten und Verlusten erstellen
                insert_sql_winner = f"INSERT INTO {tablename} (name, points, lose) VALUES (%s, %s, %s)"
                insert_values_winner = (winname, 1, 0)
                self.cursor.execute(insert_sql_winner, insert_values_winner)
                self.connection.commit()
                print(winname, "hat nun 1 Punkt.")

            if currentDataLoser is not None and currentDataLoser[0] is not None:

                # Verlierer-Verluste erhöhen
                lose_loser = int(str(currentDataLoser[0])) + 1

                # Punkte und Verluste des Verlierers aktualisieren
                sqlupdate_loser = f"UPDATE {tablename} SET lose = %s WHERE name = %s"
                updatevalues_loser = (lose_loser, losename)
                self.cursor.execute(sqlupdate_loser, updatevalues_loser)
                self.connection.commit()
                print(losename, "hat einen Verlust hinzugefügt.")

            else:
                # Wenn der Verlierer-Eintrag nicht existiert, einen neuen Eintrag mit Punkten und Verlusten updaten
                insert_sql_loser = f"UPDATE {tablename} SET lose = %s WHERE name = %s"
                insert_values_loser = (1, losename)
                self.cursor.execute(insert_sql_loser, insert_values_loser)
                self.connection.commit()
                print(losename, "hat nun 1 Verlust.")

            return True

        except mysql.connector.Error as e:
            print(f"Fehler beim Hinzufügen von Punkten und Verlusten: {e}")
            return False
                    


    def insertQuery(self,name,password):
        #SQL Insert-Befehl 
        sql = f"INSERT INTO {self.tablenameSpieler()}(name,passwort) VALUES (%s, %s)"
        values = (name,password)

        try:
            #Führt die SQL-Befehle aus.
            self.cursor.execute(sql,values)

            #Änderungen bestätigen
            self.connection.commit()
            result = self.cursor.fetchall()
            return result
        except mysql.connector.Error as e:
            print(f"Fehler bei der Ausführung des Inserates: {e}")
            return False

    #Wird bei der Registration angewendet, um zu überprüfen ob der nutzername bereits angelegt ist
    def checkEntryExists(self, name):
        tablename = self.tablenameSpieler()
        # SQL-Abfrage
        sql = f"SELECT * FROM {tablename} WHERE name = %s"
        values = (name,)

        try:
            # SQL-Abfrage ausführen
            self.cursor.execute(sql, values)

            # Überprüfen, ob der Eintrag vorhanden ist
            entryExist = self.cursor.fetchone() is not None

            if entryExist:
                print(f"Der Eintrag '{name}' ist bereits in der Datenbank vermerkt, versuche es mit einem anderen Namen!")
            else:
                print(f"{name} wird nun in der Datenbank vermerkt.")
            return entryExist
        except mysql.connector.Error as e:
            print(f"Fehler bei der Ausführung der Abfrage: {e}")
            return False
            

    def checkLogin(self,name,passwort):
        try:
            # SQL-Abfrage
            sql = "SELECT COUNT(*) FROM spieler WHERE name = %(name)s AND passwort = %(passwort)s"
            values = {'name': name, 'passwort': passwort}
            self.cursor.execute(sql, values)
            result = self.cursor.fetchone()
            count = result[0] if result is not None else 0

            if count == 1:
                print(f"Anmeldung mit '{name}' ist erfolgreich. Viel Spaß beim Spielen!")
                return True
            else:
                # Kein Eintrag gefunden oder ungültige Anmeldedaten
                print("Anmeldung gescheitert.")
                return False

        except mysql.connector.Error as e:
            print("[Fehlgeschlagen] Es ist ein Fehler aufgetreten:", e)
            return False

    def checkPoints(self,name):
        tablename = self.tablenameSpieler()

        sql = f"SELECT points,lose FROM {tablename} WHERE name = %s"
        value = (name,)

        try:
            self.cursor.execute(sql,value)
            result = self.cursor.fetchone()
            
            if result:
                points = result[0]
                lose = result[1]
                print(name,"hat folgende Menge an Punkte/n und Verluste/n:",points,lose)
                return points,lose
            else:
                print(name,"hat keine Punkte.")
                return result

        except mysql.connector.Error as e:
            print("[Fehlgeschlagen] Fehler bei der Frage des Punktestands:", str(e))
            return False

    def checklose(self,name):
        tablename = self.tablenameSpieler()

        sql = f"SELECT lose FROM {tablename} WHERE name = %s"
        value = (name,)

        try:
            self.cursor.execute(sql,value)
            result = self.cursor.fetchone()
            
            if result:
                print(name,"hat folgende Menge an Punkte/n und Verluste/n:",result[0],result[1])
                return result[0],result[1]
            else:
                print(name,"hat keine Punkte.")
                return result

        except mysql.connector.Error as e:
            print("[Fehlgeschlagen] Fehler bei der Frage des Punktestands:", str(e))
            return False
    def setLoginStatus(self,name,isLoggedIn):
        
        tablename = self.tablenameSpieler()

        sql = f"UPDATE {tablename} SET isLoggedIn = %s WHERE name = %s"
        value = (isLoggedIn,name)

        try:
            #SQL-Abfrage werden ausgeführt
            self.cursor.execute(sql,value)

            #Änderungen werden bestätigt
            self.connection.commit()
            print("Deine Anmeldung wurde in der Datenbank auf True gesetzt!")
            return True
        
        except mysql.connector.Error as e:
            print("[Fehlgeschlagen] Fehler bei Aktualisieren des Anmeldestatus:", str(e))
            return False


    def disconnect(self):
        if self.connection:
            self.connection.close()
            return ("Verbindung mit der Datenbank wurde erfolgreich geschlossen.")
        if self.cursor:
            self.cursor.close()
            return ("Verbindung mit dem Cursor wurde erfolgreich geschlossen.")

