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
	
	def _validate_from(self, e):
		if e.tag not in self.VALID_TAGS_FILE:
			return False
		
		if isinstance(e, Html):
			if len(e.content) != 2 or not isinstance(e.content[0], Head) or not isinstance(e.content[1], Body):
				return False
		
		# if isinstance(e, Head):

		# if isinstance(e, (Body, Div)):

		# if e.tag in self.TEXT_ONLY_TAGS:

		# if isinstance(e, P):

		# if isinstance(e, Span):

		# if isinstance(e, (Ul, Ol)):
		
		# if isinstance(e, Tr):

		# if isinstance(e, Table):

		return True
	
	def is_valid(self):
		return self._validate_from(self.elem)

	def write_to_file(self, file_name):
		try:
			with open(file_name, "w") as f:
				f.write(str(self.elem))
		except Exception as e:
			print(f"Error: {e}")
