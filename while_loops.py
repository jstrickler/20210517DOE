
i = 0
while i < 3:
    print(i)
    i += 1
print()

for i in range(3):
    print(i)
print()

while True:
    user_name = input("Enter your name (q to quit): ")
    if user_name == 'q':
        break  # exit loop
    if user_name.strip() == '':
        print("Please enter your name...")
        continue # go to top of loop

    print("Welcome, {}\n".format(user_name))

