# loops
# for (int i = 0; i< 5; i++)
for i in range(5):
    print("for loop", i)
print()


i = 0
while i < 5:
    print("while loop", i, end=", ")
    # i++ won't work
    i += 1
print()
print()
