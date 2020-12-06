

with open("input5.txt") as f:
	tickets = f.read().split()

print("Found %d tickets" % len(tickets))

def update(code, minval, maxval):
	if not code:
		return minval

	mid = (maxval-minval)/2
	if code[0] in ('F', 'L'):
		return update(code[1:], minval, minval+mid)
	elif code[0] in ('B', 'R'):
		return update(code[1:], minval+mid, maxval)


m = [update(t[0:7],0,128) * 8 + update(t[7:],0,8) for t in tickets]
print("Highest ticket ID %d" % max(m))
m.sort()
for i in range(len(m)):
	if m[i+1] != m[i]+1:
	print("My ticket is %d" % (m[i]+1))
		break
		
	
