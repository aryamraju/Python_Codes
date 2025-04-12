class RBI:
    def agricultural_loan(self):
        interest_rate = 3.5
        return interest_rate

class SBI(RBI):
    def educational_loan(self):
        interest_rate = 4.0
        return interest_rate
    def home_loan(self):
        interest_rate = 6.5
        return interest_rate
    def vehicle_loan(self):
        interest_rate = 7.5
        return interest_rate

class SIB(RBI):
    def personal_loan(self):
        interest_rate = 8.0
        return interest_rate
    def business_loan(self):
        interest_rate = 9.0
        return interest_rate
    def gold_loan(self):
        interest_rate = 10.0
        return interest_rate

class HDFC(RBI):
    def housing_loan(self):
        interest_rate = 5.5
        return interest_rate
    def education_loan(self):
        interest_rate = 6.0
        return interest_rate
    def car_loan(self):
        interest_rate = 7.0
        return interest_rate

class FB(RBI):
    def personal_loan(self):
        interest_rate = 8.5
        return interest_rate
    def business_loan(self):
        interest_rate = 9.5
        return interest_rate
    def gold_loan(self):
        interest_rate = 10.5
        return interest_rate

while True:
    print("\nWelcome to the Bank Loan System")
    print("1. SBI")
    print("2. SIB")
    print("3. HDFC")
    print("4. FB")
    print("5. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        bank = SBI()
        loan_type =int(input("Enter loan type:\n1.agricultural\n2.educational\n3.home\n4.vehicle\n "))
        if loan_type == 1:
            loan = "agricultural"
            name =  input("Enter Your Name:")
            age = int(input("Enter Your Age:"))
            if age <= 18:
                print("You are not eligible for the loan")
                continue
            else:
                print("You are eligible for the loan")
            amount = int(input("Enter the amount you want to borrow:"))
            repayment_period = int(input("Enter the repayment period in years:"))
            interest_rate = bank.agricultural_loan()
            interest = (amount * interest_rate * repayment_period) / 100
            total_amount = amount + interest
            print(f"Total amount to be paid after {repayment_period} years is: {total_amount}")


        elif loan_type == 2:
            loan = "educational"
            name =  input("Enter Your Name:")
            age = int(input("Enter Your Age:"))
            if age <= 18:
                print("You are not eligible for the loan")
                continue
            else:
                print("You are eligible for the loan")
            amount = int(input("Enter the amount you want to borrow:"))
            repayment_period = int(input("Enter the repayment period in years:"))
            
            interest_rate = bank.educational_loan()
            interest = (amount * interest_rate * repayment_period) / 100
            total_amount = amount + interest
            print(f"Total amount to be paid after {repayment_period} years is: {total_amount}")
        elif loan_type == 3:
            loan = "home"
            name =  input("Enter Your Name:")
            age = int(input("Enter Your Age:"))
            if age <= 18:
                print("You are not eligible for the loan")
                continue
            else:
                print("You are eligible for the loan")
            amount = int(input("Enter the amount you want to borrow:"))
            repayment_period = int(input("Enter the repayment period in years:"))
         
            interest_rate = bank.home_loan()
            interest = (amount * interest_rate * repayment_period) / 100
            total_amount = amount + interest
            print(f"Total amount to be paid after {repayment_period} years is: {total_amount}")
        elif loan_type == 4:
            loan = "vehicle"
            name =  input("Enter Your Name:")
            age = int(input("Enter Your Age:"))
            if age <= 18:
                print("You are not eligible for the loan")
                continue
            else:
                print("You are eligible for the loan")
            amount = int(input("Enter the amount you want to borrow:"))
            repayment_period = int(input("Enter the repayment period in years:"))
            interest_rate = bank.vehicle_loan()
            interest = (amount * interest_rate * repayment_period) / 100
            total_amount = amount + interest
            print(f"Total amount to be paid after {repayment_period} years is: {total_amount}")
        else:
            print("Invalid loan type")
            continue
        print(f"Interest rate for {loan_type} loan in SBI is: {interest_rate}%")

    elif choice == 2:
        bank = SIB()
        loan_type = int(input("Enter loan type:\n1.personal\n2.business\n3.gold\n"))
        if loan_type == 1:
            loan = "personal"
            name =  input("Enter Your Name:")
            age = int(input("Enter Your Age:"))
            if age <= 18:
                print("You are not eligible for the loan")
                continue
            else:
                print("You are eligible for the loan")
            amount = int(input("Enter the amount you want to borrow:"))
            repayment_period = int(input("Enter the repayment period in years:"))
            interest_rate = bank.personal_loan()
            interest = (amount * interest_rate * repayment_period) / 100
            total_amount = amount + interest
            print(f"Total amount to be paid after {repayment_period} years is: {total_amount}")
        elif loan_type == 2:
            loan = "business"
            name =  input("Enter Your Name:")
            age = int(input("Enter Your Age:"))
            if age <= 18:
                print("You are not eligible for the loan")
                continue
            else:
                print("You are eligible for the loan")
            amount = int(input("Enter the amount you want to borrow:"))
            repayment_period = int(input("Enter the repayment period in years:"))
            
            interest_rate = bank.business_loan()
            interest = (amount * interest_rate * repayment_period) / 100
            total_amount = amount + interest
            print(f"Total amount to be paid after {repayment_period} years is: {total_amount}")
        elif loan_type == 3:
            loan = "gold"
            name =  input("Enter Your Name:")
            age = int(input("Enter Your Age:"))
            if age <= 18:
                print("You are not eligible for the loan")
                continue
            else:
                print("You are eligible for the loan")
            amount = int(input("Enter the amount you want to borrow:"))
            repayment_period = int(input("Enter the repayment period in years:"))

            interest_rate = bank.gold_loan()
            interest = (amount * interest_rate * repayment_period) / 100
            total_amount = amount + interest
            print(f"Total amount to be paid after {repayment_period} years is: {total_amount}")
        else:
            print("Invalid loan type")
            continue
        print(f"Interest rate for {loan_type} loan in SIB is: {interest_rate}%")

    elif choice == 3:
        bank = HDFC()
        loan_type = int(input("Enter loan type:\n1.housing\n2.education\n3.car\n"))
        if loan_type == 1:
            loan = "housing"
            name =  input("Enter Your Name:")
            age = int(input("Enter Your Age:"))
            if age <= 18:
                print("You are not eligible for the loan")
                continue
            else:
                print("You are eligible for the loan")
            amount = int(input("Enter the amount you want to borrow:"))
            repayment_period = int(input("Enter the repayment period in years:"))
            
            interest_rate = bank.housing_loan()
            interest = (amount * interest_rate * repayment_period) / 100
            total_amount = amount + interest
            print(f"Total amount to be paid after {repayment_period} years is: {total_amount}")
        elif loan_type == 2:
            loan = "education"
            name =  input("Enter Your Name:")
            age = int(input("Enter Your Age:"))
            if age <= 18:
                print("You are not eligible for the loan")
                continue
            else:
                print("You are eligible for the loan")
            amount = int(input("Enter the amount you want to borrow:"))
            repayment_period = int(input("Enter the repayment period in years:"))
            if age <= 18:
                print("You are not eligible for the loan")
                continue
            else:
                print("You are eligible for the loan")
            interest_rate = bank.education_loan()
            interest = (amount * interest_rate * repayment_period) / 100
            total_amount = amount + interest
            print(f"Total amount to be paid after {repayment_period} years is: {total_amount}")
        elif loan_type == 3:
            loan = "car"
            name =  input("Enter Your Name:")
            age = int(input("Enter Your Age:"))
            if age <= 18:
                print("You are not eligible for the loan")
                continue
            else:
                print("You are eligible for the loan")
            amount = int(input("Enter the amount you want to borrow:"))
            repayment_period = int(input("Enter the repayment period in years:"))
            
            interest_rate = bank.car_loan()
            interest = (amount * interest_rate * repayment_period) / 100
            total_amount = amount + interest
            print(f"Total amount to be paid after {repayment_period} years is: {total_amount}")
        else:
            print("Invalid loan type")
            continue
        print(f"Interest rate for {loan_type} loan in HDFC is: {interest_rate}%")

    elif choice == 4:
        bank = FB()
        loan_type = int(input("Enter loan type:\n1.personal\n2.business\n3.gold\n"))
        if loan_type == 1:
            loan = "personal"
            name =  input("Enter Your Name:")
            age = int(input("Enter Your Age:"))
            if age <= 18:
                print("You are not eligible for the loan")
                continue
            else:
                print("You are eligible for the loan")
            amount = int(input("Enter the amount you want to borrow:"))
            repayment_period = int(input("Enter the repayment period in years:"))
            interest_rate = bank.personal_loan()
            interest = (amount * interest_rate * repayment_period) / 100
            total_amount = amount + interest       
            print(f"Total amount to be paid after {repayment_period} years is: {total_amount}")
        elif loan_type == 2:
            loan = "business"
            name =  input("Enter Your Name:")
            age = int(input("Enter Your Age:"))
            if age <= 18:
                print("You are not eligible for the loan")
                continue
            else:
                print("You are eligible for the loan")
            amount = int(input("Enter the amount you want to borrow:"))
            repayment_period = int(input("Enter the repayment period in years:"))
            interest_rate = bank.business_loan()
            interest = (amount * interest_rate * repayment_period) / 100
            total_amount = amount + interest
            print(f"Total amount to be paid after {repayment_period} years is: {total_amount}")
        elif loan_type == 3:
            loan = "gold"
            name =  input("Enter Your Name:")
            age = int(input("Enter Your Age:"))
            if age <= 18:
                print("You are not eligible for the loan")
                continue
            else:
                print("You are eligible for the loan")
            amount = int(input("Enter the amount you want to borrow:"))
            repayment_period = int(input("Enter the repayment period in years:"))
            interest_rate = bank.gold_loan()
            interest = (amount * interest_rate * repayment_period) / 100
            total_amount = amount + interest
            print(f"Total amount to be paid after {repayment_period} years is: {total_amount}")
        else:
            print("Invalid loan type")
            continue
        print(f"Interest rate for {loan_type} loan in FB is: {interest_rate}%")

    elif choice == 5:
        print("Thank you for using the Bank Loan System. Have a great day!")
        break

    else:
        print("Invalid choice, please try again.")
    print("\n" + "=" * 40)
    print("            LOAN APPROVAL BILL")
    print("=" * 40)
    print(f"Name           : {name}")
    print(f"Age            : {age}")
    print(f"Bank           : {bank.__class__.__name__}")
    print(f"Loan Type      : {loan} Loan")
    print(f"Interest Rate  : {interest_rate}%")
    print("=" * 40 + "\n")