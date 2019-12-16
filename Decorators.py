def wrapitUp(func):
    print("I am in gift wrapper")
    func()

def gift():
    print("I am in gift")


gift = wrapitUp(gift)
gift
