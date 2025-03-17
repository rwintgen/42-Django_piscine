class Text(str):
	def __str__(self):
		text_content = super().__str__()
		text_content = text_content.replace('<', '&lt;')
		text_content = text_content.replace('>', '&gt;')
		text_content = text_content.replace('"', '&quot;')
		text_content = text_content.replace('\n', '\n<br />\n')
		return text_content


class Elem:
	class ValidationError(Exception):
		def __init__(self):
			super().__init__("Invalid argument(s)")

	def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
		if tag_type not in ['simple', 'double']:
			raise self.ValidationError

		self.tag = tag
		self.attr = attr
		self.content = []
		if content is not None:
			self.add_content(content)
		self.tag_type = tag_type

	def __str__(self):
	# structure to expect:
		# tag_type = double : <{tag} {attr}>{content}</{tag}>
		# tag_type = simple : <{tag} {attr}/>
		result = "<{tag}{attr}"

		if self.tag_type == 'double':
			result += ">{content}</{tag}>"
		elif self.tag_type == 'simple':
			result += "/>"

		result = result.format(tag = self.tag, attr = self.__make_attr(), content = self.__make_content())
		return result

	def __make_attr(self):
		result = ''
		for pair in sorted(self.attr.items()):
			result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
		return result

	def __make_content(self):
		if len(self.content) == 0:
			return ''
		result = '\n'
		for elem in self.content:
			result += "{elem}".format(elem = elem) + "\n"
		result = "  ".join(line for line in result.splitlines(True))
		return result

	def add_content(self, content):
		if not Elem.check_type(content):
			raise self.ValidationError
		if type(content) == list:
			self.content += [elem for elem in content if elem != Text('')]
		elif content != Text(''):
			self.content.append(content)

	@staticmethod
	def check_type(content):
		return (isinstance(content, Elem) or type(content) == Text or
				(type(content) == list and all([type(elem) == Text or
												isinstance(elem, Elem)
												for elem in content])))

def test():
    html =	Elem('html', content = [
				Elem('head', content = 
	   				Elem('title', content = Text("Hello ground!"))),
				Elem('body', content = [
					Elem('h1', content = Text("Oh no, not again!")),
					Elem('img', {'src': 'http://i.imgur.com/pfp3T.jpg'}, None, "simple")
		])
	])
    print(html)

if __name__ == '__main__':
	test()