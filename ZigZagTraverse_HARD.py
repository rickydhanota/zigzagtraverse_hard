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

    while not isOutOfBounds(row, col, height, width):
        result.append(array[row][col])
        if goingdown:
            if col == 0 or row == height:
                goingdown = False
                if row == height: 
                    col += 1
                else:
                    row += 1
            else:
                row += 1
                col -= 1
        else:
            if row == 0 or col == width:
                goingdown = True
                if col == width:
                    row += 1
                else:
                    col +=1
            else:
                row -= 1
                col += 1
    return result

def isOutOfBounds(row, col, height, width):
    return row < 0 or row > height or col < 0 or col > width

print(zigzagTraverse(
    [[1, 3, 4, 10],
    [2, 5, 9, 11],
    [6, 8, 12,15],
    [7, 13,14,16]]
))



