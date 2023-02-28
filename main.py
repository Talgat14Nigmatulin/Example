#1
'''class Shop(object):


    def __init__(self, name, quantity, sumn, description):
        self.name = name
        self.quantity = quantity
        self.sumn = sumn
        self.description = description

    def namm(self):
        return f'Name: {self.name}'
    
    def quav(self):
        return f'Description: {self.description}'
    
    def quant(self):
        return f'Quantity: {self.quantity}'
    
    def su(self):
        return f'Summ: {self.sumn}'
    
        
    def sas(self):
        things = int(input('Сколько вы хотите купить штук?: '))
        return f'{1500 * things}uzs3'

    
    
if __name__ == '__main__':
    shoping = Shop('Marker', 'Black, small', 1500, 10)

    print(shoping.namm())
    print(shoping.quav())
    print(shoping.quant())
    print(shoping.su())
    print(shoping.sas())'''


#2
def get_uniq(numbers: tuple) -> list:
    set1 = set()
    set2 = set()
    for number in numbers:
        if number not in set1:
            set1.add(number)
        else:
            set2.add(number)
    return [number for number in numbers if number in set1 - set2]
 
 
a = (1,2,3,4,5,6,7,8,9,1)


print(get_uniq(a))

def get_birzadbirzad(numbers: tuple) -> list:
    set1 = set()
    set2 = set()
    for number in numbers:
        if number not in set1:
            set1.add(number)
        else:
            set2.add(number)
    return [number for number in numbers if number in set1 - set2]
 
 
b = (1,2,3,4,5,6,7,8,9,2)


print(get_birzadbirzad(b))

def get_elfwef(numbers: tuple) -> list:
    set1 = set()
    set2 = set()
    for number in numbers:
        if number not in set1:
            set1.add(number)
        else:
            set2.add(number)
    return [number for number in numbers if number in set1 - set2]
 
 
c = (1,2,3,3,5,6,7,8,9,1)


print(get_elfwef(c))



        