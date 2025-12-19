# So we use with block for files -- we can do any operation inside 
# its scope on file and when we move out of the scope python closes and saves the file
# automatically and safely ! -- best practice for files
# r mode -- does not create a file!

with open("story.txt", "r") as f:
    story = f.read() # it does not a local var -- not like functions!


# print(story) # it gives all the content from file !
# print(type(story))
# word = list()
words = set() 
start_of_word = -1

target_start = "<"
target_end = ">"

for index, char in enumerate(story):
    if char == target_start:
        start_of_word = i
    
    if char == target_end and target_start:
        word = story[start_of_word: i + 1] # slicing method
        words.add(word)
        start_of_word = -1

    
