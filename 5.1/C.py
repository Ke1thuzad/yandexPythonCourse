class RedButton:
    def __init__(self):
        self.click_amount = 0

    def click(self):
        self.click_amount += 1
        print('Тревога!')

    def count(self):
        return self.click_amount