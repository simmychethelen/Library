import tkinter
import csv
import random
import os
import sys
import ast
from datetime import datetime,timedelta
from csv import DictReader, DictWriter
from pathlib import Path
from tkinter import StringVar, OptionMenu
from tkinter import messagebox




filepath=Path('C:\\Users\\simmy\\PycharmProjects\\pythonProject2\\book.csv')
filepath2=Path('C:\\Users\\simmy\\PycharmProjects\\pythonProject2\\member.csv')
filepath3=Path('C:\\Users\\simmy\\PycharmProjects\\pythonProject2\\checkouts.csv')

class Library:
    #The bookid calculation
    def __init__(self,title):
        n = random.randint(1, 999)  # creating a unique bookid
        b = 'VI' + str(n)
        self.bookid=b
        self.title=title
        self.author=''
        self.status=''


    def addbook(self):
        frame3 = tkinter.LabelFrame(window, width=700, height=450, bg='PeachPuff4')
        frame3.grid(row=2, columnspan=2, sticky='nsew', padx=10)

        head = tkinter.Label(frame3, text='******You can add books******', font=("times", 14, "bold"))
        head.grid(row=2, column=0, columnspan=3, sticky='nsew')
        idlabel = tkinter.Label(frame3, text='Book Id :', font=("times", 12, "bold"), fg='white', bg='dark slate gray',
                                relief="ridge")
        idlabel.grid(row=3, column=0, sticky='nsew')
        identry = tkinter.Label(frame3, text=self.bookid, font=("times", 12, "bold"), fg='white', bg='dark slate gray',
                                relief="ridge")
        identry.grid(row=3, column=1, sticky='nsew')
        booktitle = tkinter.Label(frame3, text='Book Title:', font=("times", 12, "bold"), fg='white',
                                  bg='dark slate gray', relief="ridge")
        booktitle.grid(row=4, column=0, sticky='nsew')
        titleentry = tkinter.Entry(frame3)
        titleentry.grid(row=4, column=1, sticky='nsew')
        author = tkinter.Label(frame3, text='Author:', font=("times", 12, "bold"), fg='white', bg='dark slate gray',
                               relief="ridge")
        author.grid(row=5, column=0, sticky='nsew')
        authorentry = tkinter.Entry(frame3)
        authorentry.grid(row=5, column=1, sticky='nsew')
        status = tkinter.Label(frame3, text='Status:', font=("times", 12, "bold"), fg='white', bg='dark slate gray',
                               relief="ridge")
        status.grid(row=6, column=0, sticky='nsew')
        statusentry = tkinter.Spinbox(frame3, values=('A', 'NA'), width=2)
        statusentry.grid(row=6, column=1, sticky='nsew')

        def save():
            try:
                self.title = titleentry.get()
                self.author = authorentry.get()
                self.status = statusentry.get()
                if self.title and self.author and self.status:
                    if filepath.exists():
                        with open('book.csv', 'a', newline='') as bookfile:
                            fieldnames = ['Bookid', 'Book title', 'Author', 'Status']
                            book = csv.DictWriter(bookfile, fieldnames=fieldnames)
                            book.writerow(
                                {'Bookid': self.bookid, 'Book title': self.title.title(), 'Author': self.author.title(),
                                 'Status': self.status.upper()})

                    else:
                        fieldnames = ['Bookid', 'Book title', 'Author', 'Status']
                        with open('book.csv', 'w', newline='') as bookfile:
                            b = csv.DictWriter(bookfile, fieldnames=fieldnames)
                            b.writeheader()
                            b.writerow(
                                {'Bookid': self.bookid, 'Book title': self.title.title(), 'Author': self.author.title(),
                                 'Status': self.status.upper()})
                    titleentry.delete(0, tkinter.END)  # Reset book title field
                    authorentry.delete(0, tkinter.END)  # Reset author field
                    statusentry.delete(0, tkinter.END)  # Reset status field
                    messagebox.showinfo("Success", "Book details saved successfully.")
                else:
                    messagebox.showerror(title='Error', message='Fields cannot be empty')
            except IOError:
                messagebox.showerror("Error", "Error while writing to file")
            except Exception:
                messagebox.showerror("Error", "An unexpected error occurred")

        # save button for books
        save = tkinter.Button(frame3, command=save, text='Save', font=("times", 12, "bold"), fg='white',
                              bg='dark slate gray', relief="raised", activebackground="saddle brown",
                              activeforeground="yellow")
        save.grid(row=7, column=0, sticky='nsew', pady=5)

        def reset():
            n = random.randint(1, 999)  # creating a unique bookid
            b = 'VI' + str(n)
            identry = tkinter.Label(frame3, text=b, font=("times", 12, "bold"), fg='white', bg='dark slate gray',
                                    relief="ridge")
            identry.grid(row=3, column=1, sticky='nsew')
            titleentry.delete(0, tkinter.END)  # Reset book title field
            authorentry.delete(0, tkinter.END)  # Reset author field
            statusentry.delete(0, tkinter.END)  # Reset status field

    ###############Reset and Exit button for  add books##############
        resetfield=tkinter.Button(frame3,command=reset,text='Reset',font=("times", 12, "bold"),fg='white',bg='dark slate gray',relief="raised",activebackground="saddle brown",activeforeground="yellow")
        resetfield.grid(row=7,column=1,sticky='nsew',pady=5)
        addexit=tkinter.Button(frame3,command=frame3.destroy,text='Exit',font=("times", 12, "bold"),fg='white',bg='dark slate gray',relief="raised",activebackground="saddle brown",activeforeground="yellow")
        addexit.grid(row=7,column=2,sticky='nsew',pady=5)

    def delbook(self):

        frame3 = tkinter.LabelFrame(window, width=800, height=450, bg='PeachPuff4')  # frame 3
        frame3.grid(row=2, columnspan=2, sticky='nsew', padx=10)
        head = tkinter.Label(frame3, text='******You can delete books******', font=("times", 14, "bold"))
        head.grid(row=2, column=0, columnspan=3, sticky='nsew', pady=5)

        idlabel = tkinter.Label(frame3, text='Book Title :', font=("times", 12, "bold"), fg='white',
                                bg='dark slate gray', relief="sunken")
        idlabel.grid(row=3, column=0, sticky='nsew')
        book = []
        with open('book.csv', 'r') as bfile:
            b = DictReader(bfile)
            for i in b:
                a = i['Book title']
                book.append(a)

        def show(*args):

            bk = clicked.get()
            id = ''
            with open('book.csv', 'r') as bfile:
                b = DictReader(bfile)
                for i in b:
                    if i['Book title'] == bk:
                        id = i['Bookid']
            found = False
            newfound = False
            # creating a temp file as original
            with open('book.csv', 'r', newline='') as book1file, \
                    open('tempbook.csv', mode='w') as copyfile:
                bid = csv.DictReader(book1file)
                fieldnames = bid.fieldnames
                writer = csv.DictWriter(copyfile, fieldnames)
                writer.writeheader()
                for item in bid:
                    if item['Bookid'] == id:
                        au = item['Author']
                        st = item['Status']
                        booktitle = tkinter.Label(frame3, text="Book Id", font=("times", 12, "bold"), fg='white',
                                                  bg='dark slate gray', relief="sunken")
                        booktitle.grid(row=4, column=0, sticky='nsew')
                        bookt = tkinter.Label(frame3, text=id, relief='solid')
                        bookt.grid(row=4, column=1, sticky='nsew')
                        bookauth = tkinter.Label(frame3, text="Author", font=("times", 12, "bold"), fg='white',
                                                 bg='dark slate gray', relief="sunken")
                        bookauth.grid(row=5, column=0, sticky='nsew')
                        bookau = tkinter.Label(frame3, text=au, relief='solid')
                        bookau.grid(row=5, column=1, sticky='nsew')
                        bookstat = tkinter.Label(frame3, text="Status", font=("times", 12, "bold"), fg='white',
                                                 bg='dark slate gray', relief="sunken")
                        bookstat.grid(row=6, column=0, sticky='nsew')
                        bookst = tkinter.Label(frame3, text=st, relief='solid')
                        bookst.grid(row=6, column=1, sticky='nsew')
                        found = True
                    elif item['Bookid'] != id:
                        writer.writerow(item)  # writes the other files into new csv except for the matching one
                        newfound = True

                if not found:
                    messagebox.showerror(title='Error', message='No Book in that ID')

        clicked = tkinter.StringVar(frame3)
        clicked.set(book[0])
        bookentry = OptionMenu(frame3, clicked, *book)
        bookentry.grid(row=3, column=1, sticky='nsew')
        clicked.trace_add("write", show)

        def delcopy():  # DElete button
            import os
            os.replace('tempbook.csv', 'book.csv')  # replaces the original data file with the content of new csv file
            messagebox.showerror(title='Success', message='Book deleted')

        # del and exit buttons
        delbutton = tkinter.Button(frame3, command=delcopy, text='Delete', font=("times", 12, "bold"), fg='white',
                                   bg='dark slate gray', relief="raised", activebackground="saddle brown",
                                   activeforeground="yellow")
        delbutton.grid(row=7, column=1, sticky='nsew', pady=5)
        delexit = tkinter.Button(frame3, command=frame3.destroy, text='Exit', font=("times", 12, "bold"), fg='white',
                                 bg='dark slate gray', relief="raised", activebackground="saddle brown",
                                 activeforeground="yellow")
        delexit.grid(row=7, column=2, sticky='nsew', pady=5)
    def searchauthor(self):
        author=[]
        frame3 = tkinter.LabelFrame(window, width=700, height=450, bg='PeachPuff4')
        frame3.grid(row=2, columnspan=2, sticky='nsew',padx=10)
        head=tkinter.Label(frame3,text='******Search Books by Authors******',font=("times", 14, "bold"))
        head.grid(row=2,column=0,columnspan=3,sticky='nsew',pady=5)
        auth=tkinter.Label(frame3,text='Author:',font=("times", 12, "bold"),fg='white',bg='gray24',relief="ridge")
        auth.grid(row=3,column=0,sticky='nsew')

        with open('book.csv','r',newline='') as bookfile:
            b=DictReader(bookfile)
            for item in b:
                a=item['Author']
                author.append(a)
        def selected(*args):
            ch=clicked.get()
            with open('book.csv', 'r',newline='') as book1file:
                b1 = DictReader(book1file)
                for item in b1:
                    if item['Author']==ch:
                        au = item['Bookid']
                        nm = item['Book title']
                        st = item['Status']
                        bookid = tkinter.Label(frame3, text="Book Id",font=("times", 12, "bold"),fg='white',bg='gray24',relief="ridge")
                        bookid.grid(row=4, column=0, sticky='nsew')
                        bookid = tkinter.Label(frame3, text=au,relief='solid')
                        bookid.grid(row=4, column=1, sticky='nw')
                        booktitle = tkinter.Label(frame3, text="Book Title",font=("times", 12, "bold"),fg='white',bg='gray24',relief="ridge")
                        booktitle.grid(row=5, column=0, sticky='nsew')
                        booktitle = tkinter.Label(frame3, text=nm,relief='solid')
                        booktitle.grid(row=5, column=1, sticky='nw')
                        bookstat = tkinter.Label(frame3, text="Status",font=("times", 12, "bold"),fg='white',bg='gray24',relief="ridge")
                        bookstat.grid(row=6, column=0, sticky='nsew')
                        bookstat = tkinter.Label(frame3, text=st,relief='solid')
                        bookstat.grid(row=6, column=1, sticky='nw')
        clicked = tkinter.StringVar(frame3)
        clicked.set(author[0])
        authentry = OptionMenu(frame3, clicked,*author)
        authentry.grid(row=3, column=1,sticky='nw')
        clicked.trace_add("write", selected)
        delexit=tkinter.Button(frame3,command=frame3.destroy,text='Exit',font=("times", 12, "bold"),fg='white',bg='gray24',relief="raised",activebackground="saddle brown",activeforeground="yellow")
        delexit.grid(row=7,column=1,sticky='nsew',pady=5)

    def searchtitle(self):
        title = []
        frame3 = tkinter.LabelFrame(window, width=700, height=450, bg='PeachPuff4')
        frame3.grid(row=2, columnspan=2, sticky='nsew', padx=10)
        head = tkinter.Label(frame3, text='******Search Books by Title******', font=("times", 14, "bold"))
        head.grid(row=2, column=0, columnspan=3, sticky='nsew', pady=5)
        auth = tkinter.Label(frame3, text='Title:', font=("times", 12, "bold"), fg='white', bg='gray24', relief="ridge")
        auth.grid(row=3, column=0, sticky='nsew')

        with open('book.csv', 'r', newline='') as bookfile:
            b = DictReader(bookfile)
            for item in b:
                a = item['Book title']
                title.append(a)

        def selected(*args):
            ch = clicked.get()
            with open('book.csv', 'r', newline='') as book1file:
                b1 = DictReader(book1file)
                for item in b1:
                    if item['Book title'] == ch:
                        au = item['Bookid']
                        nm = item['Author']
                        st = item['Status']
                        bookid = tkinter.Label(frame3, text="Book Id", font=("times", 12, "bold"), fg='white',
                                               bg='gray24', relief="ridge")
                        bookid.grid(row=4, column=0, sticky='nsew')
                        bookid = tkinter.Label(frame3, text=au, relief='solid')
                        bookid.grid(row=4, column=1, sticky='nsew')
                        bookauth = tkinter.Label(frame3, text="Author:", font=("times", 12, "bold"), fg='white',
                                                 bg='gray24', relief="ridge")
                        bookauth.grid(row=5, column=0, sticky='nsew')
                        bookauth = tkinter.Label(frame3, text=nm, relief='solid')
                        bookauth.grid(row=5, column=1, sticky='nsew')
                        bookstat = tkinter.Label(frame3, text="Status", font=("times", 12, "bold"), fg='white',
                                                 bg='gray24', relief="ridge")
                        bookstat.grid(row=6, column=0, sticky='nsew')
                        bookstat = tkinter.Label(frame3, text=st, relief='solid')
                        bookstat.grid(row=6, column=1, sticky='nsew')

        clicked = tkinter.StringVar(frame3)
        clicked.set(title[0])
        titleentry = OptionMenu(frame3, clicked, *title)
        titleentry.grid(row=3, column=1, sticky='nw')
        clicked.trace_add("write", selected)
        titleexit = tkinter.Button(frame3, command=frame3.destroy, text='Exit', font=("times", 12, "bold"), fg='white',
                                   bg='gray24', relief="raised", activebackground="saddle brown",
                                   activeforeground="yellow")
        titleexit.grid(row=7, column=1, sticky='nsew', pady=5)

