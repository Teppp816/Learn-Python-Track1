# Create a function called middle_element that has one parameter named lst.

# If there are an odd number of elements in lst, the function should return the middle element. If there are an even number of elements, the function should return the average of the middle two elements.

#Write your function here
def middle_element(lst):
  # even
  if len(lst) % 2 == 0:
    sum = lst[int(len(lst) / 2)] + lst[int(len(lst) / 2 - 1)]
    return sum / 2
  else:
    middle = lst[int(len(lst) / 2)]
    return middle


#Uncomment the line below when your function is done
print(middle_element([2, -10, -4, 4, 5]))