# Determine the min moves needed to sort all 0s or 1s to an end of the array
# All moves/swaps must swap adjacent values in the array
# Return the Min Moves required to sort


def countAbove(arr, x):
    count = 0
    xNot = 0
    for i in arr:
        if i == x:
            count += xNot
        else:
            xNot += 1
    return count

def minMoves(arr):
    zerosLeft = countAbove(arr, 0)
    onesLeft = countAbove(arr, 1)

    print(f"Zeros moves needed: {zerosLeft}")
    print(f"Ones moves needed: {onesLeft}")

    return zerosLeft if zerosLeft <= onesLeft else onesLeft

arr = [0,1,1,1,1,0,0,0,0,0]

print(f"Min moves needed: {minMoves(arr)}")