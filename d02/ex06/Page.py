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
	
	# def is_valid(self):

	def write_to_file(self, file_name):
		try:
			with open(file_name, "w") as f:
				f.write(str(self.elem))
		except Exception as e:
			print(f"Error: {e}")
