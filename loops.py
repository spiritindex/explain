for i in range(1,6):  #includes first item, not the last
	print(i)

fruits = ["apple", "orange", "kiwi"]
for fruit in fruits:
	print(fruit)

print("\n")
for fruit in fruits:
	if fruit == "kiwi":
		print(fruit)
	else:
		print("Not kiwi")

print("\n")
for i in range(1,10,2):
	print(i)


print("\n")
#while loops
count = 1
while count <= 5:
	print(count)
	count +=1

correct = False
attempt = 1
password = "python"
while not(correct) and attempt<4:
	pw = input("Enter your password: ")
	if pw == password:
		print("ACCESS GRANTED (you took",attempt,"attempts)")
		correct = True
	attempt += 1


print("\n")
x = input("Enter something: ")
while x != "stop":
	x = input("Enter something: ")

print("\n")
while True:
	x = input("Say something: ")
	if x == "stop":
		break  #break statement checks if its within a loop, and simply gets out of it