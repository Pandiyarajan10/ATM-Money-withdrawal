import psycopg2
import datetime
pandy = psycopg2.connect(host = 'database-1.cmyigtchqfm2.eu-north-1.rds.amazonaws.com',user = 'postgres', password='**********',port = 5432,database ='Pandy_localDB')
kumar = pandy.cursor()
kumar.execute("""create table Bank_Details(
Account_Number int primary key,
Name varchar(20),
Age int,
Contact_Number int,
Mail varchar(50),
Location varchar(25),
Balance float)""")
pandy.commit()
kumar.execute("""insert into Bank_Details values (638523100,'Pandiyarajan',28,982658715,'Pandiyarajan@gmail.com','puducherry',10000),
              (638523101,'Leena',25,972835715,'Leena@gmail.com','puducherry',20000),
              (638523102,'Abi',27,772658810,'Abi@gmail.com','Chennai',35000),
              (638523103,'Gopi',32,762008765,'Gopi@gmail.com','Trichy',65000),
              (638523104,'Nagendran',35,994448700,'Nagendran@gmail.com','Cuddalore',72000),
              (638523105,'Srimathi',26,777635670,'Srimathi@gmail.com','Cuddalore',1000),
              (638523106,'Nirmala',23,776658710,'Nirmala@gmail.com','Chennai',200000),
              (638523107,'Suganya',33,792150016,'Suganya@gmail.com','puducherry',100000),
              (638523108,'Manimaran',31,986999716,'Manimaran@gmail.com','Cuddalore',70000),
              (638523109,'Nagaraj',30,9764858,'Nagaraj@gmail.com','Trichy',80000),
               (638523110,'Karthikeyan',32,887545111,'Karthikeyan@gmail.com','puducherry',98000),
              (638523111,'Sangeetha',28,989362584,'Sangeetha@gmail.com','Banglore',60000),
              (638523112,'Illayaraja',29,728921730,'Illayaraja@gmail.com','Banglore',850000),
              (638523113,'Sathish',35,981158700,'Sathish@gmail.com','Cuddalore',35000),
              (638523114,'Prithivi',31,995562018,'Prithivi@gmail.com','Trichy',10000)""")
pandy.commit()
kumar.execute("""create table Audit(
Account_Number int primary key,
Location varchar(25),
Withdraw_Date_Time TIMESTAMP,
Balance_Before_Withdrawal float,
Withdraw_Amount float,
Balance_After_Withdrawal float)""")
pandy.commit()
AccountNumber=int(input("Enter your account number:"))
kumar.execute("select Account_Number from Bank_Details WHERE Account_Number=%s",[AccountNumber])
Acc_no = kumar.fetchone()
if len(Acc_no)>0:
    Amount=int(input("Enter the amount to withdrawal:"))
    kumar.execute("select balance from Bank_Details WHERE Account_Number = %s", (AccountNumber,))
    balance = kumar.fetchone()
    Time = datetime.datetime.now()
    kumar.execute("UPDATE Bank_Details SET BALANCE = BALANCE - %s WHERE Account_Number = %s", [Amount, AccountNumber])
    kumar.execute("insert into audit(Account_Number,Withdraw_Amount,Withdraw_Date_Time,Balance_Before_Withdrawal) values(%s,%s,%s,%s)",[AccountNumber,Amount,Time,balance])
    kumar.execute("update Audit AI set Location=Bank_details.Location,Balance_After_Withdrawal=Bank_details.Balance from Bank_details where Bank_Details.Account_number=AI.Account_number")
    pandy.commit()