class Member:
    def __init__(self, name):
        n = random.randint(1, 999)  # creating a unique bookid
        b = 'MV' + str(n)
        self.memid = b
        self.name = name
        self.phone = ''
        self.email=''

    def addmem(self):
        # Frame for addition
        frame3 = tkinter.LabelFrame(window, width=700, height=450, bg='PeachPuff4')
        frame3.grid(row=2, columnspan=2, sticky='nsew', padx=10)
        head = tkinter.Label(frame3, text='******Become Members by Adding details******', font=("times", 14, "bold"))
        head.grid(row=2, column=0, columnspan=3, sticky='nsew', pady=5)

        idlabel = tkinter.Label(frame3, text='Membership Id ', font=("times", 12, "bold"), fg='white', bg='salmon4',
                                relief="ridge")
        idlabel.grid(row=3, column=0, sticky='nsew')

        identry = tkinter.Label(frame3, text=self.memid, relief='solid')
        identry.grid(row=3, column=1, sticky='nsew')
        namelabel = tkinter.Label(frame3, text='Name:', font=("times", 12, "bold"), fg='white', bg='salmon4',
                                  relief="ridge")
        namelabel.grid(row=4, column=0, sticky='nsew')
        nameentry = tkinter.Entry(frame3, relief='solid')
        nameentry.grid(row=4, column=1, sticky='nsew')
        phno = tkinter.Label(frame3, text='Phone number:', font=("times", 12, "bold"), fg='white', bg='salmon4',
                             relief="ridge")
        phno.grid(row=5, column=0, sticky='nsew')
        phnoentry = tkinter.Entry(frame3, relief='solid')
        phnoentry.grid(row=5, column=1, sticky='nsew')
        email = tkinter.Label(frame3, text='Email:', font=("times", 12, "bold"), fg='white', bg='salmon4',
                              relief="ridge")
        email.grid(row=6, column=0, sticky='nsew')
        emailentry = tkinter.Entry(frame3, relief='solid')
        emailentry.grid(row=6, column=1, sticky='nsew')

        def reset():
            n = random.randint(1, 999)  # creating a unique bookid
            b = 'MV' + str(n)
            identry = tkinter.Label(frame3, text=b, relief='solid')
            identry.grid(row=3, column=1, sticky='nsew')

            nameentry.delete(0, tkinter.END)  # Reset book title field
            phnoentry.delete(0, tkinter.END)  # Reset author field
            emailentry.delete(0, tkinter.END)  # Reset status field

        def save():
            self.name = nameentry.get()
            self.phone = phnoentry.get()
            self.email = emailentry.get()
            if self.name and self.phone and self.email:
                if filepath2.exists():
                    with open('member.csv', 'a', newline='') as memfile:
                        fieldnames = ['Memid', 'Mem name', 'Phoneno', 'Email']
                        m = csv.DictWriter(memfile, fieldnames=fieldnames)
                        m.writerow(
                            {'Memid': self.memid, 'Mem name': self.name.title(), 'Phoneno': self.phone, 'Email': self.email.lower()})
                    nameentry.delete(0, tkinter.END)  # Reset book title field
                    phnoentry.delete(0, tkinter.END)  # Reset author field
                    emailentry.delete(0, tkinter.END)  # Reset status field
                else:
                    fieldnames = ['Memid', 'Mem name', 'Phoneno', 'Email']
                    with open('member.csv', 'w', newline='') as memfile:
                        m = csv.DictWriter(memfile, fieldnames=fieldnames)
                        m.writeheader()
                        m.writerow(
                            {'Memid': self.memid, 'Mem name': self.name.title(), 'Phoneno': self.phone, 'Email': self.email.lower()})
                    nameentry.delete(0, tkinter.END)  # Reset book title field
                    phnoentry.delete(0, tkinter.END)  # Reset author field
                    emailentry.delete(0, tkinter.END)  # Reset status field
                messagebox.showinfo("Success", "Member details saved successfully.")
            else:
                messagebox.showerror(title='Error', message='Fields cannot be empty')

        save = tkinter.Button(frame3, text='Save', command=save, font=("times", 12, "bold"), fg='white', bg='salmon4',
                              relief="raised", activebackground="saddle brown", activeforeground="yellow")
        save.grid(row=7, column=0, sticky='nsew', pady=5)
        # After saving, reset fields

        resetfield = tkinter.Button(frame3, command=reset, text='Reset', font=("times", 12, "bold"), fg='white',
                                    bg='salmon4', relief="raised", activebackground="saddle brown",
                                    activeforeground="yellow")
        resetfield.grid(row=7, column=1, sticky='nsew', pady=5)
        addexit = tkinter.Button(frame3, command=frame3.destroy, text='Exit', font=("times", 12, "bold"), fg='white',
                                 bg='salmon4', relief="raised", activebackground="saddle brown",
                                 activeforeground="yellow")
        addexit.grid(row=7, column=2, sticky='nsew', pady=5)

    def delmem(self):
        frame3 = tkinter.LabelFrame(window, width=800, height=450, bg='PeachPuff4')  # frame 3
        frame3.grid(row=2, columnspan=2, sticky='nsew', padx=10)
        head = tkinter.Label(frame3, text='******You Can Delete Library Members******', font=("times", 14, "bold"))
        head.grid(row=2, column=0, columnspan=3, sticky='nsew', pady=5)
        idlabel = tkinter.Label(frame3, text='Member name', font=("times", 12, "bold"), fg='white', bg='salmon4',
                                relief="ridge")
        idlabel.grid(row=3, column=0, sticky='nsew')
        mem = []
        with open('member.csv', 'r') as mfile:
            b = DictReader(mfile)
            for i in b:
                a = i['Mem name']
                mem.append(a)

        def show(*args):
            found = False
            newfound = False
            ch = clicked.get()
            id = ''
            with open('member.csv', 'r') as mfile:
                b = DictReader(mfile)
                for i in b:
                    if i['Mem name'] == ch:
                        id = i['Memid']
            with open('member.csv', 'r', newline='') as memfile, \
                    open('tempmem.csv', mode='w') as copyfile:  # creating a csv file
                mid = csv.DictReader(memfile)
                fieldnames = mid.fieldnames
                writer = csv.DictWriter(copyfile, fieldnames)  # temp csv file with the same fields
                writer.writeheader()
                for item in mid:
                    print(item)
                    if item['Memid'] == id:
                        phone = item['Phoneno']
                        em = item['Email']
                        memid = tkinter.Label(frame3, text="Member Id", font=("times", 12, "bold"), fg='white',
                                              bg='salmon4', relief="ridge")
                        memid.grid(row=4, column=0, sticky='nsew')
                        memid1 = tkinter.Label(frame3, text=id, relief='solid')
                        memid1.grid(row=4, column=1, sticky='nsew')
                        ph = tkinter.Label(frame3, text="Phone number", font=("times", 12, "bold"), fg='white',
                                           bg='salmon4', relief="ridge")
                        ph.grid(row=5, column=0, sticky='nsew')
                        ph1 = tkinter.Label(frame3, text=phone, relief='solid')
                        ph1.grid(row=5, column=1, sticky='nsew')
                        email = tkinter.Label(frame3, text="Email", font=("times", 12, "bold"), fg='white',
                                              bg='salmon4', relief="ridge")
                        email.grid(row=6, column=0, sticky='nsew')
                        email1 = tkinter.Label(frame3, text=em, relief='solid')
                        email1.grid(row=6, column=1, sticky='nsew')
                        found = True
                    elif item['Memid'] != id:
                        writer.writerow(item)  # writes the other files into new csv except for the delete file
                        newfound = True

                if not found:
                    messagebox.showerror(title='Error', message='Library Member deleted')

        clicked = tkinter.StringVar(frame3)
        clicked.set(mem[0])
        mementry = OptionMenu(frame3, clicked, *mem)
        mementry.grid(row=3, column=1, sticky='nsew')
        clicked.trace_add("write", show)

        def delcopy():  # DElete button
            import os
            os.replace('tempmem.csv', 'member.csv')  # replaces the original data file with the content of new csv file
            messagebox.showerror(title='Success', message='Member deleted')

        delbutton = tkinter.Button(frame3, command=delcopy, text='Delete', font=("times", 12, "bold"), fg='white',
                                   bg='salmon4', relief="raised", activebackground="saddle brown",
                                   activeforeground="yellow")
        delbutton.grid(row=7, column=1, sticky='nsew', pady=5)
        delexit = tkinter.Button(frame3, command=frame3.destroy, text='Exit', font=("times", 12, "bold"), fg='white',
                                 bg='salmon4', relief="raised", activebackground="saddle brown",
                                 activeforeground="yellow")
        delexit.grid(row=7, column=2, sticky='nsew', pady=5)

