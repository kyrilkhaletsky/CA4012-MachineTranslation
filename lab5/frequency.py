import sys

def freq(word, string):
    num = 0    
    for i in string.split():
        if i == word:
            num +=1

    num = num / len(string.split())    
    
    return num

def grams(n, string):
    lst=[]
    s = string.split()   
    for i in range(len(s)-n+1):
        lst.append(s[i:i+n])
    
    return lst

def prob(inputs, dictionary):
    total = 0
    i = 0
    for s in inputs.split():
        for name, age in dictionary.items():
            if name == s:
                if i == 0:
                    total += age
                    i +=1
                else:
                    total *=age
      
    return total
	
def main():
    
    corpus = "the cat sat on the mat with a cat"

    inputs = "<s> a cat sat on the mat </s>"

    dictionary = {}
    
    for word in corpus.split():
        num = freq(word, corpus)
        dictionary[word] = num

    
    result = prob(inputs, dictionary)

    print(result)


    with open("corpus.txt",'r') as f1:
        for z in f1.readlines():
            if z != "\n" or z != []:
                print(grams(2, z))
                print(grams(2, inputs))

    

if __name__ == "__main__": 
    main()
