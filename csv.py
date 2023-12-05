import csv
f = open("info.csv")

r = csv.reader(f)

g1 = next(r)
print(g1)
g2 = next(r)
print(g2)
f.close()
