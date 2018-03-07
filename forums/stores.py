import itertools

class BaseStore():
	"""This class provides CRUD Functions"""
	def __init__(self, data_provider, last_id):
		self._data_provider = data_provider
		self._last_id = last_id

	def get_all(self):
		return self._data_provider

	def get_by_id(self, id):
		for instance in self.get_all():
			if instance.id == id:
				return instance

	def entity_exists(self, instance):
		result = False
		if instance is not None:
			if instance is self.get_by_id(instance.id):
				result = True
		return result

	def add(self, instance):
		instance.id = self._last_id
		self._data_provider.append(instance)
		self._last_id += 1

	def update (self, updated_instance):
		instances = self.get_all()
		for index, instance in enumerate(instances):
			if instance.id == updated_instance.id:
				instances[index] = updated_instance

	def delete(self, id):
		instance = self.get_by_id(id)
		if instance is not None:
			self._data_provider.remove(instance)

class MemberStore(BaseStore):
	"""This class inherits from BaseStore to Manage Members Information"""

	members = []
	last_id = 1

	def __init__(self):
		super().__init__(self.members, self.last_id)

	def get_by_name(self, name):
		return (member for member in self.get_all() if member.name == name)

	def get_members_with_posts(self, posts):
		members = self.get_all()
		for member, post in itertools.product(members, posts):
			if post.member_id == member.id:
				member.posts.append(post)
		return members

	def get_top_members_with_posts(self):
		members = self.get_all()
		members.sort(key=lambda member: len(member.posts), reverse=True)
		return members[:2]

class PostStore(BaseStore):
	"""This class inherits from BaseStore to Manage Posts Information"""

	posts = []
	last_id = 1

	def __init__(self):
		super().__init__(self.posts, self.last_id)

	def get_posts_by_date(self):
		posts = self.get_all()
		posts.sort(key=lambda post: post.date, reverse=True)
		return posts