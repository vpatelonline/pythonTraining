from collections import Counter
my_list=[1,1,1,1,2,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,6]
print(Counter(my_list))
print(Counter(my_list))

my_word_list=['how','are','you','what','are','you','doing','here']
print(Counter(my_word_list))

my_mix_list=[1,2,3,1,3,'a','b','a']
print(Counter(my_mix_list))

print(Counter('avdsvdsvdasfadsfdafd'))

my_sentence='How are you? where are you going today?'
print(my_sentence.split())
print(my_sentence.lower().split())
print(Counter(my_sentence))
print(Counter(my_sentence).most_common(2))
print(list(my_sentence))
print(list(Counter(my_sentence)))


from collections import defaultdict
d={'a':10}
print(d)
print(d['a'])
#print(d['b'])

d=defaultdict(lambda:0)
print(d['b'])