from elements import Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td, Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br, Elem, Text

class Page:
	VALID_TAGS_FILE = {"html", "head", "body", "title", "meta", "img", "table", "th", "tr", "td", "ul", "ol", "li", "h1", "h2", "p", "div", "span", "hr", "br", "Text"}
	VALID_TAGS_BODY = {"h1", "h2", "div", "table", "ul", "ol", "span", "Text"}
	TEXT_ONLY_TAGS = {"title", "h1", "h2", "li", "th", "td"}

	def __init__(self, elem):
		if not isinstance(elem, Elem):
			raise TypeError("Error: parameter must be of type Elem or any of its children.")
		self.elem = elem

	def __str__(self):
		if self.elem.tag == "html":
			source_code = "<!DOCTYPE html>\n"
		source_code += str(self.elem)
		return source_code
	
	def _validate_from(self, elem):		
		if elem.tag not in self.VALID_TAGS_FILE:
			return False
		
		# Test 2
		if isinstance(elem, Html):
			if len(elem.content) != 2 or not isinstance(elem.content[0], Head) or not isinstance(elem.content[1], Body):
				return False
		
		# Test 3
		if isinstance(elem, Head):
			titles = [el for el in elem.content if isinstance(el, Title)]
			if len(titles) != 1:
				return False

		# Test 4
		if isinstance(elem, (Body, Div)):
			for el in elem.content:
				if el.tag not in self.VALID_TAGS_BODY:
					return False

		# Test 5
		if elem.tag in self.TEXT_ONLY_TAGS:
			if len(elem.content) != 1 or not isinstance(elem.content[0], Text):
				return False

		# Test 6
		if isinstance(elem, P):
			if not all(isinstance(el, Text) for el in elem.content):
				return False

		# Test 7
		if isinstance(elem, Span):
			if not all(isinstance(el, (Text, P)) for el in elem.content):
				return False

		# Test 8
		if isinstance(elem, (Ul, Ol)):
			if len(elem.content) < 1 or not all(isinstance(el, Li) for el in elem.content):
				return False
		
		# Test 9
		if isinstance(elem, Tr):
			len_th = len([el for el in elem.content if isinstance(el, Th)])
			len_td = len([el for el in elem.content if isinstance(el, Td)])
			if (len_th > 0 and len_td > 0) or len_th == len_td:
				return False

		# Test 10
		if isinstance(elem, Table):
			if not all(isinstance(el, Tr) for el in elem.content):
				return False

		for child in elem.content:
			if isinstance(child, Elem) and not self._validate_from(child):
				return False

		return True
	
	def is_valid(self):
		return self._validate_from(self.elem)

	def write_to_file(self, file_name):
		try:
			with open(file_name, "w") as f:
				f.write(str(self.elem))
		except Exception as e:
			print(f"Error: {e}")

# AI-generated tests  

def test_page():
	# Valid HTML structure
	html = Html([
		Head(Title(Text("Hello ground!"))),
		Body([
			H1(Text("Oh no, not again!")),
			Span(Text("Some text"))
		])
	])
	page = Page(html)
	print("Test 1: Valid - Expected True:", page.is_valid())
	assert page.is_valid() == True
	print(page)

	# Invalid HTML structure (missing Body)
	html = Html([
		Head(Title(Text("Hello ground!")))
	])
	page = Page(html)
	print("Test 2: Missing Body - Expected False:", page.is_valid())
	assert page.is_valid() == False

	# Invalid HTML structure (multiple Titles)
	html = Html([
		Head([
			Title(Text("Hello ground!")),
			Title(Text("Another title"))
		]),
		Body([
			H1(Text("Oh no, not again!")),
			Span(Text("Some text"))
		])
	])
	page = Page(html)
	print("Test 3: Multiple Titles - Expected False:", page.is_valid())
	assert page.is_valid() == False

	# Invalid HTML structure (Body contains invalid element)
	html = Html([
		Head(Title(Text("Hello ground!"))),
		Body([
			H1(Text("Oh no, not again!")),
			Span(Text("Some text")),
			Meta(attr={'charset': 'UTF-8'})
		])
	])
	page = Page(html)
	print("Test 4: Body contains invalid element - Expected False:", page.is_valid())
	assert page.is_valid() == False

	# Invalid HTML structure (Title contains multiple elements)
	html = Html([
		Head(Title([Text("Hello"), Text("ground!")])),
		Body([
			H1(Text("Oh no, not again!")),
			Span(Text("Some text"))
		])
	])
	page = Page(html)
	print("Test 5: Title contains multiple elements - Expected False:", page.is_valid())
	assert page.is_valid() == False

	# Invalid HTML structure (P contains invalid element)
	html = Html([
		Head(Title(Text("Hello ground!"))),
		Body([
			H1(Text("Oh no, not again!")),
			P([
				Text("Valid text"),
				Span(Text("Invalid element"))
			])
		])
	])
	page = Page(html)
	print("Test 6: P contains invalid element - Expected False:", page.is_valid())
	assert page.is_valid() == False

	# Invalid HTML structure (Span contains invalid element)
	html = Html([
		Head(Title(Text("Hello ground!"))),
		Body([
			H1(Text("Oh no, not again!")),
			Span([
				Text("Valid text"),
				Ul([Li(Text("Invalid element"))])
			])
		])
	])
	page = Page(html)
	print("Test 7: Span contains invalid element - Expected False:", page.is_valid())
	assert page.is_valid() == False

	# Invalid HTML structure (Ul contains invalid element)
	html = Html([
		Head(Title(Text("Hello ground!"))),
		Body([
			H1(Text("Oh no, not again!")),
			Ul([
				Li(Text("Item 1")),
				P(Text("Invalid item"))
			])
		])
	])
	page = Page(html)
	print("Test 8: Ul contains invalid element - Expected False:", page.is_valid())
	assert page.is_valid() == False

	# Invalid HTML structure (Tr contains both Th and Td)
	html = Html([
		Head(Title(Text("Hello ground!"))),
		Body([
			Table([
				Tr([
					Th(Text("Header")),
					Td(Text("Data"))
				])
			])
		])
	])
	page = Page(html)
	print("Test 9: Tr contains both Th and Td - Expected False:", page.is_valid())
	assert page.is_valid() == False

	# Invalid HTML structure (Table contains invalid element)
	html = Html([
		Head(Title(Text("Hello ground!"))),
		Body([
			Table([
				Tr([
					Th(Text("Header 1")),
					Th(Text("Header 2"))
				]),
				Td(Text("Invalid element"))
			])
		])
	])
	page = Page(html)
	print("Test 10: Table contains invalid element - Expected False:", page.is_valid())
	assert page.is_valid() == False

	# Write valid HTML to file
	html = Html([
		Head(Title(Text("Hello ground!"))),
		Body([
			H1(Text("Oh no, not again!")),
			Span(Text("Some text"))
		])
	])
	page = Page(html)
	page.write_to_file("output.html")

if __name__ == '__main__':
	test_page()