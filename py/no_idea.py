n,m  = raw_input().strip().split()
list_of_integers = [int(i) for i in raw_input().strip().split()]
list_A = {int(i) for i in raw_input().strip().split()}
list_B = {int(i) for i in raw_input().strip().split()}

happiness = 0

for i in list_of_integers:
	if i in list_A:
		happiness +=1
	elif i in list_B:
		happiness -=1

print happiness