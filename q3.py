# create a list a = [1,1,2,3,5,8,13,21,34,55,89] and write a python program that 
# prints out all the elements less then 5

a = [1,1,2,3,5,8,13,21,34,55,89]

print(list(filter(lambda x:x<5,a)))
