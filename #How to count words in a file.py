#How to count words in a file
with open('./Functional_Programming_in_Scala.pdf', 'r) as file_reader_object:
	content=file_reader_object.read()
word_count=content.split()
print(str(word_count))