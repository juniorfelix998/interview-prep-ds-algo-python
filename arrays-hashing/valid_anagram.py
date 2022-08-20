def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t): 
        return False
    
    countS, countT = {},{}
    for i in range(len(s)): 
        countS[s[i]] = 1 + countS.get(s[i],0)
        countT[t[i]] = 1 + countT.get(t[i],0)
    for c in countS:
        if countS[c] != countT.get(c,0):
            return False
    return True

def check(s1, s2):
     
    # the sorted strings are checked
    if(sorted(s1)== sorted(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.") 

print(is_anagram('cat','rat'))