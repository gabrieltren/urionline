s =float(0)
d =int(1)

for k in range(1,40,2):
    s+= k/d
    d*=2
print("{:.2f}" .format(s))
