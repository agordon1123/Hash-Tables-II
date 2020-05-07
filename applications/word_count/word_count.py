def word_count(s):
    # Implement me.
    hashtable = {}
    ignored = ["\"", ":", ";", ",", ".", "-", "+", "=", "/", "\\", "|", "[", "]", "{", "}", "(", ")", "*", "^", "&"]

    for word in s.rstrip().split():
        word = word.lower().strip()
        if len(word) == 0:
            continue
        if word[-1] in ignored:
            while len(word) > 0 and word[-1] in ignored:
                word = word.replace(word[-1], "")
        if len(word) > 0:
            if not word in hashtable:
                hashtable[word] = 0
            hashtable[word] += 1
    
    return hashtable


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))