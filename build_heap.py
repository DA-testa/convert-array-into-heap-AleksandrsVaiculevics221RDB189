# python3
from math import floor

def build_heap(n, data):
    swap_count = 0
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
            swap_count +=1
            swaps.append((i, index))
            swap_count, swaps = sift_down(index, size, data, swap_count, swaps)
    return swap_count, swaps
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
def sift_down(i, size, data, swap_count, swaps):    
    index = i
    l = LeftChild(i+1)
    if l <= size and data[l] <data[index]:
        index = l
    r = RightChild(i+1)
    if  r <= size and data[r] <data[index]:
        index = r
    if i != index:
        data[i], data[index] = data[index], data[i]
        swap_count +=1
        swaps.append((i, index))
        swap_count, swaps = sift_down(index, size, data, swap_count, swaps)
    return swapc, swap  

def LeftChild(i):
    return 2 * i - 1
 
def RightChild(i):
    return 2 * i


def main():
    n=0
    try:
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
        text = input()
        if "I" in text:
            n = int(input())
            data = list(map(int, input().split()))
        if "F" in text:
            filename = input()
            with open ("test/" + filename, 'r') as f:
                n = int(f.readline())
                data = list(map(int,f.readline().split()))        
            assert len(data) == n
        if n == 0:
            raise ValueError("Invalid input: no value for n")    
        swap_count, swaps = build_heap(n, data)
        print(swap_count)
        for swp in swaps:
            print(swp[0], swp[0])
    # input from keyboard
        

    # checks if lenght of data is the same as the said lenght

    # calls function to assess the data 
    # and give back all swaps

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    except ValueError:
        print("Error")

if __name__ == "__main__":
    main()
