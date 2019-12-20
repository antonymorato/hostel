import tkinter as tk
import hostel
from tkinter.font import Font
from tkinter import ttk

from src.DBConnect.mongoConnect import mongoConnect
from src.DBConnect.sqlConnect import sqlConn

atrib = {"name": "", "surname": "", "patronymic": "", "bd": "",
         "email": "", "faculty": "", "course": "", "room_num": "",
         "phone_number": "", "sex": "", "clean_rating": "5",
         "electrical_appliance": {"pc": True, "microwave": False, "fridge": False, "kettle": False},
         "inventory_name": "Nothing",
         "amount": "0", "num_in_queue": "0"}


class Interface:
    def __init__(self, master):
        self.terminal = master
        root = self.root = tk.Tk()

        root.title("AdminHostel")
        root.geometry("1475x750+25+25")
        root.resizable(False, False)

        self.main_font = main_font = Font(family="Source Sans Pro", size=20, weight="normal")
        self.icon_font = Font(family="Source Sans Pro", size=32, weight="bold")
        self.additional_font = additional_font = Font(family="Source Sans Pro", size=10, weight="normal")
        self.popup_font = popup_font = Font(family="MS Sans Serif", size=12, weight="normal")
        self.bill_font = bill_font = Font(family="Source Sans Pro", size=16, weight="normal")

        # --------------------------main blocks canvas--------------------------
        self.upper_menu = upper_menu = tk.Canvas(root, height=100, width=1475, bg="#001a57", bd=0, highlightthickness=0)
        self.left_menu = left_menu = tk.Canvas(root, height=650, width=300, bg="#001a57", bd=0, highlightthickness=0)
        self.main_win = main_win = tk.Canvas(root, height=650, width=1175, bg="white", bd=0, highlightthickness=0)

        upper_menu.grid(row=1, column=1, columnspan=2)
        left_menu.grid(row=2, column=1, rowspan=5)
        main_win.grid(row=2, column=2, rowspan=5)

        upper_menu.place(x=0, y=0, width=1475, height=100)
        left_menu.place(x=0, y=100, width=300, height=650)
        main_win.place(x=300, y=100, width=1175, height=650)

        # ---------------------AdminHostel title---------------------------------
        icon_title = tk.Label(upper_menu, text="AdminHostel.", bg="#001a57", font=self.icon_font,
                              fg="white")
        icon_title.pack()
        icon_title.place(x=15, y=25)

        # ----------------------Buttons at the left------------------------------
        rooms_btn = tk.Button(left_menu, text="Кімнати", bg="#001a57", fg="white", font=main_font,
                              command=self.choose_rooms_frame)
        students_btn = tk.Button(left_menu, text="Студенти", bg="#001a57", fg="white", font=main_font,
                                 command=self.choose_students_frame)
        bills_btn = tk.Button(left_menu, text="Рахунки", bg="#001a57", fg="white", font=main_font,
                              command=self.choose_bills_frame)
        inventory_btn = tk.Button(left_menu, text="Інвентар", bg="#001a57", fg="white", font=main_font,
                                  command=self.choose_works_frame)
        works_btn = tk.Button(left_menu, text="Благоустрій", bg="#001a57", fg="white", font=main_font,
                              command=self.choose_works_frame)

        rooms_btn.pack()
        students_btn.pack()
        bills_btn.pack()
        inventory_btn.pack()
        works_btn.pack()

        left_menu.create_window(150, 50, window=rooms_btn, width=300, height=100)
        left_menu.create_window(150, 150, window=students_btn, width=300, height=100)
        left_menu.create_window(150, 250, window=bills_btn, width=300, height=100)
        left_menu.create_window(150, 350, window=inventory_btn, width=300, height=100)
        left_menu.create_window(150, 450, window=works_btn, width=300, height=100)

        # ----------------------Frames for content----------------------------------
        self.zero_frame = tk.Frame(main_win, width=1175, height=650, bg="white")  # To delete in future
        self.first_frame = tk.Frame(main_win, width=1175, height=650, bg="white")
        self.second_frame = tk.Frame(main_win, width=1175, height=650, bg="white")
        self.third_frame = tk.Frame(main_win, width=1175, height=650, bg="white")
        self.fourth_frame = tk.Frame(main_win, width=1175, height=650, bg="white")
        self.fifth_frame = tk.Frame(main_win, width=1175, height=650, bg="white")

        self.zero_frame.grid(row=2, column=2, rowspan=5)
        self.first_frame.grid(row=2, column=2, rowspan=5)
        self.second_frame.grid(row=2, column=2, rowspan=5)
        self.third_frame.grid(row=2, column=2, rowspan=5)
        self.fourth_frame.grid(row=2, column=2, rowspan=5)
        self.fifth_frame.grid(row=2, column=2, rowspan=5)

        # In order not to display (grid forget), displays only zero frame
        self.fifth_frame.grid_forget()
        self.fourth_frame.grid_forget()
        self.third_frame.grid_forget()
        self.second_frame.grid_forget()
        self.first_frame.grid_forget()

        # ------------------Zero Frame Content--------------------
        greeting = tk.Text(self.zero_frame, bg="white", bd=0,
                           padx=320, pady=260, font=self.icon_font)
        greeting.insert("end", u"Ласкаво просимо!\nАвторизуйтесь у системі.")
        greeting.pack()

        # ----------------First Frame Content (Rooms Tab)---------
        self.rooms_tree1 = rooms_tree1 = ttk.Treeview(self.first_frame)
        self.rooms_tree2 = rooms_tree2 = ttk.Treeview(self.first_frame)
        self.rooms_tree3 = rooms_tree3 = ttk.Treeview(self.first_frame)
        self.rooms_tree4 = rooms_tree4 = ttk.Treeview(self.first_frame)
        self.rooms_tree5 = rooms_tree5 = ttk.Treeview(self.first_frame)

        # TODO need to be like this: room_folder contains students
        # TODO rooms must be already added (from db or manually from front or logic)
        rooms_tree1.place(x=0, y=0, width=193, height=650)
        rooms_tree2.place(x=192, y=0, width=193, height=650)
        rooms_tree3.place(x=384, y=0, width=193, height=650)
        rooms_tree4.place(x=576, y=0, width=193, height=650)
        rooms_tree5.place(x=768, y=0, width=193, height=650)

        rooms_tree1["columns"] = ()
        rooms_tree2["columns"] = ()
        rooms_tree3["columns"] = ()
        rooms_tree4["columns"] = ()
        rooms_tree5["columns"] = ()

        rooms_tree1.column("#0", stretch=tk.NO)
        rooms_tree2.column("#0", stretch=tk.NO)
        rooms_tree3.column("#0", stretch=tk.NO)
        rooms_tree4.column("#0", stretch=tk.NO)
        rooms_tree5.column("#0", stretch=tk.NO, width=191)

        rooms_tree1.heading("#0", text="1 поверх", anchor="center")
        rooms_tree2.heading("#0", text="2 поверх", anchor="center")
        rooms_tree3.heading("#0", text="3 поверх", anchor="center")
        rooms_tree4.heading("#0", text="4 поверх", anchor="center")
        rooms_tree5.heading("#0", text="5 поверх", anchor="center")

        total_students_label = self.total_students_label = tk.Label(self.first_frame, text="Кількість студентів: ",
                                                                    font=popup_font, bg="white")

        total_free_rooms = self.total_free_rooms = tk.Label(self.first_frame, text="Вільних кімнат: ",
                                                            font=popup_font, bg="white")
        total_free_places = self.total_free_places = tk.Label(self.first_frame, text="Вільних місць: ",
                                                              font=popup_font, bg="white")

        total_students_label.place(x=970, y=5)
        total_free_rooms.place(x=970, y=35)
        total_free_places.place(x=970, y=65)

        # rooms frame is just to display rooms and their content (get them from database)
        # example, just to understand the structure
        # create function to output rooms
        # level 1 (folder)
        self.upload_rooms()

        # TODO delete this (calls only in load and delete student btns)
        self.update_total_students()

        # -----------------Second Frame Content (Students Tab)----
        self.students_tree = students_tree = ttk.Treeview(self.second_frame)

        students_tree["columns"] = ("one", "two", "three", "four", "five", "six", "seven")
        students_tree.column("#0", width=230, minwidth=230, stretch=tk.NO)
        students_tree.column("one", width=55, minwidth=55, stretch=tk.NO)
        students_tree.column("two", width=70, minwidth=70, stretch=tk.NO)
        students_tree.column("three", width=90, minwidth=90, stretch=tk.NO)
        students_tree.column("four", width=50, minwidth=50, stretch=tk.NO)
        students_tree.column("five", width=150, minwidth=150, stretch=tk.NO)
        students_tree.column("six", width=150, minwidth=150, stretch=tk.NO)
        students_tree.column("seven", width=165, minwidth=165, stretch=tk.NO)

        students_tree.heading("#0", text="ПІБ", anchor="center")
        students_tree.heading("one", text="Стать", anchor="center")
        students_tree.heading("two", text="Кімната", anchor="center")
        students_tree.heading("three", text="Факультет", anchor="center")
        students_tree.heading("four", text="Курс", anchor="center")
        students_tree.heading("five", text="Номер телефону", anchor="center")
        students_tree.heading("six", text="Дата народження", anchor="center")
        students_tree.heading("seven", text="Пошта", anchor="center")

        students_tree.place(x=0, y=0, width=961, height=650)
        style = ttk.Style()
        style.configure("Treeview.Heading", font=(None, 12), background="#d7d7d7", fieldbackground="#d7d7d7",
                        borderwidth=0)
        st_scrollbar = ttk.Scrollbar(self.second_frame, orient="vertical", command=students_tree.yview)
        st_scrollbar.place(x=960, y=0, height=650)
        students_tree.configure(yscrollcommand=st_scrollbar.set)

        style.configure("TCombobox", font=(None, 12), background="#d7d7d7", fieldbackground="#d7d7d7",
                        borderwidth=0)

        self.add_student = tk.Button(self.second_frame, text="Додати студента", command=self.show_add_student,
                                     width=25, height=2, bd=0, font=additional_font)
        self.add_student.place(x=977, y=0)

        self.delete_student = tk.Button(self.second_frame, text="Видалити студента",
                                        command=self.delete_student_func, width=25, height=2,
                                        bd=0, font=additional_font)
        self.delete_student.place(x=977, y=41)

        self.edit_student = tk.Button(self.second_frame, text="Редагувати",
                                      command=self.show_edit_student,
                                      width=25, height=2, bd=0,
                                      font=additional_font)
        self.edit_student.place(x=977, y=82)

        self.search_student_input = tk.Entry(self.second_frame,
                                             font=Font(family="Source Sans Pro", size=12, weight="normal"), width=30,
                                             bd=0,
                                             bg="#e3e3e3")

        self.search_student_input.place(x=977, y=123, height=40)

        self.search_student = tk.Button(self.second_frame, text="Пошук",
                                        command=self.search_student_func,
                                        width=25, height=2, bd=0,
                                        font=additional_font)
        self.search_student.place(x=977, y=164)

        # ----------------------Third frame content---------------------------
        self.label_bill = label_bill = tk.Label(self.third_frame, text="Створення рахунку студента",
                                                font=main_font, bg="white")
        label_bill.place(x=390, y=5)

        self.bill_surname_label = bill_surname_label = tk.Label(self.third_frame, text="Прізвище",
                                                                font=bill_font, bg="white")
        bill_surname_label.place(x=100, y=100)

        self.bill_surname_input = bill_surname_input = tk.Entry(self.third_frame, font=bill_font, bg="#e3e3e3", bd=0,
                                                                width=18)
        bill_surname_input.place(x=210, y=100)

        self.bill_name_label = bill_name_label = tk.Label(self.third_frame, text="Ім'я",
                                                          font=bill_font, bg="white")
        bill_name_label.place(x=440, y=100)

        self.bill_name_input = bill_name_input = tk.Entry(self.third_frame, font=bill_font, bg="#e3e3e3", bd=0,
                                                          width=18)
        bill_name_input.place(x=490, y=100)

        self.bill_patronymic_label = bill_patronymic_label = tk.Label(self.third_frame, text="По-батькові",
                                                                      font=bill_font, bg="white")
        bill_patronymic_label.place(x=720, y=100)

        self.bill_patronymic_input = bill_patronymic_input = tk.Entry(self.third_frame, font=bill_font, bg="#e3e3e3",
                                                                      bd=0, width=18)
        bill_patronymic_input.place(x=850, y=100)

        self.bill_phone_label = bill_phone_label = tk.Label(self.third_frame, text="Номер телефону",
                                                            font=bill_font, bg="white")
        bill_phone_label.place(x=360, y=200)

        self.bill_phone_label = bill_phone_label = tk.Entry(self.third_frame, font=bill_font, bg="#e3e3e3",
                                                            bd=0, width=18)
        bill_phone_label.place(x=540, y=200)

        self.bill_type_label = bill_type_label = tk.Label(self.third_frame, text="Тип рахунку", font=bill_font,
                                                          bg="white")
        bill_type_label.place(x=170, y=300)

        self.bill_type_input = bill_type_input = ttk.Combobox(self.third_frame,
                                                              values=["за проживання", "за електроенергію"],
                                                              font=bill_font,
                                                              width=18)
        bill_type_input.place(x=300, y=300)

        # --------Dynamic widgets---------------------------------------------
        self.dynamic_widgets = dict()
        self.fill_zeros_dynamic_widgets(self.dynamic_widgets)
        # ------------Out-all-students----------------------------------------
        self.get_all_students()

    def fill_zeros_dynamic_widgets(self, dynamic_widgets):
        dynamic_widgets.update(current_popup=None,
                               name=None)

    def reset_dynamic_widgets(self):
        for key in self.dynamic_widgets.keys():
            self.dynamic_widgets[key] = None

        # ------------------Popups--------------------------------------------

    def create_basic_popup(self, width, height):
        popup = tk.Toplevel(self.root, bg="white")
        popup.geometry(F"{width}x{height}+500+100")
        popup.grab_set()
        popup.resizable(False, False)

        self.dynamic_widgets["current_popup"] = popup
        return popup

    def show_add_student(self):
        add_st_popup = self.create_basic_popup(width=600, height=600)
        add_st_popup.title("Додати студента")

        name_label = tk.Label(add_st_popup, text="ПІБ",
                              font=self.popup_font, width=15)
        name_input = tk.Entry(add_st_popup,
                              font=self.popup_font, width=50, bd=0, bg="#e1e1e1")

        sex_label = tk.Label(add_st_popup, text="Стать",
                             font=self.popup_font, width=15, bd=0)
        sex_input = ttk.Combobox(add_st_popup,
                                 values=[
                                     "чоловіча",
                                     "жіноча"
                                 ],
                                 font=self.popup_font,
                                 width=18)

        room_label = tk.Label(add_st_popup, text="Кімната",
                              font=self.popup_font, width=15, bd=0)
        room_input = tk.Entry(add_st_popup,
                              font=self.popup_font, width=10, bd=0, bg="#e1e1e1")

        faculty_label = tk.Label(add_st_popup, text="Факультет",
                                 font=self.popup_font, width=15, bd=0)
        faculty_input = tk.Entry(add_st_popup,
                                 font=self.popup_font, width=20, bd=0, bg="#e1e1e1")

        course_label = tk.Label(add_st_popup, text="Курс",
                                font=self.popup_font, width=15, bd=0)
        course_input = ttk.Combobox(add_st_popup,
                                    values=[
                                        "1", "2", "3", "4", "5", "6"
                                    ],
                                    font=self.popup_font,
                                    width=8)
        phone_num_label = tk.Label(add_st_popup, text="Номер телефону",
                                   font=self.popup_font, width=15, bd=0)
        phone_num_input = tk.Entry(add_st_popup,
                                   font=self.popup_font, width=50, bd=0, bg="#e1e1e1")
        birth_date_label = tk.Label(add_st_popup, text="Дата народження",
                                    font=self.popup_font, width=15, bd=0)
        birth_date_input = tk.Entry(add_st_popup,
                                    font=self.popup_font, width=50, bd=0, bg="#e1e1e1")
        email_label = tk.Label(add_st_popup, text="Пошта",
                               font=self.popup_font, width=15, bd=0)
        email_input = tk.Entry(add_st_popup,
                               font=self.popup_font, width=50, bd=0, bg="#e1e1e1")

        add_st_btn = tk.Button(add_st_popup, text="Додати", comman=self.load_student_info, bd=0, width=25, height=2)

        electrical_label = tk.Label(add_st_popup, text="Електроприлади", font=self.popup_font, width=15, bd=0)

        electrical_label.place(anchor="w", rely=0.7)
        pc_var = tk.BooleanVar()
        pc_var.set(0)
        pc_checkbtn = tk.Checkbutton(add_st_popup, text="Комп'ютер", variable=pc_var, onvalue=1, offvalue=0)
        pc_checkbtn.place(x=150, y=407)
        fridge_var = tk.BooleanVar()
        fridge_var.set(0)
        fridge_checkbtn = tk.Checkbutton(add_st_popup, text="Холодильник", variable=fridge_var, onvalue=1, offvalue=0)
        fridge_checkbtn.place(x=150, y=445)
        microwave_var = tk.BooleanVar()
        microwave_var.set(0)
        microwave_checkbtn = tk.Checkbutton(add_st_popup, text="Мікрохвильовка", variable=microwave_var, onvalue=1,
                                            offvalue=0)
        microwave_checkbtn.place(x=250, y=407)
        kettle_var = tk.BooleanVar()
        kettle_var.set(0)
        kettle_checkbtn = tk.Checkbutton(add_st_popup, text="Електрочайник", variable=kettle_var, onvalue=1, offvalue=0)
        kettle_checkbtn.place(x=265, y=445)

        name_label.place(anchor="w", rely=0.1)
        name_input.place(anchor="e", relx=1, rely=0.1)
        sex_label.place(anchor="w", rely=0.2)
        sex_input.place(x=150, y=105)
        room_label.place(x=350, y=107)
        room_input.place(x=500, y=107)
        faculty_label.place(anchor="w", rely=0.3)
        faculty_input.place(x=150, y=170)
        course_label.place(x=350, y=170)
        course_input.place(x=500, y=166)
        phone_num_label.place(anchor="w", rely=0.4)
        phone_num_input.place(anchor="e", relx=1, rely=0.4)
        birth_date_label.place(anchor="w", rely=0.5)
        birth_date_input.place(anchor="e", relx=1, rely=0.5)
        email_label.place(anchor="w", rely=0.6)
        email_input.place(anchor="e", relx=1, rely=0.6)

        add_st_btn.place(anchor="center", relx=0.5, rely=0.9)

        self.dynamic_widgets["name"] = name_input
        self.dynamic_widgets["sex"] = sex_input
        self.dynamic_widgets["room"] = room_input
        self.dynamic_widgets["faculty"] = faculty_input
        self.dynamic_widgets["course"] = course_input
        self.dynamic_widgets["number"] = phone_num_input
        self.dynamic_widgets["birth_date"] = birth_date_input
        self.dynamic_widgets["email"] = email_input
        self.dynamic_widgets["pc"] = pc_var
        self.dynamic_widgets["fridge"] = fridge_var
        self.dynamic_widgets["microwave"] = microwave_var
        self.dynamic_widgets["kettle"] = kettle_var

        add_st_popup.mainloop()

    def delete_student_func(self):
        # TODO delete also from database
        item = self.students_tree.selection()[0]
        item_text = self.students_tree.item(item, "text")
        atrib["surname"], atrib["name"], atrib["patronymic"] = tuple(item_text.split())
        self.terminal.delete_student(atrib)
        self.students_tree.delete(item)
        self.update_total_students()

    def search_student_func(self, item=''):
        # TODO scroll if item is not in a visible area
        children = self.students_tree.get_children(item)
        for child in children:
            text = self.students_tree.item(child, 'text')
            if text.startswith(self.search_student_input.get()):
                self.students_tree.selection_set(child)
                return True
            else:
                res = self.search_student_func(child)
                if res:
                    return True

    def show_edit_student(self):
        # TODO edit in database (ask Denys for help)
        # TODO get from database, input new items and put into database and update treeview
        edit_st_popup = self.create_basic_popup(width=600, height=600)
        edit_st_popup.title("Редагувати студента")

        name_label_edit = tk.Label(edit_st_popup, text="ПІБ",
                                   font=self.popup_font, width=15)
        name_input_edit = tk.Entry(edit_st_popup,
                                   font=self.popup_font, width=50, bd=0, bg="#e1e1e1")

        sex_label_edit = tk.Label(edit_st_popup, text="Стать",
                                  font=self.popup_font, width=15, bd=0)
        sex_input_edit = ttk.Combobox(edit_st_popup,
                                      values=[
                                          "ч",
                                          "ж"
                                      ],
                                      font=self.popup_font,
                                      width=48)

        room_label_edit = tk.Label(edit_st_popup, text="Кімната",
                                   font=self.popup_font, width=15, bd=0)
        room_input_edit = tk.Entry(edit_st_popup,
                                   font=self.popup_font, width=50, bd=0, bg="#e1e1e1")

        faculty_label_edit = tk.Label(edit_st_popup, text="Факультет",
                                      font=self.popup_font, width=15, bd=0)
        faculty_input_edit = tk.Entry(edit_st_popup,
                                      font=self.popup_font, width=50, bd=0, bg="#e1e1e1")

        course_label_edit = tk.Label(edit_st_popup, text="Курс",
                                     font=self.popup_font, width=15, bd=0)
        course_input_edit = ttk.Combobox(edit_st_popup,
                                         values=[
                                             "1", "2", "3", "4", "5", "6"
                                         ],
                                         font=self.popup_font,
                                         width=48)
        phone_num_label_edit = tk.Label(edit_st_popup, text="Номер телефону",
                                        font=self.popup_font, width=15, bd=0)
        phone_num_input_edit = tk.Entry(edit_st_popup,
                                        font=self.popup_font, width=50, bd=0, bg="#e1e1e1")
        birth_date_label_edit = tk.Label(edit_st_popup, text="Дата народження",
                                         font=self.popup_font, width=15, bd=0)
        birth_date_input_edit = tk.Entry(edit_st_popup,
                                         font=self.popup_font, width=50, bd=0, bg="#e1e1e1")
        email_label_edit = tk.Label(edit_st_popup, text="Пошта",
                                    font=self.popup_font, width=15, bd=0)
        email_input_edit = tk.Entry(edit_st_popup,
                                    font=self.popup_font, width=50, bd=0, bg="#e1e1e1")

        add_st_btn_edit = tk.Button(edit_st_popup, text="Зберегти зміни", comman=self.load_student_info, bd=0, width=25,
                                    height=2)

        name_label_edit.place(anchor="w", rely=0.1)
        name_input_edit.place(anchor="e", relx=1, rely=0.1)
        sex_label_edit.place(anchor="w", rely=0.2)
        sex_input_edit.place(anchor="e", relx=1, rely=0.2)
        room_label_edit.place(anchor="w", rely=0.3)
        room_input_edit.place(anchor="e", relx=1, rely=0.3)
        faculty_label_edit.place(anchor="w", rely=0.4)
        faculty_input_edit.place(anchor="e", relx=1, rely=0.4)
        course_label_edit.place(anchor="w", rely=0.5)
        course_input_edit.place(anchor="e", relx=1, rely=0.5)
        phone_num_label_edit.place(anchor="w", rely=0.6)
        phone_num_input_edit.place(anchor="e", relx=1, rely=0.6)
        birth_date_label_edit.place(anchor="w", rely=0.7)
        birth_date_input_edit.place(anchor="e", relx=1, rely=0.7)
        email_label_edit.place(anchor="w", rely=0.8)
        email_input_edit.place(anchor="e", relx=1, rely=0.8)

        add_st_btn_edit.place(anchor="center", relx=0.5, rely=0.9)

        edit_st_popup.mainloop()
        # --------------------------------------------------------------------

    def close_popup(self, popup=None):
        if popup:
            popup.destroy()
        else:
            self.dynamic_widgets["current_popup"].destroy()
        self.reset_dynamic_widgets()

        # -------------------Load info into logic----------------------------------------

    # Денис тут добавляю терминал.лоад_студент
    def load_student_info(self):
        atrib["surname"], atrib["name"], atrib["patronymic"] = tuple(str(self.dynamic_widgets["name"].get()).split())
        atrib["sex"] = self.dynamic_widgets["sex"].get()
        atrib["room_num"] = self.dynamic_widgets["room"].get()
        atrib["faculty"] = self.dynamic_widgets["faculty"].get()
        atrib["course"] = self.dynamic_widgets["course"].get()
        atrib["phone_number"] = self.dynamic_widgets["number"].get()
        atrib["bd"] = self.dynamic_widgets["birth_date"].get()
        atrib["email"] = self.dynamic_widgets["email"].get()
        atrib["pc"] = self.dynamic_widgets["pc"].get()
        atrib["fridge"] = self.dynamic_widgets["fridge"].get()
        atrib["microwave"] = self.dynamic_widgets["microwave"].get()
        atrib["kettle"] = self.dynamic_widgets["kettle"].get()

        self.terminal.load_student(atrib)
        self.update_students(atrib["surname"] + " " + atrib["name"] + " " + atrib["patronymic"], atrib["sex"],
                             atrib["room_num"],
                             atrib["faculty"], atrib["course"], atrib["phone_number"], atrib["bd"], atrib["email"],
                             atrib["pc"], atrib["fridge"],
                             atrib["microwave"], atrib["kettle"])
        self.update_total_students()
        # TODO ATTENTION
        # _____ATTENTION_ATTENTION_ATTENTION_ATTENTION_ATTENTION____________
        # ________________________ATTENTION_______________________________
        # ________________________ATTENTION_______________________________
        # трохи не правильно працює можливо потрібно очищувати фрейм і заново аплодити
        self.upload_rooms()
        self.close_popup()

        # ------------------Get info from logic----------------------------------------
        # TODO add body of this functions into logic

    def update_total_students(self):
        self.total_students_label["text"] = F"Кількість студентів: {self.terminal.get_total_students()}"
        self.total_free_places["text"] = F"Вільних місць: {self.terminal.get_total_free_places()}"

        # ------------------Show Frames---------------------------------------

    def choose_rooms_frame(self):
        self.zero_frame.grid_forget()
        self.first_frame.grid(row=2, column=2, rowspan=5)
        self.fifth_frame.grid_forget()
        self.fourth_frame.grid_forget()
        self.third_frame.grid_forget()
        self.second_frame.grid_forget()

    def choose_students_frame(self):
        self.second_frame.grid(row=2, column=2, rowspan=5)
        self.fifth_frame.grid_forget()
        self.fourth_frame.grid_forget()
        self.third_frame.grid_forget()
        self.first_frame.grid_forget()
        self.zero_frame.grid_forget()

    def choose_bills_frame(self):
        self.third_frame.grid(row=2, column=2, rowspan=5)
        self.fifth_frame.grid_forget()
        self.fourth_frame.grid_forget()
        self.second_frame.grid_forget()
        self.first_frame.grid_forget()
        self.zero_frame.grid_forget()

    def choose_inventory_frame(self):
        self.fourth_frame.grid(row=2, column=2, rowspan=5)
        self.fifth_frame.grid_forget()
        self.third_frame.grid_forget()
        self.second_frame.grid_forget()
        self.first_frame.grid_forget()
        self.zero_frame.grid_forget()

    def choose_works_frame(self):
        self.fifth_frame.grid(row=2, column=2, rowspan=5)
        self.fifth_frame.grid_forget()
        self.fourth_frame.grid_forget()
        self.third_frame.grid_forget()
        self.second_frame.grid_forget()
        self.zero_frame.grid_forget()

        # ------------Update Section-----------------------------

        # TODO need to get info from database and do this insertions in a loop (the example of insertion is given)

    def update_students(self, name, sex, room, faculty, course, number, birth_date, email, pc, fridge,
                        microwave, kettle):
        self.students_tree.insert("", "end", text=name, values=(sex, room, faculty, course, number, birth_date, email,
                                                                pc, fridge, microwave, kettle))

    def get_all_students(self):
        # print(self.terminal.get_rooms())
        array = self.terminal.get_all_students()
        for i in array:
            self.update_students(i["surname"] + " " + i["name"] + " " + i["patronymic"], i["sex"],
                                 i["room_num"], i["faculty"], i["course"], i["phone_number"], i["bd"], i["email"],
                                 i["electrical_appliance"]["pc"], i["electrical_appliance"]["microwave"],
                                 i["electrical_appliance"]["fridge"], i["electrical_appliance"]["kettle"])

    def upload_rooms(self):
        levels = self.terminal.get_rooms()
        for level in range(len(levels)):
            if level == 0:
                for room in levels[level]:
                    buff = self.rooms_tree1.insert("", 2, text=room["room_num"])
                    for student in room["students"]:
                        self.rooms_tree1.insert(buff, "end", text=student)
            if level == 1:
                for room in levels[level]:
                    buff = self.rooms_tree2.insert("", 2, text=room["room_num"])
                    for student in room["students"]:
                        self.rooms_tree2.insert(buff, "end", text=student)
            if level == 2:
                for room in levels[level]:
                    buff = self.rooms_tree3.insert("", 2, text=room["room_num"])
                    for student in room["students"]:
                        self.rooms_tree3.insert(buff, "end", text=student)
            if level == 3:
                for room in levels[level]:
                    buff = self.rooms_tree4.insert("", 2, text=room["room_num"])
                    for student in room["students"]:
                        self.rooms_tree4.insert(buff, "end", text=student)
            if level == 4:
                for room in levels[level]:
                    buff = self.rooms_tree5.insert("", 2, text=room["room_num"])
                    for student in room["students"]:
                        self.rooms_tree5.insert(buff, "end", text=student)

    def create_bill(self):
        dictionary = {}
        print(self.bill_name_input)


# interface = Interface("Master")
sqlConn.connect()
mongoConnect.connect()
interface = Interface(hostel.Terminal(atrib))
interface.root.mainloop()
sqlConn.disconnect()
