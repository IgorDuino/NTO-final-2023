import gmpy2


a = [[(45, 409), (73, 89), (0, 2), (2, 3)],
[(1, 4), (0, 3), (7, 31)],
[(1, 8), (0, 5), (24, 71), (2236, 17431), (48206, 62617)],
[(79, 709), (1, 8), (205, 349)],
[(1, 4), (0, 5), (8, 11), (57, 83), (281, 509)],
[(0, 2), (5486, 13147)],
[(4, 17), (0, 2), (1951, 2003), (6, 25)],
[(109, 1249), (0, 2), (8, 11), (310, 1091)],
[(1, 8), (2, 3), (17, 37), (999, 2687)],
[(1, 4), (1, 5)],
[(1, 8), (24985, 97187), (17, 37)],
[(107, 121), (1, 8), (0, 3)],
[(1, 4), (2, 9), (6, 25)],
[(1, 2), (52, 59)],
[(1, 4), (6, 7), (8, 11), (71, 151), (22, 347), (84, 127)],
[(1, 2), (0, 3), (6, 25), (8, 11), (498, 751), (546, 977), (13, 23)],
[(34, 61), (0, 32), (2, 3), (1, 5)],
[(5755, 21601), (1, 8), (0, 3), (4, 17), (52, 59)],
[(1613, 5801), (1, 2), (4782, 23911), (4543, 4751)],
[(90, 137), (1, 2), (1237, 2939)],
[(2240, 8737), (1, 4), (2, 9), (8, 13), (1115, 14543)],
[(4, 17), (1, 16), (2, 3), (6, 7)],
[(0, 8), (2, 9), (24, 71), (6, 7), (15, 19)],
[(1, 8), (2, 3)],
[(292, 577), (1, 2), (31239, 47297), (82, 421), (250, 263), (10197, 19423)],
[(1, 4), (2, 3), (1, 5), (6252, 10163), (43, 1151)],
[(1, 4), (35, 73), (15, 53), (84, 127)],
[(1, 2), (2, 3), (0, 5), (273, 1223)],
[(0, 8), (2, 3)],
[(3148, 7901), (1, 4), (73, 149), (6, 7)],
[(29, 64), (2, 9)],
[(1, 4), (23, 239), (1084, 2213), (6, 7)],
[(1, 2), (16, 43)],
[(1, 4), (17, 37)],
[(1, 8)],
[(1, 2), (7, 31)],
[(0, 8), (1, 25)],
[(1, 2), (117, 227), (1, 5), (15, 19)],
[(1, 4), (2, 3), (8, 11), (178, 313), (14, 29)],
[(1, 2), (2200, 10247), (242, 1129), (361, 443), (941, 1759)],
[(1, 2), (582, 1291), (670, 1277), (421, 431)],
[(0, 2), (0, 3), (12774, 26569), (1, 5), (36, 113), (921, 2707), (13, 23)],
[(1, 2), (14, 131)],
[(15, 19), (1, 2), (0, 11)],
[(1, 4), (5601, 42403), (3044, 5861), (6, 7), (950, 16987)],
[(1, 2), (0, 3)],
[(1, 4)],
[(1, 8)],
[(0, 2), (6, 25), (8, 11), (558, 661), (13, 23)],
[(1, 2), (675, 1787), (6, 7)]]

res = []
for i in a:
    for j in i:
        res.append(j)

print(sorted(res, key = lambda x: x[1]))

b = [(1, 4), (6, 7), (8, 11), (8, 13), (1, 16), (4, 17), (15, 19), (13, 23), (6, 25), (14, 29), (7, 31), (17, 37), (16, 43), (15, 53), (52, 59), (34, 61), (29, 64), (24, 71), (35, 73), (57, 83), (73, 89), (36, 113), (107, 121), (84, 127), (14, 131), (90, 137), (73, 149), (71, 151), (117, 227), (23, 239), (250, 263), (178, 313), (22, 347), (205, 349), (45, 409), (82, 421), (421, 431), (361, 443), (281, 509), (292, 577), (558, 661), (79, 709), (498, 751), (546, 977), (310, 1091), (242, 1129), (43, 1151), (273, 1223), (109, 1249), (670, 1277), (582, 1291), (941, 1759), (675, 1787), (1951, 2003), (1084, 2213), (999, 2687), (921, 2707), (1237, 2939), (4543, 4751), (1613, 5801), (3044, 5861), (3148, 7901), (2240, 8737), (6252, 10163), (2200, 10247), (5486, 13147), (1115, 14543), (950, 16987), (2236, 17431), (10197, 19423), (5755, 21601), (4782, 23911), (12774, 26569), (5601, 42403), (31239, 47297), (48206, 62617), (24985, 97187)]


num, rem = [], []

for (r, p) in b:
    if gmpy2.is_prime(p):
        rem.append(r)
        num.append(p)

print(num)
print(rem)
