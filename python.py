# score = input("Enter Score: ")
# score = float(score)
# if (score >= 0.9 and score <= 1.0):
#     print("A")
# elif (score >= 0.8 and score <= 1.0):
#     print("B")
# elif (score >= 0.7 and score <= 1.0):
#     print("C")
# elif (score >= 0.6 and score <= 1.0):
#     print("D")
# elif (score < 0.6 and score > 0):
#     print("B")
# else:
#     raise ValueError()
    

# text = "X-DSPAM-Confidence:    0.8475"
# start = text.find('0')
# end = len(text)
# number = text[start:end]
# number = float(number)
# print(number)


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __eq__(self, other):
#         if isinstance(other, Point):
#             return self.x == other.x and self.y == other.y
#         return False

#     def __str__(self):
#         return f'({self.x}, {self.y})'

#     def __copy__(self):
#         return type(self)(self.x, self.y)

#     def __deepcopy__(self, memo):
#         return type(self)(copy.deepcopy(self.x, memo), copy.deepcopy(self.y, memo))



# p1 = Point(import copy
# p2 = copy.copy(p1)   # Shallow copy
# p3 = copy.deepcopy(p1)   # Deep copy

# print(p1)  # Output: (1, 2)
# print(p2)  # Output: (1, 2)
# print(p3)  # Output: (1, 2)

# print(p1 == p2)  # Output: True
# print(p1 == p3)  # Output: True
# print(p1 is p2)  # Output: False (different objects)
# print(p1 is p3)  # Output: False (different objects)

# fruit = 'Banana'
# fruit[0] = 'b'
# print(fruit)fname = input("Enter file name: ")
# fh = open(fname)

# senders = {}

# for line in fh:
#     if line.startswith('From '):
#         words = line.split()
#         sender = words[1]
#         senders[sender] = senders.get(sender, 0) + 1

# max_sender = None
# max_count = -1

# for sender, count in senders.items():
#     if max_count == -1 or count > max_count:
#         max_sender = sender
#         max_count = count

# print(max_sender, max_count)




# it will print ['From: Using the :'] because this 
# is the only part of the string that 
# matches the pattern.

# import re
# x = 'From: Using the : character'
# y = re.findall('^F.+:', x)
# print(y)\


# In this code, the pattern '^F.+?:' will match any string that starts with 'F' 
# and ends with ':' but will stop at the first ':'
#  it encounters, because of the '?' character. This will result in
# ['From:'] being printed.

# import re
# x = 'From: Using the : character'
# y = re.findall('^F.+?:', x)
# print(y)