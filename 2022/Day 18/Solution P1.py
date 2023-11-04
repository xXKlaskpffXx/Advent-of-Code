with open("2022\Day 18\Input.in") as file:
    data = [i for i in file.read().strip().split("\n")]

black_site_counter = 0
exposed_site_counter = len(data)*6

for i in data:
    x1 = int(i.split(",")[0])
    y1 = int(i.split(",")[1])
    z1 = int(i.split(",")[2])

    for i2 in data:
        x2 = int(i2.split(",")[0])
        y2 = int(i2.split(",")[1])
        z2 = int(i2.split(",")[2])

        if not ((x1 == x2) & (y1 == y2) & (z1 == z2)):
            
            if (x1 == x2) & (y1 == y2) & ((z1 - z2) >= -1) & ((z1 - z2) <= 1):
                black_site_counter += 1
            elif (x1 == x2) & ((y1 - y2) >= -1) & ((y1 - y2) <= 1) & (z1 == z2):
                black_site_counter += 1
            elif ((x1 - x2) >= -1) & ((x1 - x2) <= 1) & (y1 == y2) & (z1 == z2):
                black_site_counter += 1
print(exposed_site_counter)
print(black_site_counter)
print(exposed_site_counter - black_site_counter)