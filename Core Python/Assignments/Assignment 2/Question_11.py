print("Minimum Number of Notes")

amount = int(input("Enter amount: "))

note2000 = amount // 2000
amount = amount % 2000

note500 = amount // 500
amount = amount % 500

note200 = amount // 200
amount = amount % 200

note100 = amount // 100
amount = amount % 100

note50 = amount // 50
amount = amount % 50

note20 = amount // 20
amount = amount % 20

note10 = amount // 10
amount = amount % 10

coin5 = amount // 5
amount = amount % 5

coin2= amount // 2
amount = amount % 2

coin1 = amount // 1
amount = amount % 1

print(f"2000 Notes = {note2000}")
print(f"500 Notes  = {note500}")
print(f"200 Notes  = {note200}")
print(f"100 Notes  = {note100}")
print(f"50 Notes   = {note50}")
print(f"20 Notes   = {note20}")
print(f"5 Coins   = {coin5}")
print(f"2 Coins   = {coin2}")
print(f"1 Coins   = {coin1}")