def loginwin():
    loginwindow=tkinter.Toplevel(window)
    loginwindow.geometry('200x100')
    loginwindow.title('Password window')
    loginwindow.grab_set()
    # Prevent the login window from being closed manually (clicking the 'X' button)
    loginwindow.protocol("WM_DELETE_WINDOW", lambda: None)
    username=tkinter.Label(loginwindow,text='Username')
    username.grid(row=0,column=0)
    userentry=tkinter.Entry(loginwindow)
    userentry.grid(row=0,column=1)

    password=tkinter.Label(loginwindow,text='Password')
    password.grid(row=1,column=0)
    passentry=tkinter.Entry(loginwindow)
    passentry.grid(row=1,column=1)
    def validate():
        if userentry.get()=='admin' and passentry.get()=='password':
            messagebox.showinfo(title='Login Success',message='Successful Login')
            loginwindow.destroy()
            #addbook1()#calling function for adding books
        else:
            messagebox.showerror(title='Error',message='Login failed')


    check=tkinter.Button(loginwindow,text='Login',command=lambda :[validate()])
    check.grid(row=2,column=1)

def savechk():
    #currentdate = datetime.now().date()#current date
    #duedate = currentdate + timedelta(weeks=1)#Adding one week to current date
    nmid=[]
    id1=''
    ids=[]
    bookrow=[]
    with open('chkout.txt','r') as cfile:
        for i in cfile:
            a=i.split()[0]
            nmid.append(a)
    with open('chkout1.txt','r') as c1file:
        for i in c1file:
            id1=i.strip('\n')
            ids.append(id1)
    fieldnames=['Memid','Mem name' ,'Bookid']
    with open('checkouts.csv','a',newline='') as chkfile:
        chk1=DictWriter(chkfile,fieldnames=fieldnames)
        if chkfile.tell() == 0:  # Check if the file is empty
            chk1.writeheader()
        for i in range(len(ids)):
            row1={'Memid':nmid[0],'Mem name':nmid[1],'Bookid':ids[i]}
            chk1.writerow(row1)

    with open('book.csv','r',newline='') as abook:
        reader=DictReader(abook)
        bookrow = list(reader)
    for bookid in ids:
        for r1 in bookrow:
            if r1['Bookid']==bookid:
                r1['Status']='NA'
    with open('book.csv', 'w', newline='') as abook:
        fieldnames = bookrow[0].keys()  # Get the fieldnames from the first row
        writer = csv.DictWriter(abook, fieldnames=fieldnames)
        writer.writeheader()  # Write the header
        writer.writerows(bookrow)  # Write all rows, including updated ones
    os.remove('chkout.txt')
    os.remove('chkout1.txt')


