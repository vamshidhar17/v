words =["cat","sat","bat","map"]
with open("words.txt","w") as f:
 for word in words:
  f.write(word)