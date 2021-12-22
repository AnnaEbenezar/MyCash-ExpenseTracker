import tkinter
from tkinter import *
from tkcalendar import DateEntry


class ExpenseTracker():

    def __init__(self):
        window = Tk()
        window.title("MyCash")
        window.geometry('700x700')

        self.window_label = Label(window, font='ariel 50 bold',
                                  text='MyCash', bg='black', fg='white', bd=15,)
        self.window_label.place(x=180, y=250)
        self.window_label2 = Label(window, font='ariel 35 bold',
                                   text='Expense Tracker', bg='black',
                                   fg='white', bd=15, )
        self.window_label2.place(x=180, y=365)

        # setting button switch state
        self.btn_state = False

        # get icon images
        self.nav_icon = PhotoImage(file='navbar3.png')
        self.close_icon = PhotoImage(file='close_icon3.png')

        # frame for NavBar icon
        self.frame = Frame(window, bg='black')
        self.frame.pack(side='top', fill=X)

        # NavBar button
        self.navbar_btn = Button(self.frame, image=self.nav_icon,
                                 bg='white', bd=0, command=self.switch)
        self.navbar_btn.grid(row=1, column=1)

        # frame for NavBar
        self.NavBar = Frame(window, bg='black', height=1000, width=250)
        self.NavBar.place(x=-250, y=0)

        # NavBar options
        self.option1 = Button(self.NavBar, text='HOME', font='ariel 18 bold', bg='black', fg='white',
                              activebackground='gray', activeforeground='white', bd=0,
                              command=self.homef).place(x=25, y=60)
        self.option2 = Button(self.NavBar, text='EXPENSES', font='ariel 18 bold', bg='black', fg='white',
                              activebackground='gray', activeforeground='white', bd=0,
                              command=self.expensesf).place(x=25, y=120)
        
        # NavBar close button
        self.close_btn = Button(self.NavBar, image=self.close_icon,
                                bg='white', bd=0, command=self.switch)
        self.close_btn.place(x=180, y=5)

        # frame for Home
        self.home_frame = Frame(window, bg='white', height=700, width=700)

        # frame for Expenses
        self.expenses_frame = Frame(window, bg='white', height=700, width=700)

        window.mainloop()

    def switch(self):
        if self.btn_state is True:
            # close NavBar
            for x in range(251):
                self.NavBar.place(x=-x, y=0)
                self.frame.update()
            self.frame.config(bg='black')

            # set button state off
            self.btn_state = False

        else:
            # Open NavBar
            self.hide_frames()
            for x in range(-250, 0):
                self.NavBar.place(x=x, y=0)
                self.frame.update()
            self.frame.config(bg='SystemButtonFace')

            # set button state ON
            self.btn_state = True

    def homef(self):
        self.hide_frames()
        self.switch()
        self.home_frame.pack(fill="both", expand=1)
        self.balance_label = Label(self.home_frame, font='ariel 50 bold',
                                  text='MyCash', bg='black', fg='white', bd=15,)
        self.balance_label.grid(row = 0, column = 0, padx = 1,
                                pady = 1, columnspan = 3)

    def expensesf(self):
        self.hide_frames()
        self.switch()
        self.expenses_frame.pack(fill="both", expand=1)
        self.amt_entry = Entry(self.expenses_frame, bd=5, font='ariel 30',
                               justify=CENTER)
        self.amt_entry.pack(fill=tkinter.X, padx=5, pady=15)

        cal = DateEntry(self.expenses_frame, width=30, year=2021, month=12, day=20,
                        background='darkblue', foreground='white',
                        borderwidth=2, justify=CENTER, font='ariel 25')
        cal.pack(fill=tkinter.X, padx=5, pady=15)

    def hide_frames(self):
        self.home_frame.pack_forget()
        self.expenses_frame.pack_forget()


ExpenseTracker()
