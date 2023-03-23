
def generatorExample():
   yield "T"
   yield "U"
   yield "T"
   yield "O"
   yield "R"
   yield "I"
   yield "A"
   yield "L"
   yield "S"
# calling the generatorExample() function which is created above
result = generatorExample()
# Traversing in the above result(generator object)
for k in result:
   # Printing the corresponding value
   print(k)