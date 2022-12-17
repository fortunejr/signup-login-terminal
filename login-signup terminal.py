import datetime
xx = datetime.datetime.now()

users_data = []
ud = {

}


def signup():
    users_name = input("Enter your name: ")
    username = input("Enter Your username(Phone number): ")
    if len(username) == 11:
        psw = input("Enter password containing '@', '&' or has a number at the end: ")
        if (psw.find('@')>0) or psw.find('&')>0 or psw[-1].isdigit() == True:
            pwd2 = input("Confirm password: ")
            if psw == pwd2:
                dob = input("Enter DOB in format DD/MM/YYYY no spaces: ")
                if (int(dob[0:2])<32) and (int(dob[4:5]) < 13) and (int(dob[6:10])< 2022):
                    print(xx.year - int(dob[6:10]), dob[0:2], dob[4:5], dob[6:10])
                    if xx.year-int(dob[6:10]) >=21:
                        ud = {
                            "users_name": users_name,
                            'username': username,
                            'password': pwd2,
                            'dob': dob
                        }
                        users_data.append(ud)
                        print(users_data)
                        print("You have successfully signed up")
                    else:
                        print("you must be 21 yrs or older")
                else:
                    print("You have entered the Date of Birth in invalid format")
            else:
                print("Password does not match.")
        else:
            print("enter valid password containing '@', '&' or has a number at the end:")
    else:
        print("The username should be 11 digits")


pwd_attempts = 0


def login():
    user_id = int(input("Enter your username(Phone number): "))
    user_pwd = input("Enter your password: ")
    if (user_id == int(users_data[0]['username'])) and (user_pwd == users_data[0]['password']):
        print("welcome", users_data[0]['users_name'])
        user_sign = int(input("Please enter 1 for resetting the password\n"
              "Please enter 2 for signout."))
        if user_sign == 1:
            '''problem'''
            reset_pwd_username = int(input("Enter your username (Phone Number): "))
            for x in users_data:
                if reset_pwd_username == int(x['username']):
                    old_password = input('Please enter your old password: ')
                    if old_password == x['password']:
                        new_password = input("Enter new password: ")
                        if (new_password.find('@') > 0) or new_password.find('&') > 0 or new_password[-1].isdigit() == True:
                            x['password'] = new_password
                            print(users_data)
                        else:
                            print("enter valid password containing '@', '&' or has a number at the end:")
                    else:
                        print("Incorrect password")

                else:
                    print("this username does not exist")
            #poblem st0p
        elif user_sign == 2:
            pass
    else:
        print('you have not signed up with this contact number')


def reset_pwd():
    print("You have use the maximum attempts of login\n"
          "please reset the password by entering the details below")
    reset_username = int(input("Please enter you username (Mobile number) to confirm: "))
    reset_dob = input("Enter your Date of Birth  in DD/MM/YYYY to confirm")
    for c in users_data:
        if (reset_username == c['username']) and (reset_dob == c['dob']):
            reset_pwd1= input('please enter new password: ')
            reset_pwd2 = input('confirm password:')
            if reset_pwd1 == reset_pwd2:
                c['password'] = reset_pwd2
            else:
                print("Password are not matching")
        else:
            print("Incorrect details.")


while True:
    user_option = input("Please Enter 1 for Sign Up \n"
                        "Please Enter 2 for Sign In \n"
                        "Please Enter 3 for Quit \n")

    if user_option == '3':
        print("Thank You for Using the Application.")
        break
    elif user_option == '1':
        signup()
    elif user_option == '2':
        login()

        pwd_attempts+=1
        if pwd_attempts >= 3:
            reset_pwd()
