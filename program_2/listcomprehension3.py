word=input("enter a word:")
vowels=['a','e','i','o','u','A','E','I','O','U']
vowel_list=[]
for ch in word:
    if ch in vowels:
        vowel_list.append(ch)
print("vowels:",vowel_list)