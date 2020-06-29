print('Yo thugnificent')

boss = 'Sanjin'

def remove_punctuation(st,exception=''):
	punctuation = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
	punctuation = punctuation.replace(exception,'')
	for c in st:
		if c in punctuation:
			st = st.replace(c,'')
	return st

#1 write a function that takes in a book and returns a list of words
def create_word_list(st):
	ans = remove_punctuation(st)
	return ans.split()

#2 write a function that takes in a book and returns a list of sentences
def create_sentence_list(st):
	st = st.replace('\n\n','')
	st = st.replace('\n','')
	ans = remove_punctuation(st,'.')
	return ans.split('.')
	
#3 write a function that takes in a book and returns a list of paragraphs
def create_paragraph_list(st):
	ans = remove_punctuation(st)
	return ans.split('\n\n')

#4 write a function that takes in a book and returns a list of chapters
def create_chapter_list(st):
	ans = remove_punctuation(st,'-')
	ans = ans.replace('-',' ')
	return ans.split('CHAPTER')