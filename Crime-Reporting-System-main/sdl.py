from PIL import Image, ImageTk  # python image library
import sys
from Tkinter import *
import MySQLdb
db = MySQLdb.connect("localhost", "root", "root", "vt")
cursor = db.cursor()
colors = {1: 'red', 2: 'gold', 3: 'blue', 4: 'green', 5: 'cyan', 6: 'magenta', 7: 'yellow', 8: 'black', 9: 'orange',
          10: 'darkred', 11: 'hotpink', 12: 'indigo', 13: 'brown', 14: 'lavender', 15: 'khaki', 16: 'lavender'}

root = Tk()
root.title('LOGIN')


def menu():

    root1 = Toplevel()

    root1.minsize(1200, 1200)
    image1 = Image.open("image3.jpeg")
    photo1 = ImageTk.PhotoImage(image1)
    photo_label1 = Label(root1, image=photo1)
    photo_label1.pack()
    root1.title('CRIMINAL DATABASE')
    welcome_label = Label(root1, text="WELCOME TO CRIME ANALYSIS SYSTEM",
                          relief=RAISED, fg='white', bg='black', font=("Helvetica", 34))
    welcome_label.place(x=180, y=0)

    b1 = Button(root1, text="ENTER NEW RECORDS", command=fun1,
                bg='black', fg='white', font=("Helvetica", 20))
    b1.place(x=0, y=200)

    b2 = Button(root1, text="SEARCH A RECORD", command=fun2,
                bg='black', fg='white', font=("Helvetica", 20))
    b2.place(x=0, y=300)

    b3 = Button(root1, text="DELETE A RECORD", command=fun5,
                bg='black', fg='white', font=("Helvetica", 20))
    b3.place(x=0, y=400)

    b4 = Button(root1, text="UPDATE A RECORD", command=fun3,
                bg='black', fg='white', font=("Helvetica", 20))
    b4.place(x=0, y=500)

    b5 = Button(root1, text="GRAPH REPORTS", command=fun4,
                bg='black', fg='white', font=("Helvetica", 20))
    b5.place(x=0, y=600)

    root1.mainloop()


