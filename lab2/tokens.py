import sys

num1= sys.argv[1]
num2= sys.argv[2]

subs = ",.;:'-!?"

def tokenise(file1, file2):
    new_word_en= ""
    new_word_fr = ""

    with open(file1,'r') as f1, \
         open(file2,'r') as f2:
	    for x,y in zip(f1,f2):
		    if len(x.split()) > int(num1) and len(x.split()) < int(num2):
			    for letter in x:
				    if letter in  subs:
					    new_word_en += " " + letter + " "
				    else:
					    new_word_en += letter
			    for letter in y:
				    if letter in  subs:
					    new_word_fr += " " + letter + " "
				    else:
					    new_word_fr += letter

    return new_word_en, new_word_fr


def main():
    new_word_en, new_word_fr = tokenise("train-data.en", "train-data.fr")
    
    f = open("tokenised.txt", "w")
    f.write(new_word_en)
    f.write(new_word_fr)
    
    

if __name__ == "__main__": 
    main()
