file1 = open('pr.txt', 'r')
count = 0
ls = []
while True:

    count += 1
    line = file1.readline()
    if not line:
        break
    ls.append(line)
out = ''
for l in ls:
    c = 0
    c2 = 0
    for n in range(len(l)):
        if l[n] == ' ': c += 1
    if c == 1: out += '+'
    if c == 2: out += '-'
    if c == 3: out += '.'
    if c == 4: out += ','
    if c == 5: out += '>'
    if c == 6: out += '<'
    if c == 7: out += '?'
    if c == 8: out += ':'
    if c == 9: out += ';'
    if c == 10: out += '#'
    if c == 11: out += '`'
    if c == 12: out += '~'
    if c == 13: out += '['
    if c == 14: out += ']'
    if c >= 15 and c < 25: out += str(c - 15)

with open('out.crz', 'a') as f:
    f.write(out)
