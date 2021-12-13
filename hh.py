import tkinter as t
import tkinter.messagebox
from tkinter import ttk
import datetime
import sqlite3
import Individuals
import DB
from tkinter import filedialog as fd
import csv

class MyGUI:
    def __init__(self):

        self.won=t.Tk()
        self.won.title('Tawklna')
        self.won.iconbitmap('tawaklna.ico')
        self.notebook = ttk.Notebook(self.won)
        self.notebook.pack(pady=10, expand=True)

        self.frame = t.Frame(self.won)

        self.top_frame = t.Frame(self.frame)

        self.frame1 = t.Frame(self.top_frame)
        self.frame2 = t.Frame(self.top_frame)
        self.frame3 = t.Frame(self.top_frame)
        self.frame4 = t.Frame(self.top_frame)
        self.frame5 = t.Frame(self.top_frame)
        self.frame6 = t.Frame(self.top_frame)
        self.frame7 = t.Frame(self.top_frame)
        self.frame8 = t.Frame(self.top_frame)
        #first and last name
        self.label1 = t.Label(self.frame1, text='Enter your first name     ')
        self.fname_entry = t.Entry(self.frame1, width=10)
        self.label2 = t.Label(self.frame2, text='Enter your last name     ')
        self.lname_entry = t.Entry(self.frame2, width=10)
        #id & sex
        self.label3 = t.Label(self.frame3, text='Enter your ID                  ')
        self.Id_entry = t.Entry(self.frame3, width=10)
        self.label8 = t.Label(self.frame8, text='Enter your SEX                ')
        self.sex_entry = t.Entry(self.frame8, width=10)

        self.label4 = t.Label(self.frame4, text='Enter your Year of Birth')
        self.yOfb_entry = t.Entry(self.frame4, width=10)

        self.label5 = t.Label(self.frame5, text='Enter Type of Vaccine   ')
        self.vac_entry = t.Entry(self.frame5, width=10)

        self.label6 = t.Label(self.frame6, text='Enter the Date & Time  ')
        self.dateTime_entry = t.Entry(self.frame6, width=10)

        self.label7 = t.Label(self.frame7, text='Enter Phone number     ')
        self.pho_entry = t.Entry(self.frame7, width=10)

        self.bottom_frame = t.Frame(self.frame)
        self.calc_button = t.Button(self.bottom_frame, text='Enter', command=self.insert)
        # the secound tab -----------------------------------------------------------------------------------

        # labelFrame

        self.framee = t.Frame(self.won)
        self.labelFrame1 = t.LabelFrame(self.framee, text='individual information')
        self.labell = t.Label(self.framee, text='Enter your ID')
        # entry
        self.entry = t.Entry(self.framee, width=10)
        # button
        self.check_button = t.Button(self.framee, text='Check', command=self.check)



        #export File
        self.canvas = t.Canvas(self.framee)
        self.imgFile=""
        self.img=t.PhotoImage(file=self.imgFile)
        self.canvas.create_image(100, 100, anchor=tkinter.NW, image=self.img)
        self.canvas.pack(pady="30", padx="30")
        self.framee.pack(side='left')
        self.labell.pack(side='left')
        self.entry.pack(side='left')
        self.check_button.pack(side='left')

        #packs

        self.label1.pack(side='left')
        self.fname_entry.pack(side='left')

        self.label2.pack(side='left')
        self.lname_entry.pack(side='left')

        self.label3.pack(side='left')
        self.Id_entry .pack(side='left')

        self.label8.pack(side='left')
        self.sex_entry.pack(side='left')

        self.label4.pack(side='left')
        self.yOfb_entry.pack(side='left')

        self.label5.pack(side='left')
        self.vac_entry.pack(side='left')

        self.label6.pack(side='left')
        self.dateTime_entry.pack(side='left')

        self.label7.pack(side='left')
        self.pho_entry.pack(side='left')

        self.calc_button.pack(side='left')


        self.frame1.pack()
        self.frame2.pack()
        self.frame8.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()
        self.frame6.pack()
        self.frame7.pack()

        self.frame.pack()

        self.top_frame.pack()
        self.bottom_frame.pack()
        # the third tab-----------------------------------------------
        self.thirdTap=t.Frame(self.won)
        self.toopf=t.Frame(self.thirdTap)

        self.imLable = t.Label(self.toopf, text='click here to import a file to the database ')
        self.importBou = t.Button(self.toopf, text='Import', command=self.importCsv)

        self.downF = t.Frame(self.thirdTap)

        self.exLable = t.Label(self.toopf, text='click here to export a file from the database ')
        self.exportBou = t.Button(self.thirdTap, text='Export', command=self.expotrCsv)
        self.imLable.pack()
        self.importBou.pack()

        self.toopf.pack()

        self.exLable.pack()
        self.exportBou.pack()
        self.downF.pack()
        self.thirdTap.pack()


        self.notebook.add(self.frame, text='General Information')
        self.notebook.add(self.framee, text='Immunty check')
        self.notebook.add(self.thirdTap, text='Import & Export')




        self.won.mainloop()
    def insert(self):
        fnmae=self.fname_entry.get()
        lname = self.lname_entry .get()
        sex=self.sex_entry.get()
        id=self.Id_entry .get()
        yearof= self.yOfb_entry.get()
        vacType = self.vac_entry.get()
        pho = self.pho_entry.get()
        dateTime = self.dateTime_entry.get()
        flag ,defc = self.chekFiled(fnmae,lname,sex,id,yearof,vacType,dateTime,pho)
        if(flag):
            ind= Individuals.Individual(fnmae,lname,sex,int(id),str(yearof),vacType,str(dateTime),pho)
            DB.createTable()
            status=DB.insret(ind)
            if(status==True):
               t.messagebox.showinfo('Result','your inforamtion has enterd successfully thank you ')
            else:
                t.messagebox.showinfo('Result', 'the record alredy exsit in the database ')
        elif(not flag and defc ==-1):
            t.messagebox.showinfo('Result', 'your first name is wrong please enter a valid name')
        elif (not flag and defc == -2):
             t.messagebox.showinfo('Result', 'your last name is wrong please enter a valid name')
        elif (not flag and defc == -3):
            t.messagebox.showinfo('Result','you enterd invalid SEX please enter a valid SEX such  as  (Male or Female)')
        elif (not flag and defc == -4):
            t.messagebox.showinfo('Result', 'you enterd invalid id please enter an id  (10 digits)')
        elif (not flag and defc == -5):
            t.messagebox.showinfo('Result', 'you enterd invalid year please enter a year in this format (4 digits, must be above 1900 and less than 2003)')

        elif (not flag and defc == -6):
            t.messagebox.showinfo('Result','you enterd invalid vaccine please enter a vaccine from these vaccines (Pfizer, AstraZeneca, Moderna, J&J)')
        elif (not flag and defc == -7):
            t.messagebox.showinfo('Result','you enterd invalid date and time  number  please enter a valid date and  timw with this format 12/10/2021 10:30 AM')
        elif (not flag and defc == -8):
             t.messagebox.showinfo('Result','you enterd invalid phone number  please enter a valid phone number in this foramt 05XXXXXXXX')
        else:
            t.messagebox.showinfo('Result','please try agein')

    def check(self):

        id=str(self.entry.get())
        size=len(id)
        try:
            if (size != 10 or not id.isdigit()):
                raise ValueError

        except:
            t.messagebox.showinfo('Result', 'you enterd invalid id please enter an id  (10 digits)')
            return
        x = DB.check(self.entry.get())
        if (x == 0):
            self.imgFile = 'red.png'

        elif (x == 1):
            self.imgFile = 'yellow.png'

        else:
            self.imgFile = 'green.png'
        self.img = t.PhotoImage(file=self.imgFile)
        self.canvas.create_image(100,100, anchor=tkinter.NW, image=self.img)

    def importCsv(self):
        try:
           name = fd.askopenfilename()
           file = open(name,'r')
           csvreader = csv.reader(file)
           fields = next(csvreader)
           if(len(fields)!=8):
               raise IndexError
           counter =0
           listOfRecordes=[]
           flag=True
           for row in csvreader:
              counter+=1
              flag,num=self.chekFiled(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
              if( not flag):
                      break
              temp = Individuals.Individual(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
              listOfRecordes.append(temp)
           if (not flag):
               t.messagebox.showinfo('Result', f'faild to import becuase there is a wrong format in record number {counter} ')
               file.close()
               return
           k=DB.insretListOfRecords(listOfRecordes)
           if(k):
               t.messagebox.showinfo('Result', 'the file has enterd to the database successfully')
           elif (not k):
             t.messagebox.showinfo('Result','the file has not enterd to the database because the dublication of the records')

        except IndexError:
            t.messagebox.showinfo('Result', 'the foramt should be FirstName, LastName, Sex, ID, YOB, TOV, DT, PhoneNO' )
            file.close()
            return
        except :
            t.messagebox.showinfo('Result', 'faild to import ')
            return
        file.close()
    def expotrCsv(self):
        name = fd.askdirectory(master=self.won)
        tmpdirectory = str(name) + "/tawaklna.csv"
        try:
            file = open(tmpdirectory, 'w', newline='')
            csvwrite = csv.writer(file)
            x = DB.retrieveAll(self)
            for row in x:
                csvwrite.writerow(row)
            t.messagebox.showinfo(f'Result', f'The file has exported to the {tmpdirectory}')
        except:
            t.messagebox.showinfo('Result', 'Failed to export')
    def chekFiled(self,fname,lname,sex,id,yof,vac,datim,pho):
        try:
            flag = str(fname).isalpha()
            if (not flag):
                raise ValueError
        except:
            return False ,-1
        try:
            flag = str(lname).isalpha()
            if (not flag):
                raise ValueError

        except:
            return False , -2
        try:
            if (str(sex).lower() != 'male' and str(sex).lower() != 'female'):
                raise ValueError
        except:
            return False,-3

        try:
            size = len(id)
            if (size != 10 or not id.isdigit()):
                raise ValueError
        except:
            return False , -4

        try:
            yof= int(yof)
            if (yof < 1900 or yof > 2003):
                raise ValueError
        except ValueError:
            return False,-5
        try:
            vacSet = ['Pfizer', 'AstraZeneca', 'Moderna', 'J&J']
            flag = False
            for type in vacSet:
                if (str(vac).lower() == type.lower()):
                    flag = True
            if (not flag):
                raise ValueError
        except:
            return False,-6
        try:
            datim = str(datim).split(' ')
            st = datim[0]
            time = datim[1]
            am = datim[2]
            day, mon, year = st.split('/')
            datetime.datetime(int(year), int(mon), int(day))
            hour= time.split(':')
            if (int(hour[0]) > 12 or int(hour[0]) < 0 or int(hour[1]) < 0 or int(hour[1]) > 60):
                raise ValueError
            if (am.lower() != 'am' and am.lower() != 'pm'):
                raise ValueError
        except:
            return False,-7
        try:
            temp=str(pho)
            size = len(pho)
            if size != 10 or not temp.isdigit() or temp[0] != '0' or temp[1] != '5':
                raise ValueError
        except:
            return False,-8
        return True ,1
x= MyGUI()