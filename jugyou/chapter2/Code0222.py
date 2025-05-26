scores = {70,80,55,80}
scores.add(80)
print(scores)
print(f"要素数は{len(scores)}")
print(f"合計は{sum(scores)}")


A = {1,2,3,4}
B = {2,3,4,5}
print(A | B)  # 和集合
print(A & B)  # 積集合
print(B - A)  # 差集合
print(A ^ B)  # 排他的論理和