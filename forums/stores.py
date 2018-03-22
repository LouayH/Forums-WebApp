import itertools
from . import models
from django.utils import timezone

class BaseStore():
	"""This class provides CRUD Functions"""
	def __init__(self, data_provider):
		self._data_provider = data_provider

	def get_all(self):
		return self._data_provider.objects.all().order_by('pk')

	def get_by_id(self, id):
		return self._data_provider.objects.get(pk=id)

	def entity_exists(self, instance):
		result = False
		if instance is self.get_by_id(instance.id):
			result = True
		return result

	def delete(self, id):
		self._data_provider.objects.get(pk=id).delete()

class MemberStore(BaseStore):
	"""This class inherits from BaseStore to Manage Members Information"""

	def __init__(self):
		super().__init__(models.Member)

	def add(self, instance):
		i = self._data_provider.objects.create(name=instance.name, age=instance.age)
		i.save()

	def update (self, updated_instance):
		i = self._data_provider.objects.get(pk=updated_instance.id)
		i.name = updated_instance.name
		i.age = updated_instance.age
		i.save()

	def get_by_name(self, name):
		return self._data_provider.objects.get(name=name)

	def get_members_with_posts(self):
		return self._data_provider.objects.prefetch_related('posts')
		# member[index].posts.all()

	def get_top_members_with_posts(self):
		pass
		# members = self.get_all()
		# members.sort(key=lambda member: len(member.posts), reverse=True)
		# return members[:2]

class PostStore(BaseStore):
	"""This class inherits from BaseStore to Manage Posts Information"""

	def __init__(self):
		super().__init__(models.Post)

	def add(self, instance):
		i = self._data_provider.objects.create(title=instance.title, content=instance.content, date=timezone.now(), member_id=instance.member_id)
		i.save()

	def update (self, updated_instance):
		i = self._data_provider.objects.get(pk=updated_instance.id)
		i.title = updated_instance.title
		i.content = updated_instance.content
		i.save()

	def get_posts_by_date(self):
		return self._data_provider.objects.all().order_by('-date')