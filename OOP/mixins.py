# Mixins
# Миксины - классы которые используются для наследование и передача дочерним классам определенных методов но от них не создаются объекты
# для чего:
# 1. вы хотите предоставить множество доп методов для классов
# 2. вы хотиите использовать один конкретный метод во множестве разных классов

# class EngineMixin:
#     def start_engine(self):
#         print('Started engine')

# class RadioMixin:
#     def play_radio(self):
#         print('Started radio')       

# class Auto(EngineMixin, RadioMixin):
#     pass

# class Plane(EngineMixin):
#     pass

# class SmartPhone(RadioMixin):
#     pass

# class Train(EngineMixin, RadioMixin):
#     pass

# ---------------------------------------------------------------

# class FlyMixin:
#     def fly(self):
#         print('I can flu')

# class WalkMixin:
#     def walk(self):
#         print('I can walk')

# class SwimMixin:
#     def swim(self):
#         print('I can swim')


# class Human(WalkMixin, SwimMixin):
#     name = 'human'

#     def talk(self):
#         print('i can talk')

# class Fish(SwimMixin):
#     name = 'fish'

# class Volan(FlyMixin, SwimMixin):
#     name = 'volan'

# class Duck(FlyMixin, WalkMixin,SwimMixin):
#     name = 'duck'

# obj = Human()
# obj.walk()
# obj.swim()
