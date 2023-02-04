hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error, please enter numeric input")
    quit()
if h <= float(40):
	print(h * r)
	
else:
	print((40 * r) + (1.5 * r * (h - 40)))
