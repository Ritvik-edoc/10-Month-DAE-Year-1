# Prints welcome message and prompts user to create login credentials
print("Welcome New User!")
print("Create a login credential by entering a username and password.")
new_name = input("Enter username:")
new_password = input("Enter password:")
stored_username = new_name
stored_password = new_password
access_granted = False

# Prints confirmation (The credentials were stored succesfully)
print("\nUsername and password stored successfully!\n")
while True:
    username = input("Enter username:")
    password = input("Enter password:")
    if username == stored_username and password == stored_password:
        print("Login Successful!")
        access_granted = True
# If the credentials do not match, it prints "Login Failed !"
    else:
        print("Login Failed! Please try again.")
        access_granted = False
# IF the credentials match, it welcomes the user to the terminal
    if access_granted == True:
        print("\ntype 'ask' to view and answer questions or type 'exit' to leave the terminal.\n")
        command = input().lower()
# Aks user some questions and if they wish to leave they must type exit 
        if command == "exit":
            print("Thank you for using the terminal. Goodbye!")
            break
        elif command == "ask":
            questions = [
                "What is your name?",
                "What is your favorite color?",
                "What is your favorite food?",
                "What is your favorite hobby?",
                "What is your favorite movie?"
            ]
# If the user asks something except the set questions it will print Invalid command 
            for question in questions:
                answer = input(question + " ")
                print(f"Your answer: {answer}\n")
                if answer == "kay" or answer == "Kay":
                    print(" Seems like you don't have enough aura to use this terminal")
                    exit()

# Once it asks all the questions it thanks the user
            print("Thank you for answering the questions!\n")
            break
        else:
            print("Invalid command. Please try again.")