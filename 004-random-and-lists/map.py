line1 = ["⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "⬜️", "️⬜️"]
line3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input()  # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
p1 = position[0]
p2 = position[1]

if p1 == 'A':
  p1 = 0
elif p1 == 'B':
  p1 = 1
elif p1 == 'C':
  p1 = 2

p2 = int(p2) - 1

map[p2][p1] = 'X'

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")
