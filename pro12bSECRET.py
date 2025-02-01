import mysql.connector as sqor
mycon=sqor.connect(host="localhost",user="root",passwd="system",database="computerproject")
c=mycon.cursor()
print('\t \t \t \t WELCOME TO BIBLIOPHILES LIBRARY')
def stock():
    while True:
        print('''STOCK MENU:
1.INSERT
2.UPDATE
3.DELETE
4.DISPLAY
5.SEARCH
6.EXIT''')
        ch=int(input("ENTER YOUR CHOICE:"))
        if ch==1:
            sno=int(input("ENTER SERIAL NO.:"))
            bookno=int(input("ENTER BOOK NO.:"))
            bookname=input("ENTER BOOK NAME:")
            qty=int(input("ENTER QUANTITY:"))
            aut=input("ENTER AUTHOR:")
            pub=input("ENTER PUBLISHER:")
            cn=int(input("ENTER CLASSIFICATION NO.:"))
            source=input("ENTER SOURCE:")
            pri=int(input("ENTER PRICE:"))
            bingo=int(input("ENTER BILL NO.:"))
            st="insert into STOCK()VALUES(%s,'%s',%s,%s,'%s','%s',%s,'%s',%s,%s)"%(sno,bookname,bookno,qty,aut,pub,cn,source,pri,bingo)
            c.execute(st)
            mycon.commit()
        elif ch==2:
            a=input("ENTER COLUMN NAME TO BE UPDATED:")
            s=int(input("ENTER VALUE TO BE ASSIGNED:"))
            bookno=int(input("ENTER BOOK NO.:"))
            st="update STOCK set %s=%s where BOOK_NO=%s"%(a,s,bookno)
            c.execute(st)
            mycon.commit()
        elif ch==3:
            b=eval(input('ENTER BOOK NO. TO BE DELETED:'))
            st="delete from STOCK where BOOK_NO=%s"%(b,)
            c.execute(st)
            mycon.commit()
        elif ch==4:
            st="select *from stock"
            c.execute(st)
            f=c.fetchall()
            if f==[]:
                print("EMPTY TABLE")
            else:
                for i in f:
                    print(i)
        elif ch==5:
            bingo=int(input("ENTER BILL NO.:"))
            st="select *from stock where BILL_NO=%s"%(bingo,)
            c.execute(st)
            f=c.fetchall()
            if f==[]:
                print("BILL NO. DOESN'T EXIST")
            else:
                for i in f:
                    print(i)
        elif ch==6:
            break
        else:
            print("!!INVALID CHOICE!!")
def mem():
    while True:
        print('''MEMBERSHIP MENU:
1.INSERT
2.UPDATE
3.DELETE
4.DISPLAY
5.SEARCH
6.EXIT''')
        ch=int(input("ENTER YOUR CHOICE:"))
        if ch==1:
            sno=int(input("ENTER SERIAL NO.:"))
            regno=int(input("ENTER REGISTRATION NO.:"))
            name=input("ENTER NAME:")
            add=input("ENTER ADDRESS:")
            tom=input("ENTER TYPE OF MEMBERSHIP:")
            red=input("ENTER REGISTRATION DATE:")
            exp=input("ENTER EXPIRY DATE:")
            mail=input("ENTER EMAIL ID:")
            phone=int(input("ENTER PHONE NO:"))
            don=int(input("ENTER NO. OF BOOKS DONATED:"))
            dis=0
            if tom=='1YEAR' and don!=0:
                dis='10%'
            st="insert into MEMBERSHIP()VALUES(%s,%s,'%s','%s','%s','%s','%s','%s',%s,%s,'%s')"%(sno,regno,name,add,tom,red,exp,mail,phone,don,dis)
            c.execute(st)
            mycon.commit()
        elif ch==2:
            a=input("ENTER COLUMN TO BE UPDATED:")
            s=input("ENTER VALUE TO BE ASSIGNED:")
            regno=int(input("ENTER REGISTRATION NO.:"))
            st="update MEMBERSHIP set %s=%s where REGISTRATION_NO=%s"%(a,s,regno)
            c.execute(st)
            mycon.commit()
        elif ch==3:
            r=input('ENTER REGISTRATION NO. TO BE DELETED:')
            st="delete from MEMBERSHIP where REGISTRATION_NO='%s'"%(r,)
            c.execute(st)
            mycon.commit()
        elif ch==4:
            st="select *from membership"
            c.execute(st)
            f=c.fetchall()
            if f==[]:
                print("EMPTY TABLE")
            else:
                for i in f:
                    print(i)
        elif ch==5:
            rn=int(input("ENTER REGISTRATION NO.:"))
            st="select *from membership where REGISTRATION_NO=%s"%(rn,)
            c.execute(st)
            f=c.fetchall()
            if f==[]:
                print("REGISTRATION NO. DOESN'T EXIST")
            else:
                for i in f:
                    print(i)
        elif ch==6:
            break
        else:
            print("!!INVALID CHOICE!!")
