import sys
import re

class Parser:
	SENTENCE_START_SYMBOL = '^'
	SENTENCE_END_SYMBOL = '$'

	def __init__(self, name, depth=2, ssc = '\n', wsc = ''):
		"""Definition of abbrs.

		ssc = sentence_split_char
		wsc = word_split_char
		"""
		self.name = name
		self.depth = depth
		self.sentence_split_char = ssc
		self.word_split_char = wsc
		self.whitespace_regex = re.compile('\s+')

	def parse(self, txt):
		sentences = txt.split(self.sentence_split_char)
		i = 0
		result = []
		for sentence in sentences:
			sentence = self.whitespace_regex.sub(" ", sentence).strip()
			list_of_words = None
			if self.word_split_char:
				list_of_words = sentence.split(self.word_split_char)
			else:
				list_of_words = list(sentence.lower())
			word_list_starter = [Parser.SENTENCE_START_SYMBOL] * (self.depth - 1)
			word_list_enders = [Parser.SENTENCE_END_SYMBOL] * (self.depth - 1)
			words = word_list_starter + list_of_words + word_list_enders


			for n in range(0, len(words) - self.depth + 1):
				new_ish = words[n:n + self.depth]
				result.append(new_ish)
			import ipdb; ipdb.set_trace()

			i += 1
			if i % 1000 == 0:
				print i
				print result
