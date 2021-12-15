from re import search
from types import new_class
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Ajutt92441312', database="dbproject")
print(mydb)
mycursor=mydb.cursor()
mycursor.execute("create database if not exists dbproject")

#customer table
def buttonPressed(num1, num2, num3, num4, num5, num6):
    n1=num1.get()
    n2=num2.get()
    n3=num3.get()
    n4=num4.get()
    n5=num5.get()
    n6=num6.get()
    userList2=[]
    userList3=[]
    mycursor.execute("CREATE TABLE if not exists customers (FullName varchar(255), Nationality varchar(255),PhoneNo int,Email varchar(255),username varchar(255) Primary Key, password varchar(255))")
    a="INSERT INTO customers(FullName,Nationality,PhoneNo,Email,username,password) values (%s,%s,%s,%s,%s,%s)"
    b=(n1,n2,int(n3),n4,n5,n6)
    mycursor.execute(a,b)
    mydb.commit()
    

import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter import messagebox

main1= Tk()
main1.geometry("1280x720")


def open_win():
   main2=tkinter.Tk()
   main2.geometry("1280x720")
   main2.title("New Window")
   main2['background'] = '#192841'
   main1.destroy()
   reg=Label(main2, text='Online Airline Ticketing',bg='#192841',fg='white', font=('Blastimo', 40))
   reg.place(x=334, y=10)
   registeration=Label(main2, text='Sign In Now',padx=106, pady=15, bg='#32CD32', fg='white', font=('helvetica', 14, 'bold'))
   registeration.place(x=444, y=100)
   usr_lgn=Label(main2, text='Username',padx=61, pady=8, bg='white', fg='black', font=('helvetica', 9, 'bold'))
   usr_lgn.place(x=390, y=160) 
   usrEntry_lgn=Entry(main2, width=40)   
   usrEntry_lgn.place(x=590, y=170) 
   pswrd_lgn=Label(main2, text='Password',padx=61, pady=8, bg='white', fg='black', font=('helvetica', 9, 'bold'))
   pswrd_lgn.place(x=390, y=200)
   pswrdlgnEntry=Entry(main2, width=40)
   pswrdlgnEntry.place(x=590, y=210)  
   login_lgn=Button(main2, text='Login', command=lambda: welcome(usrEntry_lgn, pswrdlgnEntry), padx=195,pady=-10,bd= 10, bg='brown', fg='white', font=('helvetica', 9, 'bold'))

