file = open("apache_logs.txt")
print(file.read())
search_word = input("enter a word you want to search in file: ")
if(search_word in file.read()):
    print("word found")
else:
    print("word not found")
with open('apache_logs') as f:
    if 'presentation' in f.read():
        print("true")