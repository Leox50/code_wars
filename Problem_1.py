#Get the Middle Character

def get_middle(s):
    if len(s) % 2 == 0:
        x = int(len(s)/2)
        return s[x-1]+s[x]
    else:
        x = int((len(s)+1)/2)
        return s[x-1]