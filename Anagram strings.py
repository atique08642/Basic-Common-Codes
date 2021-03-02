def anagram(str1, str2):
    if len(str1) != len(str2):
        return("Not Anagram")
    else:
        string1 = sorted(str1)
        string2 = sorted(str2)
        if string1 == string2:
            return("Anagram")
        else:
            return("Not an anagram")
string1 = input()
string2 = input()
print(anagram(string1,string2))

