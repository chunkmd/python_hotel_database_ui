#!/home/alien/PycharmProjects/Hotel
# coding = utf-8

# Plămădeală Vladislav - plamadeala.vladislav@iis.utm.md
#

import random
import secrets
import tkinter.messagebox as msg_box
import tkinter.scrolledtext as tkst
from datetime import date
from datetime import datetime
import tkinter
from tkinter import font, ttk

import names  # Need to pip3 install names --user
# faker-e164 -> phone numbers pip3 install
import pycountry  # Need to pip3 install pycountry --user
import faker
import tkcalendar  # Need to pip3 install tkcalendar
from faker.config import AVAILABLE_LOCALES
from faker.proxy import Faker
from tkcalendar.dateentry import DateEntry

from src import Hotel_DB


class Hotel:

    def __init__(self, root):
        self.root = root
        self.initUI()
        self.Display_Booking()


    def initUI(self):
        self.root.title('Hotel Database Management System')
        self.geometry = self.screen_size(size=0.75)
        # print( self.geometry )
        self.root.geometry(self.geometry)
        self.center_root()
        self.root.configure(background='deep sky blue')
        self.root.protocol('WM_DELETE_WINDOW', self.Ask_Quit)
        self.setup_frames()
        self.setup_fonts()
        self.setup_variables()
        self.setup_frame_widgets()
        self.setup_buttons()  # 675 -> Button Callbacks
        self.setup_random_booking_information()
        self.root.tk.call('wm', 'iconphoto', root._w, tkinter.PhotoImage(file='img/icon.png'))


    def screen_size(self, size):
        # Obtain desired screen size
        width = self.root.winfo_screenwidth() * size
        height = self.root.winfo_screenheight() * size
        return ('{}x{}+{}+{}'
                .format(int(width), int(height), 0, 0))

    def center_root(self):
        self.root.update_idletasks()
        window_width = self.root.winfo_width()
        window_height = self.root.winfo_height()
        pos_right = \
            int(self.root.winfo_screenwidth() // 2 - window_width // 2)
        pos_down = \
            int(self.root.winfo_screenheight() // 2 - window_height // 2)
        self.root.geometry('{}x{}+{}+{}'
                           .format(window_width, window_height, pos_right, pos_down))

    def setup_frames(self):
        self.setup_main_frame()
        self.setup_button_frame()
        self.setup_reference_frame()
        self.setup_title_frame()
        self.setup_text_frame()
        self.setup_days_frame()

    # ===========================Fonts=======================================

    def setup_fonts(self):
        self.title_font = font.Font(family='Arial',
                                    size=10,
                                    weight='bold')
        self.lbl_font = font.Font(family='Arial',
                                  size=12,
                                  weight='bold')
        self.ent_font = font.Font(family='Arial',
                                  size=12,
                                  weight='bold')
        self.btn_font = font.Font(family='Arial',
                                  size=16,
                                  weight='bold')
        self.message_font = font.Font(family='Arial',
                                      size=26,
                                      weight='bold')

    # ============================Variables==================================

    def setup_variables(self):
        self.customer_ID = tkinter.StringVar()
        self.firstname = tkinter.StringVar()
        self.surname = tkinter.StringVar()
        self.address = tkinter.StringVar()
        self.date_of_birth = tkinter.StringVar()
        self.post_code = tkinter.StringVar()
        self.mobile_phone = tkinter.StringVar()
        self.email = tkinter.StringVar()
        self.nationality = tkinter.StringVar()
        self.gender = tkinter.StringVar()
        self.check_in_date = tkinter.StringVar()
        self.check_out_date = tkinter.StringVar()
        self.proof_of_ID = tkinter.StringVar()
        self.meal_type = tkinter.StringVar()
        self.room_type = tkinter.StringVar()
        self.room_number = tkinter.StringVar()
        self.room_phone = tkinter.StringVar()
        self.number_days = tkinter.StringVar()
        self.paid_tax = tkinter.StringVar()
        self.sub_total = tkinter.StringVar()
        self.total_cost = tkinter.StringVar()

    # =============================Frames====================================

    def setup_main_frame(self):
        self.frm_main = tkinter.Frame(self.root,
                                      borderwidth=10,
                                      # background='deep sky blue',
                                      relief=tkinter.RIDGE)
        self.frm_main.place(relx=0,
                            rely=0,
                            relwidth=1,
                            relheight=1)

    def setup_button_frame(self):
        self.frm_button = tkinter.Frame(self.frm_main,
                                        borderwidth=10,
                                        # background='purple',
                                        relief=tkinter.RIDGE)
        self.frm_button.place(relx=0,
                              rely=0.90,
                              relwidth=1,
                              relheight=0.10)

    def setup_reference_frame(self):
        self.frm_reference = tkinter.Frame(self.frm_main,
                                           borderwidth=10,
                                           # background='green',
                                           relief=tkinter.RIDGE)
        self.frm_reference.place(relx=0,
                                 rely=0,
                                 relwidth=0.2857,
                                 relheight=0.90)

    def setup_title_frame(self):
        self.frm_title = tkinter.Frame(self.frm_main,
                                       borderwidth=10,
                                       # background='yellow',
                                       relief=tkinter.RIDGE)
        self.frm_title.place(relx=0.2858,
                             rely=0,
                             relwidth=0.7143,
                             relheight=0.10)

    def setup_text_frame(self):
        self.frm_text = tkinter.Frame(self.frm_main,
                                      borderwidth=10,
                                      # background='red',
                                      relief=tkinter.RIDGE)
        self.frm_text.place(relx=0.2858,
                            rely=0.1005,
                            relwidth=0.7143,
                            relheight=0.55)

    def setup_days_frame(self):
        self.frm_days = tkinter.Frame(self.frm_main,
                                      borderwidth=10,
                                      # background='violet',
                                      relief=tkinter.RIDGE)
        self.frm_days.place(relx=0.2858,
                            rely=0.652,
                            relwidth=0.7143,
                            relheight=0.246)

    # =======================Frame Widgets===================================

    def setup_frame_widgets(self):

        # =======================Reference Frame=================================

        self.lbl_customer_ID = tkinter.Label(self.frm_reference,
                                             font=self.lbl_font,
                                             # background='green',
                                             text='Client Ref:')
        self.lbl_customer_ID.grid(padx=1, pady=4, row=0, column=0)
        self.ent_customer_ID = tkinter.Entry(self.frm_reference,
                                             font=self.ent_font,
                                             width=25,
                                             textvariable=self.customer_ID)
        self.ent_customer_ID.grid(padx=1, pady=4, row=0, column=1)

        self.lbl_firstname = tkinter.Label(self.frm_reference,
                                           font=self.lbl_font,
                                           # background='green',
                                           text='Numele:')
        self.lbl_firstname.grid(padx=1, pady=4, row=1, column=0)
        self.ent_firstname = tkinter.Entry(self.frm_reference,
                                           font=self.ent_font,
                                           textvariable=self.firstname,
                                           width=25)
        self.ent_firstname.grid(padx=1, pady=4, row=1, column=1)

        self.lbl_surname = tkinter.Label(self.frm_reference,
                                         font=self.lbl_font,
                                         # background='green',
                                         text='Familia:')
        self.lbl_surname.grid(padx=1, pady=4, row=2, column=0)
        self.ent_surname = tkinter.Entry(self.frm_reference,
                                         font=self.ent_font,
                                         textvariable=self.surname,
                                         width=25)
        self.ent_surname.grid(padx=1, pady=4, row=2, column=1)

        self.lbl_address = tkinter.Label(self.frm_reference,
                                         font=self.lbl_font,
                                         # background='green',
                                         text='Adresa:')
        self.lbl_address.grid(padx=1, pady=4, row=3, column=0)

        self.ent_address = tkinter.Entry(self.frm_reference,
                                         font=self.ent_font,
                                         textvariable=self.address,
                                         width=25)
        self.ent_address.grid(padx=1, pady=4, row=3, column=1)

        self.lbl_DOB = tkinter.Label(self.frm_reference,
                                     font=self.lbl_font,
                                     # background='green',
                                     text='Ziua de naștere:')
        self.lbl_DOB.grid(padx=1, pady=4, row=4, column=0)
        self.ent_DOB = tkinter.Entry(self.frm_reference,
                                     font=self.ent_font,
                                     textvariable=self.date_of_birth,
                                     width=25)
        self.ent_DOB.grid(padx=1, pady=4, row=4, column=1)

        self.lbl_post_code = tkinter.Label(self.frm_reference,
                                           font=self.lbl_font,
                                           # background='green',
                                           text='Cod poștal:')
        self.lbl_post_code.grid(padx=1, pady=4, row=5, column=0)
        self.ent_post_code = tkinter.Entry(self.frm_reference,
                                           font=self.ent_font,
                                           textvariable=self.post_code,
                                           width=25)
        self.ent_post_code.grid(padx=1, pady=4, row=5, column=1)

        self.lbl_mobile = tkinter.Label(self.frm_reference,
                                        font=self.lbl_font,
                                        # background='green',
                                        text='Telefon:')
        self.lbl_mobile.grid(padx=1, pady=4, row=6, column=0)
        self.ent_mobile = tkinter.Entry(self.frm_reference,
                                        font=self.ent_font,
                                        textvariable=self.mobile_phone,
                                        width=25)
        self.ent_mobile.grid(padx=1, pady=4, row=6, column=1)

        self.lbl_email = tkinter.Label(self.frm_reference,
                                       font=self.lbl_font,
                                       # background='green',
                                       text='Email:')
        self.lbl_email.grid(padx=1, pady=4, row=7, column=0)
        self.ent_email = tkinter.Entry(self.frm_reference,
                                       font=self.ent_font,
                                       textvariable=self.email,
                                       width=25)
        self.ent_email.grid(padx=1, pady=4, row=7, column=1)

        self.lbl_nationality = tkinter.Label(self.frm_reference,
                                             font=self.lbl_font,
                                             # background='green',
                                             text='Naționalitate:')
        self.lbl_nationality.grid(padx=1, pady=4, row=8, column=0)
        self.ent_nationality = tkinter.Entry(self.frm_reference,
                                             font=self.ent_font,
                                             textvariable=self.nationality,
                                             width=25)
        self.ent_nationality.grid(padx=1, pady=4, row=8, column=1)

        self.lbl_gender = tkinter.Label(self.frm_reference,
                                        font=self.lbl_font,
                                        # background='green',
                                        text='Sex:')
        self.lbl_gender.grid(padx=1, pady=4, row=9, column=0)

        self.ent_gender = ttk.Combobox(self.frm_reference,
                                       font=self.ent_font,
                                       textvariable=self.gender,
                                       width=24)
        self.ent_gender['values'] = ('',
                                     'M',
                                     'F',
                                     'Altul',
                                     'Fără răspuns')
        self.ent_gender.current(0)
        self.ent_gender.grid(padx=1, pady=4, row=9, column=1)

        self.lbl_check_in_date = tkinter.Label(self.frm_reference,
                                               font=self.lbl_font,
                                               # background='green',
                                               text='Data Check In:')
        self.lbl_check_in_date.grid(padx=1, pady=4, row=10, column=0)

        # =============================DateEntry=================================
        # pip3 install tkcalendar -> https://github.com/j4321/tkcalendar
        # date_pattern - note
        # =======================================================================

        self.ent_check_in_date = DateEntry(self.frm_reference,
                                           font=self.ent_font,
                                           year=2020,  # Default to today
                                           month=4,  # If not present
                                           date_pattern='dd-mm-y',
                                           textvariable=self.check_in_date,
                                           width=24)
        self.ent_check_in_date.grid(padx=6, pady=4, row=10, column=1)

        self.lbl_check_out_date = tkinter.Label(self.frm_reference,
                                                font=self.lbl_font,
                                                # background='green',
                                                text='Data Check Out:')
        self.lbl_check_out_date.grid(padx=6, pady=4, row=11, column=0)
        self.ent_check_out_date = DateEntry(self.frm_reference,
                                            font=self.ent_font,
                                            year=2020,
                                            month=4,
                                            date_pattern='dd-mm-y',
                                            textvariable=self.check_out_date,
                                            width=24)
        self.ent_check_out_date.grid(padx=6, pady=4, row=11, column=1)

        self.lbl_proof_of_ID = tkinter.Label(self.frm_reference,
                                             font=self.lbl_font,
                                             # background='green',
                                             text='Document:')
        self.lbl_proof_of_ID.grid(padx=6, pady=4, row=12, column=0)

        self.ent_proof_of_ID = ttk.Combobox(self.frm_reference,
                                            font=self.ent_font,
                                            textvariable=self.proof_of_ID,
                                            width=24)
        self.ent_proof_of_ID['values'] = ('',
                                          'Pașaport',
                                          'Buletin',
                                          'Certif. naștere',
                                          'Permis de conducere')
        self.ent_proof_of_ID.current(0)
        self.ent_proof_of_ID.grid(padx=6, pady=4, row=12, column=1)

        self.lbl_meal_type = tkinter.Label(self.frm_reference,
                                           font=self.lbl_font,
                                           # background='green',
                                           text='Masa:')
        self.lbl_meal_type.grid(padx=6, pady=4, row=13, column=0)
        self.ent_meal_type = ttk.Combobox(self.frm_reference,
                                          font=self.ent_font,
                                          textvariable=self.meal_type,
                                          width=24)
        self.ent_meal_type['values'] = ('',
                                        'Dejun mic',
                                        'Dejun mare',
                                        'Dejun + Șampanie',
                                        'Dejun Instant',
                                        'Prânz',
                                        'Prânz la pachet',
                                        'Cina',
                                        'Cina Duminică',
                                        'Cină mare')
        self.ent_meal_type.current(0)
        self.ent_meal_type.grid(padx=6, pady=4, row=13, column=1)

        self.lbl_room_type = tkinter.Label(self.frm_reference,
                                           font=self.lbl_font,
                                           # background='green',
                                           text='Tip cameră:')
        self.lbl_room_type.grid(padx=6, pady=4, row=14, column=0)
        self.ent_room_type = ttk.Combobox(self.frm_reference,
                                          font=self.ent_font,
                                          textvariable=self.room_type,
                                          width=24)
        self.ent_room_type['values'] = ('',
                                        'Single',
                                        'Double',
                                        'Twin',
                                        'Studio',
                                        'Triple',
                                        'Quad',
                                        'Queen Room',
                                        'King Room',
                                        'Mini Suite Room',
                                        'Suite Room')
        self.ent_room_type.current(0)
        self.ent_room_type.grid(padx=6, pady=4, row=14, column=1)

        self.lbl_room_number = tkinter.Label(self.frm_reference,
                                             font=self.lbl_font,
                                             # background='green',
                                             text='No. cameră:')
        self.lbl_room_number.grid(padx=6, pady=4, row=15, column=0)
        self.ent_room_number = ttk.Combobox(self.frm_reference,
                                            font=self.ent_font,
                                            textvariable=self.room_number,
                                            width=24)
        self.ent_room_number['values'] = ('',
                                          '001',
                                          '002',
                                          '003',
                                          '004',
                                          '005',
                                          '006',
                                          '007',
                                          '008',
                                          '009',
                                          '010')
        self.ent_room_number.current(0)
        self.ent_room_number.grid(padx=6, pady=4, row=15, column=1)

        self.lbl_room_phone = tkinter.Label(self.frm_reference,
                                            font=self.lbl_font,
                                            # background='green',
                                            text='Tel. cameră:')
        self.lbl_room_phone.grid(padx=6, pady=4, row=16, column=0)
        self.ent_room_phone = ttk.Combobox(self.frm_reference,
                                           font=self.ent_font,
                                           textvariable=self.room_phone,
                                           width=24)
        self.ent_room_phone['values'] = ('',
                                         '101',
                                         '102',
                                         '103',
                                         '104',
                                         '105',
                                         '106',
                                         '107',
                                         '108',
                                         '109',
                                         '110')
        self.ent_room_phone.current(0)
        self.ent_room_phone.grid(padx=6, pady=4, row=16, column=1)

        # =========================Title Frame===================================

        self.lbl_message = tkinter.Label(self.frm_title,
                                         font=self.message_font,
                                         # background='yellow',
                                         text='\tClienții Hotel:')
        self.lbl_message.place(relx=0.25,
                               rely=0.1)

        # self.lbl_customer_reference = tkinter.Label( self.frm_title,
        #                         font = self.title_font,
        #                         background = 'yellow',
        #                         text = 'Customer Ref' )
        # self.lbl_customer_reference.place( relx = 0,
        #                                    rely = 0.30 )

        # self.lbl_first_name = tkinter.Label( self.frm_title,
        #                         font = self.title_font,
        #                         background = 'yellow',
        #                         text = 'Firstname' )
        # self.lbl_first_name.place( relx = 0.130,
        #                            rely = 0.30 )

        # self.lbl_sur_name = tkinter.Label( self.frm_title,
        #                         font = self.title_font,
        #                         background = 'yellow',
        #                         text = 'Surname' )
        # self.lbl_sur_name.place( relx = 0.23,
        #                          rely = 0.30 )

        # self.lbl_street_address = tkinter.Label( self.frm_title,
        #                         font = self.title_font,
        #                         background = 'yellow',
        #                         text = 'Street Address' )
        # self.lbl_street_address.place( relx = 0.330,
        #                                rely = 0.30 )

        # self.lbl_sex_type = tkinter.Label( self.frm_title,
        #                         font = self.title_font,
        #                         background = 'yellow',
        #                         text = 'Gender' )
        # self.lbl_sex_type.place( relx = 0.470,
        #                          rely = 0.30 )

        # self.lbl_cell_phone = tkinter.Label( self.frm_title,
        #                         font = self.title_font,
        #                         background = 'yellow',
        #                         text = 'Mobile' )
        # self.lbl_cell_phone.place( relx = 0.550,
        #                            rely = 0.30 )

        # self.lbl_country = tkinter.Label( self.frm_title,
        #                         font = self.title_font,
        #                         background = 'yellow',
        #                         text = 'Nationality' )
        # self.lbl_country.place( relx = 0.630,
        #                         rely = 0.30 )

        # self.lbl_ID = tkinter.Label( self.frm_title,
        #                         font = self.title_font,
        #                         background = 'yellow',
        #                         text = 'ID' )
        # self.lbl_ID.place( relx = 0.745,
        #                    rely = 0.30 )

        # self.lbl_date_in = tkinter.Label( self.frm_title,
        #                         font = self.title_font,
        #                         background = 'yellow',
        #                         text = 'In' )
        # self.lbl_date_in.place( relx = 0.795,
        #                         rely = 0.30 )

        # self.lbl_date_out = tkinter.Label( self.frm_title,
        #                         font = self.title_font,
        #                         background = 'yellow',
        #                         text = 'Out' )
        # self.lbl_date_out.place( relx = 0.835,
        #                          rely = 0.30 )

        # self.lbl_E_mail = tkinter.Label( self.frm_title,
        #                         font = self.title_font,
        #                         background = 'yellow',
        #                         text = 'Email' )
        # self.lbl_E_mail.place( relx = 0.890,
        #                        rely = 0.30 )

        # =======================Text Frame Scrolled Text========================

        self.tbox = tkst.ScrolledText(self.frm_text,
                                      # background='red',
                                      foreground='blue',
                                      wrap=tkinter.WORD,
                                      relief=tkinter.RIDGE)
        self.tbox.place(relx=0,
                        rely=0,
                        relwidth=1,
                        relheight=1)

        # Decided to place a 'Treeview' widget into ScrolledText================

        style = ttk.Style()
        style.configure('Treeview.Heading', font=self.title_font)
        style.configure('Treeview', # background='red',
                        foreground='blue')

        self.tree_view = ttk.Treeview(self.tbox,
                                      column=('column1',
                                              'column2',
                                              'column3',
                                              'column4',
                                              'column5'), show='headings')
        self.tree_view.column('column1', width=100)
        self.tree_view.column('column2', width=120)
        self.tree_view.column('column3', width=120)
        self.tree_view.column('column4', width=120)
        self.tree_view.heading('#1', text='Referința :')
        self.tree_view.heading('#2', text='Numele :')
        self.tree_view.heading('#3', text='Familia :')
        self.tree_view.heading('#4', text='Telefon :')
        self.tree_view.heading('#5', text='Email :')
        self.tree_view.bind('<<TreeviewSelect>>',
                            self.On_Tree_Select)
        self.tree_view.place(relx=0,
                             rely=0,
                             relwidth=1,
                             relheight=1)

        # =======================Number Of Days Frame============================

        self.lbl_number_days = tkinter.Label(self.frm_days,
                                             font=self.lbl_font,
                                             # background='violet',
                                             text='Nr. de zile:')
        self.lbl_number_days.grid(padx=6, pady=4, row=0, column=0)
        self.ent_number_days = tkinter.Entry(self.frm_days,
                                             font=self.ent_font,
                                             textvariable=self.number_days,
                                             width=80)
        self.ent_number_days.grid(padx=6, pady=4, row=0, column=1)

        self.lbl_paid_tax = tkinter.Label(self.frm_days,
                                          font=self.lbl_font,
                                          # background='violet',
                                          text= 'Taxe plătite:')
        self.lbl_paid_tax.grid(padx=6, pady=4, row=1, column=0)
        self.ent_paid_tax = tkinter.Entry(self.frm_days,
                                          font=self.ent_font,
                                          textvariable=self.paid_tax,
                                          width=80)
        self.ent_paid_tax.grid(padx=6, pady=4, row=1, column=1)

        self.lbl_sub_total = tkinter.Label(self.frm_days,
                                           font=self.lbl_font,
                                           # background='violet',
                                           text='Subtotal:')
        self.lbl_sub_total.grid(padx=6, pady=4, row=2, column=0)
        self.ent_sub_total = tkinter.Entry(self.frm_days,
                                           font=self.ent_font,
                                           textvariable=self.sub_total,
                                           width=80)
        self.ent_sub_total.grid(padx=6, pady=4, row=2, column=1)

        self.lbl_total_cost = tkinter.Label(self.frm_days,
                                            font=self.lbl_font,
                                            # background='violet',
                                            text='Cost Total:')
        self.lbl_total_cost.grid(padx=6, pady=4, row=3, column=0)
        self.ent_total_cost = tkinter.Entry(self.frm_days,
                                            font=self.ent_font,
                                            textvariable=self.total_cost,
                                            width=80)
        self.ent_total_cost.grid(padx=6, pady=4, row=3, column=1)

    # =======================Button Callbacks================================

    def Ask_Quit(self):
        exit_program = tkinter.messagebox.askyesno(
            title='Hotel Database Management System',
            message='Confirmați ieșirea din program?')
        if exit_program > 0:
            Hotel_DB.dumpSQL()
            self.root.destroy()
        else:
            return None

    def Reset(self):
        self.ent_customer_ID.delete(0, tkinter.END)
        self.ent_firstname.delete(0, tkinter.END)
        self.ent_surname.delete(0, tkinter.END)
        self.ent_address.delete(0, tkinter.END)
        self.ent_DOB.delete(0, tkinter.END)
        self.ent_post_code.delete(0, tkinter.END)
        self.ent_mobile.delete(0, tkinter.END)
        self.ent_email.delete(0, tkinter.END)
        self.ent_nationality.delete(0, tkinter.END)
        self.ent_gender.current(0)
        self.check_in_date.set('')
        self.check_out_date.set('')
        self.ent_proof_of_ID.current(0)
        self.ent_meal_type.current(0)
        self.ent_room_type.current(0)
        self.ent_room_number.current(0)
        self.ent_room_phone.current(0)
        self.number_days.set('')
        self.paid_tax.set('')
        self.sub_total.set('')
        self.total_cost.set('')
        # for idx in self.tree_view.get_children():
        #     self.tree_view.delete( idx )

    def Random_Data(self):
        self.setup_random_booking_information()

    def Add_Booking(self):
        booking = [(self.ent_customer_ID.get(),
                    self.ent_firstname.get(),
                    self.ent_surname.get(),
                    self.ent_address.get(),
                    self.ent_DOB.get(),
                    self.ent_post_code.get(),
                    self.ent_mobile.get(),
                    self.ent_email.get(),
                    self.ent_nationality.get(),
                    self.ent_gender.get(),
                    self.check_in_date.get(),
                    self.check_out_date.get(),
                    self.ent_proof_of_ID.get(),
                    self.ent_meal_type.get(),
                    self.ent_room_type.get(),
                    self.ent_room_number.get(),
                    self.ent_room_phone.get())]

        last_row = Hotel_DB.insert_hotel_booking(booking)
        print('Last Row ID is :', last_row)
        self.total_days()

    def Delete_Booking(self, message=True):
        customerID = self.On_Tree_Select(event=None)
        print('Delete CID', customerID)
        if message == True:
            delete_booking = tkinter.messagebox.askyesno(
                title='Hotel Database Management System',
                message='Confirmați ștergerea intrării?')
            if delete_booking > 0:
                self.Search_Booking()
                RV = Hotel_DB.delete_hotel_booking_record(customerID)
                self.Display_Booking()
                print(RV)
            else:
                return

    def Update_Booking(self):
        ID = self.customer_ID.get()
        booking = [(self.ent_customer_ID.get(),
                    self.ent_firstname.get(),
                    self.ent_surname.get(),
                    self.ent_address.get(),
                    self.ent_DOB.get(),
                    self.ent_post_code.get(),
                    self.ent_mobile.get(),
                    self.ent_email.get(),
                    self.ent_nationality.get(),
                    self.ent_gender.get(),
                    self.check_in_date.get(),
                    self.check_out_date.get(),
                    self.ent_proof_of_ID.get(),
                    self.ent_meal_type.get(),
                    self.ent_room_type.get(),
                    self.ent_room_number.get(),
                    self.ent_room_phone.get(), ID)]

        Hotel_DB.update_hotel_booking_record(booking)

    def Search_Booking(self):
        customerID = self.On_Tree_Select(event=None)
        data = Hotel_DB.search_hotel_booking_record(customerID)
        # print( data.keys())
        # print( data[3] )
        # print( data[r'Address'])
        self.Reset()

        self.customer_ID.set(data[r'Customer_ID'])
        self.firstname.set(data[r'Firstname'])
        self.surname.set(data[r'Surname'])
        self.address.set(data[r'Address'])
        self.date_of_birth.set(data[r'Birth_Date'])
        self.post_code.set(data[r'Post_Code'])
        self.mobile_phone.set(data[r'Mobile'])
        self.email.set(data[r'Email'])
        self.nationality.set(data[r'Nationality'])
        self.gender.set(data[r'Gender'])
        self.check_in_date.set(data[r'DateIn'])
        self.check_out_date.set(data[r'DateOut'])
        self.proof_of_ID.set(data[r'ID_Type'])
        self.meal_type.set(data[r'Meal_Type'])
        self.room_type.set(data[r'Room_Type'])
        self.room_number.set(data[r'Room_Number'])
        self.room_phone.set(data[r'Room_Phone'])

    def Display_Booking(self):
        for idx in self.tree_view.get_children():
            self.tree_view.delete(idx)
        for row in Hotel_DB.display_hotel_booking_record():
            self.tree_view.insert('', tkinter.END,
                                  values=(row[r'Customer_ID'],
                                          row[r'Firstname'],
                                          row[r'Surname'],
                                          row[r'Mobile'],
                                          row[r'Email']))

    def On_Tree_Select(self, event):
        print("selected items:")
        # curItem = self.tree_view.focus() # These 2 lines work!
        # print( self.tree_view.item( curItem ))

        item = self.tree_view.selection()[0]
        # print( 'Item Clicked :', item )
        # print( 'Customer Reference :',
        #        self.tree_view.item( item )['values'][0] )
        # print( 'Customer First Name :',
        #        self.tree_view.item( item )['values'][1] )
        # print( 'Customer Last Name :',
        #        self.tree_view.item( item )['values'][2] )
        # print( 'Customer Mobile Phone :',
        #        self.tree_view.item( item )['values'][3] )
        # print( 'Customer Email :',
        #        self.tree_view.item( item )['values'][4] )

        ''' Return Customer Reference Number '''

        return self.tree_view.item(item)['values'][0]

    # ===============================Buttons=================================

    def setup_buttons(self):  # self.frm_button purple
        self.btn_total_data = tkinter.Button(self.frm_button,
                                             font=self.btn_font,
                                             borderwidth=4,
                                             activeforeground='SlateBlue1',
                                             activebackground='thistle',
                                             command=self.Add_Booking,
                                             text='Adaugă')
        self.btn_total_data.grid(padx=20, pady=7, row=0, column=0)

        self.btn_display = tkinter.Button(self.frm_button,
                                          font=self.btn_font,
                                          borderwidth=4,
                                          # activeforeground='blue',
                                          # activebackground='sea green',
                                          command=self.Display_Booking,
                                          text='Arată')
        self.btn_display.grid(padx=20, pady=7, row=0, column=1)

        self.btn_update = tkinter.Button(self.frm_button,
                                         font=self.btn_font,
                                         borderwidth=4,
                                         # activeforeground='Orange',
                                         # activebackground='purple',
                                         command=self.Update_Booking,
                                         text='Actualizează')
        self.btn_update.grid(padx=20, pady=7, row=0, column=2)

        self.btn_delete = tkinter.Button(self.frm_button,
                                         font=self.btn_font,
                                         borderwidth=4,
                                         # activeforeground='gray25',
                                         # activebackground='black',
                                         command=self.Delete_Booking,
                                         text='Șterge')
        self.btn_delete.grid(padx=20, pady=7, row=0, column=3)

        self.btn_search = tkinter.Button(self.frm_button,
                                         font=self.btn_font,
                                         borderwidth=4,
                                         # activeforeground='blue',
                                         # activebackground='ghost white',
                                         command=self.Search_Booking,
                                         text='Caută')
        self.btn_search.grid(padx=20, pady=7, row=0, column=4)

        self.btn_reset = tkinter.Button(self.frm_button,
                                        font=self.btn_font,
                                        borderwidth=4,
                                        # activeforeground='red',
                                        # activebackground='ghost white',
                                        command=self.Reset,
                                        text='Reset')
        self.btn_reset.grid(padx=20, pady=7, row=0, column=5)

        self.btn_random = tkinter.Button(self.frm_button,
                                         font=self.btn_font,
                                         borderwidth=4,
                                         # activeforeground='yellow',
                                         # activebackground='gray34',
                                         command=self.Random_Data,
                                         text='Random')
        self.btn_random.grid(padx=20, pady=7, row=0, column=6)

        self.btn_total_days = tkinter.Button(self.frm_button,
                                             font=self.btn_font,
                                             borderwidth=4,
                                             # activeforeground='yellow',
                                             # activebackground='gray34',
                                             command=self.total_days,
                                             text='Total Zile')
        self.btn_total_days.grid(padx=20, pady=7, row=0, column=7)

        self.btn_exit = tkinter.Button(self.frm_button,
                                       font=self.btn_font,
                                       borderwidth=4,
                                       # activeforeground='green',
                                       # activebackground='ghost white',
                                       command=self.Ask_Quit,
                                       text='Exit')
        self.btn_exit.grid(padx=20, pady=7, row=0, column=8)


    # =======================Random Booking Information======================

    # def generate_random_string( self, string_length = 10 ):
    #     ''' Generate a random string of fixed length '''
    #     letters = string.ascii_lowercase
    #     return ''.join( secrets.choice( letters )
    #                     for i in range( string_length ))

    def generate_random_birth_date(self,
                                   start_date='-90y',
                                   end_date='-15y'):
        fake = Faker()
        FD = fake.date_of_birth()  # Max age = 115
        return (FD.strftime('%d-%m-%Y'))

    def generate_random_future_date(self):
        fake = Faker()
        FD = fake.date_between(start_date='today',
                               end_date='+25d')
        return FD.strftime('%d-%m-%Y')

    def generate_date_today(self):
        TD = date.today()
        return TD.strftime('%d-%m-%Y')

    def generate_random_address(self):
        fake = Faker()
        return fake.address()

    def generate_random_email(self):
        fake = Faker()
        return fake.email()

    def generate_random_first_name(self):
        return names.get_first_name()

    def generate_random_surname(self):
        return names.get_last_name()

    def generate_random_mobile_number(self):
        ''' Yes, well, cell phone number '''
        prefix = ['021', '022', '025', '027', '029']
        pre_cell = str(secrets.choice(prefix))
        num_cell = str(secrets.randbits(32))
        return pre_cell + num_cell

    def generate_random_post_code(self):
        ''' 7 digit number '''
        lowest_number = int(1000000)
        highest_number = int(9999998)
        SG = secrets.SystemRandom()
        post_code = SG.randint(lowest_number, highest_number)
        return (str(post_code))

    def generate_random_country(self):
        ''' Random Country '''
        rand_num = random.randint(0, len(pycountry.countries))
        country_name = list(pycountry.countries)[rand_num].name
        return (country_name)

    def generate_random_gender(self):
        ''' Random Gender '''
        RG = random.randint(1, len(self.ent_gender['values'][:-1]))
        return (self.ent_gender['values'][RG])

    def generate_random_ID_type(self):
        ''' Random type of ID '''
        RID = random.randint(1,
                             len(self.ent_proof_of_ID['values'][:-1]))
        return (self.ent_proof_of_ID['values'][RID])

    def generate_random_meal(self):
        ''' Random Meal '''
        RM = random.randint(1,
                            len(self.ent_meal_type['values'][:-1]))
        return (self.ent_meal_type['values'][RM])

    def generate_random_room_type(self):
        ''' Random Room Type '''
        RRT = random.randint(1,
                             len(self.ent_room_type['values'][:-1]))
        return (self.ent_room_type['values'][RRT])

    def generate_random_room_number(self):
        ''' Random Room Number '''
        RRN = random.randint(1,
                             len(self.ent_room_number['values'][:-1]))
        return (self.ent_room_number['values'][RRN])

    def generate_random_room_phone(self):
        ''' Random Room Phone Number '''
        RRPN = random.randint(1,
                              len(self.ent_room_phone['values'][:-1]))
        return (self.ent_room_phone['values'][RRPN])

    def setup_random_booking_information(self):
        self.customer_ID.set(str(secrets.token_hex(5)))
        self.firstname.set(self.generate_random_first_name())
        self.surname.set(self.generate_random_surname())
        self.address.set(self.generate_random_address())
        self.date_of_birth.set(self.generate_random_birth_date())
        self.post_code.set(self.generate_random_post_code())
        self.mobile_phone.set(self.generate_random_mobile_number())
        self.email.set(self.generate_random_email())
        self.nationality.set(self.generate_random_country())
        self.gender.set(self.generate_random_gender())
        self.check_in_date.set(self.generate_date_today())
        self.check_out_date.set(self.generate_random_future_date())
        self.proof_of_ID.set(self.generate_random_ID_type())
        self.meal_type.set(self.generate_random_meal())
        self.room_type.set(self.generate_random_room_type())
        self.room_number.set(self.generate_random_room_number())
        self.room_phone.set(self.generate_random_room_phone())

    # ===========================Total Days==================================
    def total_days(self):
        date_format = '%d-%m-%Y'
        in_date = datetime.strptime(
            self.check_in_date.get(), date_format)
        out_date = datetime.strptime(
            self.check_out_date.get(), date_format)
        self.number_days.set(abs((out_date - in_date).days))

        self.meal_cost = {'Dejun mic': 17.00,
                          'Dejun mare': 22.00,
                          'Dejun + Șampanie': 32.00,
                          'Dejun Instant': 15.00,
                          'Prânz': 25.00,
                          'Prânz la pachet': 16.00,
                          'Cina': 35.00,
                          'Cina Duminică': 38.00,
                          'Cină mare': 45.00}

        self.room_cost = {'Single': 34.00,
                          'Double': 43.00,
                          'Twin': 63.00,
                          'Studio': 83.00,
                          'Triple': 103.00,
                          'Quad': 123.00,
                          'Queen Room': 143.00,
                          'King Room': 163.00,
                          'Mini Suite Room': 183.00,
                          'Suite Room': 250.00}

        # MT = self.generate_random_meal()
        # RT = self.generate_random_room_type()
        MT = self.meal_type.get()
        RT = self.room_type.get()
        print('Zile totale este :', self.number_days.get())
        print('Masa aleasă este :', MT)
        print('Cost Masa   este :', self.meal_cost[MT])
        print('Tip Camera  este :', RT)
        print('Cost Camera este :', self.room_cost[RT])

        # ===========================Math========================================

        meal_cost = float(self.meal_cost[MT])
        room_cost = float(self.room_cost[RT])
        number_of_days = float(self.number_days.get())
        meal_room = float(meal_cost + room_cost)
        days_meal_room = float(number_of_days * meal_room)

        the_tax = str('%.2f' % ((days_meal_room) * 0.09)) + 'MDL'
        sub_total = str('%.2f' % ((days_meal_room))) + 'MDL'
        the_total = str('%.2f' % (days_meal_room +
                                        ((days_meal_room) * 0.09))) + 'MDL'
        self.paid_tax.set(the_tax)
        self.sub_total.set(sub_total)
        self.total_cost.set(the_total)

        print('Taxe plătite  :', the_tax)
        print('Subtotal      :', sub_total)
        print('Cost total    :', the_total)


if __name__ == '__main__':
    root = tkinter.Tk()
    application = Hotel(root)
    root.mainloop()
