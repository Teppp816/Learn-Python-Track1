# More Than N

# Create a function named more_than_n() that has three parameters named my_list, item, and n.

# The function should return True if item appears in the list more than n times. The function should return False otherwise.

# Write your function here
def more_than_n(my_list, item, n):
  if my_list.count(item) > n:
    return True
  else:
    return False


# Uncomment the line below when your function is done
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 4, 3))