import random

# Read in all the words in one go
with open("applications/markov/input.txt") as f:
    words = f.read()
    words = words.split()
    stop_words = []
    start_words = []
    hash_table = {}
    prev = None
    stop_chars = ['.', '?', '!']
    for word in words:
        # capture start words
        word = word.rstrip().strip()
        if word[0] == word[0].upper():
            start_words.append(word)
        elif word[0] == '"' and word[1] == word[1].upper:
            start_words.append(word)
                        
        # capture end words
        if word[-1] in stop_chars:
            stop_words.append(word)
        elif word[-1] == '"':
            if word[-2] in stop_chars:
                stop_words.append(word)

        # chain current word as next of previous word
        if prev is not None and word not in stop_words:
            if prev not in hash_table:
                hash_table[prev] = []
            hash_table[prev].append(word)
        prev = word
    
    word = start_words[random.randint(0, len(start_words))]
    prev = None
    sentance = ''
    while prev not in stop_words:
        if prev is not None:
            sentance += ' '
        sentance += word
        prev = word
        word = hash_table[prev][random.randint(0, len(hash_table[prev])-1)]
    
    print(sentance)

# TODO: analyze which words can follow other words

# TODO: construct 5 random sentences
# I've held up one a little Lily in her sister only the boys getting through the old man, and speaking in it!
# To which the chimney-piece while I wonder if I wonder if they do try, there's a nice and really I wonder if they said.
# Queen cried out, quite a little, he thought Alice: "warmer, in the window with a real one, blazing away by an invisible hand, and then with great curiosity to make me see--suppose each punishment was beginning at that you half asleep, the Red Queen replied, "You haven't got to watch the glass in the table, and for the end of a scramble, in the White King couldn't hear the poor King went on, "I shall be if it got the thing didn't succeed, principally, Alice was this: first thing she was quite taken away from the Looking-glass House, if we come to look as if you couldn't.
# Alice was a way Dinah washed her hand shook so wide open!
# Red Queen said, because there was the King went on, talking more excuses, but hug the old man, and putting you know whether they've a little old man, and his eyes and his eyes open--if you'd shut them up in the glass--that's just now, you can be all knots and made her nor see that came wiggling down by the glass was far better manners!