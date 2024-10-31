from manage_tables import management 
manage = management()

class manage_travel:
  
    def search_start(self ,start):
        if 'st' in start:
            a = start.replace('st ' , '')
            return manage.find_street(a)[0]
        elif 'sq' in start:
            b = start.replace('sq ', '')
            return manage.find_square(b)[0]
        elif 'rg' in start:
            c = start.replace('rg ', '')
            return manage.find_region(c)[0]

    def search_end(self, end):
        if 'st' in end:
            a = end.replace('st ' , '')
            return manage.find_street(a)[0]
        elif 'sq' in end:
            b = end.replace('sq ', '')
            return manage.find_square(b)[0]
        elif 'rg' in end:
            c = end.replace('rg ', '')
            return manage.find_region(c)[0]
    

    def start_trip(self ,start , end):

        if self.search_start(start) :
            if self.search_end(end):
                return True

    
    def finde_Station_taxies(self , start):
        number = self.search_start(start)
        all_taxi = manage.find_alltaxi(number)
        return all_taxi


    def show_Condition(self , all_taxi):
        shooww = []

        s = all_taxi
        for i in s[1:]:
            
            if i is None:
                continue
            else:
                codeing = manage.find_code(i)
                shooww.append('Drive:{} is {} '.format(codeing[3],codeing[5]))
        return shooww 


    def change_drv_stition(self , code , maghsad):
        number_first = manage.find_station(code)
        number_sec_stait = self.search_end(maghsad)
        manage.delete_drv_staite(number_first,code)

        manage.add_drv_stait(number_sec_stait,code)
