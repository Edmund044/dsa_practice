def grid_paths(rows,columns):
    cache = {}
    for row in rows:
        cache[(row,1)] = 1
    for column in columns:
        cache[(1,column)] = 1

    for row in range(2,rows+ 1):
        for column in  range(2,columns+1):
            cache[(row,column)] = cache[(row-1,column)] + cache[(row,column-1)]

    return cache[(rows,columns)]        



    # cache = {}

    # for row in range(1,rows+1):
    #     cache[(row,1)] = 1
    # for column in range(1,columns + 1):
    #     cache[(1,column)] = 1

    # for row in range(2,rows+1):
    #     for column in range(2,columns+1):
    #         cache[(row,column)] = cache[(row - 1,column)] + cache[(row,column - 1)]
    
    # return cache[(rows,columns)]                 


    # cache = {}
    # for row in range(1, rows + 1):
    #     cache[(row,1)] = 1
    # for column in range(1, columns + 1):
    #     cache[(1,column)] = 1

    # for row in range(2,rows + 1):
    #     for column in range(2,columns + 1):
    #         cache[(row,column)] = cache[(row - 1,column)] + cache[(row,column - 1)]

    # return cache[(row,column)]        


        

print(grid_paths(18,6))
print(grid_paths(3,3))        