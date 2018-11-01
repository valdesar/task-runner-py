file = open("test.txt", "r") 
ind = 1
#for line in file:
#    print (line)

data = file.readlines()
data[1] = 'Mage\n'

file.close()

with open('test.txt', 'w') as file:
    file.writelines( data )


#print (file.readline(2))