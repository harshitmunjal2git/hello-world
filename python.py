x=5
print(x)
try:
  print(x)
except:
  print("x is not defined thus error")
def my_fun(a):
  return a*a

x=my_fun(7)
print(x)
 
#lambda
x=lambda a,b:a+b
print(x(1,2))
