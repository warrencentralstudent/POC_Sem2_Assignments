def times2(a): return a * 2
def div2(a): return a / 2
def exp2(a): return a ** 2

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 

mapped_times2 = map(times2, my_list)


mapped_times2_list = list(mapped_times2)
print(mapped_times2_list)


div2 = map(div2, my_list)

div2 =list(div2)
print(div2)

exp2 = map(exp2, my_list)

exp2 =list(exp2)
print(exp2)

