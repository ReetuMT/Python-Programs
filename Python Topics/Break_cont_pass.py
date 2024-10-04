# break , continue , pass Statemnet

# Break statement is used to exit the loop
for i in range(10):
    if i == 5:
        break
    print(i)
print("Break statement ends here")
# Continue Statment is skips the iteration of the loop and moves to the next iteration.

for i in range(5):
    if i==2:
        continue
    print(i)

print("Continue statement ends here")
# Pass statement is does nothing
for i in range(3):
    if i==1:
        pass
    print(i)