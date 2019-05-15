import sys
import math


def grams(n, string):
    lst=[]
    s = string.split()   
    for i in range(len(s)-n+1):
        lst.append(s[i:i+n])
    
    return lst
    

def calculate_match(output_gram, reference_gram):
    matched_number = 0
    for j in output_gram:
        matched = [i for i, x in enumerate(reference_gram) if x == j]

        if matched != []: 
            matched_number+=1
            del reference_gram[matched[0]]
    return matched_number
	
	
def main():
    
    output = "The gunman was shot dead by police ."
    reference_1 = "The gunman was shot dead by the police ."
    reference_2 = "The gunman was shot dead by the police ."
    reference_3 = "Police killed the gunman ."
    reference_4 = "The gunman was shot dead by the police ."
    
    reference = [reference_1,reference_2,reference_3,reference_4]
    
    p = [0,0,0,0]
    
    for i in range(1,5):
        output_gram = grams(i, output)

        correct_list = []
        for ref in reference:
            reference_gram = grams(i, ref)
            correct_list.append(calculate_match(output_gram,reference_gram))
        p[i-1] = max(correct_list)/float(len(output_gram))


    p = p[0] * p[1] * p[2] * p[3]

    ref_len_list = [len(r.split()) for r in reference]
    ref_len = min(ref_len_list, key=lambda x:abs(x-len(output.split())))


    BP = min(1,len(output.split())/float(ref_len))
    print (BP)

    print (math.pow(p, 1.0 / 4) * BP)
    

if __name__ == "__main__": 
    main()
