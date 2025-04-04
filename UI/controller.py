import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model



    def handleSearchIscritti(self, e):
        self._view.txtOut.controls.clear()
        codins = self._view.ddCodins.value
        if codins is None:
            self._view.txtOut.controls.append(ft.Text("Seleziona un corso", color="red"))
            self._view._page.update()
            return
        studenti = self._model.getStudentiByCodins(codins)
        n_students = len(studenti)
        self._view.txtOut.controls.append(ft.Text(f"Ci sono al corso {n_students} studenti:"))
        for s in studenti:
            self._view.txtOut.controls.append(ft.Text(str(s)))
        self._view._page.update()


    def handleCercaStudente(self, e):
        self._view.txtOut.controls.clear()
        matricola = self._view.txtInMatricola.value
        if matricola == "":
            self._view.txtOut.controls.append(ft.Text("Devi inserire una matricola", color="red"))
            self._view._page.update()
            return
        cognomeNome = self._model.getStudenteByMatricola(matricola)
        if cognomeNome is None:
            self._view.txtOut.controls.append(ft.Text("Matricola non esistente, riprova", color="red"))
            self._view._page.update()
            return
        self._view.txtInCognome.disabled = False
        self._view.txtInNome.disabled = False
        self._view.txtInCognome.value = cognomeNome[0]
        self._view.txtInNome.value = cognomeNome[1]
        self._view._page.update()



    def handleCercaCorsi(self, e):
        self._view.txtOut.controls.clear()
        matricola = self._view.txtInMatricola.value
        if matricola == "":
            self._view.txtOut.controls.append(ft.Text("Devi inserire una matricola", color="red"))
            self._view._page.update()
            return
        corsi = self._model.getCorsiByMatricola(matricola)
        if len(corsi) == 0:
            self._view.txtOut.controls.append(ft.Text("Questa matricola non esiste", color="red"))
            self._view._page.update()
            return
        self._view.txtOut.controls.append(ft.Text(f"Risultano {len(corsi)} studenti:"))
        for c in corsi:
            self._view.txtOut.controls.append(ft.Text(str(c)))
        self._view._page.update()



    def handleIscriviti(self, e):
        self._view.txtOut.controls.clear()
        codins = self._view.ddCodins.value
        if codins is None:
            self._view.txtOut.controls.append(ft.Text("Seleziona un corso per iscrivere uno studente ad un corso", color="red"))
            self._view._page.update()
            return
        matricola = self._view.txtInMatricola.value
        if matricola == "":
            self._view.txtOut.controls.append(ft.Text("Devi inserire una matricola per iscrivere uno studente ad un corso", color="red"))
            self._view._page.update()
            return
        self._model.iscriviStudenteACorso(matricola, codins)







    def fillDDCodins(self):
        for c in self._model.getCodins():
            self._view.ddCodins.options.append(ft.dropdown.Option(key=c.codins, text=str(c)))


