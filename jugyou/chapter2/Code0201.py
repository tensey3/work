netwoek = 88
database = 95
security = 90
total = netwoek + database + security
avg = total / 3
print(f"合計点:{total}")
print(f"平均点:{avg}")

a = [netwoek, database, security]
print(f"合計点:{sum(a)}")
print(f"平均点:{sum(a)/len(a)}")