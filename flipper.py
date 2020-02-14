from pathlib import Path

#Test data was retrieved from https://www.cemc.uwaterloo.ca/contests/computing/2019/index.html?fbclid=IwAR0ZZiB69k31Mi8LRRVKT6hQ1GfeRHuupnC5AVyEsniaVV2ofy2sB7al1iY

def flipGrid(flips):
    numGrid = [[1,2],[3,4]]
    print(numGrid)
    for letter in flips:
        if letter == 'H':
            numGrid = flipHorizontal(numGrid)
        elif letter == 'V':
            numGrid = flipVertical(numGrid)

    print("Final grid:")
    print(numGrid)

def flipHorizontal(grid):
    numGrid =   [
                    [ grid[1][0], grid[1][1] ],
                    [ grid[0][0], grid[0][1]]
                ]
    #print('Flipping horizontal')

    return numGrid

def flipVertical(grid):
    numGrid =   [
                    [ grid[0][1], grid[0][0] ],
                    [ grid[1][1], grid[1][0]]
                ]
    #print('Flipping vertical')

    return numGrid

inputFile = open("all_data\\s1_j4\\j4.05.in")
line = inputFile.readline()
print("Initial grid:")
print(line)
flipGrid(line)
