class gova:
    name=""
    drink=""
    def party(self):
        print("Let's party!")
    def beach(self):
        print("Let's go to the beach!") 
ramesh=gova()
suresh=gova()

ramesh.name="Ramesh"
suresh.name="Suresh"

ramesh.drink="yes"
suresh.drink="no"

print(ramesh.name)
print("drink",ramesh.drink)

print(suresh.name)
print("drink",suresh.drink)

ramesh.party()
suresh.beach()

print("\n")

class laptop:
    price=0
    processor=""
    ram=""
hp=laptop()
dell=laptop()
lenovo=laptop()
hp.price=45000
hp.processor="i5"
hp.ram="8GB"

dell.price=55000
dell.processor="i7"
dell.ram="16GB"

lenovo.price=60000
lenovo.processor="i9"
lenovo.ram="32GB"

print("HP laptop price:", hp.price)
print("hp processor:", hp.processor)
print("hp ram:", hp.ram)
print("\n")
print("Dell laptop price:", dell.price)
print("dell processor:", dell.processor)
print("dell ram:", dell.ram)
print("\n")
print("Lenovo laptop price:", lenovo.price)
print("lenovo processor:", lenovo.processor)
print("lenovo ram:", lenovo.ram)



