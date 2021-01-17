x=int(input("Insira um valor qualquer para x: "))
y=int(input("Insira outro valor qualquerpara y: "))
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def mult(x,y):
    return x*y
def div(x,y):
    return x/y
def div_int(x,y):
    return x//y
def mod(x,y):
    return x%y

operadores = [add,subtract,mult,div,div_int,mod]
sinais = ["+","-","x","/","//","resto"]
for i in range(0,len(operadores)):
    print(x,sinais[i],y,'=',operadores[i](x,y))
