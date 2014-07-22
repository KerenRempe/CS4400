from tkinter import *
from datetime import date
class poop:
    def __init__(self,win): 
        self.login()
        self.Connect()

    def login(self): 
        l=Label(win, text="Georgia Tech ID")
        l.grid(row=0, column=0, sticky=E+W)
        self.iv=IntVar()
        e=Entry(win, textvariable=self.iv)
        e.grid(row=0, column=1, sticky=E+W)
        e.delete(0, END)
        l1=Label(win, text="Password")
        l1.grid(row=1, column=0, sticky=E+W)
        self.iv1=StringVar()
        e1=Entry(win, textvariable=self.iv1)
        e1.grid(row=1, column=1, sticky=E+W)
        b1=Button(win,text="OK", command=self.logincheck)
        b1.grid(row=2, column=0, sticky=E+W)
        b2=Button(win, text="Exit", command=self.exit)
        b2.grid(row=2, column=1, sticky=E+W)

    def exit(self):
        win.destroy()

    def Connect(self):
        import pymysql
        try:
            self.db=pymysql.connect(host="academic-mysql.cc.gatech.edu", passwd="gR5I5t0F", user="cs4400_Group_31", db="cs4400_Group_31")
            return(self.db)
        except:
            messagebox.showinfo(message="Please check your Internet!")
        
    def logincheck(self):
        un=self.iv.get()
        pd=self.iv1.get()
        c=self.db.cursor()
        usernames=c.execute("SELECT GTID FROM USER WHERE PASSWORD=(%s)", pd)
        actual=c.fetchall()
        if int(actual[0][0])==un: 
            self.Mainmenu()
        else:
            messagebox.showinfo(title="Incorrect Login Information", message="This is an unrecognizable username/password combination!")
        
    def Mainmenu(self):
        win.withdraw()
        self.win1=Toplevel()
        self.win1.title("Main Menu")
        l=Label(self.win1, text="Academic Year 2014!!!")
        l.grid(row=0, column=0, sticky=E+W)
        l1=Label(self.win1, text="Student Options")
        l1.grid(row=1, column=0, sticky=E+W)
        b2=Button(self.win1, text="Search/Schedule a Tutor", command=self.search)
        b2.grid(row=2,column=0, sticky=E+W)
        b1=Button(self.win1, text="Rate a Tutor", command=self.rate)
        b1.grid(row=2,column=1, sticky=E+W)
        l2=Label(self.win1, text="Tutor Options")
        l2.grid(row=3, column=0, sticky=E+W)
        b=Button(self.win1, text="Apply to be a tutor", command=self.apply)
        b.grid(row=4,column=0, sticky=E+W)
        b3=Button(self.win1, text="Find my Schedule", command=self.findmysched)
        b3.grid(row=4, column=1, sticky=E+W)
        l3=Label(self.win1, text="Professor Options")
        l3.grid(row=5, column=0, sticky=E+W)
        b4=Button(self.win1, text="Add Recommendation", command=self.recommend1)
        b4.grid(row=6, column=0, sticky=E+W)
        l4=Label(self.win1, text="Administrator Options")
        l4.grid(row=7, column=0, sticky=E+W)
        b5=Button(self.win1, text="Summary 1", command=self.sum1)
        b5.grid(row=8, column=0, sticky=E+W)
        b6=Button(self.win1, text="Summary 2", command=self.sum2)
        b6.grid(row=8, column=1, sticky=E+W)
        b7=Button(self.win1, text="Exit", command=self.exit)
        b7.grid(row=9, column=0, sticky=E+W)

    def semester(self):
        from datetime import date
        today=date.today()
        month=str(today.month)
        if len(month)==1:
            month="0"+str(month)
        day=str(today.day)
        if len(day)==1:
            day="0"+str(day)
        yearr=str(today.year)
        dat=yearr+month+day
        #find spring
        if '20140105'<=dat<='20140511':
            return('Fall 2014')
        if '20140512'<= dat <='20140817':
            return('Summer 2014')
        elif '20140818' <= dat <='20150104':
            return('Fall 2014')
        elif '20150105' <= dat <='20150510':
            return('Spring 2015')
        elif '20150511' <= dat <= '20150816':
            return('Summer 2015')
        elif '20150817' <= dat <= '20160110':
            return('Fall 2015')
        elif '20160111' <= dat <= '20160515':
            return('Spring 2016')
        elif '20160516' <= dat <= '20160821':
            return('Summer 2016')
        elif '20160822' <= dat <= '20170105':
            return('Fall 2016')

    def search(self):
        c=self.db.cursor()
        nn=c.execute("SELECT STUD_GTID FROM STUDENT")
        nn=c.fetchall()
        toned=[]
        self.win4=Toplevel()
        self.win4.title("Search/Schedule a Tutor")
        self.win1.withdraw()
        for i in nn:
            for y in i:
                toned.append(y)
        if self.iv.get() not in toned:
            messagebox.showinfo(title="None of your beeswax!", message="This function is only allowed for students.")
            self.win4.withdraw()
            self.Mainmenu()
        else:
            self.win4=Toplevel()
            self.win4.title("Search/Schedule a Tutor")
            self.win1.withdraw()
            l=Label(self.win4, text="Select a Course.")
            l.grid(row=0, column=0, sticky=E+W)
            l1=Label(self.win4, text="School Number")
            l1.grid(row=1, column=0, sticky=E+W)
            c=self.db.cursor()
            o=c.execute("SELECT * FROM COURSE")
            self.o=c.fetchall()
            self.count=1
            r=2
            self.iv6=IntVar()
            for i in self.o:
                co=str(i[1])+" "+str(i[0])
                rb="rb"+str(self.count)
                rb=Radiobutton(self.win4, text=co, value=self.count, variable=self.iv6)
                rb.grid(row=r, column=0, sticky=E+W)
                self.count=self.count+1
                r=r+1
            r=r+1
            b=Button(self.win4, text="Select Course", command=self.search1)
            b.grid(row=r, column=0, sticky=E+W)
            self.thisistherow=r
            r=r+1
            b1=Button(self.win4, text="Cancel", command=self.endsearch)
            b1.grid(row=r, column=0, sticky=E+W)
        
    def endsearch(self):
        self.win4.withdraw()
        self.Mainmenu()

    def search1(self):
        num=self.iv6.get()
        if num==0:
            messagebox.showinfo(message="Please select a course.")
        else:                
            nu=self.o[num][0]
            co=self.o[num][1]
            self.nu=nu
            self.co=co
            l2=Label(self.win4, text="Day  Time")
            l2.grid(row=0, column=1, sticky=E+W)
            # i only want for this semester ****
            c=self.db.cursor()
            j=c.execute("SELECT TIME, WEEKDAY FROM AVAILABLE_TIME_SLOTS WHERE SEMESTER=(%s)", self.semester())
            j=c.fetchall()
            self.Search=IntVar()
            count=1
            self.daytime=[]
            for i in j:
                day=i[1]
                time=i[0]
                rb="rbbb"+str(count)
                this=str(day)+" "+str(time)
                rb=Radiobutton(self.win4, text=this, value=count, variable=self.Search)
                rb.grid(row=count, column=1, columnspan=2, sticky=E+W)
                self.daytime.append([day, time, count])
                count=count+1
            l4=Label(self.win4, text="Tutor sessions can only be scheduled for one hour per week for a selected course.")
            l4.grid(row=count, column=1, sticky=E+W)
            count=count+1
            b5=Button(self.win4, text="Select Day and Time", command=self.search2)
            b5.grid(row=self.thisistherow, column=1, sticky=E+W)
        

    def search2(self):
        a=self.Search.get()
        if a==0:
            messagebox.showinfo(message="Please select a day and time.")
        else:
            c=self.db.cursor()
            #how do you do a view in python....?
            for i in self.daytime:
                if i[2]==a:
                    self.time=i[1]
                    self.weekday=i[0]
                    s=c.execute("SELECT STUDENT.FNAME, STUDENT.LNAME, STUDENT.EMAIL, AVG(RECOMMENDS.NUMERIC_E) AS Average_Prof_Rating, COUNT(DISTINCT RATES.NUMERIC_E) AS Number_Professors, AVG(RATES.NUMERIC_E) AS Average_Student_Rating, COUNT(RATES.NUMERIC_E) AS Number_Students, TUTOR.TUT_GTID FROM TUTOR INNER JOIN RECOMMENDS ON TUTOR.TUT_GTID= RECOMMENDS.TUT_GTID INNER JOIN STUDENT ON STUDENT.STUD_GTID=TUTOR.TUT_GTID LEFT JOIN RATES ON TUTOR.TUT_GTID=RATES.TUT_GTID INNER JOIN TUTORS ON TUTOR.TUT_GTID=TUTORS.TUT_GTID INNER JOIN AVAILABLE_TIME_SLOTS ON AVAILABLE_TIME_SLOTS.TUT_GTID=TUTOR.TUT_GTID WHERE (%s) IN (SELECT COURSE_NUM FROM COURSE WHERE SCHOOL=(%s)) AND (%s) IN (SELECT TIME FROM AVAILABLE_TIME_SLOTS WHERE WEEKDAY=(%s)) GROUP BY STUDENT.LNAME, STUDENT.FNAME ORDER BY Average_Student_Rating DESC",(str(self.nu),str(self.co),str(i[1]),str(i[0])))
                    s=c.fetchall()
                    print(s)
                    l=Label(self.win4, text="Available Tutors")
                    l.grid(column=4, row=0, sticky=E+W)
                    l1=Label(self.win4, text="Fname \t Lname \t Email \t Average_Prof_Rating \t Num_Professors \t Average Student Rating \t Number Students")
                    l1.grid(column=4, row=1, sticky=E+W)
                    count=2
                    self.search2=IntVar()
                    self.mydick={}
                    # s= ('Stud', 'ent', 'stud.ent', Decimal('1.0000'), 1, Decimal('1.0000'), 10, 1),
                    for i in s:
                        rb="rbbb"+str(count)
                        this=str(i[0])+" \t"+str(i[1])+" \t"+str(i[2])+" \t"+str(i[3])+" \t"+str(i[4])+" \t"+str(i[5])+"\t"+str(i[6])
                        rb=Radiobutton(self.win4,text=this, value=count, variable=self.search2)
                        rb.grid(row=count, column=4, columnspan=2, sticky=E+W)
                        self.mydick[count]=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]]
                        count=count+1
                    b=Button(self.win4, text="Select a Tutor", command=self.search3)
                    b.grid(row=count, column=4, sticky=E+W)

    def search3(self):
        if self.search2.get()==0:
            messagebox.showinfo("You have to select a tutor in order to schedule an appointment.")
        else:           
            s=self.semester()
            print(s)
            n=self.mydick[self.search2.get()]
            gtid=n[7]
            c=self.db.cursor()
            try:
                l=c.execute("INSERT INTO CHOOSES (UGRAD_GTID, SCHOOL, COURSE_NUM, TIME, WEEKDAY, SEMESTER, TUT_GTID) VALUES ((%s),(%s),(%s),(%s),(%s),(%s),(%s))",(str(self.iv.get()), str(self.co.get()), str(self.nu.get()), str(self.time.get()), str(self.weekday.get()), str(s), str(gtid)))
            except:
                messagebox.showinfo(message="Unfortuantely that particular time has already been taken for that particular tutor. Please Select a different time or tutor.")
        
        
    def apply(self):
        c=self.db.cursor()
        nn=c.execute("SELECT STUD_GTID FROM STUDENT")
        nn=c.fetchall()
        toned=[]
        self.win2=Toplevel()
        self.win2.title("Apply to be a Tutor")
        self.win1.withdraw()
        for i in nn:
            for y in i:
                toned.append(y)
        if self.iv.get() not in toned:
            messagebox.showinfo(title="None of your beeswax!", message="This function is only allowed for students.")
            self.win2.withdraw()
            self.Mainmenu()
        else:
            self.gtid=IntVar()
            self.fn=StringVar()
            self.ln=StringVar()
            self.email=StringVar()
            self.gpa=StringVar()
            self.telephone=IntVar()
            self.el=IntVar()
            l=Label(self.win2, text="Georgia Tech ID")
            l.grid(row=0, column=0, sticky=E+W)
            l1=Label(self.win2, text="First Name")
            l1.grid(row=1, column=0, sticky=E+W)
            l2=Label(self.win2, text="Last Name")
            l2.grid(row=2, column=0, sticky=E+W)
            l3=Label(self.win2, text="E-mail")
            l3.grid(row=3, column=0, sticky=E+W)
            l4=Label(self.win2, text="GPA")
            l4.grid(row=4, column=0, sticky=E+W)
            l5=Label(self.win2, text="Telephone Number")
            l5.grid(row=5, column=0, sticky=E+W)
            e=Entry(self.win2, textvariable=self.gtid)
            e.grid(row=0, column=1, sticky=E+W)
            e.delete(0, END)
            e1=Entry(self.win2, textvariable=self.fn)
            e1.grid(row=1, column=1, sticky=E+W)
            e2=Entry(self.win2, textvariable=self.ln)
            e2.grid(row=2, column=1, sticky=E+W)
            e3=Entry(self.win2, textvariable=self.email)
            e3.grid(row=3, column=1, sticky=E+W)
            e4=Entry(self.win2, textvariable=self.gpa)
            e4.grid(row=4, column=1, sticky=E+W)
            e5=Entry(self.win2, textvariable=self.telephone)
            e5.grid(row=5, column=1, sticky=E+W)
            e5.delete(0, END)
            rb=Radiobutton(self.win2, text="Undergraduate", variable=self.el, value=1)
            rb.grid(row=6, column=0, sticky=E+W)
            rb1=Radiobutton(self.win2, text="Graduate", variable=self.el, value=2)
            rb1.grid(row=7, column=0, sticky=E+W)
            b=Button(self.win2, text="Okay", command=self.insertApp)
            b.grid(row=9, column=1, sticky=E+W)
            b1=Button(self.win2, text="Cancel", command=self.cancel)
            b1.grid(row=9, column=0, sticky=E+W) 

    def insertApp(self):
        #check you can insert info
        if self.gtid.get()==0 and self.fn.get()=="" and self.ln.get()=="" and self.email.get()=="" and self.gpa.get()=="" and self.tn.get()==0 and self.el.get()==0:
            messagebox.showinfo(message="Yikes! You didn't fill in all the entry boxes.")
        gtid=self.gtid.get()
        fn=self.fn.get
        ln=self.ln.get()
        email=self.email.get()
        gpa=self.gpa.get()
        tn=self.telephone.get()
        el=self.el.get()
        if gtid!=self.iv.get():
            messagebox.showinfo(message="An individual cannot apply for another individual.")
        c=self.db.cursor()
        st=c.execute("SELECT STUD_GTID FROM STUDENT")
        st=c.fetchall()
        alist=[]
        for i in st:
            for q in i:
                alist.append(q)
        if gtid not in alist:
            messagebox.showinfo(message="You are not a student and are not elligible to apply to be a tutor.")
            self.killthiswin()
        tu=c.execute("SELECT TUT_GTID FROM TUTOR")
        tu=c.fetchall()
        if gtid in tu:
            messagebox.showinfo(message="You are already a tutor! Congrats!")
            self.killthiswin()
        if float(gpa)<3.0:
            messagebox.showinfo(title="You are subpar...", message="Your GPA does not meet the 3.0 minimum.")
        try:
            i=c.execute("INSERT INTO TUTOR (TUT_GTID, TELEPHONE, GPA) VALUES ((%s), (%s), (%s))", (str(gtid), str(tn), str(gpa))) 
            if self.el.get()==2:
                p=c.execute("INSERT INTO GRAD (GRAD_GTID) VALUES (%s)", str(gtid))
                self.win2.withdraw()
                self.win3=Toplevel()
                self.win3.title("Graduate TA")
                c=self.db.cursor()
                courses=c.execute("SELECT * FROM COURSE")
                courses=c.fetchall()
                l=Label(self.win3, text="Select the School and Course that you want to tutor.")
                l.grid(row=0, column=0, sticky=E+W)
                self.meg=IntVar()
                self.csg=IntVar()
                self.mathg=IntVar()
                self.ieg=IntVar()
                self.cssg=IntVar()
                self.musig=IntVar()
                self.MEG=IntVar()
                self.CSG=IntVar()
                self.MATHG=IntVar()
                self.IEG=IntVar()
                self.CSSG=IntVar()
                self.MUSIG=IntVar()
                rb=Radiobutton(self.win3, text="ME 2110", variable=self.meg, value=1)
                rb.grid(row=1, column=0, sticky=E+W)
                rb=Radiobutton(self.win3, text="CS 2200", variable=self.csg, value=2)
                rb.grid(row=2, column=0, sticky=E+W)
                rb=Radiobutton(self.win3, text="MATH 3012", variable=self.mathg, value=3)
                rb.grid(row=3, column=0, sticky=E+W)
                rb=Radiobutton(self.win3, text="IE 3232", variable=self.ieg, value=4)
                rb.grid(row=4, column=0, sticky=E+W)
                rb=Radiobutton(self.win3, text="CS 4400", variable=self.cssg, value=5)
                rb.grid(row=5, column=0, sticky=E+W)
                rb=Radiobutton(self.win3, text="MUSI 4630", variable=self.musig, value=6)
                rb.grid(row=6, column=0, sticky=E+W)
                l2=Label(self.win3, text="Select the School and Course that you have been a GTA for in the past.")
                l2.grid(row=0, column=1, sticky=E+W)
                rb=Radiobutton(self.win3, text="ME 2110", variable=self.MEG, value=1)
                rb.grid(row=1, column=1, sticky=E+W)
                rb=Radiobutton(self.win3, text="CS 2200", variable=self.CSG, value=2)
                rb.grid(row=2, column=1, sticky=E+W)
                rb=Radiobutton(self.win3, text="MATH 3012", variable=self.MATHG, value=3)
                rb.grid(row=3, column=1, sticky=E+W)
                rb=Radiobutton(self.win3, text="IE 3232", variable=self.IEG, value=4)
                rb.grid(row=4, column=1, sticky=E+W)
                rb=Radiobutton(self.win3, text="CS 4400", variable=self.CSSG, value=5)
                rb.grid(row=5, column=1, sticky=E+W)
                rb=Radiobutton(self.win3, text="MUSI 4630", variable=self.MUSIG, value=6)
                rb.grid(row=6, column=1, sticky=E+W)
                b=Button(self.win3, text="Select", command=self.destinyschild)
                b.grid(row=7, column=0, sticky=E+W)
                
            if self.el.get()==1:
                tt=c.execute("INSERT INTO UNDERGRAD (UGRAD_GTID) VALUES (%s)", str(gtid))
                self.win2.withdraw()
                self.win3=Toplevel()
                self.win3.title("Undergraduate TA")
                c=self.db.cursor()
                courses=c.execute("SELECT * FROM COURSE")
                courses=c.fetchall()
                l=Label(self.win3, text="Select the School and Course you can tutor.")
                l.grid(row=0, column=0, sticky=E+W)
                #((2110, 'ME'), (2200, 'CS'), (3012, 'MATH'), (3232, 'IE'), (4400, 'CS'), (4630, 'MUSI'))
                self.meg=IntVar()
                self.csg=IntVar()
                self.mathg=IntVar()
                self.ieg=IntVar()
                self.cssg=IntVar()
                self.musig=IntVar()
                rb=Radiobutton(self.win3, text="ME 2110", variable=self.meg, value=1)
                rb.grid(row=1, column=0, sticky=E+W)
                rb=Radiobutton(self.win3, text="CS 2200", variable=self.csg, value=2)
                rb.grid(row=2, column=0, sticky=E+W)
                rb=Radiobutton(self.win3, text="MATH 3012", variable=self.mathg, value=3)
                rb.grid(row=3, column=0, sticky=E+W)
                rb=Radiobutton(self.win3, text="IE 3232", variable=self.ieg, value=4)
                rb.grid(row=4, column=0, sticky=E+W)
                rb=Radiobutton(self.win3, text="CS 4400", variable=self.cssg, value=5)
                rb.grid(row=5, column=0, sticky=E+W)
                rb=Radiobutton(self.win3, text="MUSI 4630", variable=self.musig, value=6)
                rb.grid(row=6, column=0, sticky=E+W)
                b=Button(self.win3, text="Select", command=self.beyonce)
                b.grid(row=7, column=0, sticky=E+W)
        except:
            messagebox.showinfo(title="Oh no!", message="You can only apply to be a tutor once!")
            self.killthiswin()
            
    def beyonce(self):
        c=self.db.cursor()
        if self.meg.get()==1:
            a=c.execute("INSERT INTO TUTORS (TUT_GTID, SCHOOL, COURSE_NUM, GTA) VALUES ((%s),(%s),(%s),(%s))",(str(self.iv.get()), "ME", "2110", str(0)))
        if self.csg.get()==2:
            a=c.execute("INSERT INTO TUTORS (TUT_GTID, SCHOOL, COURSE_NUM, GTA) VALUES ((%s),(%s),(%s),(%s))",(str(self.iv.get()), "CS", "2200", str(0)))
        if self.mathg.get()==3:
            a=c.execute("INSERT INTO TUTORS (TUT_GTID, SCHOOL, COURSE_NUM, GTA) VALUES ((%s),(%s),(%s),(%s))",(str(self.iv.get()), "MATH", "3012", str(0)))
        if self.ieg.get()==4:
            a=c.execute("INSERT INTO TUTORS (TUT_GTID, SCHOOL, COURSE_NUM, GTA) VALUES ((%s),(%s),(%s),(%s))",(str(self.iv.get()), "IE", "3232", str(0)))        
        if self.cssg.get()==5:
            a=c.execute("INSERT INTO TUTORS (TUT_GTID, SCHOOL, COURSE_NUM, GTA) VALUES ((%s),(%s),(%s),(%s))",(str(self.iv.get()), "CS", "4400", str(0)))
        if self.musig.get()==6:
            a=c.execute("INSERT INTO TUTORS (TUT_GTID, SCHOOL, COURSE_NUM, GTA) VALUES ((%s),(%s),(%s),(%s))",(str(self.iv.get()), "MUSI", "4630", str(0)))
        if self.meg.get()==0 and self.csg.get()==0 and self.mathg.get()==0 and self.ieg.get()==0 and self.cssg.get()==0 and self.musig.get()==0:
            messagebox.showinfo(title="Oh no you didn't!", message="You have to select at least one course you can tutor.")
        self.insertapp2()


    def destinyschild(self):
        c=self.db.cursor()
        if self.meg.get()==1 and self.MEG.get()==0:
            a=c.execute("INSERT INTO TUTORS (TUT_GTID, SCHOOL, COURSE_NUM, GTA) VALUES ((%s),(%s),(%s),(%s))",(str(self.iv.get()), "ME", "2110", str(0)))
        if self.meg.get()==1 and self.MEG.get()==1:
            a=c.execute("INSERT INTO TUTORS (TUT_GTID, SCHOOL, COURSE_NUM, GTA) VALUES ((%s),(%s),(%s),(%s))",(str(self.iv.get()), "ME", "2110", str(1)))
        if self.csg.get()==2 and self.CSG.get()==0:
            a=c.execute("INSERT INTO TUTORS (TUT_GTID, SCHOOL, COURSE_NUM, GTA) VALUES ((%s),(%s),(%s),(%s))",(str(self.iv.get()), "CS", "2200", str(0)))
        if self.csg.get()==2 and self.CSG.get()==2:
            a=c.execute("INSERT INTO TUTORS (TUT_GTID, SCHOOL, COURSE_NUM, GTA) VALUES ((%s),(%s),(%s),(%s))",(str(self.iv.get()), "CS", "2200", str(1)))
        if self.mathg.get()==3 and self.MATHG.get()==0:
            a=c.execute("INSERT INTO TUTORS (TUT_GTID, SCHOOL, COURSE_NUM, GTA) VALUES ((%s),(%s),(%s),(%s))",(str(self.iv.get()), "MATH", "3012", str(0)))
        if self.mathg.get()==3 and self.MATHG.get()==3:
            a=c.execute("INSERT INTO TUTORS (TUT_GTID, SCHOOL, COURSE_NUM, GTA) VALUES ((%s),(%s),(%s),(%s))",(str(self.iv.get()), "MATH", "3012", str(1)))
        if self.ieg.get()==4 and self.IEG.get()==0:
            a=c.execute("INSERT INTO TUTORS (TUT_GTID, SCHOOL, COURSE_NUM, GTA) VALUES ((%s),(%s),(%s),(%s))",(str(self.iv.get()), "IE", "3232", str(0)))
        if self.ieg.get()==4 and self.IEG.get()==4:
            a=c.execute("INSERT INTO TUTORS (TUT_GTID, SCHOOL, COURSE_NUM, GTA) VALUES ((%s),(%s),(%s),(%s))",(str(self.iv.get()), "IE", "3232", str(1)))  
        if self.cssg.get()==5 and self.CSSG.get()==0:
            a=c.execute("INSERT INTO TUTORS (TUT_GTID, SCHOOL, COURSE_NUM, GTA) VALUES ((%s),(%s),(%s),(%s))",(str(self.iv.get()), "CS", "4400", str(0)))
        if self.cssg.get()==5 and self.CSSG.get()==5:
            a=c.execute("INSERT INTO TUTORS (TUT_GTID, SCHOOL, COURSE_NUM, GTA) VALUES ((%s),(%s),(%s),(%s))",(str(self.iv.get()), "CS", "4400", str(1)))
        if self.musig.get()==6 and self.MUSIG.get()==0:
            a=c.execute("INSERT INTO TUTORS (TUT_GTID, SCHOOL, COURSE_NUM, GTA) VALUES ((%s),(%s),(%s),(%s))",(str(self.iv.get()), "MUSI", "4630", str(0)))
        if self.musig.get()==6 and self.MUSIG.get()==6:
            a=c.execute("INSERT INTO TUTORS (TUT_GTID, SCHOOL, COURSE_NUM, GTA) VALUES ((%s),(%s),(%s),(%s))",(str(self.iv.get()), "MUSI", "4630", str(1)))
        if self.meg.get()==0 and self.csg.get()==0 and self.mathg.get()==0 and self.ieg.get()==0 and self.cssg.get()==0 and self.musig.get()==0:
            messagebox.showinfo(title="Oh no you didn't!", message="You have to select at least one course you can tutor.")
        self.insertapp2()
        
    def killthiswin(self):
        self.win2.withdraw()
        self.Mainmenu()

    def insertapp2(self):
        self.win3.withdraw()
        c=self.db.cursor()
        self.win2.withdraw()
        self.win6=Toplevel()
        self.win6.title("Available Days/Times")
        l=Label(self.win6, text="Monday")
        l.grid(column=0, row=0, sticky=E+W)
        l1=Label(self.win6, text="Tuesday")
        l1.grid(column=0, row=2, sticky=E+W)
        l2=Label(self.win6, text="Wednesday")
        l2.grid(column=0, row=4, sticky=E+W)
        l3=Label(self.win6, text="Thursday")
        l3.grid(column=0, row=6, sticky=E+W)
        l4=Label(self.win6, text="Friday")
        l4.grid(column=0, row=8, sticky=E+W)
        self.m9=IntVar()
        self.m10=IntVar()
        self.m11=IntVar()
        self.m12=IntVar()
        self.m1=IntVar()
        self.m2=IntVar()
        self.m3=IntVar()
        self.m4=IntVar()
        self.t9=IntVar()
        self.t10=IntVar()
        self.t11=IntVar()
        self.t12=IntVar()
        self.t1=IntVar()
        self.t2=IntVar()
        self.t3=IntVar()
        self.t4=IntVar()
        self.w9=IntVar()
        self.w10=IntVar()
        self.w11=IntVar()
        self.w12=IntVar()
        self.w1=IntVar()
        self.w2=IntVar()
        self.w3=IntVar()
        self.w4=IntVar()
        self.th9=IntVar()
        self.th10=IntVar()
        self.th11=IntVar()
        self.th12=IntVar()
        self.th1=IntVar()
        self.th2=IntVar()
        self.th3=IntVar()
        self.th4=IntVar()
        self.f9=IntVar()
        self.f10=IntVar()
        self.f11=IntVar()
        self.f12=IntVar()
        self.f1=IntVar()
        self.f2=IntVar()
        self.f3=IntVar()
        self.f4=IntVar()
        #Checkbutton( onvalue= offvalue=
        #in case you have to height width
        rb=Radiobutton(self.win6, text="9am", value=1, variable=self.m9)
        rb.grid(column=0, row=1, sticky=E+W)
        rb1=Radiobutton(self.win6, text="10am", value=2, variable=self.m10)
        rb1.grid(column=1, row=1, sticky=E+W)
        rb2=Radiobutton(self.win6, text="11am", value=3, variable=self.m11)
        rb2.grid(column=2, row=1, sticky=E+W)
        rb3=Radiobutton(self.win6, text="12pm", value=4, variable=self.m12)
        rb3.grid(column=3, row=1, sticky=E+W)
        rb4=Radiobutton(self.win6, text="1pm", value=5, variable=self.m1)
        rb4.grid(column=4, row=1, sticky=E+W)
        rb5=Radiobutton(self.win6, text="2pm", value=6, variable=self.m2)
        rb5.grid(column=5, row=1, sticky=E+W)
        rb6=Radiobutton(self.win6, text="3pm", value=7, variable=self.m3)
        rb6.grid(column=6, row=1, sticky=E+W)
        rb7=Radiobutton(self.win6, text="4pm", value=8, variable=self.m4)
        rb7.grid(column=7, row=1, sticky=E+W)
        rb8=Radiobutton(self.win6, text="9am", value=9, variable=self.t9)
        rb8.grid(column=0, row=3, sticky=E+W)
        rb9=Radiobutton(self.win6, text="10am", value=10, variable=self.t10)
        rb9.grid(column=1, row=3, sticky=E+W)
        rb10=Radiobutton(self.win6, text="11am", value=11, variable=self.t11)
        rb10.grid(column=2, row=3, sticky=E+W)
        rb11=Radiobutton(self.win6, text="12pm", value=12, variable=self.t12)
        rb11.grid(column=3, row=3, sticky=E+W)
        rb12=Radiobutton(self.win6, text="1pm", value=13, variable=self.t1)
        rb12.grid(column=4, row=3, sticky=E+W)
        rb13=Radiobutton(self.win6, text="2pm", value=14, variable=self.t2)
        rb13.grid(column=5, row=3, sticky=E+W)
        rb14=Radiobutton(self.win6, text="3pm", value=15, variable=self.t3)
        rb14.grid(column=6, row=3, sticky=E+W)
        rb15=Radiobutton(self.win6, text="4pm", value=16, variable=self.t4)
        rb15.grid(column=7, row=3, sticky=E+W)
        rb16=Radiobutton(self.win6, text="9am", value=17, variable=self.w9)
        rb16.grid(column=0, row=5, sticky=E+W)
        rb17=Radiobutton(self.win6, text="10am", value=18, variable=self.w10)
        rb17.grid(column=1, row=5, sticky=E+W)
        rb18=Radiobutton(self.win6, text="11am", value=19, variable=self.w11)
        rb18.grid(column=2, row=5, sticky=E+W)
        rb19=Radiobutton(self.win6, text="12pm", value=20, variable=self.w12)
        rb19.grid(column=3, row=5, sticky=E+W)
        rb20=Radiobutton(self.win6, text="1pm", value=21, variable=self.w1)
        rb20.grid(column=4, row=5, sticky=E+W)
        rb21=Radiobutton(self.win6, text="2pm", value=22, variable=self.w2)
        rb21.grid(column=5, row=5, sticky=E+W)
        rb22=Radiobutton(self.win6, text="3pm", value=23, variable=self.w3)
        rb22.grid(column=6, row=5, sticky=E+W)
        rb23=Radiobutton(self.win6, text="4pm", value=24, variable=self.w4)
        rb23.grid(column=7, row=5, sticky=E+W)
        rb24=Radiobutton(self.win6, text="9am", value=25, variable=self.th9)
        rb24.grid(column=0, row=7, sticky=E+W)
        rb25=Radiobutton(self.win6, text="10am", value=26, variable=self.th10)
        rb25.grid(column=1, row=7, sticky=E+W)
        rb26=Radiobutton(self.win6, text="11am", value=27, variable=self.th11)
        rb26.grid(column=2, row=7, sticky=E+W)
        rb27=Radiobutton(self.win6, text="12pm", value=28, variable=self.th12)
        rb27.grid(column=3, row=7, sticky=E+W)
        rb28=Radiobutton(self.win6, text="1pm", value=29, variable=self.th1)
        rb28.grid(column=4, row=7, sticky=E+W)
        rb29=Radiobutton(self.win6, text="2pm", value=30, variable=self.th2)
        rb29.grid(column=5, row=7, sticky=E+W)
        rb30=Radiobutton(self.win6, text="3pm", value=31, variable=self.th3)
        rb30.grid(column=6, row=7, sticky=E+W)
        rb31=Radiobutton(self.win6, text="4pm", value=32, variable=self.th4)
        rb31.grid(column=7, row=7, sticky=E+W)
        rb32=Radiobutton(self.win6, text="9am", value=33, variable=self.f9)
        rb32.grid(column=0, row=9, sticky=E+W)
        rb33=Radiobutton(self.win6, text="10am", value=34, variable=self.f10)
        rb33.grid(column=1, row=9, sticky=E+W)
        rb34=Radiobutton(self.win6, text="11am", value=35, variable=self.f11)
        rb34.grid(column=2, row=9, sticky=E+W)
        rb35=Radiobutton(self.win6, text="12pm", value=36, variable=self.f12)
        rb35.grid(column=3, row=9, sticky=E+W)
        rb36=Radiobutton(self.win6, text="1pm", value=37, variable=self.f1)
        rb36.grid(column=4, row=9, sticky=E+W)
        rb37=Radiobutton(self.win6, text="2pm", value=38, variable=self.f2)
        rb37.grid(column=5, row=9, sticky=E+W)
        rb38=Radiobutton(self.win6, text="3pm", value=39, variable=self.f3)
        rb38.grid(column=6, row=9, sticky=E+W)
        rb39=Radiobutton(self.win6, text="4pm", value=40, variable=self.f4)
        rb39.grid(column=7, row=9, sticky=E+W)
        b=Button(self.win6, text="Select", command=self.insertapp3)
        b.grid(row=10, column=0, sticky=E+W)
        b1=Button(self.win6, text="Unselect All", command=self.unselect)
        b1.grid(row=10, column=1, sticky=E+W)

    def unselect(self):
        self.m9.set(0)
        self.m10.set(0)
        self.m11.set(0)
        self.m12.set(0)
        self.m1.set(0)
        self.m2.set(0)
        self.m3.set(0)
        self.m4.set(0)
        self.t9.set(0)
        self.t10.set(0)
        self.t11.set(0)
        self.t12.set(0)
        self.t1.set(0)
        self.t2.set(0)
        self.t3.set(0)
        self.t4.set(0)
        self.w9.set(0)
        self.w10.set(0)
        self.w11.set(0)
        self.w12.set(0)
        self.w1.set(0)
        self.w2.set(0)
        self.w3.set(0)
        self.w4.set(0)
        self.th9.set(0)
        self.th10.set(0)
        self.th11.set(0)
        self.th12.set(0)
        self.th1.set(0)
        self.th2.set(0)
        self.th3.set(0)
        self.th4.set(0)
        self.f9.set(0)
        self.f10.set(0)
        self.f11.set(0)
        self.f12.set(0)
        self.f1.set(0)
        self.f2.set(0)
        self.f3.set(0)
        self.f4.set(0)

    def insertapp3(self):
        c=self.db.cursor()
        adict={1: 'self.m9.get()', 2: 'self.m10.get()', 3: 'self.m11.get()', 4: 'self.m12.get()', 5: 'self.m1.get()', 6: 'self.m2.get()', 7: 'self.m3.get()', 8: 'self.m4.get()', 9: 'self.t9.get()', 10: 'self.t10.get()', 11: 'self.t11.get()', 12: 'self.t12.get()', 13: 'self.t1.get()', 14: 'self.t2.get()', 15: 'self.t3.get()', 16: 'self.t4.get()', 17: 'self.w9.get()', 18: 'self.w10.get()', 19: 'self.w11.get()', 20: 'self.w12.get()', 21: 'self.w1.get()', 22: 'self.w2.get()', 23: 'self.w3.get()', 24: 'self.w4.get()', 25: 'self.th9.get()', 26: 'self.th10.get()', 27: 'self.th11.get()', 28: 'self.th12.get()', 29: 'self.th1.get()', 30: 'self.th2.get()', 31: 'self.th3.get()', 32: 'self.th4.get()', 33: 'self.f9.get()', 34: 'self.f10.get()', 35: 'self.f11.get()', 36: 'self.f12.get()', 37: 'self.f1.get()', 38: 'self.f2.get()', 39: 'self.f3.get()', 40: 'self.f4.get()'}
        if self.m9.get()==1:
            a1=c.execute("INSERT INTO AVAILABLE_TIME_SLOTS (TIME, SEMESTER, WEEKDAY, TUT_GTID) VALUES ((%s),(%s),(%s),(%s))",( "9:00:00",self.semester(), "M",str(self.iv.get())))
        if self.m10.get()==2:
                 a2=c.execute("INSERT INTO AVAILABLE_TIME_SLOTS (TIME, SEMESTER, WEEKDAY, TUT_GTID) VALUES ((%s),(%s),(%s),(%s))",( "10:00:00",self.semester(), "M",str(self.iv.get())))
        if self.m11.get()==3:
                 a3=c.execute("INSERT INTO AVAILABLE_TIME_SLOTS (TIME, SEMESTER, WEEKDAY, TUT_GTID) VALUES ((%s),(%s),(%s),(%s))",( "11:00:00",self.semester(), "M",str(self.iv.get())))
        if self.m12.get()==4:
                 a4=c.execute("INSERT INTO AVAILABLE_TIME_SLOTS (TIME, SEMESTER, WEEKDAY, TUT_GTID) VALUES ((%s),(%s),(%s),(%s))", ("12:00:00",self.semester(), "M",str(self.iv.get())))
        if self.m1.get()==5:
                 a5=c.execute("INSERT INTO AVAILABLE_TIME_SLOTS (TIME, SEMESTER, WEEKDAY, TUT_GTID) VALUES ((%s),(%s),(%s),(%s))",( "13:00:00",self.semester(), "M",str(self.iv.get())))
        if self.m2.get()==6:
                 a6=c.execute("INSERT INTO AVAILABLE_TIME_SLOTS (TIME, SEMESTER, WEEKDAY, TUT_GTID) VALUES ((%s),(%s),(%s),(%s))", ("14:00:00",self.semester(), "M",str(self.iv.get())))
        if self.m3.get()==7:
                 a7=c.execute("INSERT INTO AVAILABLE_TIME_SLOTS (TIME, SEMESTER, WEEKDAY, TUT_GTID) VALUES ((%s),(%s),(%s),(%s))", ("15:00:00",self.semester(), "M",str(self.iv.get())))
        if self.m4.get()==8:
                 a8=c.execute("INSERT INTO AVAILABLE_TIME_SLOTS (TIME, SEMESTER, WEEKDAY, TUT_GTID) VALUES ((%s),(%s),(%s),(%s))", ("16:00:00",self.semester(), "M",str(self.iv.get())))
        if self.t9.get()==9:
                 a9=c.execute("INSERT INTO AVAILABLE_TIME_SLOTS (TIME, SEMESTER, WEEKDAY, TUT_GTID) VALUES ((%s),(%s),(%s),(%s))", ("9:00:00",self.semester(), "T",str(self.iv.get())))
        if self.t10.get()==10:
                 a10=c.execute("INSERT INTO AVAILABLE_TIME_SLOTS (TIME, SEMESTER, WEEKDAY, TUT_GTID) VALUES ((%s),(%s),(%s),(%s))", ("10:00:00",self.semester(), "T",str(self.iv.get())))
        if self.t11.get()==11:
                 a11=c.execute("INSERT INTO AVAILABLE_TIME_SLOTS (TIME, SEMESTER, WEEKDAY, TUT_GTID) VALUES ((%s),(%s),(%s),(%s))", ("11:00:00",self.semester(), "T",str(self.iv.get())))
        if self.t12.get()==12:
                 a12=c.execute("INSERT INTO AVAILABLE_TIME_SLOTS (TIME, SEMESTER, WEEKDAY, TUT_GTID) VALUES ((%s),(%s),(%s),(%s))", ("12:00:00",self.semester(), "T",str(self.iv.get())))
        if self.t1.get()==13:
                 a13=c.execute("INSERT INTO AVAILABLE_TIME_SLOTS (TIME, SEMESTER, WEEKDAY, TUT_GTID) VALUES ((%s),(%s),(%s),(%s))", ("13:00:00",self.semester(), "T",str(self.iv.get())))
        if self.t2.get()==14:
                 a14=c.execute("INSERT INTO AVAILABLE_TIME_SLOTS (TIME, SEMESTER, WEEKDAY, TUT_GTID) VALUES ((%s),(%s),(%s),(%s))",( "14:00:00",self.semester(), "T",str(self.iv.get())))
        if self.t3.get()==15:
                 a15=c.execute("INSERT INTO AVAILABLE_TIME_SLOTS (TIME, SEMESTER, WEEKDAY, TUT_GTID) VALUES ((%s),(%s),(%s),(%s))", ("15:00:00",self.semester(), "T",str(self.iv.get())))
        if self.t4.get()==16:
                 a16=c.execute("INSERT INTO AVAILABLE_TIME_SLOTS (TIME, SEMESTER, WEEKDAY, TUT_GTID) VALUES ((%s),(%s),(%s),(%s))", ("16:00:00",self.semester(), "T",str(self.iv.get())))
        if self.w9.get()==17:
                 a17=c.execute("INSERT INTO AVAILABLE_TIME_SLOTS (TIME, SEMESTER, WEEKDAY, TUT_GTID) VALUES ((%s),(%s),(%s),(%s))", ("9:00:00",self.semester(), "W",str(self.iv.get())))
        if self.w10.get()==18:
                 a18=c.execute("INSERT INTO AVAILABLE_TIME_SLOTS (TIME, SEMESTER, WEEKDAY, TUT_GTID) VALUES ((%s),(%s),(%s),(%s))",( "10:00:00",self.semester(), "W",str(self.iv.get())))
        if self.w11.get()==19:
                 a19=c.execute("INSERT INTO AVAILABLE_TIME_SLOTS (TIME, SEMESTER, WEEKDAY, TUT_GTID) VALUES ((%s),(%s),(%s),(%s))",( "11:00:00",self.semester(), "W",str(self.iv.get())))
        if self.w12.get()==20:
                 a20=c.execute("INSERT INTO AVAILABLE_TIME_SLOTS (TIME, SEMESTER, WEEKDAY, TUT_GTID) VALUES ((%s),(%s),(%s),(%s))", ("12:00:00",self.semester(), "W",str(self.iv.get())))
        if self.w1.get()==21:
                 a21=c.execute("INSERT INTO AVAILABLE_TIME_SLOTS (TIME, SEMESTER, WEEKDAY, TUT_GTID) VALUES ((%s),(%s),(%s),(%s))", ("13:00:00",self.semester(), "W",str(self.iv.get())))
        if self.w2.get()==22:
                 a22=c.execute("INSERT INTO AVAILABLE_TIME_SLOTS (TIME, SEMESTER, WEEKDAY, TUT_GTID) VALUES ((%s),(%s),(%s),(%s))", ("14:00:00",self.semester(), "W",str(self.iv.get())))
        if self.w3.get()==23:
                 a23=c.execute("INSERT INTO AVAILABLE_TIME_SLOTS (TIME, SEMESTER, WEEKDAY, TUT_GTID) VALUES ((%s),(%s),(%s),(%s))", ("15:00:00",self.semester(), "W",str(self.iv.get())))
        if self.w4.get()==24:
                 a24=c.execute("INSERT INTO AVAILABLE_TIME_SLOTS (TIME, SEMESTER, WEEKDAY, TUT_GTID) VALUES ((%s),(%s),(%s),(%s))", ("16:00:00",self.semester(), "W",str(self.iv.get())))
        if self.th9.get()==25:
                 a25=c.execute("INSERT INTO AVAILABLE_TIME_SLOTS (TIME, SEMESTER, WEEKDAY, TUT_GTID) VALUES ((%s),(%s),(%s),(%s))", ("9:00:00",self.semester(), "Th",str(self.iv.get())))
        if self.th10.get()==26:
                 a26=c.execute("INSERT INTO AVAILABLE_TIME_SLOTS (TIME, SEMESTER, WEEKDAY, TUT_GTID) VALUES ((%s),(%s),(%s),(%s))", ("10:00:00",self.semester(), "Th",str(self.iv.get())))
        if self.th11.get()==27:
                 a27=c.execute("INSERT INTO AVAILABLE_TIME_SLOTS (TIME, SEMESTER, WEEKDAY, TUT_GTID) VALUES ((%s),(%s),(%s),(%s))", ("11:00:00",self.semester(), "Th",str(self.iv.get())))
        if self.th12.get()==28:
                 a28=c.execute("INSERT INTO AVAILABLE_TIME_SLOTS (TIME, SEMESTER, WEEKDAY, TUT_GTID) VALUES ((%s),(%s),(%s),(%s))", ("12:00:00",self.semester(), "Th",str(self.iv.get())))
        if self.th1.get()==29:
                 a29=c.execute("INSERT INTO AVAILABLE_TIME_SLOTS (TIME, SEMESTER, WEEKDAY, TUT_GTID) VALUES ((%s),(%s),(%s),(%s))", ("13:00:00",self.semester(), "Th",str(self.iv.get())))
        if self.th2.get()==30:
                 a30=c.execute("INSERT INTO AVAILABLE_TIME_SLOTS (TIME, SEMESTER, WEEKDAY, TUT_GTID) VALUES ((%s),(%s),(%s),(%s))", ("14:00:00",self.semester(), "Th",str(self.iv.get())))
        if self.th3.get()==31:
                 a31=c.execute("INSERT INTO AVAILABLE_TIME_SLOTS (TIME, SEMESTER, WEEKDAY, TUT_GTID) VALUES ((%s),(%s),(%s),(%s))", ("15:00:00",self.semester(), "Th",str(self.iv.get())))
        if self.th4.get()==32:
                 a32=c.execute("INSERT INTO AVAILABLE_TIME_SLOTS (TIME, SEMESTER, WEEKDAY, TUT_GTID) VALUES ((%s),(%s),(%s),(%s))", ("16:00:00",self.semester(), "Th",str(self.iv.get())))
        if self.f9.get()==33:
                 a33=c.execute("INSERT INTO AVAILABLE_TIME_SLOTS (TIME, SEMESTER, WEEKDAY, TUT_GTID) VALUES ((%s),(%s),(%s),(%s))", ("9:00:00",self.semester(), "F",str(self.iv.get())))
        if self.f10.get()==34:
                 a34=c.execute("INSERT INTO AVAILABLE_TIME_SLOTS (TIME, SEMESTER, WEEKDAY, TUT_GTID) VALUES ((%s),(%s),(%s),(%s))", ("10:00:00",self.semester(), "F",str(self.iv.get())))
        if self.f11.get()==35:
                 a35=c.execute("INSERT INTO AVAILABLE_TIME_SLOTS (TIME, SEMESTER, WEEKDAY, TUT_GTID) VALUES ((%s),(%s),(%s),(%s))",( "11:00:00",self.semester(), "F",str(self.iv.get())))
        if self.f12.get()==36:
                 a36=c.execute("INSERT INTO AVAILABLE_TIME_SLOTS (TIME, SEMESTER, WEEKDAY, TUT_GTID) VALUES ((%s),(%s),(%s),(%s))", ("12:00:00",self.semester(), "F",str(self.iv.get())))
        if self.f1.get()==37:
                 a37=c.execute("INSERT INTO AVAILABLE_TIME_SLOTS (TIME, SEMESTER, WEEKDAY, TUT_GTID) VALUES ((%s),(%s),(%s),(%s))",( "13:00:00",self.semester(), "F",str(self.iv.get())))
        if self.f2.get()==38:
                 a38=c.execute("INSERT INTO AVAILABLE_TIME_SLOTS (TIME, SEMESTER, WEEKDAY, TUT_GTID) VALUES ((%s),(%s),(%s),(%s))", ("14:00:00",self.semester(), "F",str(self.iv.get())))
        if self.f3.get()==39:
                 a39=c.execute("INSERT INTO AVAILABLE_TIME_SLOTS (TIME, SEMESTER, WEEKDAY, TUT_GTID) VALUES ((%s),(%s),(%s),(%s))", ("15:00:00",self.semester(), "F",str(self.iv.get())))
        if self.f4.get()==40:
                 a40=c.execute("INSERT INTO AVAILABLE_TIME_SLOTS (TIME, SEMESTER, WEEKDAY, TUT_GTID) VALUES ((%s),(%s),(%s),(%s))", ("16:00:00",self.semester(), "F",str(self.iv.get())))
        self.win6.withdraw()
        self.Mainmenu()

    def cancel(self):
        self.win2.withdraw()
        self.Mainmenu()

    def rate(self):
        self.win1.withdraw()
        self.win5=Toplevel()
        self.win5.title("Rate a Tutor") 
        c=self.db.cursor()
        j=c.execute("SELECT * FROM UNDERGRAD")
        j=c.fetchall()
        alist=[]
        for i in j:
            for q in i:
                alist.append(q)
        if self.iv.get() not in alist:
            messagebox.showinfo(message="You must be a undergraduate student to rate a tutor.")
        o=c.execute("SELECT COURSE_NUM, SCHOOL FROM CHOOSES WHERE UGRAD_GTID=(%s)", self.iv.get())
        self.o=c.fetchall()
        blist=[]
        for i in self.o:
            for q in i:
                blist.append(q)       
        if len(blist)==0:
            messagebox.showinfo(message="You have not had a tutoring session yet and therefore can't rate a tutor.")
            self.win5.withdraw()
            self.Mainmenu()
        self.count=1
        r=1
        self.iv6=IntVar()
        l=Label(self.win5, text="Course")
        l.grid(row=0, column=0, sticky=E+W) 
        for i in self.o:
            co=str(i[1])+" "+str(i[0])
            rb="rb"+str(self.count)
            rb=Radiobutton(self.win5, text=co, value=self.count, variable=self.iv6)
            rb.grid(row=r, column=0, sticky=E+W)
            self.count=self.count+1
            r=r+1
        r=r+1
        b=Button(self.win5, text="Select Course", command=self.rate1)
        b.grid(column=0, row=r, sticky=E+W)
        self.r=r+1
        b1=Button(self.win5, text="Cancel", command=self.cancel1)
        b1.grid(column=0, row=self.r, sticky=E+W)
        self.r=r+1

    def cancel1(self):
        self.win5.withdraw()
        self.Mainmenu()
        
    def rate1(self):
        position=int(self.iv6.get())-1
        co=self.o[position][1]
        num=self.o[position][0]
        c=self.db.cursor()
        n=c.execute("SELECT FNAME, LNAME, TUT_GTID FROM STUDENT INNER JOIN CHOOSES ON STUDENT.STUD_GTID=CHOOSES.TUT_GTID WHERE UGRAD_GTID=(%s) AND SCHOOL=(%s) AND COURSE_NUM=(%s)", (str(self.iv.get()), str(co), str(num)))
        n=c.fetchall()
        self.n=n
        self.r=0
        l=Label(self.win5, text="Tutor Name")
        l.grid(column=1, row=self.r, sticky=E+W)
        count=1
        self.iv7=IntVar()
        self.r=self.r+1
        for i in n:
            name=str(i[0])+" "+str(i[1])
            rb="rb"+str(count)
            rb=Radiobutton(self.win5, text=name, value=count, variable=self.iv7)
            rb.grid(column=1, row=self.r, sticky=E+W)
            count=count+1
            self.r=self.r+1
        self.coun=count
        self.r=self.r+1
        b=Button(self.win5, text="Select Tutor Name", command=self.rate2)
        b.grid(column=1, row=self.r, sticky=E+W)
        

    def rate2(self):
        l=Label(self.win5, text="Descriptive Evaluation")
        l.grid(column=2, row=0, sticky=W) 
        self.descript=StringVar()
        e=Entry(self.win5, textvariable=self.descript, width=30)
        e.grid(column=2, row=1,columnspan=3, sticky=E+W)
        l1=Label(self.win5, text="Numeric Evaluation")
        l1.grid(column=2, row=2, sticky=W)
        self.numet=IntVar()
        rb=Radiobutton(self.win5, text="4 Highly Recommend", variable=self.numet, value=4)
        rb.grid(column=2, row=3, sticky=W)
        rb1=Radiobutton(self.win5, text="3 Recommend", variable=self.numet, value=3)
        rb1.grid(column=2, row=4, sticky=W)
        rb2=Radiobutton(self.win5, text="2 Recommend with Reservations", variable=self.numet, value=2)
        rb2.grid(column=2, row=5, sticky=W)
        rb3=Radiobutton(self.win5, text="1 Do Not Recommend", variable=self.numet, value=1)
        rb3.grid(column=2, row=6, sticky=W)
        b=Button(self.win5, text="Okay", command=self.rate3)
        b.grid(column=2, row=7, sticky=W)

    def rate3(self):
        if self.descript.get()=="" or self.numet.get()==0:
            messagebox.showinfo(message="You have not filled in all the fields.")
        else:
            position=int(self.iv6.get())-1
            tup1=self.o[position]
            coursenum=tup1[0]
            school=tup1[1]
            #FNAME, LNAME, STUD_GTID self.iv7.get() is the value for the position in the tuple self.n
            position=int(self.iv7.get())-1
            tup2=self.n[position]
            fname=tup2[0]
            lname=tup2[1]
            gtid=tup2[2]
            c=self.db.cursor()
            a=self.semester()
            try:
                h=c.execute("INSERT INTO RATES (UGRAD_GTID, SCHOOL, COURSE_NUM, TUT_GTID, NUMERIC_E, DESCRIP_E, SEMESTER) VALUES ((%s), (%s), (%s), (%s), (%s), (%s), (%s))",( str(self.iv.get()), str(school), str(coursenum), str(gtid), str(self.numet.get()), str(self.descript.get()), str(self.semester())))  
                self.win5.withdraw()
                self.Mainmenu()
            except:
                messagebox.showinfo(message="You can only rate a tutor for a course once per semester.")

    def recommend1(self):
        self.win1.withdraw()
        self.win7=Toplevel()
        self.win7.title("Professor Recommendation") 
        c=self.db.cursor()
        j=c.execute("SELECT * FROM PROFESSOR")
        j=c.fetchall()
        alist=[]
        for i in j:
            for q in i:
                alist.append(q)
        if self.iv.get() not in alist:
            messagebox.showinfo(message="You must be a professor to rate a tutor.")
            self.win7.withdraw()
            self.Mainmenu()
        o=c.execute("SELECT TUT_GTID FROM TUTOR WHERE GPA>='3.0'")
        self.tutors=c.fetchall()
        self.count=1
        r=1
        self.gtidforrec=IntVar()
        l=Label(self.win7, text="Students GTIDs")
        l.grid(row=0, column=0, sticky=E+W)
        for i in self.tutors:
            co=str(i[0])
            rb="rb"+str(self.count)
            rb=Radiobutton(self.win7, text=co, value=co, variable=self.gtidforrec)
            rb.grid(row=r, column=0, sticky=E+W)
            self.count=self.count+1
            r=r+1
        r=r+1
        b=Button(self.win7, text="Select GTID", command=self.recommend2)
        b.grid(column=0, row=r, sticky=E+W)
        self.r=r+1
        b1=Button(self.win7, text="Cancel", command=self.blowthisup)
        b1.grid(column=0, row=self.r, sticky=E+W)
        self.r=r+1

    def blowthisup(self):
        self.win7.withdraw()
        self.Mainmenu()
        
    def recommend2(self):
        l=Label(self.win7, text="Descriptive Evaluation")
        l.grid(column=2, row=0, sticky=W) 
        self.desc=StringVar()
        e=Entry(self.win7, textvariable=self.desc, width=30)
        e.grid(column=2, row=1,columnspan=3, sticky=E+W)
        l1=Label(self.win7, text="Numeric Evaluation")
        l1.grid(column=2, row=2, sticky=W)
        self.numpp=IntVar()
        rb=Radiobutton(self.win7, text="4 Highly Recommend", variable=self.numpp, value=4)
        rb.grid(column=2, row=3, sticky=W)
        rb1=Radiobutton(self.win7, text="3 Recommend", variable=self.numpp, value=3)
        rb1.grid(column=2, row=4, sticky=W)
        rb2=Radiobutton(self.win7, text="2 Recommend with Reservations", variable=self.numpp, value=2)
        rb2.grid(column=2, row=5, sticky=W)
        rb3=Radiobutton(self.win7, text="1 Do Not Recommend", variable=self.numpp, value=1)
        rb3.grid(column=2, row=6, sticky=W)
        b=Button(self.win7, text="Okay", command=self.recommend3)
        b.grid(column=2, row=7, sticky=W)

    def recommend3(self):
        if self.desc.get()=="" or self.numpp.get()==0:
            messagebox.showinfo(message="You have not filled in all the fields.")
        else:
            try:
                c=self.db.cursor()
                h=c.execute("INSERT INTO RECOMMENDS (TUT_GTID, PROF_GTID, DESCRIP_E, NUMERIC_E) VALUES ((%s), (%s), (%s), (%s))",( str(self.gtidforrec.get()), str(self.iv.get()), str(self.desc.get()), str(self.numpp.get())))  
                self.win7.withdraw()
                self.Mainmenu()
            except:
                messagebox.showinfo(message="You can't recommend a tutor more than once.")

    def findmysched(self):
        self.win1.withdraw()
        c=self.db.cursor()
        p=c.execute("SELECT TUT_GTID FROM TUTOR")
        p=c.fetchall()
        eh=[]
        for i in p:
            for y in i:
                eh.append(y)
        if self.iv.get() not in eh:
            messagebox.showinfo(title="Not for you!", message="You must be a Tutor to have a Schedule.")
            self.Mainmenu()
        else:
            self.win10=Toplevel()
            self.win10.title("Find My Schedule")
            c=self.db.cursor()
            h=c.execute("SELECT FNAME, LNAME FROM STUDENT WHERE STUD_GTID =(%s)", str(self.iv.get()))
            h=c.fetchall()
            a=""
            for i in h:
                for l in i:
                    a=a+str(l)
            con="Schedule for Student "+a+" with GTID "+str(self.iv.get())
            l=Label(self.win10, text=con)
            l.grid(row=0, column=0, sticky=E+W, columnspan=6)
            l1=Label(self.win10, text="Day")
            l1.grid(row=1, column=0, sticky=E+W)
            l2=Label(self.win10, text="Time")
            l2.grid(row=1, column=1, sticky=E+W)
            l3=Label(self.win10, text="First Name")
            l3.grid(row=1, column=2, sticky=E+W)
            l4=Label(self.win10, text="Last Name")
            l4.grid(row=1, column=3, sticky=E+W)
            l5=Label(self.win10, text="E-mail")
            l5.grid(row=1, column=4, sticky=E+W)
            l6=Label(self.win10, text="Course")
            l6.grid(row=1, column=5, sticky=E+W)
            n=c.execute("SELECT CHOOSES.WEEKDAY, CHOOSES.TIME, STUDENT.FNAME, STUDENT.LNAME, STUDENT.EMAIL, CHOOSES.SCHOOL, CHOOSES.COURSE_NUM FROM CHOOSES JOIN TUTOR ON TUTOR.TUT_GTID=CHOOSES.TUT_GTID JOIN UNDERGRAD ON CHOOSES.UGRAD_GTID=UNDERGRAD.UGRAD_GTID JOIN STUDENT ON STUDENT.STUD_GTID=UNDERGRAD.UGRAD_GTID WHERE TUTOR.TUT_GTID=(%s)",str(self.iv.get()))
            n=c.fetchall()
            #(('W', datetime.timedelta(0, 39600), 'Brock', 'Li', 'brock.li', 'CS', 2200),)
            if len(n)!=0:
                count=2
                col=0
                for y in n:
                    l7=Label(self.win10, text=y[0])
                    l7.grid(row=count, column=col, sticky=E+W)
                    col=col+1
                    l8=Label(self.win10, text=y[1])
                    l8.grid(row=count, column=col, sticky=E+W)
                    col=col+1
                    l9=Label(self.win10, text=y[2])
                    l9.grid(row=count, column=col, sticky=E+W)
                    col=col+1
                    l10=Label(self.win10, text=y[3])
                    l10.grid(row=count, column=col, sticky=E+W)
                    col=col+1
                    l11=Label(self.win10, text=y[4])
                    l11.grid(row=count, column=col, sticky=E+W)
                    col=col+1
                    con=str(y[5])+" "+str(y[6])
                    l12=Label(self.win10, text=con)
                    l12.grid(row=count, column=col, sticky=E+W)
                    count=count+1
                    col=0
                    
            
            
        
    def sum1(self):
        self.win1.withdraw()
        c=self.db.cursor()
        p=c.execute("SELECT * FROM ADMINISTRATOR")
        p=c.fetchall()
        eh=[]
        for i in p:
            for y in i:
                eh.append(y)
        if self.iv.get() not in eh:
            messagebox.showinfo(title="Reserved Procedure", message="This function is only allowed for the administrators")
            self.Mainmenu()
        else:
            self.win8=Toplevel()
            self.win8.title("Summary 1")
            c=self.db.cursor()
            self.fall2014=IntVar()
            self.summer2014=IntVar()
            self.spring2014=IntVar()
            l=Label(self.win8, text="Academic Year 2014")
            l.grid(column=0, row=0, sticky=E+W)
            w = Checkbutton(self.win8, onvalue=3, offvalue=0, variable=self.fall2014)
            w.grid(column=2, row=0, sticky=E+W, columnspan=1)
            l1=Label(self.win8, text = "Fall")
            l1.grid(column=1, row=0, sticky=E+W)
            w1 = Checkbutton(self.win8, onvalue=1, offvalue=0, variable=self.spring2014)
            w1.grid(column=4, row=0, sticky=E+W, columnspan=1)
            l2=Label(self.win8, text = "Spring")
            l2.grid(column=3, row=0, sticky=E+W)
            w2 = Checkbutton(self.win8, onvalue=2, offvalue=0, variable=self.summer2014)
            w2.grid(column=6, row=0, sticky=E+W, columnspan=1)
            l3=Label(self.win8, text = "Summmer")
            l3.grid(column=5, row=0, sticky=E+W)
            b=Button(self.win8, text="Ok", command=self.sum12)
            b.grid(column =7 , row =0, sticky =E+W)
 

    def sum12(self):
        c=self.db.cursor()
        if self.spring2014.get()==1 and self.summer2014.get()==0 and self.fall2014.get()==0:
            b=c.execute("CREATE VIEW Admin_Report1 AS (SELECT CONCAT(CHOOSES.SCHOOL,CHOOSES.COURSE_NUM) AS Course, SEMESTER, COUNT(DISTINCT CHOOSES.UGRAD_GTID) AS Num_Students, COUNT(DISTINCT CHOOSES.TUT_GTID) AS Num_Tutors FROM CHOOSES  WHERE SEMESTER IN ((%s))  GROUP BY CONCAT(SCHOOL,COURSE_NUM), SEMESTER ORDER BY SCHOOL, COURSE_NUM, SEMESTER)","Spring 2014")
        if self.summer2014.get()==2 and self.spring2014.get()==0 and self.fall2014.get()==0:
            b=c.execute("CREATE VIEW Admin_Report1 AS (SELECT CONCAT(CHOOSES.SCHOOL,CHOOSES.COURSE_NUM) AS Course, SEMESTER, COUNT(DISTINCT CHOOSES.UGRAD_GTID) AS Num_Students, COUNT(DISTINCT CHOOSES.TUT_GTID) AS Num_Tutors FROM CHOOSES  WHERE SEMESTER IN ((%s))  GROUP BY CONCAT(SCHOOL,COURSE_NUM), SEMESTER ORDER BY SCHOOL, COURSE_NUM, SEMESTER)","Summer 2014")
        if self.fall2014.get()==3 and self.spring2014.get()==0 and self.summer2014.get()==0:
            b=c.execute("CREATE VIEW Admin_Report1 AS (SELECT CONCAT(CHOOSES.SCHOOL,CHOOSES.COURSE_NUM) AS Course, SEMESTER, COUNT(DISTINCT CHOOSES.UGRAD_GTID) AS Num_Students, COUNT(DISTINCT CHOOSES.TUT_GTID) AS Num_Tutors FROM CHOOSES  WHERE SEMESTER IN ((%s))  GROUP BY CONCAT(SCHOOL,COURSE_NUM), SEMESTER ORDER BY SCHOOL, COURSE_NUM, SEMESTER)","Fall 2014")
        if self.spring2014.get()==1 and self.summer2014.get()==2 and self.fall2014.get()==0:
            b=c.execute("CREATE VIEW Admin_Report1 AS (SELECT CONCAT(CHOOSES.SCHOOL,CHOOSES.COURSE_NUM) AS Course, SEMESTER, COUNT(DISTINCT CHOOSES.UGRAD_GTID) AS Num_Students, COUNT(DISTINCT CHOOSES.TUT_GTID) AS Num_Tutors FROM CHOOSES  WHERE SEMESTER IN ((%s), (%s))  GROUP BY CONCAT(SCHOOL,COURSE_NUM), SEMESTER ORDER BY SCHOOL, COURSE_NUM, SEMESTER)",("Spring 2014", "Summer 2014"))
        if self.spring2014.get()==1 and self.summer2014.get()==0 and self.fall2014.get()==3:
            b=c.execute("CREATE VIEW Admin_Report1 AS (SELECT CONCAT(CHOOSES.SCHOOL,CHOOSES.COURSE_NUM) AS Course, SEMESTER, COUNT(DISTINCT CHOOSES.UGRAD_GTID) AS Num_Students, COUNT(DISTINCT CHOOSES.TUT_GTID) AS Num_Tutors FROM CHOOSES  WHERE SEMESTER IN ((%s), (%s))  GROUP BY CONCAT(SCHOOL,COURSE_NUM), SEMESTER ORDER BY SCHOOL, COURSE_NUM, SEMESTER)",("Spring 2014", "Fall 2014"))
        if self.spring2014.get()==0 and self.summer2014.get()==2 and self.fall2014.get()==3:
            b=c.execute("CREATE VIEW Admin_Report1 AS (SELECT CONCAT(CHOOSES.SCHOOL,CHOOSES.COURSE_NUM) AS Course, SEMESTER, COUNT(DISTINCT CHOOSES.UGRAD_GTID) AS Num_Students, COUNT(DISTINCT CHOOSES.TUT_GTID) AS Num_Tutors FROM CHOOSES  WHERE SEMESTER IN ((%s), (%s))  GROUP BY CONCAT(SCHOOL,COURSE_NUM), SEMESTER ORDER BY SCHOOL, COURSE_NUM, SEMESTER)",("Summer 2014", "Fall 2014"))
        if self.spring2014.get()==1 and self.summer2014.get()==2 and self.fall2014.get()==3:
            b=c.execute("CREATE VIEW Admin_Report1 AS (SELECT CONCAT(CHOOSES.SCHOOL,CHOOSES.COURSE_NUM) AS Course, SEMESTER, COUNT(DISTINCT CHOOSES.UGRAD_GTID) AS Num_Students, COUNT(DISTINCT CHOOSES.TUT_GTID) AS Num_Tutors FROM CHOOSES  WHERE SEMESTER IN ((%s), (%s), (%s))  GROUP BY CONCAT(SCHOOL,COURSE_NUM), SEMESTER ORDER BY SCHOOL, COURSE_NUM, SEMESTER)",("Spring 2014","Summer 2014", "Fall 2014"))
        elif self.spring2014.get()==0 and self.summer2014.get()==0 and self.fall2014.get()==0:
            messagebox.showinfo(title="Error!", message="Please select a semester!")
        h=c.execute("SELECT * FROM Admin_Report1")
        n=c.fetchall()
        #((b'CS2200', 'Spring 2014', 1, 1), (b'CS4400', 'Fall 2014', 1, 1))
        #self.win8
        l=Label(self.win8, text="Course")
        l.grid(row=1, column=0, sticky=E+W)
        l1=Label(self.win8, text="Semester")
        l1.grid(row=1, column=1, sticky=E+W)
        l2=Label(self.win8, text="Number of Students")
        l2.grid(row=1, column=2, sticky=E+W)
        l3=Label(self.win8, text="Number of Tutors")
        l3.grid(row=1, column=3, sticky=E+W)
        t=c.execute("CREATE VIEW Totals AS (SELECT Course ,SUM(Num_Students) AS Total_Num_Students, SUM(Num_Tutors) AS Total_Num_Tutors FROM Admin_Report1 GROUP BY Course ORDER BY Course)")  
        t=c.execute("SELECT * FROM Totals")
        t=c.fetchall()
        print(t)
        col=0
        ro=2
        num=0
        #((,))
        for i in n:
            l4=Label(self.win8, text=i[0])
            l4.grid(row=ro, column=col, sticky=E+W)
            col=col+1
            l5=Label(self.win8, text=i[1])
            l5.grid(row=ro, column=col, sticky=E+W)
            col=col+1
            l6=Label(self.win8, text=i[2])
            l6.grid(row=ro, column=col, sticky=E+W)
            col=col+1
            l7=Label(self.win8, text=i[3])
            l7.grid(row=ro, column=col, sticky=E+W)
            col=col+1
            col=0
            ro=ro+1
        q=c.execute("SELECT SUM(Total_Num_Students) AS Grand_Total_Num_Students, SUM(Total_Num_Tutors) AS Grand_Total_Num_Tutors FROM Totals") 
        q=c.fetchall()
        print(q)
       # except:
