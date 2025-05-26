name = input("名前を入力してください>>")
print(f"{name}さん、こんにちは")
food = input(f"{name}さんの好きな食べ物を教えてください>>")
if food == "カレー":
    print("素敵です。カレーは最高ですねよね")
else:
    print(f"{food}も美味しいですよね")