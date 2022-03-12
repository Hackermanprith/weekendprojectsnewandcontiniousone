from xml.etree.ElementPath import prepare_child


def solve(s):
    for i in range(len(s)):
        if i == 1:
            s = s.capitalize()
        elif s[i] == " ":
            s = s.capitalize()
                
            
    return s

b=solve("hello world")
print(b)