#            print("this didn't work...")
            
    def sum2(self):
        self.win1.withdraw()
        c=self.db.cursor()
        p=c.execute("SELECT * FROM ADMINISTRATOR")
        p=c.fetchall()
        eh=[]
        for i in p:
            for y in i:
                eh.append(y)
        if self.iv.get() not in eh:
            messagebox.showinfo(title="Reserved Procedure", message="This function is only allowed for the administrators")
            self.Mainmenu()
        else:
            self.win9=Toplevel()
            self.win9.title("Summary 1")
            c=self.db.cursor()
            self.fall=IntVar()
            self.spring=IntVar()
            self.summer=IntVar()
            l=Label(self.win9, text="Academic Year 2014")
            l.grid(column=0, row=0, sticky=E+W)
            sp = Label(self.win9, text = "    ")
            sp.grid(column = 1, row = 0, sticky=E+W)
            w = Checkbutton(self.win9, variable=self.fall, onvalue=3, offvalue=0)
            w.grid(column=2, row=0, sticky=E+W)
            l1=Label(self.win9, text = "Fall")
            l1.grid(column=3, row=0, sticky=E+W)
            sp1 = Label(self.win9, text = "    ")
            sp1.grid(column = 4, row = 0, sticky=E+W)
            w1 = Checkbutton(self.win9, variable=self.spring, onvalue=1, offvalue=0)
            w1.grid(column=5, row=0, sticky=E+W)
            l2=Label(self.win9, text = "Spring")
            l2.grid(column=6, row=0, sticky=E+W)
            sp2 = Label(self.win9, text = "    ")
            sp2.grid(column = 7, row = 0, sticky=E+W)
            w2 = Checkbutton(self.win9, onvalue=2, offvalue=2, variable=self.summer)
            w2.grid(column=8, row=0, sticky=E+W)
            l3=Label(self.win9, text = "Summmer")
            l3.grid(column=9, row=0, sticky=E+W)
            sp3 = Label(self.win9, text = "    ")
            sp3.grid(column = 10, row = 0, sticky=E+W)
            b=Button(self.win9, text="Ok", command=self.sum22)
            b.grid(column = 10, row =0, sticky =E+W)
            
    def sum22(self):
        c=self.db.cursor()
        #THE SQL UNDER EACH IF STATEMENT IS INCORRECT 
        if self.spring.get()==1 and self.summer.get()==0 and self.fall.get()==0:
            b=c.execute("CREATE VIEW Admin_Report1 AS (SELECT CONCAT(CHOOSES.SCHOOL,CHOOSES.COURSE_NUM) AS Course, SEMESTER, COUNT(DISTINCT CHOOSES.UGRAD_GTID) AS Num_Students, COUNT(DISTINCT CHOOSES.TUT_GTID) AS Num_Tutors FROM CHOOSES  WHERE SEMESTER IN ((%s))  GROUP BY CONCAT(SCHOOL,COURSE_NUM), SEMESTER ORDER BY SCHOOL, COURSE_NUM, SEMESTER)","Spring 2014")
        if self.summer.get()==2 and self.spring.get()==0 and self.fall.get()==0:
            b=c.execute("CREATE VIEW Admin_Report1 AS (SELECT CONCAT(CHOOSES.SCHOOL,CHOOSES.COURSE_NUM) AS Course, SEMESTER, COUNT(DISTINCT CHOOSES.UGRAD_GTID) AS Num_Students, COUNT(DISTINCT CHOOSES.TUT_GTID) AS Num_Tutors FROM CHOOSES  WHERE SEMESTER IN ((%s))  GROUP BY CONCAT(SCHOOL,COURSE_NUM), SEMESTER ORDER BY SCHOOL, COURSE_NUM, SEMESTER)","Summer 2014")
        if self.fall.get()==3 and self.spring.get()==0 and self.summer.get()==0:
            b=c.execute("CREATE VIEW Admin_Report1 AS (SELECT CONCAT(CHOOSES.SCHOOL,CHOOSES.COURSE_NUM) AS Course, SEMESTER, COUNT(DISTINCT CHOOSES.UGRAD_GTID) AS Num_Students, COUNT(DISTINCT CHOOSES.TUT_GTID) AS Num_Tutors FROM CHOOSES  WHERE SEMESTER IN ((%s))  GROUP BY CONCAT(SCHOOL,COURSE_NUM), SEMESTER ORDER BY SCHOOL, COURSE_NUM, SEMESTER)","Fall 2014")
        if self.spring.get()==1 and self.summer.get()==2 and self.fall.get()==0:
            b=c.execute("CREATE VIEW Admin_Report1 AS (SELECT CONCAT(CHOOSES.SCHOOL,CHOOSES.COURSE_NUM) AS Course, SEMESTER, COUNT(DISTINCT CHOOSES.UGRAD_GTID) AS Num_Students, COUNT(DISTINCT CHOOSES.TUT_GTID) AS Num_Tutors FROM CHOOSES  WHERE SEMESTER IN ((%s), (%s))  GROUP BY CONCAT(SCHOOL,COURSE_NUM), SEMESTER ORDER BY SCHOOL, COURSE_NUM, SEMESTER)",("Spring 2014", "Summer 2014"))
        if self.spring.get()==1 and self.summer.get()==0 and self.fall.get()==3:
            b=c.execute("CREATE VIEW Admin_Report1 AS (SELECT CONCAT(CHOOSES.SCHOOL,CHOOSES.COURSE_NUM) AS Course, SEMESTER, COUNT(DISTINCT CHOOSES.UGRAD_GTID) AS Num_Students, COUNT(DISTINCT CHOOSES.TUT_GTID) AS Num_Tutors FROM CHOOSES  WHERE SEMESTER IN ((%s), (%s))  GROUP BY CONCAT(SCHOOL,COURSE_NUM), SEMESTER ORDER BY SCHOOL, COURSE_NUM, SEMESTER)",("Spring 2014", "Fall 2014"))
        if self.spring.get()==0 and self.summer.get()==2 and self.fall.get()==3:
            b=c.execute("CREATE VIEW Admin_Report1 AS (SELECT CONCAT(CHOOSES.SCHOOL,CHOOSES.COURSE_NUM) AS Course, SEMESTER, COUNT(DISTINCT CHOOSES.UGRAD_GTID) AS Num_Students, COUNT(DISTINCT CHOOSES.TUT_GTID) AS Num_Tutors FROM CHOOSES  WHERE SEMESTER IN ((%s), (%s))  GROUP BY CONCAT(SCHOOL,COURSE_NUM), SEMESTER ORDER BY SCHOOL, COURSE_NUM, SEMESTER)",("Summer 2014", "Fall 2014"))
        if self.spring.get()==1 and self.summer.get()==2 and self.fall.get()==3:
            b=c.execute("CREATE VIEW Admin_Report1 AS (SELECT CONCAT(CHOOSES.SCHOOL,CHOOSES.COURSE_NUM) AS Course, SEMESTER, COUNT(DISTINCT CHOOSES.UGRAD_GTID) AS Num_Students, COUNT(DISTINCT CHOOSES.TUT_GTID) AS Num_Tutors FROM CHOOSES  WHERE SEMESTER IN ((%s), (%s), (%s))  GROUP BY CONCAT(SCHOOL,COURSE_NUM), SEMESTER ORDER BY SCHOOL, COURSE_NUM, SEMESTER)",("Spring 2014","Summer 2014", "Fall 2014"))
        if self.spring.get()==0 and self.summer.get()==0 and self.fall.get()==0:
            messagebox.showinfo(title="Error!", message="Please select a semester!")
        h=c.execute("SELECT * FROM 'Admin_Report2'")
        n=c.fetchall()
        print(n)
