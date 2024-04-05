import random
class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 10
        self.progress = 1
        self.money = 30
        self.alive = True

    def to_study(self):
        print(" 👨‍🎓Время учёбы👨‍🎓 ")
        self.progress += 0.12
        self.gladness -= 3
        self.money += 0.10


    def to_sleep(self):
        print(" 😴Я спать😴 ")
        self.gladness += 3
        self.money -= 0.10

    def to_chill(self):
        print(" 🎉Время отдыха🎉 ")
        self.gladness += 5
        self.progress -= 0.1
        self.money -= 10

    def to_work(self):
        print(" 👩‍💻Время работы👩‍💻 ")
        self.gladness -= 1
        self.progress += 0.1
        self.money += 10

    def is_alive(self):
        if self.progress < -0.5:
            print("⬆❌                   ВОН…!         ❌⬆")
            self.alive = False
        elif self.gladness <= 0:
            print("⬆❌               Депрессия…!         ❌⬆")
            self.alive = False
        elif self.progress > 5:
            print("⬆❌                Автомат…!         ❌⬆")
            self.alive = False
        elif self.money <= 0:
            print("⬆❌         Нет денег-нет учёбы...!         ❌⬆")
            self.alive = False

    def end_of_day(self):
        print("---------------------------------------")
        print(f"😂Радость = {self.gladness}")
        print(f"⬆⬆Прогресс = {round(self.progress, 2)}")
        print(f"💵Деньги = {round(self.money, 2)}")
        print("---------------------------------------")

    def live(self, day):
        day = " День " + str(day) + " ученика(цы) " + self.name + " из жизни в колледже "
        print(f"{day:+^60}")
        live_cube = random.randint(1, 4)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        elif live_cube == 4:
            self.to_work()
        self.end_of_day()
        self.is_alive()

nick = Student(name="👨Ника👨")
kate = Student(name="👩Кейт👩")
Misha = Student(name="👦Миши👦")
Anna= Student(name="👩Анны👩")
for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)
    if kate.alive == False:
        break
    kate.live(day)
    if Misha.alive == False:
        break
    Misha.live(day)
    if Anna.alive == False:
        break
    Anna.live(day)