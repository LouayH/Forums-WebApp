from django.db import models
from django.core.validators import MinValueValidator 

class Member(models.Model):
	name = models.CharField(max_length=200)
	age = models.PositiveIntegerField(validators=[MinValueValidator(1)])

	def __repr__(self):
		return (f"{self.name}, {self.age} Years Old")

	def as_dict(self):
		return {
			"id": self.id,
			"name": self.name,
			"age": self.age
		}

class Post(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	date = models.DateTimeField()
	member = models.ForeignKey(Member, related_name="posts", on_delete=models.CASCADE)

	def __repr__(self):
		return (f"{self.title}")

	def as_dict(self):
		return {
			"id": self.id,
			"title": self.title,
			"content": self.content,
			"date": self.date,
			"member_id": self.member_id
		}