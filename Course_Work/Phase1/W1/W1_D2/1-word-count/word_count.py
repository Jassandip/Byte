from operator import itemgetter
from collections import Counter



def word_counts(filename, n):
    w = {}
    wc =[]
    with open(filename, 'r') as input_file:
        for line in input_file:
            for word in line.split():
                if word in w:
                    w[word] += 1
                else:
                    w[word] = 1
    h =[]
    h2 = 0
    for j in range(0,n): 
        for i in w:
            if w[i] >= h2:
                h = i
                h2 = w[i]
            else:
                pass
        s = str(w[h])
        print (h+" : "+s)
        h2 = 0
        del w[h]
    
        
              
  
if __name__ == "__main__":
    wcounts = word_counts('article.txt', 11)
    # now how do you display your data?
