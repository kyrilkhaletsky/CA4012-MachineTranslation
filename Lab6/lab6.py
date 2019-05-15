def probability(source, target, n):
	alignments= alignment(source, target)
	new_alig = alignments
	for i in range(0,n):
		count_dict = getCounts(new_alig)
		prob_dict = getTransProb(count_dict)
		new_alig = new_align(alignments, prob_dict)
	print(prob_dict)

def new_align(alignments, prob_dict):
	new_align = {}
	for keys, value in alignments.items():
		word1, word2 = keys[0], keys[1]
		if keys not in new_align:
			new_align[keys] = prob_dict[word1, word2]
	return new_align

def getTransProb(count_dict):
	total_dict = {}
	prob_dict = {}
	for keys, value in count_dict.items():
		word1, word2 = keys[0], keys[1]
		if word2 not in total_dict:
			total_dict[word2] = value
		else:
			total_dict[word2] += value
	
	for keys, value in count_dict.items():
		word1, word2 = keys[0], keys[1]
		if (word1, word2) not in prob_dict:
			prob_dict[(word1, word2)] = value / total_dict[word2]		
	return prob_dict
	
def getCounts(alignments):
	div_dict = {}
	count_dict = {}
	for keys, value in alignments.items():
		word1, word2, sentence = keys[0], keys[1], keys[2]
		if (word1, sentence) not in div_dict:
			div_dict[(word1, sentence)] = value
		else:
			div_dict[(word1, sentence)] += value

	for keys, value in alignments.items():
		word1, word2, sentence = keys[0], keys[1], keys[2]
		if (word1, word2) not in count_dict:
			count_dict[(word1, word2)] = value / div_dict[(word1, sentence)]
		else:
			count_dict[(word1, word2)] += value / div_dict[(word1, sentence)]

	return count_dict			

def alignment(source, target):
	new_dict = {}
	length = float(getUniqueWords(source))
	sentence = 0
	for sline, tline in zip(source,target):
		sline = sline.strip().split()
		tline = tline.strip().split()
		for i in range(0, len(sline)):
			for j in range(0, len(tline)):
				if (tline[j], sline[i], sentence) not in new_dict:
					new_dict[( tline[j], sline[i], sentence)] = 1/length
		sentence += 1			
	return new_dict

def getUniqueWords(source):
	lists = []
	for line in source:
		for word in line.strip().split():
			if word not in lists:
				lists.append(word)
	return len(lists)

def main():
	f1 = open("source.txt")
	f2 = open("target.txt")
	source , target = f1.readlines(), f2.readlines()
	probability(source,target, 2)

if __name__ == '__main__':
	main()

