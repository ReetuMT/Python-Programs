# For Loop Repeats the code block a specific number of times 

for i in range(5):
    print(i) # 0 1 2 3 4


# Example 2 shows For Loop with a List of Dictionaries
fruit = [
    {
        "id": 1,
        "name": "Apple"
    },
    {
        "id": 2,
        "name": "Banana"
    }
]

for i in fruit:
    print(i)           # Print the entire dictionary
    print(i["id"])     
    print(i["name"])   # Print the name of the fruit
