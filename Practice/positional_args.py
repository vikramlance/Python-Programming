def test(a, b=None, c=None):
  print("wow a")
  print(a)
  print("wow b")
  print(b)
  print("wow c")
  print(c)    
  return None

m = test(1,2)
# wow a
# 1
# wow b
# 2
# wow c

m = test(1,c=2)
# wow a
# 1
# wow b
# None
# wow c
# 2
