def get_data():
  file = open("challenge.txt", 'r')
  content = file.read()
  file.close()
  
  return content

def structure_data(data):
  list_of_rows = data.split('\n')
  final_list = []
  for row in list_of_rows:
    list_of_chars = [char for char in row]
    final_list.append(list_of_chars)
  return final_list
  
def searching(grid, row, col ,found_numbers):
  if(grid[row][col] == '.' or grid[row][col] not in normal_chars):
    return
  
  found_number = int(get_number(grid, row, col))
  
  if(found_number not in found_numbers):
    found_numbers.append(found_number)

def get_number(grid, row, col):
  new_col = col
  char = grid[row][col]
  numbers = ('0','1','2','3','4','5','6','7','8','9')
  my_number = ''
  while(char in numbers and new_col > 0):
    new_col -= 1
    char = grid[row][new_col]
  
  if(char in numbers):
    my_number += char
  else:
    new_col += 1
    char = grid[row][new_col]
    my_number += char
  
  while(char in numbers and new_col < len(grid[row]) - 1):
    new_col += 1
    char = grid[row][new_col]
    if(char in numbers):
      my_number += char
      
  return my_number
  
  
  

string_data = get_data()
enhanced_data = structure_data(string_data)
normal_chars = ('0','1','2','3','4','5','6','7','8','9','.')
numbers = ('0','1','2','3','4','5','6','7','8','9')
total_sum = 0

for i in range(0, len(enhanced_data)):
  for j in range(0, len(enhanced_data[i])):
    if(enhanced_data[i][j] not in normal_chars):
      found_numbers = []
      searching(enhanced_data, i - 1, j - 1, found_numbers)
      searching(enhanced_data, i - 1, j, found_numbers)
      searching(enhanced_data, i - 1, j + 1, found_numbers)
      searching(enhanced_data, i, j - 1, found_numbers)
      searching(enhanced_data, i, j + 1, found_numbers)
      searching(enhanced_data, i + 1, j - 1, found_numbers)
      searching(enhanced_data, i + 1, j, found_numbers)
      searching(enhanced_data, i + 1, j + 1, found_numbers)
      
      if(enhanced_data[i][j] == '*' and len(found_numbers) > 1):
        my_product = 1
        for number in found_numbers:
          my_product *= number
        total_sum += my_product
        
print(total_sum)
      