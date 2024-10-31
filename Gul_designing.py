###~ by Sahar_Khorshid ~  ###
from tkinter import *
from tkinter import font
# from tkinter.font import Fontfont,   
from tkinter import ttk
import tkinter as tk
import sqlite3
from tkinter import messagebox
from manage_tables import management 
from mange import manage_travel
m_t = manage_travel()
manag_tbl = management()
import time



def choose ():
    root1 = Tk()
    root1.title('~Choose~')
    root1.geometry("500x200")
    root1.resizable(False,False)
    signin_mn = ttk.Label(root1,text = 'مدیر', font='bold')
    signin_mn.place(relx = 0.25,rely = 0.05)
    signin1_Op = ttk.Label(root1,text = 'اپراتور' , font='bold')
    signin1_Op.place(relx = 0.71,rely = 0.05)

    l_code_manag = Label(root1, text='نام کاربری'  , font=('arial', 11 ))
    l_code_manag.place(relx = 0.02,rely = 0.3)
    entr_code_manag = Entry(root1)
    entr_code_manag.place(relx = 0.15,rely = 0.3)

    l_pass_manage = Label(root1, text='رمز'  , font=('arial', 11 ))
    l_pass_manage.place(relx = 0.06,rely = 0.5)
    entr_pass_manage = Entry(root1)
    entr_pass_manage.place(relx = 0.15,rely = 0.5)


    l_code = Label(root1, text='نام کاربری'  , font=('arial', 11))
    l_code.place(relx = 0.85,rely = 0.3)
    entr_code_op = Entry(root1)
    entr_code_op.place(relx = 0.59,rely = 0.3 )

    l_usrname = Label(root1, text='رمز', font=('arial', 11))
    l_usrname.place(relx = 0.86,rely = 0.5)
    entr_pass_op = Entry(root1)
    entr_pass_op.place(relx = 0.59,rely = 0.5)  

   


    def login_Manager():

        m_Login = manag_tbl.manager_check(entr_code_manag.get(),entr_pass_manage.get())
        if m_Login:
            w = manger()
                
        else:
            l = Label(root1,text='ورود ناموفق')
            l.pack()


    def login_OPr():
        try:
            e = manag_tbl.Operator_check(entr_code_op.get(), entr_pass_op.get())
            if e :
                w = Operator()
                
            else:
                l = Label(root1,text='ورود ناموفق')
                l.pack()
                
        except:
                messagebox.showerror("ERROR","bad username or password")
     

    btn8 = ttk.Button(root1, text=' ورود ', command=login_Manager)
    btn8.place(relx = 0.2,rely = 0.7 )
    btn9 = ttk.Button(root1, text=' ورود ', command=login_OPr)
    btn9.place(relx = 0.65,rely = 0.7 )
    


    

    def Operator():
        root_travel = Tk()
        root_travel.title('سفر')
        root_travel.geometry("400x400")
        root_travel.resizable(False,False)

        l_mabda = Label(root_travel,text='مبدا')
        l_mabda.pack(ipadx=40 , ipady=10, pady=8)
        entr_mabda = Entry(root_travel,width = 35)
        entr_mabda.pack(ipadx=40 , ipady=10, pady=8)

        l_mags = Label(root_travel,text='مقصد')
        l_mags.pack(ipadx=40 , ipady=10, pady=8)
        entr_mags = Entry(root_travel,width = 35)
        entr_mags.pack(ipadx=40 , ipady=10, pady=8)
        

        def change_password():
            root_change_pass_op = Tk()
            root_change_pass_op.title('~Choose~')
            root_change_pass_op.geometry("300x300")
            root_change_pass_op.resizable(False,False)
            l_usr = Label(root_change_pass_op,text= ' تغییر رمز کاربر'  ,font=('arial', 16 ,'bold') , bg='#8FBC8B')
            l_usr.place(relx = 0.3,rely = 0.05)

            l_last_pass = Label(root_change_pass_op,text='رمز  قبلی')
            l_last_pass.place(relx = 0.11,rely = 0.18)
            entr_old_pass = Entry(root_change_pass_op,width = 30)
            entr_old_pass.place(relx = 0.3,rely = 0.18)

            l_pass = Label(root_change_pass_op,text='رمز')
            l_pass.place(relx = 0.15,rely = 0.26)
            entr_pass = Entry(root_change_pass_op,width = 30)
            entr_pass.place(relx = 0.3,rely = 0.26)

            l_pass = Label(root_change_pass_op,text=' تکرار رمز')
            l_pass.place(relx = 0.1,rely = 0.34)
            entr_pass2 = Entry(root_change_pass_op,width = 30)
            entr_pass2.place(relx = 0.3,rely = 0.34)

            def changing():
                old_check = manag_tbl.Operator_check(entr_code_op.get(), entr_old_pass.get())
                if old_check:
                    if entr_pass.get() == entr_pass2.get():
                        w = manag_tbl.change_pass_Operator(entr_code_op.get(),entr_pass.get())
                        if w  :
                            l = Label(root_change_pass_op,text='   تغییر رمز با موفقیت انجام شد     ')
                            l.place(relx = 0.3,rely = 0.75)
                        else :
                            l2 = Label(root_change_pass_op,text='نام کاربری یا رمز نامعتبر است!')
                            l2.place(relx = 0.3,rely = 0.75)
                    else:
                        l2 = Label(root_change_pass_op,text='لطفا تکرار رمز را درست وارد نماید !')
                        l2.place(relx = 0.3,rely = 0.75)
                else:
                    l2 = Label(root_change_pass_op,text='لطفا رمز قبلی را درست وارد نماید !')
                    l2.place(relx = 0.3,rely = 0.75)

            btn4 = ttk.Button(root_change_pass_op,text='ذخیره تغییرات', command=changing ,width = 20)
            btn4.place(relx = 0.34,rely = 0.5)


        def change_con():
            root_cond = Tk()
            root_cond.geometry('250x115')
            root_cond.resizable(False,False)
            root_cond.title("تعیین وضعیت")
            l_search_c = Label(root_cond, text='درج کد').pack()
            entr_cod = Entry(root_cond, width=30)
            entr_cod.pack()
            
            def active():
                manag_tbl.Change_Condition(entr_cod.get(), 'active')
                l2 = Label(root_cond,text="   فعال شد    ")
                l2.place(relx = 0.30,rely = 0.65)
            def inactive():
                manag_tbl.Change_Condition(entr_cod.get(),'inactive')
                l2 = Label(root_cond,text="  غیر فعال شد   ")
                l2.place(relx = 0.30,rely = 0.65)


            btn_signin6 = ttk.Button(root_cond,text = ' فعال شدن ', command=active)
            btn_signin6.place(relx = 0.15, rely = 0.4)
            btn_signin6 = ttk.Button(root_cond,text = ' غیر فعال شدن', command=inactive)
            btn_signin6.place(relx = 0.51,rely = 0.4)
        

        def show_drv_st():
            root_show = Tk()
            root_show.title('نمایش تاکسی ها')
            root_show.geometry('400x400')
            root_show.resizable(False, True)
            find_st = m_t.finde_Station_taxies(str(entr_mabda.get()))
            find_tx = m_t.show_Condition(find_st)
            l0 = Label(root_show,text='تاکسی های این ایستگاه' , font=(3))
            l0.pack()
            for i in find_tx:

                l = Label(root_show,text=str(i), font=(2))
                l.pack()

            l_write_code_drv = ttk.Label(root_show, text='کد راننده ', font=(1))
            l_write_code_drv.place(relx=0.06 , rely=0.6)
            entr_code_drv_trip = ttk.Entry(root_show)
            entr_code_drv_trip.place(relx=0.25 , rely=0.6)
            
            def showing():
                code_driver = int(str(entr_code_drv_trip.get()))
                first_num = manag_tbl.find_station(entr_code_drv_trip.get())
                manag_tbl.delete_drv_staite(first_num,code_driver)
                
                secend = m_t.search_end(entr_mags.get())
                manag_tbl.add_drv_stait(secend,code_driver)
                # manag_tbl.change_drv_stat(first_num, secend, entr_code_drv_trip.get())
                l_ = Label(root_show,text='انجام شد')
                l_.place(rely=0.9,relx=0.4)

            btn10 = ttk.Button(root_show , text=' انجام سفر ', command=showing)
            btn10.place(relx=0.6 , rely=0.6)

        btn_signin3 = ttk.Button(root_travel,text = 'سفر',command = show_drv_st)
        btn_signin3.pack(ipadx=40 , ipady=10, pady=8)

        menubar = Menu(root_travel)
        menubar.add_command(label="تغییر وضعیت راننده", command=change_con)
        
        changemenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="  تغیر رمز ", command=change_password)

        root_travel.config(menu=menubar)

    
    




 




        
    def manger():
        root_manager = Tk()
        root_manager.geometry('400x400')
        root_manager.title('مدیرت تاکسیرانی بیسم')


        def adding_drv():
            root_add_dr = Tk()
            root_add_dr.geometry('400x400')
            root_add_dr.title(' ثبت نام راننده جدید ')
            
            l_code = Label(root_add_dr, text='کد')
            l_code.pack()
            entr_code = Entry(root_add_dr)
            entr_code.pack()
            
            l_fname = Label(root_add_dr, text='نام')
            l_fname.pack()
            entr_fname = Entry(root_add_dr)
            entr_fname.pack()
            
            l_lname = Label(root_add_dr, text='نام خانوادگی')
            l_lname.pack()
            entr_lname = Entry(root_add_dr)
            entr_lname.pack()
            
            l_age = Label(root_add_dr, text='سن')
            l_age.pack()
            entr_age = Entry(root_add_dr)
            entr_age.pack()
            
            
            entr_date = Entry(root_add_dr)
            entr_date.pack()
            l_date = Label(root_add_dr, text='تاریخ تولد')
            l_date.pack()

            entr_conditin = Entry(root_add_dr)
            entr_conditin.pack()
            l_condition = Label(root_add_dr, text='وضعیت')
            l_condition.pack()

            def done():

                w = manag_tbl.add_new_d(entr_fname.get(), entr_lname.get(),int(str(entr_age.get())), int(str(entr_code.get())) ,entr_date.get() , entr_conditin.get())

                if w is None:
                    l = Label(root_add_dr,text='yes')
                    l.pack()
                else :
                    l2 = Label(root_add_dr,text='nooo')
                    l2.pack()

            btn6 = ttk.Button(root_add_dr, text='اضافه کردن', command=done)
            btn6.pack()


        def adding_Op():
            root_add_op = Tk()
            root_add_op.geometry('300x300')
            
            l_usrname = Label(root_add_op, text='نام کاربری')
            l_usrname.pack()
            entr_usrname = Entry(root_add_op)
            entr_usrname.pack()

            l_pass = Label(root_add_op, text='رمز')
            l_pass.pack()
            entr_pass = Entry(root_add_op)
            entr_pass.pack()
            
            l_Fname = Label(root_add_op, text='نام')
            l_Fname.pack()
            entr_Fname = Entry(root_add_op)
            entr_Fname.pack()

            l_Lname = Label(root_add_op, text='نام خانوداگی')
            l_Lname.pack()
            entr_Lname = Entry(root_add_op)
            entr_Lname.pack()

            def done ():
                w = manag_tbl.add_Operator(entr_usrname.get(), entr_pass.get(), entr_Fname.get(), entr_Lname.get())
                if w is not None:
                    l = Label(root_add_op,text='yes')
                    l.pack()
                else :
                    l2 = Label(root_add_op,text='nooo')
                    l2.pack()
            btn6_1 = ttk.Button(root_add_op, text='انجام شدن', command=done)
            btn6_1.pack()

        
        def delet_drv():
            root_delet_drv = Tk()
            root_delet_drv.geometry('400x400')
            root_delet_drv.title(' حذف راننده از مجوعه ')
            
            l_code = Label(root_delet_drv, text='کد')
            l_code.pack()
            entr_code = Entry(root_delet_drv)
            entr_code.pack()
            
            def showing_select():
                pr = manag_tbl.find_code(entr_code.get())
                l_print = Label(root_delet_drv, text='code: {} \n Fname: {} \n Lname: {} \n brith_date: {} \n'.format(pr[3],pr[0],pr[1],pr[4]))
                l_print.pack()

                btn7_0 = ttk.Button(root_delet_drv, text='حذف',command=done)
                btn7_0.pack()

            def done():
                w = manag_tbl.delete_drv(entr_code.get())
                if w is None:
                    l = Label(root_delet_drv,text='yes')
                    l.pack()
                else :
                    l2 = Label(root_delet_drv,text='nooo')
                    l2.pack()

            btn7 = ttk.Button(root_delet_drv, text='نمایش راننده انتخابی',command=showing_select)
            btn7.pack()


        def delet_op():
            root_delet_op = Tk()
            root_delet_op.geometry('400x400')
            root_delet_op.title(' حذف اپراتور از مجموعه ')
            
            l_code = Label(root_delet_op, text='نام کاربری')
            l_code.pack()
            entr_usrname = Entry(root_delet_op)
            entr_usrname.pack()
            
            def showing_select():
                pr = manag_tbl.search_Operator(entr_usrname.get())
                l_print = Label(root_delet_op, text='User name: {} \n Fname: {} \n Lname: {} \n'.format(pr[0],pr[2],pr[3]))
                l_print.pack()

                btn7_0 = ttk.Button(root_delet_op, text='حذف',command=done)
                btn7_0.pack()

            def done():
                w = manag_tbl.delet_Operator(entr_usrname.get())
                if w is None:
                    l = Label(root_delet_op,text='yes')
                    l.pack()
                else :
                    l2 = Label(root_delet_op,text='nooo')
                    l2.pack()

            btn7 = ttk.Button(root_delet_op, text='نمایش اپراتور انتخابی',command=showing_select)
            btn7.pack()

            # def search_

        def search_drv():
            root_search_drv = Tk() 
            root_search_drv.geometry('400x400')
            root_search_drv.title(' جستوجو راننده') 
            root_search_drv.resizable(False,False)


            l_code = Label(root_search_drv, text='کـد'  , font=('arial', 16 ,'bold'))
            l_code.place(relx = 0.2,rely = 0.015)
            entr_code = Entry(root_search_drv)
            entr_code.place(relx = 0.080,rely = 0.08 )


            l_fname = Label(root_search_drv, text='نـام', font=('arial', 15, 'bold'))
            l_fname.place(relx = 0.74,rely = 0.025)
            entr_fname = Entry(root_search_drv)
            entr_fname.place(relx = 0.6,rely = 0.1)
            
            l_lname = Label(root_search_drv, text='نام خانوادگی'  , font=('arial', 15, 'bold'))
            l_lname.place(relx = 0.65,rely = 0.175)
            entr_lname = Entry(root_search_drv)
            entr_lname.place(relx = 0.6,rely = 0.255)


            def search_drv_code():

                pr = manag_tbl.find_code(entr_code.get())
                if pr:
                    l_print = Label(root_search_drv, text='code: {} \n Fname: {} \n Lname: {} \n brith_date: {} \n He is {} now'.format(pr[3],pr[0],pr[1],pr[4], pr[5]) , font=('arial', 15))
                    l_print.place(relx = 0.2,rely = 0.5)
                else:
                    l_hoshdar= Label(root_search_drv, text=' !متاسفانه موردی یافت نشد ', font=('arial', 15, 'bold'), bg='red')
                    l_hoshdar.place(relx = 0.2,rely = 0.5)
            

            def search_drv_name():
                pr = manag_tbl.find_name(entr_fname.get(),entr_lname.get())
                if pr:
                    l_print = Label(root_search_drv, text='code: {} \n Fname: {} \n Lname: {} \n brith_date: {} \n He is {} now'.format(pr[3],pr[0],pr[1],pr[4], pr[5]) , font=('arial', 15))
                    l_print.place(relx = 0.2,rely = 0.5)
                else:
                    l_hoshdar= Label(root_search_drv, text=' !متاسفانه موردی یافت نشد ', font=('arial', 15, 'bold'), bg='red')
                    l_hoshdar.place(relx = 0.2,rely = 0.5)

                

            btn8 = ttk.Button(root_search_drv, text=' جستوجو ', command=search_drv_code)
            btn8.place(relx = 0.128,rely = 0.175 )
            btn9 = ttk.Button(root_search_drv, text=' جستوجو ', command=search_drv_name)
            btn9.place(relx = 0.65,rely = 0.33 )
                    
        def search_OPr():
            root_search_op = Tk()
            root_search_op.geometry('400x400')
            root_search_op.title(' جستوجو اپراتور') 
            root_search_op.resizable(False,False)

            l_code = Label(root_search_op, text='نام کاربری'  , font=('arial', 16 ,'bold'))
            l_code.place(relx = 0.2,rely = 0.015)
            entr_code = Entry(root_search_op)
            entr_code.place(relx = 0.080,rely = 0.08 )

            l_fname = Label(root_search_op, text='نـام', font=('arial', 15, 'bold'))
            l_fname.place(relx = 0.74,rely = 0.025)
            entr_fname = Entry(root_search_op)
            entr_fname.place(relx = 0.6,rely = 0.1)
            
            l_lname = Label(root_search_op, text='نام خانوادگی'  , font=('arial', 15, 'bold'))
            l_lname.place(relx = 0.65,rely = 0.175)
            entr_lname = Entry(root_search_op)
            entr_lname.place(relx = 0.6,rely = 0.255)

            def search_Op_code():

                pr = manag_tbl.search_Operator(entr_code.get())
                if pr:
                    l_print = Label(root_search_op, text='  code: {}   \n   Fname: {}   \n   Lname: {}   \n '.format(pr[0],pr[2],pr[3]) , font=('arial', 15))
                    l_print.place(relx = 0.3,rely = 0.5)
                else:

                    l_hoshdar= Label(root_search_op, text=' !متاسفانه موردی یافت نشد ', font=('arial', 15, 'bold'), bg='red')
                    l_hoshdar.place(relx = 0.2,rely = 0.5)
            

            def search_OP_name():
                pr = manag_tbl.search_name_Operator(entr_fname.get(),entr_lname.get())
                if pr:
                    l_print = Label(root_search_op, text='  code: {}   \n   Fname: {}   \n   Lname: {}   \n '.format(pr[0],pr[2],pr[3]) , font=('arial', 15))
                    l_print.place(relx = 0.3,rely = 0.5)
                else:
                    l_hoshdar= Label(root_search_op, text=' !متاسفانه موردی یافت نشد ', font=('arial', 15, 'bold'), bg='red')
                    l_hoshdar.place(relx = 0.2,rely = 0.5)

                

            btn8 = ttk.Button(root_search_op, text=' جستوجو ', command=search_Op_code)
            btn8.place(relx = 0.128,rely = 0.175 )
            btn9 = ttk.Button(root_search_op, text=' جستوجو ', command=search_OP_name)
            btn9.place(relx = 0.65,rely = 0.33 )

        def all_taxi():
            root_show_all_tax = Tk()
            root_show_all_tax.geometry('500x400')
            root_show_all_tax.resizable(False,False)
            root_show_all_tax.title('نمایش همه راننده های مجموعه')
            scrollbar = Scrollbar(root_show_all_tax)
            scrollbar.pack( side = RIGHT ,fill = BOTH )
            mylist = Listbox(root_show_all_tax, yscrollcommand = scrollbar.set )
            all_ = manag_tbl.all_driver()
            for i in all_:
                st = '  code: {}     FName: {}   LName: {}   age: {}      He is {} Now \n'.format(i[3],i[0],i[1],i[2],i[5])
                mylist.insert(END,root_show_all_tax, st)
                
            mylist.pack(ipadx=400 , ipady=200)
            scrollbar.config( command = mylist.yview )

        def all_stition():
            root_show_all_station = Tk()
            root_show_all_station.geometry('1700x250')
            root_show_all_station.title('نمایش تقسیم بندی ایستگاه')
            root_show_all_station.resizable(False , False)

            all_ = manag_tbl.all_Station_ranges()
            for i in all_:
                st = '  Number-Station: {})    Square: {}   |   Street: {}   |  Region: {}  \n'.format(i[0],i[1],i[2],i[3])
                l_show = ttk.Label(root_show_all_station, text=st , font=(3))
                l_show.pack()
        
        def all_OPrator():
            root_show_all_OP = Tk()
            root_show_all_OP.geometry('600x250')
            root_show_all_OP.title('اپراتور ها')
            root_show_all_OP.resizable(False , False)
   
            all_ = manag_tbl.all_Opr()
            for i in all_:
                st = '  user_Operator: {})  FName: {}  | LName: {} | Password: {}  \n'.format(i[0],i[2],i[3],i[1])
                l_show = ttk.Label(root_show_all_OP, text=st , font=(3))
                l_show.pack()
        


        def change_pass_manager():
            root_change_pass_manager = Tk()
            root_change_pass_manager.title('~Choose~')
            root_change_pass_manager.geometry("300x300")
            root_change_pass_manager.resizable(False,False)
            l_usr = Label(root_change_pass_manager,text= ' تغییر رمز کاربر  '  ,font=('arial', 16 ,'bold') , bg='#8FBC8B')
            l_usr.place(relx = 0.3,rely = 0.03)


            l_last_pass = Label(root_change_pass_manager,text='رمز  قبلی')
            l_last_pass.place(relx = 0.11,rely = 0.18)
            entr_old_pass = Entry(root_change_pass_manager,width = 30)
            entr_old_pass.place(relx = 0.3,rely = 0.18)


            l_pass = Label(root_change_pass_manager,text='رمز')
            l_pass.place(relx = 0.15,rely = 0.26)
            entr_pass = Entry(root_change_pass_manager,width = 30)
            entr_pass.place(relx = 0.3,rely = 0.26)

            l_pass = Label(root_change_pass_manager,text=' تکرار رمز')
            l_pass.place(relx = 0.1,rely = 0.34)
            entr_pass2 = Entry(root_change_pass_manager,width = 30)
            entr_pass2.place(relx = 0.3,rely = 0.34)

            def changing():
                old_check = manag_tbl.manager_check(entr_code_manag.get(), entr_old_pass.get())
                if old_check:
                    if entr_pass.get() == entr_pass2.get():
                        w = manag_tbl.change_pass_maager(entr_code_manag.get(),entr_pass.get())
                        if w  :
                            l = Label(root_change_pass_manager,text='   تغییر رمز با موفقیت انجام شد     ')
                            l.place(relx = 0.3,rely = 0.75)
                        else :
                            l2 = Label(root_change_pass_manager,text='  نام کاربری یا رمز نامعتبر است!   ')
                            l2.place(relx = 0.3,rely = 0.75)
                    else:
                        l2 = Label(root_change_pass_manager,text='لطفا تکرار رمز را درست وارد نماید !')
                        l2.place(relx = 0.3,rely = 0.75)
                else:
                    l2 = Label(root_change_pass_manager,text='لطفا رمز قبلی را درست وارد نماید !')
                    l2.place(relx = 0.3,rely = 0.75)

            btn4 = ttk.Button(root_change_pass_manager,text='ذخیره تغییرات', command=changing ,width = 20)
            btn4.place(relx = 0.34,rely = 0.5)




        menubar = Menu(root_manager)
        addingmenu = Menu(menubar, tearoff=0)
        # addingmenu.add_command(label="Cut")
        addingmenu.add_command(label="اپراتور جدید", command=adding_Op)
        addingmenu.add_command(label="راننده جدید", command=adding_drv)
        menubar.add_cascade(label="ثبت نام", menu=addingmenu)

        showmenu = Menu(menubar, tearoff=0)
        showmenu.add_command(label=" مناق تقسیم شده ایستگاه ها", command=all_stition)
        showmenu.add_command(label="راننده ها ", command=all_taxi)
        showmenu.add_command(label="اپراتور ها ", command=all_OPrator)
        menubar.add_cascade(label="نمایش همه", menu=showmenu)
   

        deletemenu = Menu(menubar, tearoff=0)
        deletemenu.add_command(label="اپراتور", command=delet_op)
        deletemenu.add_command(label="راننده", command=delet_drv)
        menubar.add_cascade(label="حذف", menu=deletemenu)

        searchmenu = Menu(menubar, tearoff=0)
        searchmenu.add_command(label="اپراتور", command=search_OPr)
        searchmenu.add_command(label="راننده", command=search_drv)
        menubar.add_cascade(label="جستوجو ", menu=searchmenu)

        changemenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="  تغیر رمز ", command=change_pass_manager)

        root_manager.config(menu=menubar)
        


    root1.mainloop()
    








star = choose()
