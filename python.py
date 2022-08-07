import json
def logsign():
    print("Press Button '1' To Log In")
    print("Press Button '2' To Sign Up")
    start=input("What Do You Want!")
    if start=='1':
        l=[]
        dic={}
        username=input("Enter a Username: ")
        password=input("Enter Your Password: ")
        confirm_password=input("Enter Your Confirm Password: ")
        if password==confirm_password:

            digit,special,upper,lower=0,0,0,0
            if len(password)>=8:
                for i in password:
                    if (i.isupper()):
                        upper=1
                    if (i.isdigit()):
                        digit=1
                    if (i.islower()):
                        lower=1
                    if(i=='@'or i=='$' or i=='_' or i=='#' or i=="!" or i=="%" or i=="&" or i=="*"):
                        special=1
            total=upper+digit+lower+special
            if total==4: 
                gender=input("Enter Your Gender 'Male' and 'Female': ")
                dob=input("Enter Your DOB: ")
                dic['name']=username
                dic['password']=password
                dic['gender']=gender
                dic['DOB']=dob
                l.append(dic)
                with open("UserDetails.json","a") as f:
                    json.dump(l,f,indent=4)
                
                print("You are Logged in Successfully!")
            else:
                print("Password Contains One Special Character, One Capital Letter, One Small Letter and One Digit! ")

    else:
        if start=='2':
            print("Sign Up")
        username1=input("Enter a Username: ")
        password1=input("Enter Your Password: ")
        upper,lower,digit,special=0,0,0,0
        if len(password1)>=8:
            for i in password1:
                if (i.isupper()):
                    upper=1
                if (i.isdigit()):
                    digit=1
                if (i.islower()):
                    lower=1
                if(i=='@'or i=='$' or i=='_' or i=='#' or i=="!" or i=="%" or i=="&" or i=="*" ):
                    special=1
            total=upper+digit+lower+special 
            if total!=4:
                print("Please use  atleast one capital letter , Smalll letter, Digit and Special character!! ")
            else:
                password2=input("Enter Your Confirmed Password: ")
                if password1!=password2:
                    print("Please! Enter Correct Password!")
                elif password1==password2:
                    f1=open("UserDetails.json",'r')
                    file=f1.read()
                    if username1 in file:
                        print("You are Already Exist!")
                        print(file)
                        
                    else:
                        gender1=input("Enter Your Gender 'Male' and 'Female': ")
                        bio1=input("Enter Your Bio: ")
                        dob1=input("Enter Your DOB: ")
                        dic1={}
                        list=[]
                        dic1['name']=username1
                        dic1['password']=password1
                        dic1['gender']=gender1
                        dic1['Bio']=bio1
                        dic1['DOB']=dob1
                        list.append(dic1)
                        c=json.dumps(list,indent=4)
                        f2=open("UseDetails.json",'a')
                        f2.writelines(c)
                        f2.close()
                        for k in dic1:
                            print(k,":-",dic1[k])
                            print("You are signed up successfully")
                        print(dic1)
        else:
            print("Your Password Is Too Short")

logsign()