
with open("input8.txt") as f:
	all = f.readlines()

cmds = [line.split() for line in all]


def process(tmp):
	accumulator = 0
	i = 0;
	try:
		while tmp[i][0] != None:
			cmd, val = tmp[i]
			if cmd == "acc":
				accumulator += int(val)
				tmp[i][0] = None
				i+=1
			elif cmd == "jmp":
				tmp[i][0] = None
				i+=int(val)
			elif cmd == "nop":
				tmp[i][0] = None
				i+=1
	except IndexError:
		return accumulator, True
	return accumulator, tmp[i][0] != None

import copy
c = copy.deepcopy(cmds)
print("Accumulator value is %d. Valid? %s" % process(c))

for i in range(0, len(cmds)):
	if cmds[i][0] == "acc":
		continue

	c = copy.deepcopy(cmds)
	c[i][0] = "nop" if c[i][0] == "jmp" else "jmp"
	acc, valid = process(c)
	print("Accumulator value is %d. Valid? %s" % (acc, valid))
	if valid:
		break
	
	
