
def create_histogram(file):
    hashtable = {}
    ignored = ["\"", ":", ";", ",", ".", "-", "+", "=" "/", "\\", "|", "[", "]", "{", "}", "(", ")", "*", "^", "&"]

    f = open(file, 'r')

    for line in f:
        for word in line.rstrip().split(' '):
            word = word.lower()
            if len(word) == 0 or word[-1] in ignored:
                continue
            if not word in hashtable:
                hashtable[word] = 0
            hashtable[word] += 1
    f.close()

    for key in sorted(hashtable.keys(), key=lambda x: hashtable[x], reverse=True):
        print(key, ' ' * (16 - len(key)), '#' * hashtable[key])

create_histogram('applications/histo/robin.txt')
