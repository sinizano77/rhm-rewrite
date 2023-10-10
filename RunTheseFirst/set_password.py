_DEFAULT_DATABASE = 'Rhm_Db'

#@@@@@@@CHANGE THESE IF THESE ARE DIFFERENT@@@@@@@@@
_USERNAME = 'postgres'
_HOST_IP = '127.0.0.1'
_DEFAULT_PORT = '5432'

#It's main - nuff said
def main():
    password = ask_password()
    writeToFile(password)

#Asks user for their password
def ask_password() -> str:
    return input("What is the Postgres password?: ")

#Write content to file
def writeToFile(password: str) -> None:
    file = open("secret.txt", "w")
    file.write(f"{_DEFAULT_DATABASE},{_USERNAME},{password},{_HOST_IP},{_DEFAULT_PORT}")
    print_stuff()
    file.close()

#print these to the user
def print_stuff() -> None:
    print('====================')
    print('Data successfully saved!')
    print('If you want to change the password run password.py')
    print('====================\n')

# Running password creator/changer
if __name__ == '__main__':
    main()
