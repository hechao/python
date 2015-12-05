#! /usr/bin/python
original = raw_input("Enter a word:")

pyg = "ay" 

if len(original) > 0 and original.isalpha():
  new_word = original.lower()
  first = new_word[0]
  new_word = new_word + first +pyg
  new_word = new_word[1:len(new_word)]
  print new_word

else:
  print "please enter a valid answer"