def fun1():

    w1 = Toplevel()
    w1.minsize(700, 700)
    image3 = Image.open("insert.jpg")
    photo3 = ImageTk.PhotoImage(image3)
    photo_label3 = Label(w1, image=photo3)
    photo_label3.pack()
    w1.title('ADD NEW RECORD')

    def accept():

        name = str(n.get())
        add = str(ad.get())
        year = int(y.get())
        city = str(ci.get())
        city_no = int(cn.get())
        gender = str(g.get())
        age = int(a.get())
        time = str(t.get())
        crimelevel = str(cl.get())

        try:
            sql = "INSERT INTO mytable VALUES('%s','%s','%d','%s','%d','%s','%d','%s','%s')" % (
                name, add, year, city, city_no, gender, age, time, crimelevel)
            cursor.execute(sql)
            db.commit()
            success = Toplevel()
            success.title('Success')
            l1 = Label(success, text='RECORD ENTERED SUCCESSFULLY',
                       relief=RAISED, fg='white', bg='black', font=("Helvetica", 20))
            l1.pack()

        except:
            error = Toplevel()
            error.title('Error')
            l21 = Label(error, text='ERROR IN ENTERING THE RECORD',
                        relief=RAISED, fg='white', bg='black', font=("Helvetica", 20))
            l21.pack()
            db.rollback()

    l1 = Label(w1, text='Enter the name of criminal', relief=RAISED,
               bg='black', fg='white', font=("Helvetica", 15))
    n = Entry(w1, bg='black', fg='white', font=("Helvetica", 15))

    l2 = Label(w1, text='Enter the address of the criminal',
               relief=RAISED, bg='black', fg='white', font=("Helvetica", 15))
    ad = Entry(w1, bg='black', fg='white', font=("Helvetica", 15))

    l3 = Label(w1, text='Enter the year of crime commited',
               relief=RAISED, bg='black', fg='white', font=("Helvetica", 15))
    y = Entry(w1, bg='black', fg='white', font=("Helvetica", 15))

    l4 = Label(w1, text='Enter the city', relief=RAISED,
               bg='black', fg='white', font=("Helvetica", 15))
    ci = Entry(w1, bg='black', fg='white', font=("Helvetica", 15))

    l5 = Label(w1, text='Enter the city_no', relief=RAISED,
               bg='black', fg='white', font=("Helvetica", 15))
    cn = Entry(w1, bg='black', fg='white', font=("Helvetica", 15))

    l6 = Label(w1, text='Enter the gender', relief=RAISED,
               bg='black', fg='white', font=("Helvetica", 15))
    g = Entry(w1, bg='black', fg='white', font=("Helvetica", 15))

    l7 = Label(w1, text='Enter the age', relief=RAISED,
               bg='black', fg='white', font=("Helvetica", 15))
    a = Entry(w1, bg='black', fg='white', font=("Helvetica", 15))

    l8 = Label(w1, text='Enter the time of crime', relief=RAISED,
               bg='black', fg='white', font=("Helvetica", 15))
    t = Entry(w1, bg='black', fg='white', font=("Helvetica", 15))

    l9 = Label(w1, text='Enter the crimelevel', relief=RAISED,
               bg='black', fg='white', font=("Helvetica", 15))
    cl = Entry(w1, bg='black', fg='white', font=("Helvetica", 15))

    submit = Button(w1, text='SUBMIT', command=accept,
                    bg='black', fg='white', font=("Helvetica", 28))

    l1.place(x=0, y=0)
    n.place(x=300, y=0)

    l2.place(x=0, y=50)
    ad.place(x=300, y=50)

    l3.place(x=0, y=100)
    y.place(x=300, y=100)

    l4.place(x=0, y=150)
    ci.place(x=300, y=150)

    l5.place(x=0, y=200)
    cn.place(x=300, y=200)

    l6.place(x=0, y=300)
    g.place(x=300, y=300)

    l7.place(x=0, y=350)
    a.place(x=300, y=350)

    l8.place(x=0, y=400)
    t.place(x=300, y=400)

    l9.place(x=0, y=450)
    cl.place(x=300, y=450)

    submit.place(x=300, y=500)
    w1.mainloop()


def fun2():

    w2 = Toplevel()
    w2.minsize(700, 700)
    image2 = Image.open("image4.jpg")
    photo2 = ImageTk.PhotoImage(image2)
    photo_label2 = Label(w2, image=photo2)
    photo_label2.pack()
    w2.title('SEARCH RECORD')

    def search():

        name = str(n1.get())
        try:
            sql = "SELECT * FROM mytable where name='%s'" % name
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                name = row[0]
                address = row[1]
                year = row[2]
                city = row[3]
                city_no = row[4]
                gender = row[5]
                age = row[6]
                time = row[7]
                crimelevel = row[8]
                eb = Label(w2, text='%-20s,%-60s,%-10d,%-20s,%-7d,%-3s,%-7d,%-15s,%-15s' % (name, address, year, city,
                           city_no, gender, age, time, crimelevel), bg='black', fg='white', font=("Helvetica", 16)).place(x=0, y=200)
        except:
            error = Toplevel()
            l1 = Label(error, text='RECORD NOT FOUND', relief=RAISED)
            l1.pack()
            pass

    l_1 = Label(w2, text='enter the name of criminal to be searched:',
                relief=RAISED, bg='black', fg='white', font=("Helvetica", 18))
    n1 = Entry(w2, bg='black', fg='white', font=("Helvetica", 18))
    l_1.place(x=0, y=0)
    n1.place(x=500, y=0)
    submit1 = Button(w2, text='SUBMIT', command=search,
                     bg='black', fg='white', font=("Helvetica", 28))
    submit1.place(x=500, y=100)
    w2.mainloop()


