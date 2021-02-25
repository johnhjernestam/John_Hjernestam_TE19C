def f(x):
    return -x**2

print(f(3))
print(f(-3))

# annat exempel

def sayHello():
    print("Hej")

sayHello()

# mer

def skrivUt(text):
    print(text)

skrivUt("TE19 är bäst")
skrivUt("TE19C ska sluta spela spel kort")

# mer, sista

def minsta(tal1,tal2):
    if tal1 < tal2:
        return tal2
    else:
        return tal1

print(minsta(1,1000000))