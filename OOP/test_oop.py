class Spell:
    def __init__(self,name,formula) -> None:
        self.name = name
        self.formula = formula
    
        
    def get_description(self):
        return f'{self.name} {self.formula} го бухатос и еб@тос'
    
    def execute(self):
        return f'потом стапее'
    

    def __str__(self) -> str:
        return f'Зелия: {self.name}\nФормула: {self.formula}\nЗаклинани: Го бухатос и еб@тос\nпотом стапее нах'
    
class One(Spell):
    def zaklinani(self):
        print('Zarkpotronos')

class Two(Spell):
    def zaklinani(self):
        print('AShkalaiMashkalai')


class Thre(Spell):
    def zaklinani(self):
        print('TakalokPakolok')

    
 
a = Spell('Марибутос', 'H₂SO₄')
# print(a.get_description())
print()
# print(a.execute())
print(a)
o = One('Марибутос', 'H₂SO₄')
t = Two('Марибутос', 'H₂SO₄')
h= Thre('Марибутос', 'H₂SO₄')
o.zaklinani()
t.zaklinani()
h.zaklinani()