def fun5():

    w5 = Toplevel()
    w5.minsize(700, 700)
    w5.title('DELETE RECORD')
    image = Image.open("delete.jpg")
    photo = ImageTk.PhotoImage(image)
    photo_label = Label(w5, image=photo)
    photo_label.pack()

    def remove():

        name = str(n1.get())

        try:

            sql = "SELECT * FROM mytable where name='%s'" % name
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                name = row[0]
                address = row[1]
                year = row[2]
                city = row[3]
                city_no = row[4]
                gender = row[5]
                age = row[6]
                time = row[7]
                crimelevel = row[8]
                msg = Label(w5, text='DELETED RECORD:', fg='white',
                            bg='black', font=("Helvetica", 14)).place(x=0, y=200)
                eb = Label(w5, text='%-20s,%-60s,%-10d,%-20s,%-7d,%-3s,%-7d,%-15s,%-15s' % (name, address, year, city,
                           city_no, gender, age, time, crimelevel), fg='white', bg='black', font=("Helvetica", 14)).place(x=0, y=300)

                sql1 = "DELETE from mytable where name='%s'" % name
                cursor.execute(sql1)

        except:
            error = Toplevel()
            l1 = Label(error, text='RECORD NOT FOUND', relief=RAISED)
            l1.pack()
            pass

    l_1 = Label(w5, text='enter the name of criminal to be deleted:',
                relief=RAISED, bg='black', fg='white', font=("Helvetica", 18))
    n1 = Entry(w5, bg='black', fg='white', font=("Helvetica", 18))
    l_1.place(x=0, y=0)
    n1.place(x=500, y=0)
    submit1 = Button(w5, text='SUBMIT', command=remove,
                     bg='black', fg='white', font=("Helvetica", 28))
    submit1.place(x=500, y=100)

    w5.mainloop()


