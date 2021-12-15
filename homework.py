from algorithm import findShortestPath

if __name__=='__main__':

    #Read Input
    with open("C:/Users/suviy/OneDrive/Documents/VSCode/inputBFS.txt", "r") as input_file:
        input = input_file.read().splitlines() 

    algorithm = input[0]
    stateSpace = tuple([int(i) for i in input[1].split()])
    startLocation = tuple([int(i) for i in input[2].split()])
    goalLocation = tuple([int(i) for i in input[3].split()])
    actionGrids = input[4]
    cave = {}
    for grid in input[5:]:
        gridPoint = grid.split()
        coordinates = tuple(int(i) for i in gridPoint[:3])
        actions = [int(i) for i in gridPoint[3:]]
        cave[coordinates] = actions
    

    #Finds the shortest path
    answerSet = findShortestPath(algorithm, stateSpace, startLocation, goalLocation, actionGrids, cave)
    # print("answer = ",answerSet)

    #Write the answer in an output file
    with open("C:/Users/suviy/OneDrive/Documents/VSCode/output.txt", "w") as fp:
        if answerSet=="FAIL":
            fp.writelines(answerSet)
        else:
            fp.writelines(str(answerSet[0]))
            fp.writelines("\n"+str(answerSet[1]))

            for step in answerSet[2]:
                fp.writelines(f"\n{step[0][0]} {step[0][1]} {step[0][2]} {step[1]}")