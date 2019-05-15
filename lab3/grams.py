import sys

def grams(n, string):
    lst=[]
    s = string.split()   
    for i in range(len(s)-n+1):
        lst.append(s[i:i+n])
    
    return lst
	
def main():
    
    string = "cat sat on the mat"
    
    for i in range(1,5):
        print(grams(i, string))
    

if __name__ == "__main__": 
    main()
