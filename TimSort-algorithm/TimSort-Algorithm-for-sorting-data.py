# Opening text file of unsorted data
dataset = open('unsorted_data.txt', 'w')
 
# TimSort Algorithm
# Use a lambda inside sort to convert them to float and then sort properly
sorted(dataset, key = lambda k: int(k.split(' ')[1]))
new_dataset = '\n'.join(sorted(dataset, key = lambda m: int(m.split(' ')[1])))
 
# Print the sorted data
print(new_dataset)
 
# Saving the sorted dataset into text file
new_dataset.write('sorted_data.txt')
new_dataset.close()