#this sql is wrong... for sure but needs to be fixed and replace the admin report1         
#        b=c.execute("CREATE VIEW Admin_Report2 AS (SELECT CONCAT(CHOOSES.SCHOOL, ‘ ‘,CHOOSES.COURSE_NUM) AS Course, $Semester, COUNT(SELECT DISTINCT TUT_GTID FROM TUTORS WHERE TUTORS.GTA=’TRUE’) AS GTAs, AVG(SELECT RATES.NUMERICAL_E FROM RATES JOIN TUTORS ON RATES. TUT_GTID=TUTORS.TUT_GTID WHERE TUTORS.GTA=’TRUE’) AS AvgRating_GTAs,COUNT(SELECT DISTINCT TUT_GTID FROM TUTORS WHERE TUTORS.GTA=’FALSE’) AS Not_GTAs, AVG(SELECT RATES.NUMERICAL_E FROM RATES JOIN TUTORS ON RATES.TUTOR_GTID= TUTORS.TUT_GTID WHERE TUTORS.GTA=’FALSE’) AS AvgRating_Not_GTAs FROM CHOOSES WHERE SEMESTER IN ($Semester) GROUP BY Course, ORDER BY SCHOOL, COURSE_NUM, SEMESTER ORDER BY CHOOSES. SCHOOL, CHOOSES.COURSE_NUM, SEMESTER)") 
       # except:
#            print("poop....")
        


            
            #frame.grid(row=0,column=0)
            #canvas=Canvas(frame,bg='#FFFFFF',width=600,height=600,scrollregion=(0,0,500,500))
            #vbar=Scrollbar(frame,orient=VERTICAL)
            #vbar.pack(side=RIGHT,fill=Y)
            #vbar.config(command=canvas.yview)
            #canvas.config(width=300,height=300)
            #canvas.config(yscrollcommand=vbar.set)
            #canvas.pack(side=LEFT,expand=True,fill=BOTH)    


win=Tk()
app=poop(win)
win.title("Georgia Tech Tutor System")
win.mainloop()
