def sortedSquares(nums):
    squares = []
    for num in nums:
        sq = num*num
        squares.append(sq)
    squares.sort()
    print(squares)
    
sortedSquares([-7,-3,2,3,11])