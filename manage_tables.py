import sqlite3
from types import coroutine

class management:
    
    def __init__(self, db_name = "bisim_manage.sqlite"):
        self.conn = sqlite3.connect(db_name)
    
    def all_driver(self):
        c = self.conn.cursor()
        c.execute("SELECT * FROM info_Driver")
        al = c.fetchall()
        return al



    def find_code(self, cod_id):
        c = self.conn.cursor()
        al= c.execute("SELECT * FROM info_Driver WHERE Code = '{}'".format(
                cod_id))
        if al :
            searching = al.fetchone()
            return searching
        else:
            return False
        
    def find_name(self, FName , Lname):
        c = self.conn.cursor()
        al= c.execute("SELECT * FROM info_Driver WHERE FName = '{}' AND LName = '{}'".format(
                FName , Lname))
        if al :
            searching = al.fetchone()
            return searching
        else:
            return False


    def find_age(self, Age):
        c = self.conn.cursor()
        al= c.execute("SELECT * FROM info_Driver WHERE age LIKE '%{}%' ".format(
                Age))
        return al.fetchall()

   
    def add_new_d(self, FName, LName, age , Code , date , condition):
        r = self.find_code(Code)
        if r == None:
            c = self.conn.cursor()
            c.execute( "INSERT INTO info_Driver (FName , LName ,age , Code , Date_birth ,Condition ) VALUES ('{}', '{}','{}','{}' ,'{}', '{}')".format(FName, LName , age, Code , date , condition))
            self.conn.commit()
        else:
            return False


    
    def delete_drv(self, id_pl):
        c = self.conn.cursor()
        al = c.execute( "DELETE FROM info_Driver WHERE Code = '{}'".format(
                id_pl))
        self.conn.commit()
        return al.fetchone()

    
    def all_Station_ranges(self):
        c = self.conn.cursor()
        c.execute("SELECT * FROM Station_ranges")
        al = c.fetchall()
        return al


    def find_street(self, st):
        c = self.conn.cursor()
        al= c.execute("SELECT * FROM Station_ranges WHERE street LIKE '%{}%'".format(
                st))
        if al :
            searching = al.fetchone()
            return searching
        else:
            return False

    def find_square(self, sq):
        c = self.conn.cursor()
        al= c.execute("SELECT * FROM Station_ranges WHERE square LIKE '%{}%'".format(
                sq))
        if al :
            searching = al.fetchone()
            return searching
        else:
            return False

    def find_region(self, rg):
        c = self.conn.cursor()
        al= c.execute("SELECT * FROM Station_ranges WHERE region LIKE '%{}%'".format(
                rg))
        if al :
            searching = al.fetchone()
            return searching
        else:
            return False
    

    def all_drivers_station(self):
        c = self.conn.cursor()
        c.execute("SELECT * FROM driver_stations")
        al = c.fetchall()
        return al


    def find_station(self, code):
        c = self.conn.cursor()
        al= c.execute("SELECT * FROM driver_stations WHERE Driver_code1 = {} OR Driver_code2 = {}  OR Driver_code3 = {} OR Driver_code4 = {} OR Driver_code5 = {}  OR Driver_code6 = {}  OR Driver_code7 = {}  OR Driver_code8 = {}  OR Driver_code9 = {}".format(
                code , code , code, code, code, code, code, code, code))
        if al :
            searching = al.fetchone()
            return searching[0]
        else:
            return False

    def find_alltaxi(self, number):
        c = self.conn.cursor()
        al= c.execute("SELECT * FROM driver_stations WHERE Number_station = '{}' ".format(number))
        if al :
            searching = al.fetchone()
            return searching
        else:
            return False


    def add_drv_stait(self , number , code):
        c = self.conn.cursor()
        al= c.execute("SELECT * FROM driver_stations WHERE Driver_code1 OR Driver_code2  OR Driver_code3 OR Driver_code4 OR Driver_code5  OR Driver_code6  OR Driver_code7  OR Driver_code8 OR Driver_code9 IS NULL  ")
        if al :
            
            searching = al.fetchall()
            for numb in searching:
                if numb[0] == number:
                    for  k , i in enumerate(numb[1:11]):
                        if i == None:
                            if k is not None:
                                n = str(k + 1)
                                al = c.execute( "UPDATE driver_stations SET Driver_code{} ={}  WHERE Number_station = {} ".format(n,code,number))
                                self.conn.commit()
                                return al.rowcount
                                break
    
    def delete_drv_staite(self , number , code):
        all_taxi = self.find_alltaxi(number)
        c = self.conn.cursor()
        for k , drivers in enumerate(all_taxi[1:11]):
            if drivers == code:
                n = str(k + 1)
                al = c.execute( "UPDATE driver_stations SET Driver_code{} = NUlL WHERE Number_station = {}  ".format(n , number))
                self.conn.commit()
                return al.rowcount

    def change_drv_stat(self , number_F,number_S,code):
        self.delete_drv_staite(number_F,code)
        self.add_drv_stait(number_S,code)


   


    def all_Opr(self):
        c = self.conn.cursor()
        c.execute("SELECT * FROM log_in")
        al = c.fetchall()
        return al


    def Operator_check(self, usrN, password):
        c = self.conn.cursor()
        check = c.execute("SELECT * FROM log_in WHERE usr_Operator = '{}' AND pass_Operator = '{}' ".format(usrN,password))
        if check :
            searching = check.fetchone()
            return searching
        else:
            return False

    def search_Operator(self, usrN):
        c = self.conn.cursor()
        check = c.execute("SELECT * FROM log_in WHERE usr_Operator = '{}' ".format(usrN))
        if check :
            searching = check.fetchone()
            return searching
        else:
            return False

    def search_name_Operator(self, FName , Lname):
        c = self.conn.cursor()
        al= c.execute("SELECT * FROM log_in WHERE Fname_Op = '{}' AND Lname_Op = '{}'".format(
                FName , Lname))
        if al :
            searching = al.fetchone()
            return searching
        else:
            return False

    def add_Operator(self , usrN , password , Fname , Lname):
        r = self.Operator_check(usrN, password)
        if r == None:
            if len(usrN) and len(password):
                c = self.conn.cursor()
                c.execute( "INSERT INTO log_in (usr_Operator , pass_Operator ,Fname_Op, Lname_Op) VALUES('{}', '{}','{}','{}' )".format(usrN,password, Fname , Lname))
                self.conn.commit()
                return 'added'
        else:
            return None
    
    def change_pass_Operator(self, usrN , password):
        c = self.conn.cursor()
        if len(usrN) and len(password):
            al = c.execute( "UPDATE log_in SET pass_Operator ={}  WHERE usr_Operator = {} ".format(password,usrN))
        self.conn.commit()
        return al.rowcount
    
    def delet_Operator(self , usrN):
        c = self.conn.cursor()
        al = c.execute( "DELETE FROM log_in WHERE usr_Operator = '{}'".format(usrN))
        self.conn.commit()
        return al.fetchone()
        

    def manager_check(self , usrN , password):
        c = self.conn.cursor()
        check = c.execute("SELECT * FROM log_in WHERE user_manager = '{}' AND passw_manager = '{}' ".format(usrN,password))
        if check :
            searching = check.fetchone()
            return searching
        else:
            return False

    def change_pass_maager(self, usrN , password):
        c = self.conn.cursor()
        if len(usrN) and len(password):
            al = c.execute( "UPDATE log_in SET passw_manager ={}  WHERE user_manager = {} ".format(password,usrN))
        self.conn.commit()
        return al.rowcount

    
    def Change_Condition(self ,code,condition):
        c = self.conn.cursor()
        if len(str(code)) and len(condition):
            al = c.execute( "UPDATE info_Driver SET Condition = '{}'  WHERE Code = {} ".format(condition,code))
        self.conn.commit()
        return al.rowcount


    
