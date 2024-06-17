import ELSTER
import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("ELSTER")
        self.geometry("450x400")
        for c in range(2): self.grid_columnconfigure(c, weight=1)
        for r in range(10): self.grid_rowconfigure(r, weight=1)

        # поле поиска
        self.input_search = customtkinter.CTkEntry(self, placeholder_text="что желаете найти?")
        self.input_search.grid(row=0, column=0, padx=20,pady=0, columnspan=2, sticky="ew")

        # табличка поиска
        self.label_point = customtkinter.CTkLabel(self, text="В каком радиусе от точки искать?")
        self.label_point.grid(row=1,column=0, padx=20, columnspan=2, sticky="ew")

        # поле координат X
        self.input_X = customtkinter.CTkEntry(self, placeholder_text="X")
        self.input_X.grid(row=2, column=0, padx=20,pady=0, sticky="ew")

        # поле координат Y
        self.input_Y = customtkinter.CTkEntry(self, placeholder_text="Y")
        self.input_Y.grid(row=3, column=0, padx=20,pady=0, sticky="ew")

        # табличка метров
        self.label_meter = customtkinter.CTkLabel(self, text="количество метров")
        self.label_meter.grid(row=2,column=1, padx=20, pady=0, columnspan=2, sticky="ew")

        # поле метров
        self.input_meter = customtkinter.CTkEntry(self, placeholder_text="метры")
        self.input_meter.grid(row=3, column=1, padx=20, pady=0, sticky="ew")

        # табличка данных
        self.label_data = customtkinter.CTkLabel(self, text="какие данные вывести?")
        self.label_data.grid(row=4,column=0, padx=20, pady=0, columnspan=2, sticky="ew")

        # chekbox
        self.checkbox_name = customtkinter.CTkCheckBox(self, text="название")
        self.checkbox_name.grid(row=5,column=0, padx=20, pady=0, sticky="ew")

        self.checkbox_address = customtkinter.CTkCheckBox(self, text="адрес")
        self.checkbox_address.grid(row=6,column=0, padx=20, pady=0, sticky="ew")

        self.checkbox_phone = customtkinter.CTkCheckBox(self, text="телефон")
        self.checkbox_phone.grid(row=7,column=0, padx=20, pady=0, sticky="ew")

        self.checkbox_time = customtkinter.CTkCheckBox(self, text="время работы")
        self.checkbox_time.grid(row=5,column=1, padx=20, pady=0, sticky="ew")

        self.checkbox_coordinates = customtkinter.CTkCheckBox(self, text="координаты")
        self.checkbox_coordinates.grid(row=6,column=1, padx=20, pady=0, sticky="ew")

        self.checkbox_distance = customtkinter.CTkCheckBox(self, text="удалённость от точки")
        self.checkbox_distance.grid(row=7,column=1, padx=20, pady=0, sticky="ew")

        self.checkbox_url = customtkinter.CTkCheckBox(self, text="ссылка")
        self.checkbox_url.grid(row=8,column=0, padx=20, pady=0, sticky="ew")

        # табличка "в каком формате выводить?"
        self.label_import = customtkinter.CTkLabel(self, text="в каком формате вернуть данные?")
        self.label_import.grid(row=9,column=0, padx=20, pady=0, columnspan=2, sticky="ew")

        # кнопка excel
        self.import_to_excel = customtkinter.CTkButton(self,  fg_color="green", hover_color="darkgreen",text="EXCEL", command=self.import_to_excel)
        self.import_to_excel.grid(row=10, column=0, padx=10,pady=10,sticky="ew")

        # кнопка csv
        self.import_to_csv = customtkinter.CTkButton(self, fg_color="green", hover_color="darkgreen",text="CSV", command=self.import_to_csv)
        self.import_to_csv.grid(row=10, column=1, padx=10,pady=10,sticky="ew")

    '''
    получение данных с формы
    '''
    def get_data_for_form(self):
        return {
            'search': self.input_search.get(),
            'X': self.input_X.get(),
            'Y': self.input_Y.get(),
            'meter': self.input_meter.get(),
            'name': self.checkbox_name.get(),
            'address': self.checkbox_address.get(),
            'url': self.checkbox_url.get(),
            'phone': self.checkbox_phone.get(),
            'time': self.checkbox_time.get(),
            'checkbox_coordinates': self.checkbox_coordinates.get(),
            'distance': self.checkbox_distance.get(),
            }

    '''
    удаление лишних столбцов
    '''
    def change_dict(self, data_form: dict, data:dict) -> dict:
        if (data_form['name'] == 0):
            del data['название']
        if (data_form['address'] == 0):
            del data['адресс']
        if (data_form['phone'] == 0):
            del data['телефоны']
        if (data_form['time'] == 0):
            del data['время работы']
        if (data_form['checkbox_coordinates'] == 0):
            del data['координаты здания']
        if (data_form['distance'] == 0):
            del data['дистанция до точки']
        if (data_form['url'] == 0):
            del data['ссылка']
        return data

    '''
    импортирование в excel
    '''
    def import_to_excel(self):
        data_form = self.get_data_for_form()
        data = ELSTER.get_dict(SearchedOrganization=data_form['search'], X=data_form['X'], Y=data_form['Y'], distance=data_form['meter'])
        data = self.change_dict(data_form=data_form, data=data)
        ELSTER.data_to_excel(data)

    '''
    импортирование в csv
    '''
    def import_to_csv(self):
        data_form = self.get_data_for_form()
        data = ELSTER.get_dict(SearchedOrganization=data_form['search'], X=data_form['X'], Y=data_form['Y'], distance=data_form['meter'])
        data = self.change_dict(data_form=data_form, data=data)
        ELSTER.data_to_csv(data)

if __name__ == "__main__":
    app = App()
    app.mainloop()