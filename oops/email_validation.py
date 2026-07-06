class EmailValidation :
    def __init__(self, e):
        self.email = e

    def check(self):
        has_at = "@" in self.email
        has_upper = self.email.isupper()

        if has_upper:
            print("email contain capital letters")
        else :
            if has_at:
                print(f"{self.email} is valid")
            else:
                print("not valid : doesn't contain @")
    

email = input("enter any email id : ")
e = EmailValidation(email)
e.check()


