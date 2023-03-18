# python3
from math import floor

def build_heap(n, data):
    swapc = 0
    swaps = []
    size = n-1
    for i in range (floor(n/2), -1, -1):
        index = i
        l = LeftChild(i+1)
        if l <= size and data[l] <data[index]:
            index = l
        r = RightChild(i+1)
        if  r <= size and data[r] <data[index]:
            index = r
        if i != index:
            data[i], data[index] = data[index], data[i]
            swapc +=1
            swap.append((i, index))
            swapc, swap = sift_down(index, size, data, swapc, swap)
    return swapc, swap
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
def sift_down(i, size, data, swap_count, swap_list):    
    index = i
    l = LeftChild(i+1)
    if l <= size and data[l] <data[index]:
        index = l
    r = RightChild(i+1)
    if  r <= size and data[r] <data[index]:
        index = r
    if i != index:
        data[i], data[index] = data[index], data[i]
        swapc +=1
        swap.append((i, index))
        swapc, swap = sift_down(index, size, data, swapc, swap)
    return swapc, swap  

def LeftChild(i):
    return 2 * i - 1
 
def RightChild(i):
    return 2 * i


def main():
    try:
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file


    # input from keyboard
        n = int(input())
        data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght
        assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
        swapc, swap = build_heap(n, data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
        print(swapc)
        for swp in swaps:
            print(swp[0], swp[0])
    #
    except ValueError:
        print("Error")

if __name__ == "__main__":
    main()
