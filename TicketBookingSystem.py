import smtplib
import random
import time
class Ticket:
  global emaillist,passwordlist,caps,small,num,special
  caps=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
  small=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  num=["1","2","3","4","5","6","7","8","9","0"]
  special = [" ", "!", "#", "$", "%", "&", "'", "(", ")", "*", "+", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", "`", "{", "|", "}", "~", ","]
  def __init__(self):
    print("\n")
    print("--------WELCOME TO OUR TICKET BOOKING SYSTEM---------")
    print("\n")
    print("New user Enter 1")
    print("Already have an account Enter 2")
    print("\n")
    choice=int(input("Enter your choice "))
    print("\n")
    if choice==1:
      self.first()
      self.book()
    if choice==2:
      self.second()
      
  def first(self):
    print("______Enter the details below to create an account_____")
    print("\n")
    while True:
      name=input("Enter your FirstName:  ")
      if name.isalpha():
        break
      else:
        print("\n")
        print(".....Invalid data.....")
        print("\n")
     
    while True:
      print("\n")
      name=input("Enter your LastName:  ")
      if name.isalpha():
        break
      else:
        print("\n")
        print(".....Invalid data.....")
        print("\n")
    while True:
      print("\n")
      age=input("Enter your Age:  ")
      if age.isdecimal():
        break
      else:
        print("\n")
        print(".....Invalid data.....")
        print("\n")
    while True:
      print("\n")
      no=input("Enter your Mobile no:  ")
      if len(no)==10 and no.isnumeric():
        break
      else:
        print("\n")
        print(".....Invalid data.....")
        print("\n")
    while True:
      print("\n")
      global email
      email=input("Enter your Email id:  ")
     
      if "@gmail.com" in email:
        wemail=email +" "
        with open("file.txt","a") as f:
          f.write(email)
        break
      else:
        print("\n")
        print(".....Invalid data.....")
        print("\n")
    while True:
      print("\n")
      global password
      password=input("Enter Password:  ")
      capscount=self.capsfun()
      smallcount=self.smallfun()
      numcount=self.numfun()
      specialcount=self.specialfun()
      tot=0
      tot=tot+capscount+smallcount+numcount+specialcount
      if tot==4 and len(password)>=6:
        passwordw=password + "\n"
        with open("file.txt","a") as f: 
          f.write(passwordw)
        break
      else:
        print("\n")
        print(".....Weak password.....")
        print("Hint for strong password")
        print("1) Password must contain atleast 1 Uppercase")
        print("2) Password must contain atleast 1 Lowercase")
        print("3) Password must contain atleast 1 number")
        print("4) Password must contain atleast 1 specialchracter")
        print("5) Password length must greater than 6")
        print("\n")
  
    while True:
      print("\n")
      repass=input("Enter your password again: ")
      if repass==password:
        break
      else:
        print("\n")
        print(".....Invalid Password.....")
        print("\n")
    print("\n")
    print("------Account created sucessfully------")
    print("\n")
    print("...use email and password to login...")
    print("\n")
    while True:
      print("\n")
      loginemail=input("Enter your registered Email: ")
      if loginemail==email:
        break
      else:
        print("\n")
        print(".....Invalid email.....")
        print("\n")
    while True:
      print("\n")
      loginpass=input("Enter your pass:  ")
      if loginpass==password:
        print("\n") 
        print("....Logged in Successfully....")
        print("\n")
        print("____Welcome to our booking..make your journey memorable with us____")
        break
      else:
        print("\n")
        print("....Invalid password....")
        print("\n")    
              
  def capsfun(self):
    for i in range(len(caps)):
      if caps[i] in password:
        return 1
    return 0
  def smallfun(self):
    for i in range(len(small)):
      if small[i] in password:
        return 1
    return 0
  def numfun(self):
    for i in range(len(num)):
      if num[i] in password:
        return 1
    return 0
  def specialfun(self):
    for i in range(len(special)):
      if special[i] in password:
        return 1
    return 0
      
  def book(self):
    while True:
      print("\n")
      current=input(("Enter your Current Location: "))
      if current.isalpha():
        break
      else:
        print("\n")
        print("....Invalid Data....")
        print("\n")
    while True:
      print("\n")
      destination=input(("Enter your Destination: "))
      if current.isalpha():
        break
      else:
        print("\n")
        print("....Invalid Data....")
        print("\n")

    print("\n")
    print("For AC Enter 1 ")
    print("For NON AC Enter 2. ")
    print("\n")
    bus_choice=int(input("Enter your choice: "))
    print("\n")
    print("....Bus Timings Listed Below....")
    print("\n")
    print("From 6.00  am to 10.00 am")
    print("From 8.00  am to 1.00  pm")
    print("From 10.00 am to 3.00  pm")
    print("From 11.00 am to 4.00  pm")
    print("From 12.00 pm to 5.00  pm")
    print("From 5.00  pm to 9.00  pm")
    print("From 6.00  am to 10.00 pm")
    print("From 7.00  am to 11.00 pm")
    print("From 8.00  am to 12.00 pm")
    print("\n")
    timing=input("Select your Timing: ")
    print("\n")
    no_of_tickets=int(input("How many tickets you want to book: "))
    print("\n")
    if bus_choice==1:
      price=no_of_tickets*200
    elif bus_choice==2:
      price=no_of_tickets*160
    print("Price for the ticket is",price)
    print("\n")
    status=input("Type Yes to conform your Booking or Type NO to cancel your booking: ").upper()
    if status=="YES":
      try:
        otp=str(random.randint(1111,9999))
        msg="WELCOME "+email+" "+ "your OTP for Ticket Booking is "+otp
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("summa223344@gmail.com", "plpl mzkc gkrq fifm")
        server.sendmail("summa223344@gmail.com",email,msg)
        server.quit()
      except:
        print("Sending email was failed due to unexpected issue")
        print("OOPS!... Sorry for Disappointment")
        print("Email will sent you again")   
        otp=str(random.randint(1111,9999))
        msg="WELCOME "+email+" "+ "your OTP for Ticket Booking is "+otp
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("summa223344@gmail.com", "plpl mzkc gkrq fifm")
        server.sendmail("summa223344@gmail.com",email,msg)
        server.quit()
      print("\n")
      print("OTP is sent to your registered email id")
      while True:
        recvotp=input("Enter your OTP: ")
        if recvotp==otp:
          print("\n")
          print("....Verified....")
          break
        else:
          print("....Incorrect OTP....")
          print("\n")
      print("\n")
      print(".......Ticket Booked Successfully.......")
      print("\n")
      print("<<<<<   happy journey      >>>>>")
      print("\n")
      print("Byeee!!!!.............")
    elif status=="NO":
      print("\n")
      print("Your Tickets are cancelled")
      print("....Better Luck Next Time....")
  def second(self):
    global email,password
    email=input("Enter your email: ")
    password=input("Enter your password: ")
    with open("file.txt","r") as f:
      for i in f:
        if email in i and password in i:
          print("Logged in successfully")
          self.book()
        else: 
          print('Invalid Data')



obj=Ticket()

 