class Sms_ru():

    def __init__(self, phone:str):
        self.phone = phone

    def validation_phone(self):
        """Валидация телефона"""
        for i in ["+", "-", " ", "(", ")"]:
            self.phone = self.phone.replace(i, "")
        if self.phone[0] == "7" or self.phone[0] == "8":
            self.phone = self.phone[1:]
        if len(self.phone) == 10 and self.phone.isdigit() == True:
            return True
        else:
            return False


