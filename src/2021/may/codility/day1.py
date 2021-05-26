def solution(S):

    # FASTER VERSION USING FSM
    bchecker = False
    for char in S:
        if char == "b":
           bchecker = True 
        elif char == "a" and bchecker == True:
           return False 
    return True

    # SLOWER VERSION O(n^2)
    # for i in range(0, len(S)):
    #     if S[i] == "b":
    #         for j in range(i + 1, len(S)):
    #             if S[j] == "a":
    #                 return False
    # return True