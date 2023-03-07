class Pizza:
    def __init__(self, description, cost):
        self.description = description
        self.cost = cost

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost



class Klasik(Pizza):  # inheritance
    def __init__(self):
        self.cost = 100
        self.description = "Klasik Pizza standart malzemeleri : Yeni Sucuk, Mozarella Peyniri, Pizza Sos "




class Margherita(Pizza):  # inheritance
    def __init__(self):
        self.cost = 120
        self.description = "Margherita Pizza standart malzemeleri : Mozarella Peyniri, Pizza Sos "




class TurkPizza(Pizza):  # inheritance
    def __init__(self):
        self.cost = 130
        self.description = "Turk Pizza standart malzemeleri : et, Jambon, Pepperoni, Yeni Sucuk, Sosis "





class DominosPizza(Pizza):  # inheritance
    def __init__(self):
        self.cost = 200
        self.description = "Dominos Pizza standart malzemeleri : Jambon, Pepperoni, Yeni Sucuk, Sosis, Mozarella Peyniri, Pizza Sos,  Biber, Domates, Dominos Sos "



class Decorator(Pizza):
    def __init__(self, description, cost):
        Pizza.__init__(self, description, cost)

    def get_description(self):
        return Pizza.get_description(self)

    def get_cost(self):
        return Pizza.get_cost(self)



class Zeytin(Decorator):
    def __init__(self):
        self.cost = 6
        self.description = "\t Ekstra malzeme : Zeytin "


class Mantar(Decorator):
    def __init__(self):
        self.cost = 8
        self.description = "\t Ekstra malzeme : Mantar "


class KeciPeyniri(Decorator):
    def __init__(self):
        self.cost = 15
        self.description = "\t Ekstra malzeme : Keci Peyniri "


class Et(Decorator):
    def __init__(self):
        self.cost = 20
        self.description = "\t Ekstra malzeme : Et "


class Sogan(Decorator):
    def __init__(self):
        self.cost = 7
        self.description = "\t Ekstra malzeme : Soğan "

class Mısır(Decorator):
    def __init__(self):
        self.cost = 9
        self.description = "\t Ekstra malzeme : Mısır "
