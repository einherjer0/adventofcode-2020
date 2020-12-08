

with open("input7.txt") as f:
	all = f.readlines()

rules = dict()

for rule in all:
	rule = rule.replace("bags", "").replace("bag","").replace(".","").rstrip()
	key, val = rule.split("contain")
	rules[key.rstrip()] = [(v.split()[0],' '.join(v.split()[1:])) for v in val.split(",")]

print("Found %d rules." % len(rules))

def contains(outside_bag, bag_name):
	return any([bag == bag_name for count, bag in rules[outside_bag]])

def is_empty(bag_name):
	return rules[bag_name][0] == ('no', 'other')

def find_containing_bags(target_bag_name):
	if is_empty(target_bag_name):
		return
	for bag_name in rules.keys():
		if contains(bag_name, target_bag_name):
			if bag_name not in good_bags:
				good_bags.append(bag_name)
			find_containing_bags(bag_name)

good_bags = list()
find_containing_bags("shiny gold")
print("%d bags contain shiny gold bag" % len(good_bags))	

def count_bags(target_bag_name):
	if is_empty(target_bag_name):
		return 1
	return 1+sum([int(count)*count_bags(bag) for count, bag in rules[target_bag_name]])

print("shiny gold bag can contains %d bags" % (count("shiny gold")-1))
