#używając __add__, __sub__, itd. ????
import re
import string
def generate_slupek(operation):
   '''generates slupek
   arguments:
      operation (str): operation as string separated by spaces
   raises:
     none
   returns:
     None
   '''
   num_1, operator, num_2 = operation.split()
   #czy używać lista = re.findall(r'(\d+|\D)', operation) itd.
   result = eval(operation)
   length = max(len(num_1), len(num_2)+2, len(str(result)))
   print(num_1.rjust(length))
   print((operator+num_2.rjust(length-len(operator))))
   print('-' * length)
   print(str(result).rjust(length))
generate_slupek("81 * 92480984203942") #czy może działać tylko z spacjami?
