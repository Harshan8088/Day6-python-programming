text=input("enter a sentance:").lower()
words=text.split()
frequency={}
for word in words:
    if word in frequency:
        frequency[word]+=1
    else:
        frequency[word]=1
    
print(frequency)