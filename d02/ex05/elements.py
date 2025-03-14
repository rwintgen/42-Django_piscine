from elem import Elem, Text

# Elem arguments order: self, tag, attr, content, tag_type

class Html(Elem):
	def __init__(self, content = None, attr = {}):
		super().__init__("html", attr, content, "double")

class Head(Elem):
	def __init__(self, content = None, attr = {}):
		super().__init__("head", attr, content, "double")

class Body(Elem):
	def __init__(self, content = None, attr = {}):
		super().__init__("body", attr, content, "double")

class Title(Elem):
	def __init__(self, content = None, attr = {}):
		super().__init__("title", attr, content, "double")

class Meta(Elem):
	def __init__(self, content = None, attr = {}):
		super().__init__("meta", attr, None, "simple")

class Img(Elem):
	def __init__(self, content = None, attr = {}):
		super().__init__("img", attr, None, "simple")

class Table(Elem):
	def __init__(self, content = None, attr = {}):
		super().__init__("table", attr, content, "double")

class Th(Elem):
	def __init__(self, content = None, attr = {}):
		super().__init__("th", attr, content, "double")

class Tr(Elem):
	def __init__(self, content = None, attr = {}):
		super().__init__("tr", attr, content, "double")

class Td(Elem):
	def __init__(self, content = None, attr = {}):
		super().__init__("td", attr, content, "double")

class Ul(Elem):
	def __init__(self, content = None, attr = {}):
		super().__init__("ul", attr, content, "double")

class Ol(Elem):
	def __init__(self, content = None, attr = {}):
		super().__init__("ol", attr, content, "double")

class Li(Elem):
	def __init__(self, content = None, attr = {}):
		super().__init__("li", attr, content, "double")

class H1(Elem):
	def __init__(self, content = None, attr = {}):
		super().__init__("h1", attr, content, "double")

class H2(Elem):
	def __init__(self, content = None, attr = {}):
		super().__init__("h2", attr, content, "double")

class P(Elem):
	def __init__(self, content = None, attr = {}):
		super().__init__("p", attr, content, "double")

class Div(Elem):
	def __init__(self, content = None, attr = {}):
		super().__init__("div", attr, content, "double")

class Span(Elem):
	def __init__(self, content = None, attr = {}):
		super().__init__("span", attr, content, "double")

class Hr(Elem):
	def __init__(self, content = None, attr = {}):
		super().__init__("hr", attr, None, "simple")

class Br(Elem):
	def __init__(self, content = None, attr = {}):
		super().__init__("br", attr, None, "simple")

def subject_test():
	html =	Html([
				Head(
					Title(Text("Hello ground!"))),
				Body([
					H1(Text("Oh no, not again!")),
					Img({'src': 'http://i.imgur.com/pfp3T.jpg'})
				])
			])
	print(html)

def deeper_test():
	html =	Html([
				Head([
					Meta(attr = {"charset" : "UTF-8"}),
					Title(Text("Test with CV from d00!"))]),
				Body([
					H1(Text("Hello!")),
					H2(Text("This is my resume.")),
					Div([
						Table([
							Tr([
								Th(Text("name")),
								Th(Text("surname")),
								Th(Text("email"))]),
							Tr([
								Td(Text("romain")),
								Td(Text("wintgens")),
								Td(Text("rwintgen@student.42madrid.com"))])])], {"id" : "table_id"})]),
					Div([
						P(Text("skills")),
						Ul([
							Li(Text("cuddling my girlfriend")),
							Li(Text("listening to daft punk")),
							Li(Text("drinking gin & tonic"))])], {"class" : "list_class"})], {"lang" : "en"})
	print(html)

if __name__ == '__main__':
	subject_test()
	# deeper_test()
