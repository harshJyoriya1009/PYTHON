# if (n:=len([1,2,3,4,5])) >3:
#     print("The")

# Example: Finding the length of words that are longer than 3 characters
words = ["apple", "banana", "cherry", "fig", "kiwi"]
long_words = [word for word in words if (n := len(word)) > 3]

print(long_words)
