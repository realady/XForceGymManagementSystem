import mysql.connector as c
import tabulate as t
hostname=input("HOSTNAME FOR GYM : ")
username=input(f"ADMIN USERNAME FOR GYM ({hostname}) : ")
password=input(f"PASSWORD FOR {username}@{hostname} : ")
con=c.connect(host=hostname,user=username, passwd=password)
if con.is_connected():
    print("SUCCESSFULLY CONNECTED TO GYM'S DATABASE")
if con.is_connected():
    cursor=con.cursor()

    print('''

    |||||                                      |||||
    ||||        ----------------------          ||||
    |||========| XFORCE GYM MANGEMENT |==========|||
    ||||        ----------------------          ||||
    |||||                                      |||||

    ''')

    #CREATING IMPORTANT TABLES

    cursor.execute("CREATE DATABASE IF NOT EXISTS GYM;")
    cursor.execute("USE GYM")
    cursor.execute("CREATE TABLE IF NOT EXISTS FEES(SILVER INT, GOLD INT, PLATINUM INT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS LOGIN(USERNAME VARCHAR(25), PASSWORD VARCHAR(25) NOT NULL)")
    cursor.execute("CREATE TABLE IF NOT EXISTS MEMBER(ID INT, NAME VARCHAR(25), GENDER CHAR(1), CATAGORY VARCHAR(25), AMOUNT INT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS SNO(ID INT, DID INT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS TRAINER(ID INT, NAME VARCHAR(25), AGE VARCHAR(25), GENDER CHAR(1), SALARY INT)")
    con.commit()   
    cursor.execute("SELECT * FROM LOGIN")
    flag=0
    for i in cursor:
        flag=1
    if flag==0:
        print("FIRST TIME SETUP PLEASE CAREFULLY FILL\n\n")
        print("THESE ARE GOING TO BE YOUT LOGIN CREDENTIALS PLEASE ENTER CAREFULLY")
        username=input("ENTER THE ADMIN USERNAME TO LOGIN : ")
        password=input("ENTER THE ADMIN PASSOWRD TO LOGIN : ")
        cursor.execute(f"INSERT INTO LOGIN VALUES('{username}','{password}')")
        con.commit()
    cursor.execute("SELECT * FROM SNO")
    flag=0
    for i in cursor:
        flag=1
    if flag==0:
        cursor.execute("INSERT INTO SNO VALUES(0,0)")
        con.commit()
    cursor.execute("SELECT * FROM FEES")
    flag=0
    for i in cursor:
        flag=1
    if flag==0:
        print("THESE PRICES ARE PERMANENT PLEASE CAREFULLY FILL !")
        silver=int(input("ENTER THE PRICE FOR THE SILVER SUBSCRIPTION : "))
        gold=int(input("ENTER THE PRICE FOR THE GOLD SUBSCRIPTION : "))
        platinum=int(input("ENTER THE PRICE FOR THE PLATINUM SUBSCRIPTION : "))
        cursor.execute(f"INSERT INTO FEES VALUES({silver}, {gold}, {platinum})")
        con.commit()
