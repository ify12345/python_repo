code1 = 'rectangle'
code2 = 'triangle'
code3 = 'arrow head'

shape_code = input('ENTER SHAPE CODE:')
shape_length = int(input('ENTER SHAPE LENGTH:'))

def rectangle():
  for j in range(shape_length):
    for i in range(shape_length):
        print('*',end="")
    print() 

def triangle():
    for i in range(1, shape_length+1):
     print('* '* i)

def arrow_head():
 for i in range(0,shape_length):
      for j in range(0,i+1):
        print('*', end=' ')
      print()
 for i in range(shape_length,1, -1):  
    for j in range(1,i):
        print('*', end=' ')
    print() 



if shape_code == code1:
   rectangle()
elif shape_code == code2:
   triangle()
elif shape_code == code3:
   arrow_head()
else:
   print('enter a valid shape')
   

