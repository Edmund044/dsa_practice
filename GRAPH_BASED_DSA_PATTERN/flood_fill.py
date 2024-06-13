def flood_fill(image,sr,sc,color):
    def dfs(image,sr,sc,color,starting_pixel):
        if sr <0 or sc <0  or sr > len(image) -1 or sc > len(image(0)) or image[sr][sc] == color or image[sr][sc] != starting_pixel:
            return
 
        image[sr][sc] = color
        dfs(image,sr-1,sc,color,starting_pixel)
        dfs(image,sr+1,sc,color,starting_pixel)
        dfs(image,sr,sc-1,color,starting_pixel)
        dfs(image,sr,sc+1,color,starting_pixel)
    dfs(image,sr,sc,color,image[sr][sc])
    return image

#     dfs(image,sr,sc,color,image[sr][sc])
#     return image    

# def dfs(image,sr,sc,new_color,starting_pixel):
#     if sr < 0 or sc < 0 or sr > len(image)-1 or sc > len(image[0]) -1 or image[sr][sc] == new_color or image[sr][sc] != starting_pixel:
#         return

#     image[sr][sc] = new_color
#     dfs(image,sr-1,sc,new_color,starting_pixel)
#     dfs(image,sr+1,sc,new_color,starting_pixel)
#     dfs(image,sr,sc+1,new_color,starting_pixel)
#     dfs(image,sr,sc-1,new_color,starting_pixel)


print(flood_fill([[0,0,0],[0,0,0]],0,0,2))
print(flood_fill([[1,1,1],[1,1,0],[1,0,1]],1,1,2))
print(len([[0,0,0],[0,0,0]]))
