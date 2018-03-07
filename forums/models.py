import datetime
class Member():
	"""This class provides a way to store member name and age"""

	def __init__(self, name, age):
		self.id = 0
		self.name = name
		self.age = age
		self.posts = []

	def __str__(self):
		return (f"{self.name}, {self.age} Years Old")

class Post():
	"""This class provides a way to store post title and content"""

	def __init__ (self, title, content, member_id = 0):
		self.id = 0
		self.title = title
		self.content = content
		self.member_id = member_id
		self.date = datetime.datetime.now()

	def __str__(self):
		return (f"{self.title}, {self.content[:20]}...")