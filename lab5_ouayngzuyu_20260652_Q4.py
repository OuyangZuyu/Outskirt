


from collections import Counter

def top_3_frequency_words(f):
    a=[]
    word = ""
    for char in f:
        if char == " ":
            if word:
                a.append(word)
                word = ""
        else:
            word += char
    if word:
        a.append(word)
    fre = Counter(a)
    return [k for k,v in fre.most_common(3)]

f = open("article.txt", "r")
content = f.read() 
print(top_3_frequency_words(content))