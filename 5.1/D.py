class Programmer:
    def __init__(self, name, position):
        self.positions = {'Junior': 0, 'Middle': 1, 'Senior': 2}
        self.name = name
        self.position = self.positions[position]
        self.time_worked = 0
        self.salary = 0

    def work(self, time):
        self.time_worked += time
        self.salary += time * (5 + min(3, self.position + 1) * 5 + max(0, self.position - 2))

    def rise(self):
        self.position += 1

    def info(self):
        return f'{self.name} {self.time_worked}ч. {self.salary}тгр.'


programmer = Programmer('Васильев Иван', 'Junior')
programmer.work(750)
print(programmer.info())
programmer.rise()
programmer.work(500)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
