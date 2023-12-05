def get_data():
  file = open("challenge.txt", 'r')
  content = file.read()
  file.close()
  return content

def enhanced_data():
  data = get_data()
  row_data = data.split('\n')
  my_dict = {}
  for i in range(0,len(row_data)):
    list_char = row_data[i].split(" ")
    my_dict[list_char[1].replace(":","")] = {
      'winning': list_char[3:7],
      'numbers': list_char[8:]
    }
  return my_dict

data_structure = enhanced_data()
total_sum = 0
for key,value in data_structure.items():
  print(f'{key}\n')
  winning_numbers = []
  my_sum = 0
  for item in value['numbers']:
    if(item in value['winning']):
      winning_numbers.append(item)
  for number in winning_numbers:
    if(my_sum == 0):
      my_sum += 1
    else:
      my_sum *= 2
  total_sum += my_sum
  

    