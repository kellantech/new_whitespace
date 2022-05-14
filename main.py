file1 = open('pr.txt', 'r')
count = 0
ls = []
while True:

    count += 1
    line = file1.readline()
    if not line:
        break
    ls.append( line)	
out = ''
for l in ls:
	c=0
	for n in range(len(l)):
		if l[n] == ' ':c+=1
	if c == 1: 		out += '+'
	if c == 2: 		out += '-'
	if c == 3: 		out += '.'
	if c == 4: 		out += ','
	if c == 5: 		out += '>'
	if c == 5: 		out += '<'
	if c == 6: 		out += '?'
with open('out.crz','a') as f:
	f.write(out)