while True:
    print('''

    |||||                                      |||||
    ||||        ----------------------          ||||
    |||========|  XFORCE ADMIN LOGIN  |==========|||
    ||||        ----------------------          ||||
    |||||                                      |||||

    ''')
    print("""
    
    1. LOGIN
    2. EXIT

    """)
    ch=int(input("ENTER THE ACTION TO PERFORM (1, 2) : "))
    if ch==1:
        cursor.execute("SELECT * FROM LOGIN")
        for i in cursor:
            t_user, t_pass=i
        password=input(f"ENTER THE ADMIN PASSWORD FOR ADMIN USERNAME ({t_user}) : ")
        if password==t_pass:
            while True :
                print('''
        |||||                                      |||||
        ||||        ----------------------          ||||
        |||========|   XFORCE GYM HOME    |==========|||
        ||||        ----------------------          ||||
        |||||                                      |||||

        ''')
                print("""
                
                1. ADD TRAINER
                2. ADD MEMBER
                3. REMOVE TRAINER
                4. REMOVE MEMBER
                5. MODIFY
                6. SHOW TRAINERS
                7. SHOW MEMBERS
                8. GO BACK
                
                """)
                ch=int(input("ENTER THE ACTION TO PERFORM (1, 2, 3, 4, 5, 6, 7, 8) : "))
                if ch==1:
                    trainer_name=input("NAME OF THE TRAINER : ")
                    trainer_age=input(f"ENTER YOUR AGE OF {trainer_name.upper()} : ")
                    trainer_gender=input(f"ENTER THE GENDER OF {trainer_name.upper()} (M , F, O) : ")
                    trainer_salary=input(f"ENTER THE SALARY FOR {trainer_name.upper()} : ")
                    cursor.execute("SELECT * FROM SNO")
                    for i in cursor:
                        t_id,t_did=i
                    t_id+=1
                    cursor.execute(f"INSERT INTO TRAINER VALUES({t_id},'{trainer_name.upper()}', '{trainer_age.upper()}', '{trainer_gender.upper()}', {trainer_salary})")
                    cursor.execute(f"UPDATE SNO SET ID={t_id}")
                    con.commit()
                    print(f"""
                    
                    TRAINER ADDED WITH FOLLOWING DETAILS :
                    NAME : {trainer_name}
                    AGE : {trainer_age}
                    GENDER : {trainer_gender}
                    SALARY : ₹{trainer_salary}

                    UNIQUE ID FOR {trainer_name} : {t_id}

                    """)
                elif ch==2:
                    member_name=input("ENTER THE NAME OF THE MEMBER : ")
                    member_gender=input(f"ENTER THE GENDER OF {member_name.upper()}(M, F, O) : ")
                    member_catagory=""
                    cursor.execute("SELECT * FROM FEES")
                    show=cursor.fetchall()
                    print(show)

                    print(f"""
                    
                    1. SILVER --> ₹{show[0][0]}
                    2. GOLD --> ₹{show[0][1]}
                    3. PLATINUM --> ₹{show[0][2]}
                    
                    """)
                    ch=int(input("ENTER THE CHOICE : "))
                    if ch==1:
                        member_catagory="SILVER"
                    if ch==2:
                        member_catagory="GOLD"
                    if ch==3:
                        member_catagory="PLATINUM"
                    cursor.execute(f"SELECT {member_catagory} FROM FEES")
                    member_amount=cursor.fetchall()
                    member_amount=member_amount[0][0]
                    cursor.execute("SELECT * FROM SNO")
                    for i in cursor:
                        t_id,t_did=i
                    t_did+=1
                    cursor.execute(f"UPDATE SNO SET DID={t_did}")
                    cursor.execute(f"INSERT INTO MEMBER VALUES({t_did}, '{member_name.upper()}', '{member_gender.upper()}', '{member_catagory}' , {member_amount})")
                    con.commit()
                    print(f"""
                    
                    MEMBER ADDED WITH FOLLOWING DETAILS :
                    NAME : {member_name.upper()}
                    GENDER : {member_gender.upper()}
                    SUBSCRIPTIOM : {member_catagory}
                    AMOUNT : ₹{member_amount}

                    UNIQUE ID FOR {member_name.upper()} : {t_did}

                     """)
                elif ch==3:
                    ch=input("DO YOU WANT TO SHOW THE TRAINERS (Y, N) : ")
                    if ch.upper()=="Y":
                        cursor.execute("SELECT * FROM TRAINER")
                        trainers=cursor.fetchall()
                        lstcon=[]
                        print()
                        head=["TRAINER ID", "NAME", "AGE", "GENDER", "SALARY"]
                        print(t.tabulate(trainers, tablefmt="psql", headers=head))
                    print()
                    ch=int(input("ENTER THE ID OF TRAINER TO REMOVE : "))
                    cursor.execute(f"DELETE FROM TRAINER WHERE ID={ch}")
                    print(f"TRAINER WITH TRAINER ID : {ch} REMOVED")
                    con.commit()
                elif ch==4:
                    ch=input("DO YOU WANT TO SHOW THE MEMBERS (Y, N) : ")
                    if ch.upper()=="Y":
                        cursor.execute("SELECT * FROM MEMBER")
                        members=cursor.fetchall()
                        lstcon=[]
                        print()
                        head=["MEMBER ID", "NAME", "GENDER", "SUBSCRIPTION PLAN", "SUBSCRIPTION FEES"]
                        print(t.tabulate(members, tablefmt="psql", headers=head))
                    ch=int(input("ENTER THE ID OF MEMBER TO REMOVE : "))
                    cursor.execute(f"DELETE FROM MEMBER WHERE ID={ch}")
                    print(f"MEMBER WITH MEMBER ID : {ch} REMOVED")
                    con.commit()
                elif ch==5:
                    while True:
                        print('''
        |||||                                      |||||
        ||||        ----------------------          ||||
        |||========| XFORCE MODIFICTAIONS |==========|||
        ||||        ----------------------          ||||
        |||||                                      |||||

        ''')
                        print("""
                    1. TRAINER
                    2. MEMBER
                    3. GO BACK
                    
                    """)
                        ask=int(input("ENTER THE ACTION TO PERFORM (1, 2, 3): "))
                        if ask==1:
                            cursor.execute("SELECT * FROM TRAINER")
                            trainers=cursor.fetchall()
                            print()
                            head=["TRAINER ID", "NAME", "AGE", "GENDER", "SALARY"]
                            print(t.tabulate(trainers, tablefmt="psql", headers=head))
                            while True:
                                print("""
1. NAME
2. AGE
3. GENDER
4. SALARY
5. BACK
                                """)
                                vu=int(input("ENTER THE MODIFICATION TO BE DONE (1, 2, 3, 4, 5) : "))
                                if vu==1:
                                    cursor.execute("SELECT * FROM TRAINER")
                                    trainers=cursor.fetchall()
                                    print()
                                    head=["TRAINER ID", "NAME", "AGE", "GENDER", "SALARY"]
                                    print(t.tabulate(trainers, tablefmt="psql", headers=head))
                                    ids=int(input("ENTER THE ID OF THE TRAINER TO PERFORM THE ACTION : "))     
                                    cursor.execute("SELECT * FROM TRAINER")
                                    trainer=cursor.fetchall()
                                    for i in trainer:
                                        if i[0]==ids:
                                            val=input(f"ENTER THE NAME FOR THE TRAINER ID {ids} : ")
                                            cursor.execute(f"UPDATE TRAINER SET NAME = '{val.upper()}' WHERE ID = {ids}")
                                            con.commit()
                                    ask=(input("DO YOU WANT TO SEE UPDATED TABLE (Y, N) : "))
                                    if ask.upper()=="Y":
                                        cursor.execute("SELECT * FROM TRAINER")
                                        trainers=cursor.fetchall()
                                        print()
                                        head=["TRAINER ID", "NAME", "AGE", "GENDER", "SALARY"]
                                        print(t.tabulate(trainers, tablefmt="psql", headers=head))
                                if vu==2:
                                    cursor.execute("SELECT * FROM TRAINER")
                                    trainers=cursor.fetchall()
                                    print()
                                    head=["TRAINER ID", "NAME", "AGE", "GENDER", "SALARY"]
                                    print(t.tabulate(trainers, tablefmt="psql", headers=head))
                                    ids=int(input("ENTER THE ID OF THE TRAINER TO PERFORM THE ACTION : "))                                 
                                    cursor.execute("SELECT * FROM TRAINER")
                                    trainer=cursor.fetchall()
                                    for i in trainer:
                                        if i[0]==ids:
                                            val=input(f"ENTER THE AGE FOR THE TRAINER ID {ids} : ")
                                            cursor.execute(f"UPDATE TRAINER SET AGE = '{val.upper()}' WHERE ID = {ids}")
                                            con.commit()
                                    ask=(input("DO YOU WANT TO SEE UPDATED TABLE (Y, N) : "))
                                    if ask.upper()=="Y":
                                        cursor.execute("SELECT * FROM TRAINER")
                                        trainers=cursor.fetchall()
                                        print()
                                        head=["TRAINER ID", "NAME", "AGE", "GENDER", "SALARY"]
                                        print(t.tabulate(trainers, tablefmt="psql", headers=head))
                                if vu==3:
                                    cursor.execute("SELECT * FROM TRAINER")
                                    trainers=cursor.fetchall()
                                    print()
                                    head=["TRAINER ID", "NAME", "AGE", "GENDER", "SALARY"]
                                    print(t.tabulate(trainers, tablefmt="psql", headers=head))
                                    ids=int(input("ENTER THE ID OF THE TRAINER TO PERFORM THE ACTION : "))                                   
                                    cursor.execute("SELECT * FROM TRAINER")
                                    trainer=cursor.fetchall()
                                    for i in trainer:
                                        if i[0]==ids:
                                            val=input(f"ENTER THE GENDER FOR THE TRAINER ID {ids} : ")
                                            cursor.execute(f"UPDATE TRAINER SET GENDER = '{val.upper()}' WHERE ID = {ids}")
                                            con.commit()

                                    ask=(input("DO YOU WANT TO SEE UPDATED TABLE (Y, N) : "))
                                    if ask.upper()=="Y":
                                        cursor.execute("SELECT * FROM TRAINER")
                                        trainers=cursor.fetchall()
                                        print()
                                        head=["TRAINER ID", "NAME", "AGE", "GENDER", "SALARY"]
                                        print(t.tabulate(trainers, tablefmt="psql", headers=head))
                                if vu==4:
                                    cursor.execute("SELECT * FROM TRAINER")
                                    trainers=cursor.fetchall()
                                    print()
                                    head=["TRAINER ID", "NAME", "AGE", "GENDER", "SALARY"]
                                    print(t.tabulate(trainers, tablefmt="psql", headers=head))
                                    ids=int(input("ENTER THE ID OF THE TRAINER TO PERFORM THE ACTION : "))                                   
                                    cursor.execute("SELECT * FROM TRAINER")
                                    trainer=cursor.fetchall()
                                    for i in trainer:
                                        if i[0]==ids:
                                            val=input(f"ENTER THE SALARY FOR THE TRAINER ID {ids} : ")
                                            cursor.execute(f"UPDATE TRAINER SET SALARY = {val.upper()} WHERE ID = {ids}")
                                            con.commit()

                                    ask=(input("DO YOU WANT TO SEE UPDATED TABLE (Y, N) : "))
                                    if ask.upper()=="Y":
                                        cursor.execute("SELECT * FROM TRAINER")
                                        trainers=cursor.fetchall()
                                        print()
                                        head=["TRAINER ID", "NAME", "AGE", "GENDER", "SALARY"]
                                        print(t.tabulate(trainers, tablefmt="psql", headers=head))
                                if vu==5:
                                    break
                                else:
                                    pass
                        if ask==2:
                            while True:
                                print("""
1. NAME
2. GENDER
3. SUBSCRIPTION PLAN
4. SUBSCRIPTION FEES
5. BACK
                                """)
                                vu=int(input("ENTER THE MODIFICATION TO BE DONE (1, 2, 3, 4, 5) : "))
                                if vu==1:
                                    cursor.execute("SELECT * FROM MEMBER")
                                    trainers=cursor.fetchall()
                                    print()
                                    head=["MEMBER ID", "NAME", "GENDER", "SUBSCRIPTION PLAN", "SUBSCRIPTION FEES"]
                                    print(t.tabulate(trainers, tablefmt="psql", headers=head))
                                    ids=int(input("ENTER THE ID OF THE MEMBER TO PERFORM THE ACTION : "))
                                    
                                    cursor.execute("SELECT * FROM MEMBER")
                                    trainer=cursor.fetchall()
                                    for i in trainer:
                                        if i[0]==ids:
                                            val=input(f"ENTER THE NAME FOR MEMBER ID {ids} : ")
                                            cursor.execute(f"UPDATE MEMBER SET NAME = '{val.upper()}' WHERE ID = {ids}")
                                            con.commit()                                                                       
                                if vu==2:
                                    cursor.execute("SELECT * FROM MEMBER")
                                    trainers=cursor.fetchall()
                                    print()
                                    head=["MEMBER ID", "NAME", "GENDER", "SUBSCRIPTION PLAN", "SUBSCRIPTION FEES"]
                                    print(t.tabulate(trainers, tablefmt="psql", headers=head))
                                    ids=int(input("ENTER THE ID OF THE MEMBER TO PERFORM THE ACTION : "))
                                    
                                    cursor.execute("SELECT * FROM MEMBER")
                                    trainer=cursor.fetchall()
                                    for i in trainer:
                                        if i[0]==ids:
                                            val=input(f"ENTER THE GENDER FOR MEMBER ID {ids} (M, F, O) : ")
                                            cursor.execute(f"UPDATE MEMBER SET GENDER = '{val.upper()}' WHERE ID = {ids}")
                                            con.commit()
                                if vu==3:
                                    cursor.execute("SELECT * FROM MEMBER")
                                    trainers=cursor.fetchall()
                                    print()
                                    head=["MEMBER ID", "NAME", "GENDER", "SUBSCRIPTION PLAN", "SUBSCRIPTION FEES"]
                                    print(t.tabulate(trainers, tablefmt="psql", headers=head))
                                    ids=int(input("ENTER THE ID OF THE MEMBER TO PERFORM THE ACTION : "))
                                    
                                    cursor.execute("SELECT * FROM MEMBER")
                                    trainer=cursor.fetchall()
                                    for i in trainer:
                                        if i[0]==ids:
                                            val=input(f"ENTER THE SUBSCRIPTION PLAN FOR MEMBER ID {ids} : ")
                                            cursor.execute(f"UPDATE MEMBER SET CATAGORY = '{val.upper()}' WHERE ID = {ids}")
                                            con.commit()
                                if vu==4:
                                    cursor.execute("SELECT * FROM MEMBER")
                                    trainers=cursor.fetchall()
                                    print()
                                    head=["MEMBER ID", "NAME", "GENDER", "SUBSCRIPTION PLAN", "SUBSCRIPTION FEES"]
                                    print(t.tabulate(trainers, tablefmt="psql", headers=head))
                                    ids=int(input("ENTER THE ID OF THE MEMBER TO PERFORM THE ACTION : "))
                                    
                                    cursor.execute("SELECT * FROM MEMBER")
                                    trainer=cursor.fetchall()
                                    for i in trainer:
                                        if i[0]==ids:
                                            val=input(f"ENTER THE SUBSCRIPTION FEES FOR MEMBER ID {ids} : ")
                                            cursor.execute(f"UPDATE MEMBER SET AMOUNT = '{val.upper()}' WHERE ID = {ids}")
                                            con.commit()
                                if vu==5:
                                    break
                                else:
                                    pass    
                        if ask==3:
                            break
                        else:
                            pass                         
                elif ch==6:
                    cursor.execute("SELECT * FROM TRAINER")
                    trainers=cursor.fetchall()
                    lstcon=[]
                    print()
                    head=["TRAINER ID", "NAME", "AGE", "GENDER", "SALARY"]
                    print(t.tabulate(trainers, tablefmt="psql", headers=head))
                elif ch==7:
                    cursor.execute("SELECT * FROM MEMBER")
                    members=cursor.fetchall()
                    lstcon=[]
                    print()
                    head=["MEMBER ID", "NAME", "GENDER", "SUBSCRIPTION PLAN", "SUBSCRIPTION FEES"]
                    print(t.tabulate(members, tablefmt="psql", headers=head))
                elif ch==8:
                    break
        else:
            print(f"WRONG PASSWORD FOR USERNAME({t_user})")
    elif ch==2:
        break