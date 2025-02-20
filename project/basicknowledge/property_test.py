class Person:
    def __init__(self,name,age):
        self._name=name
        self._age=age
    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self,value):
        if value<0:
            raise ValueError("年齢は０以上である必要があります")
        self._age=value

# test
p= Person("Tom",25)
p.age=30
print(p.age)
# p.age=-5 #ValueError: 年齢は０以上である必要があります