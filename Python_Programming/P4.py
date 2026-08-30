    #  READ WRITE FILES

word_stats = {}
with open("poem.txt", "r") as f:
    for line in f:
        words = line.split(' ')
        for word in words:
            word_stats[word]+=1
        else:
            word_stats[word] = 1
