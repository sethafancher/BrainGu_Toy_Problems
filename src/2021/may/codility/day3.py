def solution(A):
    nums = {}
    for num in A:
        nums[num] = 1
    for num in nums:
        if num + 1 in nums or num - 1 in nums:
            return True
    return False

def solution(N):
    num = N
    numStr = str(N)
    if num < 0:
        length = len(numStr) - 1
        while length > 0:
            if numStr[length] == '5':
                numStr = numStr[:length] + numStr[length+1:]
                return int(numStr)
            length-=1
    else:
        for i in range(len(numStr)):
            if numStr[i] == '5':
                numStr = numStr[:i] + numStr[i+1:]
                return int(numStr)