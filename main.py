for i in range(0,7):
  print(i)

def find_value(num,list):
  for i in range(0,len(list)):
    if(list[i]==num):
      return True
    
  return False



my_list = [1,34,4,5,2]
print(find_value(5,my_list))