def fun3():

    w3 = Toplevel()
    w3.minsize(1200, 1200)
    w3.title('UPDATE QUERY')

    image = Image.open("update.jpg")
    photo = ImageTk.PhotoImage(image)
    photo_label = Label(w3, image=photo)
    photo_label.pack()

    def update():
        oname = str(n2.get())

        add = str(ad1.get())
        year = int(y1.get())
        city = str(ci1.get())
        city_no = int(cn1.get())
        gender = str(g1.get())
        age = int(a1.get())
        time = str(t1.get())
        crimelevel = str(cl1.get())

        try:

            cursor.execute("UPDATE mytable SET address='%s',year='%d',city='%s',city_no='%d',gender='%s',age='%d',time='%s',crimelevel='%s' where name='%s'" % (
                add, year, city, city_no, gender, age, time, crimelevel, oname))

            db.commit()

            success = Toplevel()
            success.title('Success')
            l1 = Label(success, text='RECORD UPDATED SUCCESSFULLY',
                       relief=RAISED, fg='white', bg='black', font=("Helvetica", 20))
            l1.pack()
        except:
            error = Toplevel()
            l1 = Label(error, text='RECORD NOT FOUND', relief=RAISED,
                       bg='black', fg='white', font=("Helvetica", 20))
            l1.pack()
            db.rollback()
            pass

    l_2 = Label(w3, text='enter the name of criminal to be updated:',
                relief=RAISED, bg='black', fg='white', font=("Helvetica", 15))
    l_2.place(x=0, y=0)

    n2 = Entry(w3, bg='black', fg='white', font=("Helvetica", 15))
    n2.place(x=500, y=0)

    l11 = Label(w3, text='enter the new details of the criminal',
                relief=RAISED, bg='black', fg='blue', font=("Helvetica", 20))
    l11.place(x=0, y=40)
    #n1=Entry(w3,bg='black',fg='white',font=("Helvetica", 15)).place(x=500,y=40)

    l22 = Label(w3, text='enter the address of the criminal',
                relief=RAISED, bg='black', fg='white', font=("Helvetica", 15))
    l22.place(x=0, y=80)
    ad1 = Entry(w3, bg='black', fg='white', font=("Helvetica", 15))
    ad1.place(x=500, y=80)

    l33 = Label(w3, text='enter the year the crime was commited',
                relief=RAISED, bg='black', fg='white', font=("Helvetica", 15))
    l33.place(x=0, y=120)
    y1 = Entry(w3, bg='black', fg='white', font=("Helvetica", 15))
    y1.place(x=500, y=120)

    l44 = Label(w3, text='enter the city', relief=RAISED,
                bg='black', fg='white', font=("Helvetica", 15))
    l44.place(x=0, y=160)
    ci1 = Entry(w3, bg='black', fg='white', font=("Helvetica", 15))
    ci1.place(x=500, y=160)

    l55 = Label(w3, text='enter the city_no', relief=RAISED,
                bg='black', fg='white', font=("Helvetica", 15))
    l55.place(x=0, y=200)
    cn1 = Entry(w3, bg='black', fg='white', font=("Helvetica", 15))
    cn1.place(x=500, y=200)

    l66 = Label(w3, text='enter the gender', relief=RAISED,
                bg='black', fg='white', font=("Helvetica", 15))
    l66.place(x=0, y=240)
    g1 = Entry(w3, bg='black', fg='white', font=("Helvetica", 15))
    g1.place(x=500, y=240)

    l77 = Label(w3, text='enter the age', relief=RAISED,
                bg='black', fg='white', font=("Helvetica", 15))
    l77.place(x=0, y=280)
    a1 = Entry(w3, bg='black', fg='white', font=("Helvetica", 15))
    a1.place(x=500, y=280)

    l88 = Label(w3, text='enter the time of crime', relief=RAISED,
                bg='black', fg='white', font=("Helvetica", 15))
    l88.place(x=0, y=320)
    t1 = Entry(w3, bg='black', fg='white', font=("Helvetica", 15))
    t1.place(x=500, y=320)

    l99 = Label(w3, text='enter the crimelevel', relief=RAISED,
                bg='black', fg='white', font=("Helvetica", 15))
    l99.place(x=0, y=360)
    cl1 = Entry(w3, bg='black', fg='white', font=("Helvetica", 15))
    cl1.place(x=500, y=360)

    submit = Button(w3, text='SUBMIT', command=update,
                    bg='black', fg='white', font=("Helvetica", 20))
    submit.place(x=500, y=500)

    w3.mainloop()