def checkout():
    books=[]    # to store booktitle in list for option menu
    members=[]    # to store membernames in list for option menu
    mid = ''  # to store the memberid checked out
    nm = '' #to store membername
    # and write the above 2 variables in chkout.txt file
    id=''   # to store the bookid checked out
    rows=[]    # to store each row of books dictionary in list
    # These are the heading for the frame
    frame3 = tkinter.LabelFrame(window, width=800, height=450, bg='PeachPuff4')# frame 3
    frame3.grid(row=2, columnspan=2, sticky='nsew',padx=10)
    head=tkinter.Label(frame3,text='******Library Checkouts******',font=("times", 14, "bold"))
    head.grid(row=2,column=0,columnspan=3,sticky='nsew',pady=5)
    # Opening the book.csv file and storing the book title in list called books
    with open('book.csv','r') as cbook:
        chk=DictReader(cbook)
        for book in chk:
            a=book['Book title']
            books.append(a)
    # Opening the member.csv file and storing the member name in members list
    with open('member.csv', 'r', newline='') as memfile:
        member = DictReader(memfile)
        for m in member:
            l=m['Mem name']
            members.append(l)
    # the dropdown method called for member name
    def selected1(*args):
        ch1=clicked1.get()
        with open('member.csv', 'r',newline='') as mem1file:
            m1=DictReader(mem1file)
            for item in m1:
                if item['Mem name']==str(ch1):
                    mid=item['Memid']
                    nm=item['Mem name']
                    # storing the variables id and name in chkout.txt file
                    with open('chkout.txt', 'a', newline='') as cfile:
                        cfile.write(mid.strip() + '\n')
                        cfile.write(nm.strip() + '\n')
                elif item['Mem name']=='':
                    messagebox.showerror(title='Error', message='Select Member name')
        # displaying the selected member id
        memberid1 = tkinter.Label(frame3, text=mid)
        memberid1.grid(row=4, column=1, sticky='nsew')

    # the dropdown method called for Book title
    def selected(*args):
        ch=clicked.get()
        #Opening the book.csv and storing the data in memory
        with open('book.csv', 'r',newline='') as book1file:
            b1 = DictReader(book1file)
            rows = list(b1)  # Read all rows into memory
                # Modify the required field in the row with the matching Bookid
            bookfound=False

        for row in rows:
            if row['Book title'] == ch and row['Status']=='A':
                bookfound=True
                messagebox.showinfo(title='Book', message='Book is available')
                ans=messagebox.askquestion('Checkout',"Do you want to checkout ?")
                if ans=='yes':
                    id=row['Bookid'] # storing the bookid in variable id
                    bid=id
                    ans1 = messagebox.askquestion('Checkout', "Do you want to checkout more books ?")
                    with open('chkout1.txt', 'a', newline='') as cfile:
                        cfile.write(id.strip() + '\n')
                    savecheckout.focus_set()
                    if ans1=='no':
                        break
                    else:
                        bookentry.focus_set()
                        continue
                else:
                    id=''
                    break

        # checking whether the book is not available
        if not bookfound:
            messagebox.showerror(title='Error', message='Book not available')
            savecheckout.config(state="disabled")
            chkoutexit.focus_set()

    # calling all the buttons in frame 3 for checkouts
    memlabel = tkinter.Label(frame3, text='Member Name', font=("times", 12, "bold"), fg='white', bg='LightPink4',relief="ridge")
    memlabel.grid(row=3, column=0, sticky='nw')
    clicked1 = tkinter.StringVar(frame3)
    clicked1.set(members[0]) # calling the members list here
    mementry = OptionMenu(frame3, clicked1, *members)
    mementry.grid(row=3, column=1)
    clicked1.trace_add("write", selected1)

    titlelabel=tkinter.Label(frame3,text='Title',font=("times", 12, "bold"),fg='white',bg='LightPink4',relief="ridge")
    titlelabel.grid(row=5,column=0,sticky='nsew')
    #dropdown button for book title
    clicked = tkinter.StringVar(frame3)
    clicked.set(books[0])
    bookentry = OptionMenu(frame3, clicked,*books)# calling the books list here
    bookentry.grid(row=5, column=1)
    clicked.trace_add("write", selected)
    #this method is called in exit
    def exiting():
        if os.path.exists('chkout.txt'):
            os.remove('chkout.txt')
        frame3.destroy()
    memberid = tkinter.Label(frame3, text="Member Id",font=("times", 12, "bold"),fg='white',bg='LightPink4',relief="ridge")
    memberid.grid(row=4, column=0, sticky='nsew')
    savecheckout = tkinter.Button(frame3, text='Save CheckOuts', command=savechk,font=("times", 12, "bold"),fg='white',bg='LightPink4',relief="raised",activebackground="saddle brown",activeforeground="yellow")
    savecheckout.grid(row=6, column=1, sticky='nsew')
    chkoutexit=tkinter.Button(frame3,command=exiting,text='Exit',font=("times", 12, "bold"),fg='white',bg='LightPink4',relief="raised",activebackground="saddle brown",activeforeground="yellow")
    chkoutexit.grid(row=6,column=2,sticky='nsew')

