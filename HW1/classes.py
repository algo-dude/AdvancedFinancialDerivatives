class scuba():
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.suit_size = 'large'
        self.type = 'wet'
        self.o2_tank = 'empty'
        self.mask = False
        self.regulator = False
        self.experience = 0
        self.allowed_depth = 20         

    def suit_up(self, type):
        if self.weight > 100:
            self.suit_size = 'large'
        elif self.weight > 50:
            self.suit_size = 'medium'
        elif self.weight > 10:
            self.suit_size = 'small'
        
        if type == 'dry':
            self.suit_type = 'dry'
        elif type == 'wet':
            self.suit_type = 'wet'
        else:
            self.suit_type = 'unknown'
        print (self.suit_size, self.suit_type)

    def fill_tank(self):
        self.o2_tank = 'full'
        
    def put_on_gear(self):
        self.mask = True
        self.regulator = True

    def do_scuba(self):
        if self.o2_tank == 'full' and self.suit_type != 'unknown' and self.mask == True and self.regulator == True:
            print ('you did a scuba dive')
            self.experience += 1
            self.allowed_depth += 5
            print (f'{self.name}, your experience is {self.experience} dives and you may dive to {self.allowed_depth} meters')
        else:
            print ('go fix your gear or whatever')
   