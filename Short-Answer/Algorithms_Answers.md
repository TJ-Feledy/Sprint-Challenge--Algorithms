#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)  O(n)
- 'a' is multiplied by 'n * n' which cancels out with the 'n * n * n' to give the runtime of O(n).


b)  O(n*log(n)))
- the 'for' loop has a run time of O(n), and the nested 'while' loop has a runtime of O(log(n)) which when multiplied == O(n*log(n)))


c)  O(n) or O(bunnies)
- I believe the time complexity on this one is O(n) because the recursive function call steps 'n' down by 1 each call.  So it will only run 'n' times.

## Exercise II


findFloor function takes the arguments of 'n' which is num of floors of building and 'f' which is the target floor:
    currentFloor = 0
    previousFloor = 0
    floors = [return floor # for each floor in range of n]
    midpoint = length of floors//2
    left = floors[previousFloor:midpoint]
    right = floors[midpoint:]

    if the currentFloor == f:
        return f
    
    while currentFloor is less than left[length of left -1]:
        if currentFloor is greater than f:
            floors = floors[previousFloor:currentFloor]
            return floors

        previousFloor = currentFloor
        currentFloor = currentFloor * 2

        return currentFloor
         
    while currentFloor is less than right[length of right -1]:
        if currentFloor is greater than f:
            floors = floors[previousFloor:currentFloor]
            return floors

        previousFloor = currentFloor
        currentFloor = currentFloor * 2

        return currentFloor
    
    return f

    ***RUNTIME COMPLEXITY = O(log(n))*** -- i think lol