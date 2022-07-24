def read(s):
    return [i.strip() for i in open(s, 'r')]
lines = read('19a.input')

replacements = []
for i in lines[:-2]:
    m = re.findall(r'(\S+) => (\S+)', i)
    replacements.append(m[0])
X = lines[-1]