with open("Book1.text","r") as f1 
with open("Book2.text","r") as f2 
with open("Book3.text","r") as f3 
l1 = f1.readline() 
l2 = f2.readline() 
l3 = f3.readline() 
word1 = line1.spilt() 
word2 = line2.spilt() 
word3 = line3.spilt() 
unique_list1 = [] 
unique_list2 = [] 
unique_list3 = []

for i in word1:
  if i not in unique_list1:
    unique_list1.append(i)
  return unique_list1

for x in word2:
  if x not in unique_list2:
    unique_list2.append(x)
  return unique_list2

for h in word3:
  if h not in unique_list3:
    unique_list3.append(h)
  return unique_list3



with open("Book1","r") as f1
with open("Book2","r") as f2
with open("Book3","r") as f3
l1 = f1.readline()
l2 = f2.readline()
l3 = f3.readline()
word1 = l1.spilt()
word2 = l2.spilt()
word3 = l3.spilt()
words = word1 + word2 + word3
count_a = words.count("a")
count_the = words.count("the")
count_at = words.count("at")
count_run = words.count("run")
count_to = words.count("to")
count_and = words.count("and")
count_are = words.count("are")
count_or = words.count("or")
count_for = words.count("for")
count_an = words.count("an")
count_this = words.count("this")
list_all = []
list_all.append(count_a)
list_all.append(count_the)
list_all.append(count_at)
list_all.append(count_run)
list_all.append(count_to)
list_all.append(count_and)
list_all.append(count_are)
list_all.append(count_or)
list_all.append(count_for)
list_all.append(count_an)
list_all.append(count_this)

print(list_all)

l1=test_string.split()
l2=test_string.split()
l3=test_string.split()
d={}
d2={}
d3={}
for word1 in l1:
    if(word1[0] not in d.keys()):
        d[word1[0]]=[]
        d[word1[0]].append(word1)
    else:
        if(word1 not in d[word1[0]]):
          d[word1[0]].append(word1)
for k,v in d.items():
        print(k,":",v)
for word2 in l2:
    if(word2[0] not in d2.keys()):
        d2[word2[0]]=[]
        d2[word2[0]].append(word2)
    else:
        if(word2 not in d2[word2[0]]):
          d2[word2[0]].append(word2)
for z,x in d2.items():
        print(z,":",x)

for word3 in l3:
    if(word3[0] not in d3.keys()):
        d[word3[0]]=[]
        d[word3[0]].append(word3)
    else:
        if(word3 not in d3[word3[0]]):
          d3[word3[0]].append(word3)
for t,p in d3.items():
        print(t,":",p)

