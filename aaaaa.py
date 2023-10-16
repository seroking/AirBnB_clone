class Home():
	atr = 15


lan = Home()

lan.rr = 20

dic = {"ab" : 23, "cc" : 30}

lan.__dict__ = {**dic, **lan.__dict__}

print(lan.__dict__)