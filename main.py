String = "Peter Piper picked a peck of pickled peppers. A peck of pickled peppers Peter Piper picked. If Peter Piper picked a peck of pickled peppers, Where's the peck of pickled peppers Peter Piper picked? Peter Piper picked a peck of pickled peppers. But if Peter Piper picked a peck of pickled peppers, How many pickled peppers that Peter Piper picked?"

#this function returns the number of count of selected letters.
def countletters(thisString, search):


  count = 0
  for letter in String:

    if letter.lower() == search.lower():
      count +=1 #instead of cnt = cnt + 1 i used an increment 

  return count
#dictionary of vowels
vowelCounts={'a':0, 'e':0,'i':0, 'o':0,'u':0}

for letter in String:
  letter = letter.lower()
  if letter in vowelCounts:
    vowelCounts[letter] += 1

print(vowelCounts)

#use the dictionary to count 