def gen():
    while True:
        print('''BOOK MENU:
1.INSERT
2.UPDATE
3.DELETE
4.DISPLAY
5.SEARCH
6.EXIT''')
        ch=int(input("ENTER YOUR CHOICE:"))
        if ch==1:
            sno=int(input("ENTER SERIAL NO.:"))
            bookno=int(input("ENTER BOOK NO.:"))
            bookname=input("ENTER BOOK NAME:")
            genre=input("ENTER GENRE:")
            noc=int(input("NO. OF COPIES TO BE ADDED:"))
            nob=int(input("NO. OF COPIES BORROWED:"))
            nol=noc-nob
            st="insert into BOOK()VALUES(%s,%s,'%s','%s',%s,%s,%s)"%(sno,bookno,bookname,genre,noc,nob,nol)
            c.execute(st)
            mycon.commit()
        elif ch==2:
            a=input("ENTER COLUMN TO BE UPDATED:")
            s=input("ENTER NEW VALUE:")
            bookno=int(input("ENTER BOOK NO.:"))
            st="update BOOK set %s=%s where BOOK_NO=%s"%(a,s,bookno)
            c.execute(st)
            mycon.commit()
        elif ch==3:
            bn=input('ENTER BOOK NO. TO BE DELETED:')
            st="delete from BOOK where BOOK_NO=%s"%(bn,)
            c.execute(st)
            mycon.commit()
        elif ch==4:
            st="select *from book"
            c.execute(st)
            f=c.fetchall()
            if f==[]:
                print("EMPTY TABLE")
            else:
                for i in f:
                    print(i)
        elif ch==5:
            print('''MENU:
1.SEARCH BY GENRE
2.SEARCH BY NAME''')
            i=int(input('ENTER YOUR CHOICE:'))
            if i==1:
                g=input('ENTER GENRE:')
                st='select *from BOOK where GENRE="%s"'%(g,)
                c.execute(st)
                f=c.fetchall()
                if f==[]:
                    print("GENRE DOESN'T EXIST")
                else:
                    for i in f:
                        print(i)
            elif i==2:
                n=input('ENTER BOOK NAME:')
                st="select *from BOOK where BOOK_NAME='%s'"%(n,)
                c.execute(st)
                f=c.fetchall()
                if f==[]:
                    print("BOOK DOESN'T EXIST")
                else:
                    for i in f:
                        print(i)
        elif ch==6:
            break
        else:
            print("!!INVALID CHOICE!!")
def rec():
    while True:
        print('''RECORD MENU:
1.INSERT
2.UPDATE
3.DELETE
4.DISPLAY
5.SEARCH
6.EXIT''')
        ch=int(input("ENTER YOUR CHOICE:"))
        if ch==1:
            sno=int(input("ENTER SERIAL NO.:"))
            regno=int(input("ENTER REGISTRATION NO.:"))
            name=input("ENTER NAME:")
            bookname=input("ENTER BOOK NAME:")
            isdate=input("ENTER ISSUE DATE:")
            redate=input("ENTER RETURN DATE")
            ret=input("ENTER ACTUAL RETURN DATE:")
            if ret>redate:
                fee=20
            else:
                fee=0
            st="insert into RECORD()VALUES(%s,%s,'%s','%s','%s','%s','%s',%s)"%(sno,regno,name,bookname,isdate,redate,ret,fee)   
            c.execute(st)
            mycon.commit()
        elif ch==2:
            a=input("ENTER COLUMN TO BE UPDATED:")
            s=input("ENTER NEW VALUE:")
            regno=int(input("ENTER REGISTRATION NO.:"))
            st="update RECORD set %s=%s where REGISTRATION_NO=%s"%(a,s,regno)
            c.execute(st)
            mycon.commit()
        elif ch==3:
            rn=input('ENTER REGISTRATION NO. TO BE DELETED:')
            st="delete from RECORD where REGISTRATION_NO=%s"%(rn,)
            c.execute(st)
            mycon.commit()
        elif ch==4:
            st="select *from record"
            c.execute(st)
            f=c.fetchall()
            if f==[]:
                print("EMPTY TABLE")
            else:
                for i in f:
                    print(i)
        elif ch==5:
            rn=int(input("ENTER REGISTRATION NO.:"))
            st="select *from record where REGISTRATION_NO=%s"%(rn,)
            c.execute(st)
            f=c.fetchall()
            if f==[]:
                print("REGISTRATION NO. DOESN'T EXIST")
            else:
                for i in f:
                    print(i)
        elif ch==6:
            break
        else:
            print("!!INVALID CHOICE!!")

p=input('ENTER PASSWORD:')
if p=="SECRET" or "secret":
    while True:
        print('''MENU:
1.STOCK TABLE
2.MEMBERSHIP TABLE
3.GENRE TABLE
4.RECORD TABLE
5.EXIT''')
        ch=int(input("ENTER TABLE NO.:"))
        if ch==1:
            stock()
        elif ch==2:
            mem()
        elif ch==3:
            gen()
        elif ch==4:
            rec()
        elif ch==5:
            print("THANK YOU")
            break
        else:
            print("!!!!INVALID CHOICE!!!!")
else:
    print('!!!INCORRECT PASSWORD!!!')
    
