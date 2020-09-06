# Write in a function that takes in a n x m 2 dimensiona array (that can be square shaped when n==m) and returns a one dimensional array of all the elements in zig zag order
# zig zag order starts at the top left corner of the 2 dimensional array, goes down by 1 element, and proceeds in a zig zag order all the way to the bottom right corner

# Example array looks like this:
# array = [[1, 3, 4, 10]
#          [2, 5, 9, 11]
#          [6, 8, 12,15]
#          [7, 13,14,16]]

# Output would be = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

def zigzagTraverse(array):
    height = len(array)-1
    width = len(array[0])-1
    result = []
    row = 0
    col = 0
    goingdown = True

