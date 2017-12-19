# https://techdevguide.withgoogle.com/paths/foundational/sequence-2/find-longest-word-in-dictionary-that-subsequence-of-given-string/#!

p = -1
app = ["5", "able", "ale", "apple", "bale", "kangaroo"]

def get_input(str):
	global p
	global app
	p+= 1
	return app[p]


class try_tree:
	def __init__(this):
		this.letters = dict()
		this.length = 0
		this.end = False
		this.visited = False
		this.letter = ""
		this.parent = None

	def hasLetter(this,letter):
		return letter in this.letters

	def getLetter(this,letter):
		return this.letters[letter]

	def setLetter(this,letter):
		new_tree = try_tree()
		new_tree.length = this.length + 1
		new_tree.letter = letter
		new_tree.parent = this
		this.letters[letter] = new_tree

	def setWord(this,word):
		if word == "":
			this.end = True
		else:
			this.setLetter(word[0])
			(this.letters[word[0]]).setWord(word[1:])



i = int(get_input("number of words"))
words = []
for x in range(0,i):
	words.append(get_input("word number " + str(x) + ":"))


trie = try_tree()

for x in words:
	trie.setWord(x)


ss2 = "abppplee"

trie.visited = True
leaves = [trie]

final_trie = trie
max_length = 0


for s in ss2:
	leaves_push_backlog = []
	for l in leaves:
		if(l.hasLetter(s)):
			l2 =  l.getLetter(s)
			if (not(l2.visited)):
				l2.visited = True
				leaves_push_backlog.append(l2)
				if(l2.end and (l2.length > max_length)):
					max_length = l2.length
					final_trie = l2
	leaves += leaves_push_backlog

answer = ""
while(not (final_trie.parent is None)):
	answer = final_trie.letter + answer 
	final_trie = final_trie.parent

print answer
