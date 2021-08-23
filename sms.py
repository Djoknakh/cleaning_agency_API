class Sms_ru():

    def __init__(self, phone:str):
        self.phone = phone

    def parse_phone(self):
        self.phone = self.phone.replace("+", "")
        self.phone = self.phone.replace("-", "")
        self.phone = self.phone.replace(" ", "")
        self.phone = self.phone.replace("(", "")
        self.phone = self.phone.replace(")", "")
        if self.phone[0] == "7" or self.phone[0] == "8":
            self.phone = self.phone[1:]
        if len(self.phone) == 10 and self.phone.isdigit() == True:
            print("Телефон валидный")
        else:
            print("Телефон не валидный, введите заново")

my_phone = "+7 (998) 999-99-99"
mysms = Sms_ru(my_phone)
mysms.parse_phone()
