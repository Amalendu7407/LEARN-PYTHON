file = open("fruit.txt" , "w")

fruit = [
    "apple\n",
    "banana\n",
    "guava\n",
    "mango\n"
]
file.writelines(fruit)
file.close()