var_1= 'a'
var_2 = 'b'
var_3 = 'c'
var_4 = 'd'
for i in range(1,5):
  key = 'var_{}'.format(i)  
  print (locals()[key])
