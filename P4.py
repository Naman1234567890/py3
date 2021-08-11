class BankAtm:
    def __init__(self,cardNo,pin):
        self.card = cardNo
        self.passcode = pin

    def balanceEnquiry(self):
        print("Your balance is €10,00,000.")

    def cashWithdrawl(self,amount):
        if amount <= 1000000:
            new_amount = 1000000 - amount
            print("You have withdrawn amount "+str(amount)+". Your remaining balance is "+str(new_amount))
        
        else:
            print("Not enough money in your account for requested withdrawl.")

def mainFunc():
    cardNo = input("Enter your card number: - ")
    pin = input("Insert your pin:- ")

    newUser = BankAtm(cardNo,pin)

    print('Choose help.')
    print('1. Balance Enquiry.')
    print('2. Cash Withdrawl.')

    help = int(input('Press 1 for balance enquiry/press 2 for cash withdrawl: '))

    if(help == 1):
        newUser.balanceEnquiry()
    elif(help == 2):
        amount = int(input("Enter your amount."))
        newUser.cashWithdrawl(amount)
    else:
        print("Press a valid number.")

if __name__ == "__main__":
    mainFunc()