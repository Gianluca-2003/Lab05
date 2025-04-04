from database.corso_DAO import DAO


class Model:
    def __init__(self):
        pass

    def getCodins(self):
        return DAO.getCodins()

    def getStudentiByCodins(self, codins):
        return DAO.getStudentiByCodins(codins)

    def getStudenteByMatricola(self, matricola):
        return DAO.getStudenteByMatricola(matricola)

    def getCorsiByMatricola(self, matricola):
        return DAO.getCorsiByMatricola(matricola)

    def iscriviStudenteACorso(self,matricola, codins):
        return DAO.iscriviStudenteACorso(matricola, codins)