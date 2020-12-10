

with open("input9.txt") as f:
	all = [int(x) for x in f.readlines()]

print("Found %d numbers" % len(all))

prem = 25

def check_valid(i):
	if i < prem:
		print("this can't be")
		return False
	for x in range(i-prem,i):
		for y in range(i-prem,i):
			if x==y:
				continue
			if all[x]+all[y]==all[i]:
				return True

	return False

# Find first number that is not valid
def find_first_not_valid(all, prem):
	for i in range(prem, len(all)):
		if not check_valid(i):
			print("%d is not valid" % all[i]);
			return all[i]
		else:
			print("%d is valid" % all[i]);

bad_val = find_first_not_valid(all, prem)

# Find a contiguous set of numbers that 
def find_set(all, prem, bad_val):
	for x in range(0, len(all)):
		for y in range(x, len(all)):
			if bad_val == sum(all[x:y]):
				if y-x < 2:
					continue
				return x,y

x,y = find_set(all, prem, bad_val)
sum = min(all[x:y])+max(all[x:y])

print("Sum of smallest and largest number from continuous set that sums to %d is %s" % (bad_val, sum))
		