def fun4():

    w4 = Toplevel()
    w4.geometry('1200x700')
    w4.title('GRAPH REPORT')

    image = Image.open("graph.jpg")
    photo = ImageTk.PhotoImage(image)
    photo_label = Label(w4, image=photo)
    photo_label.pack()

    def fun5():
        import matplotlib.pyplot as plt
        ax = plt.subplot(111)
        sql1 = "SELECT count(*) FROM mytable where age between 20 and 30 "
        cursor.execute(sql1)
        y = cursor.fetchone()
        cst = y
        m23 = sum(cst)
     #   print m23

        sql1 = "SELECT count(*) FROM mytable where age between 31 and 40 "
        cursor.execute(sql1)
        y = cursor.fetchone()
        cst = y
        m34 = sum(cst)
        #  print m34

        sql1 = "SELECT count(*) FROM mytable where age between 41 and 60 "
        cursor.execute(sql1)
        y = cursor.fetchone()
        cst = y
        m46 = sum(cst)
        #  print m46

        x = 50
        ax.bar(x-0.5, m23, width=0.25, color='gold', align='center')
        ax.bar(x, m34, width=0.25, color='blue', align='center')
        ax.bar(x+0.5, m46, width=0.25, color='red', align='center')
        plt.xlabel('age group')
        plt.ylabel('no of criminals')
        plt.title('crime committed by age groups')
        plt.legend(('age 20-30', 'age 30-40', 'age 40-60'), loc='upper right')
        sys.stdout.flush()
        plt.show()

    def fun6():
        import matplotlib.pyplot as plt
        ax = plt.subplot(111)
        sql1 = ("SELECT COUNT(*) FROM mytable group by gender")
        cursor.execute(sql1)
        x = cursor.fetchall()
        #          print(x)
        i = 1
        origin = 0
        colors = {1: 'black', 2: 'blue', 3: 'brown',
                  4: 'green', 5: 'cyan', 6: 'magenta'}
        for row in x:
            c = colors[i]
            ax.bar(origin+(i), row[0], width=0.25, color=c, align='center')
            i = i+1
        plt.xlabel('GENDER')
        plt.ylabel('NUMBER OF CRIMINALS')
        plt.title('GENDER V/S NUMBER OF CRIMINALS')
        plt.legend(('MALE', 'FEMALE'), loc='upper left')
        sys.stdout.flush()
        plt.show()

    def fun7():
        import matplotlib.pyplot as plt
        ax = plt.subplot(111)
        sql1 = ("SELECT COUNT(*) FROM mytable group by crimelevel")
        cursor.execute(sql1)
        x = cursor.fetchall()
       # print(x)
        i = 1
        origin = 0
        colors = {1: 'red', 2: 'gold', 3: 'blue'}
        for row in x:
            c = colors[i]
            ax.bar(origin+(i), row[0], width=0.5, color=c, align='center')
            i = i+1
        plt.xlabel('CRIME LEVEL')
        plt.ylabel('NUMBER OF CRIMINALS')
        plt.title('CRIME LEVEL V/S NUMBER OF CRIMINALS')
        plt.legend(('MAJOR', 'MINOR', 'MODERATE'), loc='upper right')
        sys.stdout.flush()
        plt.show()

    def fun8():
        import matplotlib.pyplot as plt
        ax = plt.subplot(111)
        sql1 = ("SELECT COUNT(*) FROM mytable group by city")
        cursor.execute(sql1)
        x = cursor.fetchall()
        print(x)

        labels = ['Auckland', 'Tauranga', 'Christchurch', 'Hamilton', 'Napier-Hastings', 'Invercargill', 'Dunedin', 'Palmerston North', 'Nelson', 'Rotorua',
                  'New Plymouth', ' Whangarei', 'Whanganui', 'Gisborne', 'Wellington']

        colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'red', 'gold', 'blue', 'green', 'cyan', 'magenta', 'yellow', 'lavender', 'orange',
                  'darkred', 'hotpink', 'indigo', 'brown', 'lavender', 'khaki', 'lavender']

        explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

        plt.pie(x, explode=explode, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=90)

        plt.axis('equal')
        plt.show()

        sys.stdout.flush()

    def fun9():
        minmax = Toplevel()
        minmax.title('minmax')
        # minmax.minsize(1000,700)
        minmax.attributes("-fullscreen", True)
        import matplotlib.pyplot as plt
        ax = plt.subplot(111)
        sql1 = ("SELECT min(age) from mytable")
        cursor.execute(sql1)
        x = cursor.fetchone()
        cst = sum(x)
        mm = Label(minmax, text='minimum age:%d' % (cst), fg='white',
                   bg='black', font=("Helvetica", 18)).place(x=0, y=0)

        a = cst

        sql1 = ("SELECT * from mytable where age='%d'" % a)
        cursor.execute(sql1)
        results = cursor.fetchall()
        for row in results:
            name = row[0]
            address = row[1]
            year = row[2]
            city = row[3]
            city_no = row[4]
            gender = row[5]
            age = row[6]
            time = row[7]
            crimelevel = row[8]
            eb = Label(minmax, text='%-20s,%-60s,%-10d,%-20s,%-7d,%-3s,%-7d,%-15s,%-15s' % (name, address, year, city,
                       city_no, gender, age, time, crimelevel), fg='white', bg='black', font=("Helvetica", 14)).place(x=0, y=40)

        sql1 = ("SELECT max(age) from mytable")
        cursor.execute(sql1)
        x = cursor.fetchone()
        cst1 = sum(x)
        mx = Label(minmax, text='maximum age:%d' % (cst1), fg='white',
                   bg='black', font=("Helvetica", 18)).place(x=0, y=80)

        a = cst1

        sql1 = ("SELECT * from mytable where age='%d'" % a)
        cursor.execute(sql1)
        results = cursor.fetchall()
        for row in results:
            name = row[0]
            address = row[1]
            year = row[2]
            city = row[3]
            city_no = row[4]
            gender = row[5]
            age = row[6]
            time = row[7]
            crimelevel = row[8]
            eb = Label(minmax, text='%-20s,%-60s,%-10d,%-20s,%-7d,%-3s,%-7d,%-15s,%-15s' % (name, address, year, city,
                       city_no, gender, age, time, crimelevel), fg='white', bg='black', font=("Helvetica", 14)).place(x=0, y=120)

        sys.stdout.flush()

    b6 = Button(w4, text="VIEW GRAPH OF CRIME COMMITTED BY CRIMINALS OF DIFFERENT AGE GROUPS",
                command=fun5, bg='cyan', fg='black', font=("Helvetica", 20))
    b6.place(x=0, y=200)

    b7 = Button(w4, text="VIEW GRAPH OF GENDER WISE CRIME COMMITTED IN THE CITY",
                command=fun6, bg='cyan', fg='black', font=("Helvetica", 20))
    b7.place(x=0, y=300)

    b8 = Button(w4, text="VIEW GRAPH BASED CRIMELEVEL(minor,moderate,major) ",
                command=fun7, bg='cyan', fg='black', font=("Helvetica", 20))
    b8.place(x=0, y=400)

    b9 = Button(w4, text="VIEW GRAPH OF NO OF CRIMINALS IN THE PARTICULAR CITY",
                command=fun8, bg='cyan', fg='black', font=("Helvetica", 20))
    b9.place(x=0, y=500)

    b10 = Button(w4, text="TO CALCULATE MIN MAX AGE OF CRIMINALS ALONG WITH THERE DETAILS ",
                 command=fun9, bg='cyan', fg='black', font=("Helvetica", 20))
    b10.place(x=0, y=600)

    w4.mainloop()


