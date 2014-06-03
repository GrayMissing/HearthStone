file = open('cardactions.py', 'r')
reader = file.readlines()
n = []
for row in reader:
    row = row.strip()
    newrow = "'" + row + "'" + ':' + row
    n.append(newrow)
file.close()
files = open('cardactions.py', 'w')
for newrow in n:
    files.write('    ' + newrow + ','  +'\n')

