# dict {
#   '1': [15, 33, 22],
#   '2': [9, 5, 18]
#}

def createDataStructure():
  file = open("challenge.txt", 'r')
  content = file.read()
  my_map = {}
  list_of_text = content.split('\n')
  for row in list_of_text:
    new_list = row.split()
    for i in range(0, len(new_list)):
      new_list[i] = remove_chars(new_list[i])
      
    my_map[int(new_list[1])] = new_list[2:]

  for key, value in my_map.items():
    my_map[key] = [True, 0 ,0 ,0]
    for i in range(0, len(value)):
      check_list = [12,13,14]
      if(value[i] == 'red'):
        if(int(value[i - 1]) > my_map[key][1]):
          my_map[key][1] = int(value[i - 1])
        if(int(value[i - 1]) > check_list[0]):
          my_map[key][0] = False
      elif(value[i] == 'green'):
        if(int(value[i - 1]) > my_map[key][2]):
          my_map[key][2] = int(value[i - 1])
        if(int(value[i - 1]) > check_list[1]):
          my_map[key][0] = False
      elif(value[i] == 'blue'):
        if(int(value[i - 1]) > my_map[key][3]):
          my_map[key][3] = int(value[i - 1])
        if(int(value[i - 1]) > check_list[2]):
          my_map[key][0] = False
  
      
  file.close()
  return my_map

def remove_chars(s):
  for char in [":", ",", ";"]:
    s = s.replace(char, "")
  return s

data = createDataStructure()
total_sum = 0
product = 0
for key,value in data.items():
  if(value[0] == True):
    total_sum += key
  product += value[1] * value[2] * value[3]
  

print(total_sum, product)
  