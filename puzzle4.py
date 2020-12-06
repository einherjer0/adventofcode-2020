import re

required_keys = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")


def valid_entry(key, v):
	if key == "byr":
		return len(v) == 4 and 1920 <= int(v) <= 2002
	elif key == "iyr":
		return len(v) == 4 and 2010 <= int(v) <= 2020
	elif key == "eyr":
		return len(v) == 4 and 2020 <= int(v) <= 2030
	elif key == "hgt":
		if v.endswith("cm"):
			return 150 <= int(v[:-2]) <= 193
		elif v.endswith("in"):
			return 59 <= int(v[:-2]) <= 76
		else:
			return False
	elif key == "hcl":
		return v.startswith("#") and re.match("^[a-z0-9]*$", v[1:]) and len(v) == 7
	elif key == "ecl":
		return v in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
	elif key == "pid":
		return len(v) == 9 and v.isdigit()
	elif key == "cid":
		return True

with open("input4.txt") as f:
	passport = ""
	passports = list()
	for line in f:
		if line != "\n":
			passport += line.rstrip()+" "
		else:
			passports.append(passport.rstrip())
			passport = ""

	# deal with last line...
	if passport:
		passports.append(line.rstrip())

	print("Found %d passports" % len(passports))	

c = 0
for p in passports:
	keys = tuple(info.split(":")[0] for info in p.split(" "))
	values = tuple(info.split(":")[1] for info in p.split(" "))

	if set(required_keys).issubset(set(keys)):
		test = [valid_entry(keys[i], values[i]) for i in range(0,len(keys))]
		if all(test):
			c+=1

print("Found %d valid entries" % c)
