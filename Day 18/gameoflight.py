
def test():
    with open("test") as f:
        grid = []
        for line in f.readlines():
            grid.append(list(line)[:-1])

    for _ in range(4):
        newGrid = [[0]*6 for i in range(6)]
        #corners
        ca = [grid[0][1], grid[1][0], grid[1][1]]
        cb = [grid[0][4], grid[1][5], grid[1][4]]
        cc = [grid[4][0], grid[5][1], grid[4][1]]
        cd = [grid[4][5], grid[5][4], grid[4][4]]
        newGrid[0][0] = "#" if (ca.count("#") == 3 or (grid[0][0] == "#" and ca.count("#") == 2)) else "."
        newGrid[0][5] = "#" if (cb.count("#") == 3 or (grid[0][5] == "#" and cb.count("#") == 2)) else "."
        newGrid[5][0] = "#" if (cc.count("#") == 3 or (grid[5][0] == "#" and cc.count("#") == 2)) else "."
        newGrid[5][5] = "#" if (cd.count("#") == 3 or (grid[5][5] == "#" and cd.count("#") == 2)) else "."
        
        #end rows
        for i in range(1, 5):
            r1 = [grid[0][i-1], grid[0][i+1], grid[1][i-1], grid[1][i], grid[1][i+1]]
            r99 = [grid[5][i-1], grid[5][i+1], grid[4][i-1], grid[4][i], grid[4][i+1]]
            newGrid[0][i] = "#" if r1.count("#") == 3 or (grid[0][i] == "#" and r1.count("#") == 2) else "."
            newGrid[5][i] = "#" if r99.count("#") == 3 or (grid[5][i] == "#" and r99.count("#") == 2) else "."
        
        #end columns
        for j in range(1,5):
            col1 = [grid[j-1][0], grid[j+1][0], grid[j-1][1], grid[j][1], grid[j+1][1]]
            col99 = [grid[j-1][5], grid[j+1][5], grid[j-1][4], grid[j][4], grid[j+1][4]]
            newGrid[j][0] = "#" if col1.count("#") == 3 or (grid[j][0] == "#" and col1.count("#") == 2) else "."
            newGrid[j][5] = "#" if col99.count("#") == 3 or (grid[j][5] == "#" and col99.count("#") == 2) else "."
        
            #interior
            for i in range(1, 5):
                n = [grid[j-1][i-1], grid[j-1][i], grid[j-1][i+1], grid[j][i-1], grid[j][i+1], grid[j+1][i-1], grid[j+1][i], grid[j+1][i+1]]
                newGrid[j][i] = "#" if (n.count("#") == 3 or (grid[j][i] == "#" and n.count("#") == 2)) else "."        
        grid = newGrid

    for line in grid:
        print("".join(line))

def main():
    with open("input") as f:
        grid = []
        for line in f.readlines():
            grid.append(list(line)[:-1])
    
    #part 2 only
    grid[0][0], grid[0][99], grid[99][0], grid[99][99] = "#", "#", "#", "#"

    for _ in range(100):
        newGrid = [[0]*100 for i in range(100)]
        
        #Part 1 only
        """
        #corners
        ca = [grid[0][1], grid[1][0], grid[1][1]]
        cb = [grid[0][98], grid[1][99], grid[1][98]]
        cc = [grid[98][0], grid[99][1], grid[98][1]]
        cd = [grid[98][99], grid[99][98], grid[98][98]]
        newGrid[0][0] = "#" if (ca.count("#") == 3 or (grid[0][0] == "#" and ca.count("#") == 2)) else "."
        newGrid[0][99] = "#" if (cb.count("#") == 3 or (grid[0][99] == "#" and cb.count("#") == 2)) else "."
        newGrid[99][0] = "#" if (cc.count("#") == 3 or (grid[99][0] == "#" and cc.count("#") == 2)) else "."
        newGrid[99][99] = "#" if (cd.count("#") == 3 or (grid[99][99] == "#" and cd.count("#") == 2)) else "."
        """
        #Part 2 only
        newGrid[0][0], newGrid[0][99], newGrid[99][0], newGrid[99][99] = "#", "#", "#", "#"

        #end rows
        for i in range(1, 99):
            r1 = [grid[0][i-1], grid[0][i+1], grid[1][i-1], grid[1][i], grid[1][i+1]]
            r99 = [grid[99][i-1], grid[99][i+1], grid[98][i-1], grid[98][i], grid[98][i+1]]
            newGrid[0][i] = "#" if r1.count("#") == 3 or (grid[0][i] == "#" and r1.count("#") == 2) else "."
            newGrid[99][i] = "#" if r99.count("#") == 3 or (grid[99][i] == "#" and r99.count("#") == 2) else "."
        
        #end columns
        for j in range(1,99):
            col1 = [grid[j-1][0], grid[j+1][0], grid[j-1][1], grid[j][1], grid[j+1][1]]
            col99 = [grid[j-1][99], grid[j+1][99], grid[j-1][98], grid[j][98], grid[j+1][98]]
            newGrid[j][0] = "#" if col1.count("#") == 3 or (grid[j][0] == "#" and col1.count("#") == 2) else "."
            newGrid[j][99] = "#" if col99.count("#") == 3 or (grid[j][99] == "#" and col99.count("#") == 2) else "."
        
            #interior
            for i in range(1, 99):
                n = [grid[j-1][i-1], grid[j-1][i], grid[j-1][i+1], grid[j][i-1], grid[j][i+1], grid[j+1][i-1], grid[j+1][i], grid[j+1][i+1]]
                newGrid[j][i] = "#" if (n.count("#") == 3 or (grid[j][i] == "#" and n.count("#") == 2)) else "."
        grid = newGrid

    for line in grid:
        print("".join(line))
    print(sum(line.count("#") for line in grid))

main()