# register.pack()
   login_lgn.place(x=390, y=240)
   donthave=Label(main2, text='Do not have account?',padx=66, pady=8, bg='white', fg='blue', font=('Arial', 9, 'bold'))
   donthave.place(x=390, y=287)
   register_lgn=Button(main2, text="Register", command= lambda: buttonPressed(FN_Entry, nation_entry,phone_entry,email_Entry,usr_Entry, pswrd_Entry), padx= 50, bd= 10, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
   register_lgn.place(x=660, y=285)
    
#
def welcome(no1, no2):
    h=no1.get()
    k=no2.get()
    userList=[]
    passList=[]
    mycursor.execute("SELECT username FROM customers")
    myresult = mycursor.fetchall()
    for x in myresult:
        userList.append(x)
    # print(userList)
  
    mycursor.execute("SELECT password FROM customers")
    Yresult = mycursor.fetchall()
    for x in Yresult:
        passList.append(x)
    Newlist1=[]
    Newlist2=[]
    for i in userList:
        a=''.join(i)
        Newlist1.append(a)
    for j in passList:
        b=''.join(j)
        Newlist2.append(b)

    for i in Newlist1:
        for j in Newlist2:
            if i==h and j==k:
                main3=tkinter.Tk()
                main3.geometry("1280x720")
                main3['background'] = '#192841'
                b=Label(main3, text='Welcome! To Our Services', padx=106, pady=15, bg='#32CD32', fg='white', font=('helvetica', 14, 'bold'))
                b.place(x=440, y=65)
                
                # regBook=Label(main3, text='Book Your Seat!',padx=106, pady=15, bg='#32CD32', fg='white', font=('helvetica', 14, 'bold'))
                # regBook.place(x=444, y=60)
                           
                label1=Label(main3, text='Search Scheduled Flights', padx=106, pady=15, bg='#32CD32', fg='white', font=('helvetica', 14, 'bold'))
                label1.place(x=440, y=65)
                departLabel=Label(main3, text='Departure', padx=68, pady=8, bg='white', fg='black',font=('helvetica', 12, 'bold'))
                departLabel.place(x=310, y=140)
                departt=Combobox(main3, width=20,height=10)
                departt['values']=('Lahore', 'London', 'Karachi', 'Cape Town', 'New York', 'New Delhi', 'Sharjah', 'Abu Dhabi', 'Dubai', 'Multan', 'Jeddah')
                departt.place(x=540, y=148)
                destLabel=Label(main3, text='Destination', padx=77, pady=8, bg='white', fg='black',font=('helvetica', 12, 'bold'))
                destLabel.place(x=690, y=140)
                destt=Combobox(main3, width=20)
                destt['values']=('Lahore', 'London', 'Karachi', 'Cape Town', 'New York', 'New Delhi', 'Sharjah', 'Abu Dhabi', 'Dubai', 'Multan', 'Jeddah')
                destt.place(x=950, y=148)
                dayLabel=Label(main3, text='Day of Travel', padx=70, pady=8, bg='white', fg='black',font=('helvetica', 12, 'bold'))
                dayLabel.place(x=690, y=185)
                dayy=Combobox(main3, width=20)
                dayy['values']=('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
                dayy.place(x=950, y=193)
                classLabel=Label(main3, text='Class', padx=84, pady=8, bg='white', fg='black',font=('helvetica', 12, 'bold'))
                classLabel.place(x=310, y=185)
                classs=Combobox(main3, width=20)
                classs['values']=('Economy', 'Executive', 'Business')
                classs.place(x=540, y=193)
                searchButton=Button(main3, text='Search',command=lambda: SearchOperation(departt, destt, dayy, classs),padx=50,pady=10,bd= 10, bg='brown', fg='white', font=('helvetica', 14, 'bold'))
                searchButton.place(x=550, y=250)

      
                bb=Label(main3, text='Click Below Button To Book Schedule Flights', padx=106, pady=5, bg='red', fg='white', font=('helvetica', 14, 'bold'))
                bb.place(x=400, y=360)
                searchFlights=Button(main3, text='Book Flights',command=lambda:bookDataFunc(),padx=50,pady=10,bd= 10, bg='brown', fg='white', font=('helvetica', 14, 'bold'))
                searchFlights.place(x=550, y=410)
  

                def bookDataFunc():
                    main5=tkinter.Tk()
                    main5.geometry('1280x720')
                    main5['background'] = '#192841'
                    main3.destroy()
                    regBook=Label(main5, text='Book Your Seat!',padx=106, pady=15, bg='#32CD32', fg='white', font=('helvetica', 14, 'bold'))
                    regBook.place(x=444, y=60)
                    departLabel=Label(main5, text='Departure', padx=68, pady=8, bg='white', fg='black',font=('helvetica', 12, 'bold'))
                    departLabel.place(x=310, y=140)
                    depart=Combobox(main5, width=20,height=10)
                    depart['values']=('Lahore', 'London', 'Karachi', 'Cape Town', 'New York', 'New Delhi', 'Sharjah', 'Abu Dhabi', 'Dubai', 'Multan', 'Jeddah')
                    depart.place(x=540, y=148)
                    destLabel=Label(main5, text='Destination', padx=77, pady=8, bg='white', fg='black',font=('helvetica', 12, 'bold'))
                    destLabel.place(x=690, y=140)
                    dest=Combobox(main5, width=20)
                    dest['values']=('Lahore', 'London', 'Karachi', 'Cape Town', 'New York', 'New Delhi', 'Sharjah', 'Abu Dhabi', 'Dubai', 'Multan', 'Jeddah')
                    dest.place(x=950, y=148)
                    airlineLabel=Label(main5, text='Airline Brand', padx=56, pady=8, bg='white', fg='black',font=('helvetica', 12, 'bold'))
                    airlineLabel.place(x=310, y=185)
                    airlines=Combobox(main5, width=20)
                    airlines['values']=('Emirates', 'Qatar Airways', 'PIA', 'Shaheen', 'Air Blue', 'British Airways', 'Etihad Airlines')
                    airlines.place(x=540, y=193)
                    dayLabel=Label(main5, text='Day of Travel', padx=70, pady=8, bg='white', fg='black',font=('helvetica', 12, 'bold'))
                    dayLabel.place(x=690, y=185)
                    day=Combobox(main5, width=20)
                    day['values']=('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
                    day.place(x=950, y=193)
                    classLabel=Label(main5, text='Class', padx=84, pady=8, bg='white', fg='black',font=('helvetica', 12, 'bold'))
                    classLabel.place(x=310, y=230)
                    clas=Combobox(main5, width=20)
                    clas['values']=('Economy', 'Executive', 'Business')
                    clas.place(x=540, y=238)
                    PessLabel=Label(main5, text='Passenger(s)', padx=70, pady=8, bg='white', fg='black',font=('helvetica', 12, 'bold'))
                    PessLabel.place(x=690, y=230)
                    psngrs=Combobox(main5, width=20)
                    psngrs['values']=('1', '2', '3', '3', '5')
                    psngrs.place(x=950, y=238)
                    flightNo_Label= Label(main5, text='Flight No', padx=70, pady=8, bg='white', fg='black',font=('helvetica', 12, 'bold'))
                    flightNo_Label.place(x=310, y=275)
                    flightNo_Entry=Entry(main5, width=20)
                    flightNo_Entry.place(x=540, y=283)
                    bookButton=Button(main5, text='Book Ticket',command=lambda:bookOperation(flightNo_Entry,depart, dest, airlines, day, clas, psngrs),padx=70,pady=10,bd= 10, bg='brown', fg='white', font=('helvetica', 14, 'bold'))
                    bookButton.place(x=690, y=283)


                    def bookOperation(s1,s2,s3,s4,s5,s6,s7):
                        
                        g1=s1.get()
                        g2=s2.get()
                        g3=s3.get()
                        g4=s4.get()
                        g5=s5.get()
                        g6=s6.get()
                        g7=s7.get()
                        
                        mycursor.execute("CREATE TABLE if not exists Flights(FlightNo varchar(255) Primary Key, Departure varchar(255),Destination varchar(255), AirlineBrand varchar(255), TravelDay varchar(255), Class varchar(255), Passenger int)")
                        aaj="INSERT INTO Flights(FlightNo,Departure, Destination, AirlineBrand, TravelDay, Class, Passenger) values (%s, %s,%s, %s,%s, %s, %s)"
                        val=(g1,g2,g3,g4,g5,g6,int(g7))
                        mycursor.execute(aaj,val)
                        messagebox.showinfo("Congratulations!","Your ticket has been booked.")
                        mydb.commit()


                def SearchOperation(q1,q2,q3, q4):
                    
                    hum1=q1.get()
                    hum2=q2.get()
                    hum3=q3.get()
                    hum4=q4.get()
                    mycursor.execute("CREATE TABLE IF NOT EXISTS SearchFlights(FlightNo varchar(255) Primary Key,Departure varchar(255),Destination varchar(255), AirlineBrand varchar(255), TravelDay varchar(255), Class varchar(255))")
                    ass="INSERT INTO SearchFlights(FlightNo,Departure, Destination, AirlineBrand, TravelDay, Class) values (%s,%s, %s, %s,%s, %s)"
                    abb=[('A1','Lahore', 'London','PIA','Sunday','Business'),('A2','London', 'Lahore','PIA','Sunday','Economy'),('A3','Lahore', 'London','PIA','Sunday','Ecomomic'),('A4','Lahore', 'London','PIA','Monday','Economic'),('A5','Lahore', 'London','PIA','Tuesday','Economic'),('A6','Lahore', 'New York','PIA','Sunday','Economic'), ('A7','Lahore', 'New York','PIA','Monday','Economic')]
                    mycursor.executemany(ass, abb)
                    mydb.commit()
                    # mycursor.execute("SELECT * from SearchFlights where Departure='Lahore'")
                    # myyresult=mycursor.fetchall()                                 
                    sql = "SELECT * FROM SearchFlights WHERE Departure= %s AND Destination= %s AND TravelDay=%s AND Class=%s"
                    adr = (hum1,hum2, hum3, hum4 )
                    mycursor.execute(sql, adr)
                    messagebox.showinfo('available flights',mycursor.fetchall())
                  
        
                break
           


def button():
    main2=tkinter.Tk()
    main2.geometry('1280x720')
    
    title=Label(main2, text='Online Airline Ticketing')
    title.pack()
    internal_flights=Button(main2, text='Internal Flights').place(x=90, y=49)
    external_flights=Button(main2, text='External Flights').pack()
    main2.mainloop()
 
main1.title("Online Airline Ticketing")
main1.geometry('1280x720')
main1['background'] = '#192841'
# title=Label(main1, text='Online Airline Ticketing', fg='white',font=('Bebas Neue', 40))
# title.place(x=300, y=30)
reg=Label(main1, text='Online Airline Ticketing',bg='#192841',fg='white', font=('Blastimo', 40))
reg.place(x=334, y=10)
registeration=Label(main1, text='Create Account',padx=106, pady=15, bg='#32CD32', fg='white', font=('helvetica', 14, 'bold'))
registeration.place(x=444, y=100)
FullName=Label(main1, text='Full Name',padx=63, pady=8, bg='white', fg='black', font=('helvetica', 9, 'bold'))
FullName.place(x=390, y=160)
# FullName.pack()
FN_Entry=Entry(main1, width=40)
FN_Entry.place(x=590, y=170)
Nationality=Label(main1, text='Nationality', padx=60, pady=8, bg='white', fg='black',font=('helvetica', 9, 'bold'))
Nationality.place(x=390, y=200)
# Nationality.pack()
nation_entry=Entry(main1, width=40)
nation_entry.place(x=590, y=210)
# nation_entry.pack()
phoneNo=Label(main1, text='Phone No', padx=63, pady=8, bg='white', fg='black', font=('helvetica', 9, 'bold'))
phoneNo.place(x=390, y=240)
phone_entry=Entry(main1, width=40)
phone_entry.place(x=590, y=250)
email=Label(main1, text='Email',padx=75, pady=8,  bg='white', fg='black', font=('helvetica', 9, 'bold'))
email.place(x=390, y=280)
email_Entry=Entry(main1, width=40)
email_Entry.place(x=590, y=290)
usrName=Label(main1, text='Username',padx=61, pady=8, bg='white', fg='black', font=('helvetica', 9, 'bold'))
usrName.place(x=390, y=320)
usr_Entry=Entry(main1, width=40)
usr_Entry.place(x=590, y=330)
pswrd=Label(main1, text='Password',padx=61, pady=8, bg='white', fg='black', font=('helvetica', 9, 'bold'))
pswrd.place(x=390, y=360)
pswrd_Entry=Entry(main1, width=40)
pswrd_Entry.place(x=590, y=370)
register=Button(main1, text='Register', command= lambda: buttonPressed(FN_Entry, nation_entry,phone_entry,email_Entry,usr_Entry, pswrd_Entry), padx= 186, bd= 10, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
register.place(x=390, y=400)
already=Label(main1, text='Already have an Account?',padx=66, pady=8, bg='white', fg='blue', font=('Arial', 9, 'bold'))
already.place(x=390, y=448)
login=Button(main1, text="Login", command=open_win, padx=50,pady=-10,bd= 10, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
login.place(x=680, y=446)
main1.mainloop()




# # Schedule flights table
# mycursor.execute("CREATE TABLE if not exists ScheduleFlights(FlightNo varchar(255), Departure varchar(255), Destination varchar(255), DepartureTime varchar(255), ArrivalTime varchar(255), Price int)")
# c="INSERT INTO ScheduleFlights(FlightNo, Departure, Destination, DepartureTime, ArrivalTime, price) values (%s, %s, %s, %s, %s, %s)"
# d= [('A1', 'Karachi', 'Lahore', '1000am', '330pm', 20000), ('A2', 'Islamabad', 'Lahore', '200am', '330pm', 10000), ('A3', 'Karachi', 'Islamabad', '1100am', '430pm', 15000)]
# mycursor.executemany(c,d)
# mydb.commit()
