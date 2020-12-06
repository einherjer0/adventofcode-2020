

with open("input6.txt") as f:
	all = f.read().split("\n\n")
	groups = [group.rstrip().split("\n") for group in all]
	
print("Found %d groups" % len(groups))
		
m = [len(''.join(set(''.join(group)))) for group in groups]
print("Sum of yes answer per group is %d" % sum(m))

import functools
m = [len(functools.reduce(lambda a,b : set(a) & set(b), group)) for group in groups]
print("Sum of all common yes answers per group is %d" % sum(m))


