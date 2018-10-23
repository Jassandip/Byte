
# convert title into words
# subsequently, all words NOT in exceptions need to be in Correct Title Form

def titlecase(title, exceptions):
    a = title.split()
    b = [] 
    for i in a:
        if i in exceptions:
            b.append(i)
        else:
            b.append(i.title())
    
    print(" ".join(b))    

if __name__ == "__main__":
    print (titlecase ("the quick brown fox jumps over the lazy dog", ["quick", "brown"]))
