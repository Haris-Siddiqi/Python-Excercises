# Excercise 6
# Ways to put variables in strings

# 1. f and {}
guests = 10
host = f"There are {guests} guests invited."
print(host)

# 2. format
tasty = False
dinner_review = "The dinner was alright. {}"
print(dinner_review.format(tasty))

# 3. Manually combining in print statement
change = 75
waiter = "cents is your change sir."
print(change, waiter)