def login():

    try:
        usr = str(user.get())
        pd = str(pwd.get())
        sql = "SELECT * FROM userdetails where username='%s'" % usr
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            uname = row[0]
            pword = row[1]
        if(uname == usr and pword == pd):
            menu()
        else:
            error = Toplevel()
            l1 = Label(error, text='INVALID USERNAME AND PASSWORD',
                       relief=RAISED, fg='white', bg='black', font=("Helvetica", 20))
            l1.pack()
    except:
        error = Toplevel()
        error.title('IMPORTANT')
        l1 = Label(error, text='Enter username / correct username',
                   relief=RAISED, fg='white', bg='black', font=("Helvetica", 20))
        l1.pack()


def signup():

    error = Toplevel()
    l1 = Label(error, text='ASK BRANCH MANAGER FOR USERNAME AND PASSWORD',
               fg='white', bg='black', font=("Helvetica", 30), relief=RAISED)
    l1.pack()


image = Image.open("lock.jpg")
photo = ImageTk.PhotoImage(image)
photo_label = Label(root, image=photo)
photo_label.pack()


username_label = Label(root, text="Username", relief=RAISED,
                       fg='white', bg='black', font=("Helvetica", 30))
user = Entry(root, font=("Helvetica", 20))

username_label.place(x=250, y=250)
user.place(x=450, y=250)

password_label = Label(root, text="Password", relief=RAISED,
                       fg='white', bg='black', font=("Helvetica", 30))
pwd = Entry(root, font=("Helvetica", 20))

password_label.place(x=250, y=350)
pwd.place(x=450, y=350)


b1 = Button(root, text="LOGIN", command=login, bg='black',
            fg='white', font=("Helvetica", 30))
b1.place(x=250, y=450)

b2 = Button(root, text="SIGNUP", command=signup,
            bg='black', fg='white', font=("Helvetica", 30))
b2.place(x=450, y=450)


root.geometry('1500x1500')
root.mainloop()
