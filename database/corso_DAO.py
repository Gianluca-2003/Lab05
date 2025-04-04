# Add whatever it is needed to interface with the DB Table corso

from database.DB_connect import get_connection
from model.corso import Corso
from model.studente import Studente


class DAO:
    @staticmethod
    def getCodins():
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)

        query= """SELECT *
                  FROM corso c"""
        cursor.execute(query)
        res = []
        for row in cursor:
            res.append(Corso(row["codins"],
                             row["crediti"],
                             row["nome"],
                             row["pd"]))
        cursor.close()
        cnx.close()

        return res

    @staticmethod
    def getStudentiByCodins(codins):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)

        query= """SELECT s.matricola, s.cognome, s.nome, s.CDS
                  FROM corso c, iscrizione i, studente s
                  WHERE c.codins = i.codins and i.matricola = s.matricola 
                  and c.codins = %s"""

        cursor.execute(query, (codins,))
        res = []
        for row in cursor:
            res.append(Studente(**row))

        cursor.close()
        cnx.close()

        return res

    @staticmethod
    def getStudenteByMatricola(matricola):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)

        query= """SELECT s.cognome, s.nome
                  FROM studente s 
                  WHERE s.matricola = %s"""

        cursor.execute(query, (matricola,))
        row = cursor.fetchone()

        cursor.close()
        cnx.close()

        if row:
            return (row["cognome"], row["nome"])
        else:
            return None


    def getCorsiByMatricola(matricola):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)

        query= """SELECT c.codins, c.crediti ,c.nome ,c.pd 
                    FROM corso c, iscrizione i
                    WHERE c.codins = i.codins and i.matricola = %s"""

        cursor.execute(query, (matricola,))
        res = []
        for row in cursor:
            res.append(Corso(**row))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def iscriviStudenteACorso(matricola, codins):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """
                INSERT INTO iscrizione (matricola, codins) VALUES (%s,%s)"""

        cursor.execute(query, (matricola, codins))


        print(f"Ho iscritto {matricola} al corso {codins}")

        cursor.close()
        cnx.close()





if __name__ == '__main__':
    #146101
    #190635 matricola studente esempio
    corsi = DAO.getCorsiByMatricola(190635)
    for corso in corsi:
        print(str(corso))