def returncheck():
    #Checking whether there are entries in checkouts file
    with open('checkouts.csv','r') as file:
        c = len(file.readlines())
        if c <2:
            messagebox.showerror(title='Error', message='No books are checked out')
        elif c>=2:
            returns1()

def returns1():
    frame3 = tkinter.LabelFrame(window, width=800, height=450, bg='PeachPuff4')# frame 3
    frame3.grid(row=2, columnspan=2, sticky='nsew',padx=10)
    # heading for Returns
    head=tkinter.Label(frame3,text='******Library Returns******',font=("times", 14, "bold"))
    head.grid(row=2,column=0,columnspan=3,sticky='nsew',pady=5)
    names=[] #to store bookid for dropdown
    # storing the bookid in names list for dropdown
    with open('checkouts.csv','r') as retfile:
        rows=DictReader(retfile)
        for row in rows:
            a=(row['Bookid'])
            names.append(a)

    def saveret():
        os.replace('tempret.csv', 'checkouts.csv')  # replaces the original data file with the content of new csv file
        os.remove('return.txt')
        messagebox.showinfo(title='Success', message='Saved Returns')

    #dropdown for bookid
    def selected(*args):
        ch=clicked.get()
        filefound=False
        with open('book.csv','r') as retfile:
            b1=csv.DictReader(retfile)
            rows1=list(b1)  # Read all rows into memory
        for row in rows1:
            if row['Bookid'] ==ch and row['Status']=='NA':
                filefound=True
                bnm=row['Book title']
                # storing the book title in a varible are calling in msgbox
                ans = messagebox.askquestion('Returns',message="Do you want to return "+bnm+"?")
                #changing the status into A
                if ans=='yes':
                    row['Status']='A'
                else:
                    break
        if not filefound:
            messagebox.showerror(title='Error', message='Book already returned')
            return
        # writing the changed status into book.csv
        with open('book.csv', 'w') as csvfile:
            fieldnames = ['Bookid', 'Book title', 'Author', 'Status']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()  # Write the header
            writer.writerows(rows1)
        with open('return.txt','w') as retfile:
            retfile.write(ch)
        with open('return.txt', 'r') as retfile:
            bid = retfile.readline().strip()
        found=False
        with open('checkouts.csv', 'r', newline='') as chkfile, \
            open('tempret.csv', mode='w', newline='') as copyfile:  # creating a csv file
            chkid = csv.DictReader(chkfile)
            fieldnames = chkid.fieldnames
            writer = csv.DictWriter(copyfile, fieldnames)  # temp csv file with the same fields
            writer.writeheader()
            for item in chkid:
                if item['Bookid'] == bid:
                    id = item['Memid']
                    nm = item['Mem name']
                    bnm1 = tkinter.Label(frame3, text="Book Title ", font=("times", 12, "bold"), fg='white',
                                         bg='LightPink4', relief="ridge")
                    bnm1.grid(row=3, column=0, sticky='nsew')
                    bnm2 = tkinter.Label(frame3,text=bnm)
                    bnm2.grid(row=3, column=1, sticky='nsew')
                    memname = tkinter.Label(frame3, text="Member Name ",font=("times", 12, "bold"),fg='white',bg='LightPink4',relief="ridge")
                    memname.grid(row=4, column=0, sticky='nsew')
                    memname1=tkinter.Label(frame3,text=nm)
                    memname1.grid(row=4, column=1, sticky='nw')
                    delbutton = tkinter.Button(frame3, text='Save Returns', command=saveret,font=("times", 12, "bold"),fg='white',bg='LightPink4',relief="raised",activebackground="saddle brown",activeforeground="yellow")
                    delbutton.grid(row=6, column=1, sticky='nsew')
                    retexit = tkinter.Button(frame3, command=frame3.destroy, text='Exit', font=("times", 12, "bold"),
                                                fg='white', bg='LightPink4', relief="raised",
                                                activebackground="saddle brown", activeforeground="yellow")
                    retexit.grid(row=6, column=2, sticky='nsew')

                    found=True
                elif item['Bookid']!=bid:
                    writer.writerow(item)# writes the other files into new csv except for the delete file
            if not found:
                messagebox.showerror(title='Error', message='Book not found')

    namelabel = tkinter.Label(frame3, text='Book ID',font=("times", 12, "bold"),fg='white',bg='LightPink4',relief="ridge")
    namelabel.grid(row=3, column=0, sticky='nsew')
    clicked = tkinter.StringVar(frame3)
    clicked.set(names[0])
    nameentry = OptionMenu(frame3, clicked, *names)
    nameentry.grid(row=3, column=1,sticky='nsew')
    clicked.trace_add("write", selected)


