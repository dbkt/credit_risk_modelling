import Functions

levels_dict = {1:"Consultant", 2:"Senior Consultant", 3:"Manager", 4:"Senior Manager", 5:"Director", 6:"Partner"}

class Worker:
    def __init__(self, name, title, salary, experience, count_employe):
        self.name = name
        self.title = title
        self.salary = salary
        self.experience = experience
        self.count_employe = count_employe
        self.revenue_month = None
        self.bonus = None
    
    def promote(self):
        if self.title == "Partner":
            return print("Beförderung aufgrund des bereits höchsten Levels nicht möglich.")
        elif self.title in levels_dict.values():
            self.title = levels_dict[Functions.get_key_from_value(levels_dict, self.title) + 1]
            print(f"Herzlichen Glückwunsch! Sie wurden zum {self.title} befördert!")
    
    def increase_salary(self, percent):
        self.salary *= 1 + percent
        self.salary = int(round(self.salary, 0))
        print(f"Herzlichen Glückwunsch! Sie verdienen ab sofort {self.salary}€!")
    
    def bonus_year(self, percent):
        bonus = int(round(self.salary*12*percent,0))
        self.bonus = bonus
        print(f"Aufgrund Ihrer herausragenden Leistungen erhalten Sie einen Bonus in Höhe von {bonus}€!")
        
    
    def revenue_month(self, daily_rate, days):
        revenue = int(round(daily_rate * days,0))
        self.revenue_month = revenue
        return print(f"Der Umsatz in diesem Monat betrug {revenue}€")
