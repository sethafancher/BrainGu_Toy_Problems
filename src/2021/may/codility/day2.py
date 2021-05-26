def solution(N, K):
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    palindrome = ""
    if N % 2 == 0:
       i = 0
       j = 0
       while i < N/2 and j < K:
           palindrome += letters[j]
           i+=1
           j+=1
       while i < N/2:
           palindrome += letters[0]
           i+=1
       length = N//2
       for k in range(N//2):
            palindrome += palindrome[length - 1]
            length -= 1 
       return palindrome
    else:
       i = 0
       j = 0
       while i < N//2 and j < K:
           palindrome += letters[j]
           i+=1
           j+=1
       while i < N//2:
           palindrome += letters[0]
           i+=1
       if j < K:
           palindrome += letters[j]
       else:
           palindrome += letters[0]
       length = N//2
       for k in range(N//2):
            palindrome += palindrome[length - 1]
            length -= 1 
       return palindrome