# The initial look of the Library site with buttons
window=tkinter.Tk()
window.title('Library')
window.geometry('800x500+100+10')  #1000 and 700 are width and height, 100 and 10 are the left, right space and top
window.config(bg='bisque2')

#Frame1 Title frame
frame1=tkinter.LabelFrame(window,width=700,height=50,bg='PeachPuff4')
frame1.grid(row=0,columnspan=2,sticky='nsew',padx=10)
frame1.grid_propagate(0)
label1=tkinter.Label(frame1,text="Welcome to Vision Library", font=("times", 20),bg='PeachPuff4')
label1.grid(row=0,columnspan=2,sticky='nsew')

#Frame2 contains all buttons sticky nsew streches the buttons uniformly
frame2=tkinter.LabelFrame(window,width=700,height=200,bg='seashell4')
frame2.grid(row=1,columnspan=2,sticky='nsew',padx=10,pady=10)
frame2.grid_propagate(0)

library_instance = Library('')
#This is creating an instance of the class Library with an empty string ('')
#being passed as an argument to the constructor of the Library class.
addbook=tkinter.Button(frame2,text='Add Book',font=("times", 14, "bold"),fg='white',bg='dark slate gray',relief="raised",activebackground="saddle brown",activeforeground="yellow",command=lambda:[loginwin(),library_instance.addbook()])
addbook.grid(row=1,column=0,sticky='nsew', padx=5, pady=5)
delbook=tkinter.Button(frame2,text='Delete Book',font=("times", 14, "bold"),fg='white',bg='dark slate gray',relief="raised",activebackground="saddle brown",activeforeground="yellow",command=lambda :[loginwin(),library_instance.delbook()])
delbook.grid(row=1,column=1,sticky='nsew', padx=5, pady=5)
search=tkinter.Label(frame2,text='Search',font=("times", 14, "bold"),fg='white',bg='seashell4',relief="sunken",activebackground="darkgrey",activeforeground="yellow")
search.grid(row=2,column=0,sticky='nsew', padx=5, pady=5)
auth=tkinter.Button(frame2,text='By Author',font=("times", 14, "bold"),fg='white',bg='wheat4',relief="raised",activebackground="saddle brown",activeforeground="yellow",command=library_instance.searchauthor)
auth.grid(row=2,column=1,sticky='nsew', padx=5, pady=5)
title=tkinter.Button(frame2,text='By Title',font=("times", 14, "bold"),fg='white',bg='wheat4',relief="raised",activebackground="darkgreen",activeforeground="yellow",command=library_instance.searchtitle)
title.grid(row=2,column=2,sticky='nsew', padx=5, pady=5)

