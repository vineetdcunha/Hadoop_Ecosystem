#Name: Vineet Dcunha
#"I have not given or received any unauthorized assistance on this assignment."

myfile = open('myfile.txt','r') # considering text file is placed in the same location as python
d = dict()

count_job = myfile.readlines()

for word in count_job: 
    word = word.strip()
    word = word.lower()
    words = word.split(" ") 
    for word_cnt in words:
        if word_cnt in d:
            d[word_cnt] = d[word_cnt] + 1
        else:
            d[word_cnt] = 1

print('\n'.join("{} {}".format(k, v) for k, v in d.items()))