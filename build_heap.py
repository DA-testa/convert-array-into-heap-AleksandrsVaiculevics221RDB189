# python3
from math import floor

def sift_down(data, n, i, swaps):    
    l = (i << 1 ) + 1
    r = (i << 1 ) + 2
    index = i
    if l < n and data[l] < data[index]:
        index = l
    if r < n and data[r] < data[index]:
        index = r
    if index != i:
        swaps.append((i, index))
        data[i], data[index] = data[index], data[i]
        sift_down(data, n, index, swaps)
    
def build_heap(data):
    swaps = []
    n = len(data)
    for i in range(n // 2 -1, -1, -1):
        sift_down(data, n, i, swaps)
    return swaps
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    # input from keyboard
    # checks if lenght of data is the same as the said lenght
    # calls function to assess the data 
    # and give back all swaps
    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))
    # input from keyboard
    # checks if lenght of data is the same as the said lenght
    # calls function to assess the data 
    # and give back all swaps
    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))
    # output all swaps
    
def main():
    try:
        text = input().strip()
        if "I" in text:
            n = int(input())
            data = list(map(int, input().split()))
        if "F" in text:
            filename = input()
            with open ("tests/" + filename, 'r') as f:
                n = int(f.readline())
                data = list(map(int,f.readline().split()))        
        assert len(data) == n
        swaps = build_heap(data)
        print(len(swaps))
        for swp in swaps:
            print(swp[0], swp[1])
   
    except ValueError:
        print("Error")

if __name__ == "__main__":
    main()
