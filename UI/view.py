import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.ddCodins = None
        self.btnSearchIscritti = None
        self.txtOut = None
        self.txtInMatricola = None
        self.txtInNome = None
        self.txtInCognome = None
        self.btnCercaCorsi = None
        self.btnIscriviti = None
        self.btnCercaStudente = None




    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App Gestione studenti", color="blue", size=24)
        self._page.controls.append(self._title)
        self.ddCodins = ft.Dropdown(label="Corso", width=self._page.width*0.74, hint_text="Selezionare un corso")
        self._controller.fillDDCodins()
        self.btnSearchIscritti = ft.ElevatedButton(text="cerca iscritti",
                                                   color="blue",
                                                   on_click=self._controller.handleSearchIscritti)
        row1 = ft.Row([self.ddCodins, self.btnSearchIscritti])

        self.txtInMatricola = ft.TextField(label="Matricola", width=self._page.width*0.30)
        self.txtInNome = ft.TextField(label="Nome", disabled=True,width=self._page.width*0.30)
        self.txtInCognome = ft.TextField(label="Cognome", disabled=True,width=self._page.width*0.30)

        row2 = ft.Row([self.txtInMatricola, self.txtInNome, self.txtInCognome])

        self.txtOut = ft.ListView(expand=True)

        self.btnCercaStudente = ft.ElevatedButton(text="cerca studente",
                                                  color="blue",
                                                  on_click=self._controller.handleCercaStudente)
        self.btnCercaCorsi = ft.ElevatedButton(text="cerca corsi",
                                               color="blue",
                                               on_click=self._controller.handleCercaCorsi)
        self.btnIscriviti = ft.ElevatedButton(text="iscriviti",
                                               color="blue",
                                               on_click=self._controller.handleIscriviti)

        row3 = ft.Row([self.btnCercaStudente, self.btnCercaCorsi, self.btnIscriviti], alignment=ft.MainAxisAlignment.CENTER)


        #ROW with some controls
        # text field for the name

        self._page.add(row1,row2, row3,self.txtOut)

        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