member_instance=Member('')
#This is creating an instance of the class Member with an empty string ('')
#being passed as an argument to the constructor of the Member class.
membership=tkinter.Label(frame2,text='Membership',font=("times", 14, "bold"),fg='white',bg='seashell4',relief="sunken",activebackground="darkgreen",activeforeground="yellow")
membership.grid(row=3,column=0,sticky='nsew', padx=5, pady=5)
addmember=tkinter.Button(frame2,text='Add',font=("times", 14, "bold"),fg='white',bg='salmon4',relief="raised",activebackground="darkgreen",activeforeground="yellow",command=member_instance.addmem)
addmember.grid(row=3,column=1,sticky='nsew', padx=5, pady=5)
delmember=tkinter.Button(frame2,text='Delete',font=("times", 14, "bold"),fg='white',bg='salmon4',relief="raised",activebackground="darkgreen",activeforeground="yellow",command=member_instance.delmem)
delmember.grid(row=3,column=2,sticky='nsew', padx=5, pady=5)

# the checkout method is called here
checkout=tkinter.Button(frame2,text='CheckOuts',font=("times", 14, "bold"),fg='white',bg='LightPink4',relief="raised",activebackground="darkgreen",activeforeground="yellow",command=checkout)
checkout.grid(row=4,column=0,sticky='nsew', padx=5, pady=5)
returns=tkinter.Button(frame2,text='Returns',font=("times", 14, "bold"),fg='white',bg='LightPink4',relief="raised",activebackground="darkgreen",activeforeground="yellow",command=returncheck)
returns.grid(row=4,column=1,sticky='nsew', padx=5, pady=5)

#booktitle = tkinter.Label(frame3, text="Book name: %s" % item['Book name']) To place both key and value
window.mainloop()