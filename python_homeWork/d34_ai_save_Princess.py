def displayPathtoPrincess(n,grid):
#print all the moves here
    hori = ''
    vert = ''
    for i in range(len(grid)):
        if 'p' in grid[i]:
            break
    j = grid[i].index('p')
    user = int((n-1) / 2)
    if i > user:
        vert = 'DOWN'
    else:
        vert = 'UP'
        
    if j > user:
        hori = 'RIGHT'
    else:
        hori = 'LEFT'
        
    for i in range(user):
        print(hori)
        print(vert)

grid=[['-','-','-'],
      ['-','m','-'],
      ['p','-','-']]
# print(grid)
displayPathtoPrincess(3,grid)
