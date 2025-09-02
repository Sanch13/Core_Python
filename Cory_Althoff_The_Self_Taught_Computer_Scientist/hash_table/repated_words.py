"""
В предлагаемой строке удалите все повторяющиеся слова. Например, вам
дана строка "I am a self-taught programmer looking for a job as a programmer.".
Ваша функция должна вернуть "I am a self-taught programmer looking for
a job as a.".
"""


def deleted_repeated_words(sentences: str):
	d = {}
	str_lst = []
	for word in sentences.split():
		if word not in d:
			d[word] = 1
			str_lst.append(word)

	return ' '.join(str_lst)


if __name__ == '__main__':
	s = "I am a self-taught programmer looking for a job as a."
	print(deleted_repeated_words(s))

