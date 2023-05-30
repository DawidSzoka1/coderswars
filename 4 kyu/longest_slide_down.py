def longest_slide_down(pyramid):
    count = 0
    for i in range(len(pyramid)):
        count += pyramid[i][i - 1]
    return count


#not finished