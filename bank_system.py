''' REMEMBER TO WRITE LOTS OF COMMENTS '''

from customer_account import CustomerAccount
from admin import Admin

accounts_list = []
admins_list = []

class BankSystem(object):
    def __init__(self):
        self.accounts_list = []
        self.admins_list = []
        self.load_bank_data()
    
    def load_bank_data(self):
        
        # create customers
        account_no = 1234
        customer_1 = CustomerAccount("Adam", "Smith", ["14", "Wilcot Street", "Bath", "B5 5RT"], account_no, 5000.00)
        self.accounts_list.append(customer_1)
        
        account_no+=1
        customer_2 = CustomerAccount("David", "White", ["60", "Holborn Viaduct", "London", "EC1A 2FD"], account_no, 3200.00)    
        self.accounts_list.append(customer_2)

        account_no+=1
        customer_3 = CustomerAccount("Alice", "Churchil", ["5", "Cardigan Street", "Birmingham", "B4 7BD"], account_no, 18000.00)
        self.accounts_list.append(customer_3)

        account_no+=1
        customer_4 = CustomerAccount("Ali", "Abdallah",["44", "Churchill Way West", "Basingstoke", "RG21 6YR"], account_no, 40.00)
        self.accounts_list.append(customer_4)
                
        # create admins
        admin_1 = Admin("Julian", "Padget", ["12", "London Road", "Birmingham", "B95 7TT"], "1", "1", True)
        self.admins_list.append(admin_1)

        admin_2 = Admin("Cathy",  "Newman", ["47", "Mars Street", "Newcastle", "NE12 6TZ"], "2", "2", False)
        self.admins_list.append(admin_2)


    def search_admins_by_name(self, admin_username):
        found_admin = None
        for a in self.admins_list:
            username = a.get_username()
            if username == admin_username:
                found_admin = a
                break
        if found_admin == None:
            print("\n The Admin %s does not exist! Try again...\n" %admin_username)
            
        return found_admin
        
    def search_customers_by_name(self, customer_lname):
        found_customer = None
        for a in self.accounts_list: #goes through each entry in account_list
            lastname = a.get_last_name()
            if lastname == customer_lname: #checks each entry last name against the input name
                found_customer = a
                print("customer found") #debugging, delete later
                break
        if found_customer == None:
            print("\n The Customer %s does not exist! Try again...\n" %customer_lname)
            
        return found_customer
        
        
    def main_menu(self):
        #print the options you have
        print()
        print()
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("Welcome to the Python Bank System")
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("1) Admin login")
        print ("2) Quit Python Bank System")
        print (" ")
        option = int(input ("Choose your option: "))
        return option


    def run_main_options(self):
        loop = 1         
        while loop == 1:
            choice = self.main_menu()
            if choice == 1:
                username = input ("\n Please input admin username: ")
                password = input ("\n Please input admin password: ")
                msg, admin_obj = self.admin_login(username, password)
                print(msg)
                if admin_obj != None:
                    self.run_admin_options(admin_obj)
            elif choice == 2:
                loop = 0
        print ("\n Thank-You for stopping by the bank!")


    def transferMoney(self, sender_lname, receiver_lname, receiver_account_no, amount):
        #ToDo
        pass

                
    def admin_login(self, username, password):
        #STEP A.1
        found_admin=self.search_admins_by_name(username)
        msg="\n Login failed"
        if found_admin!=None:
            if found_admin.get_password() == password:
                msg="\n Login successful"
        return msg, found_admin

    def admin_menu(self, admin_obj):
        #print the options you have
         print (" ")
         print ("Welcome Admin %s %s: Avilable options are:" %(admin_obj.get_first_name(), admin_obj.get_last_name()))
         print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
         print ("1) Transfer money")
         print ("2) Customer account operations & profile settings")
         print ("3) Delete customer")
         print ("4) Print all customers detail")
         print ("5) Sign out")
         print (" ")
         option = int(input ("Choose your option: "))
         return option


    def run_admin_options(self, admin_obj):                                
        loop = 1
        while loop == 1:
            choice = self.admin_menu(admin_obj)
            if choice == 1:
                sender_lname = input("\n Please input sender surname: ")
                amount = float(input("\n Please input the amount to be transferred: "))
                receiver_lname = input("\n Please input receiver surname: ")
                receiver_account_no = input("\n Please input receiver account number: ")
                self.transferMoney(sender_lname, receiver_lname, receiver_account_no, amount)                    
            elif choice == 2: #This option is used to access a specific customers account
                #STEP A.4
                customer_name = input("\nPlease input customer surname: \n")
                customer_account = self.search_customers_by_name(customer_name)
                if customer_account != None:
                    customer_account.run_account_options()
            
            elif choice == 3:
                #STEP A.5
                #search for the admin that they are currently logged in as
                #then check that specific admins rights
                #currentadmin = BankSystem.search_admins_by_name(admin_obj.admin_username)
                if Admin.has_full_admin_right == True:
                    print('false')
                else:
                    print('something else')
                    
                '''if Admin.has_full_admin_right == True:
                    customer_name =input("\nInput customer name you want to delete: ")
                    customer_account =self.search_customers_by_name(customer_name)
                    if customer_account != None:
                        self.accounts_list.remove(customer_account)
                        print("%s was deleted successfully!"%customer_name)
                else:
                    print("\nYou do not have permission to delete customers \n")'''
            
            elif choice == 4:
                #STEP A.6
                pass
            
            elif choice == 5:
                loop = 0
        print ("\n Exit account operations")


    def print_all_accounts_details(self):
            # list related operation - move to main.py
            i = 0
            for c in self.accounts_list:
                i+=1
                print('\n %d. ' %i, end = ' ')
                c.print_details()
                print("------------------------")


app = BankSystem()
app.run_main_options()
