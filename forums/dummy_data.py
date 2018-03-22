from . import models, stores
from time import sleep

try:
    last_id = models.Member.objects.latest('id').id
except (KeyError, models.Member.DoesNotExist):
    last_id = 0

dummy_members = [
	models.Member(id=last_id+1, name="Manar", age=23),
	models.Member(id=last_id+2, name="Nour", age=21),
	models.Member(id=last_id+3, name="Zein", age=21),
	models.Member(id=last_id+4, name="Rayan", age=21)
]

dummy_posts = [
    models.Post(title="1st Post", content="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", member_id=dummy_members[0].id),
    models.Post(title="2nd Post", content="Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.", member_id=dummy_members[2].id),
    models.Post(title="3rd Post", content="Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.", member_id=dummy_members[1].id),
    models.Post(title="4th Post", content="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", member_id=dummy_members[3].id),
    models.Post(title="5th Post", content="Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.", member_id=dummy_members[0].id),
    models.Post(title="6th Post", content="Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.", member_id=dummy_members[2].id),
    models.Post(title="7th Post", content="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", member_id=dummy_members[0].id),
    models.Post(title="8th Post", content="Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.", member_id=dummy_members[2].id),
    models.Post(title="9th Post", content="Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.", member_id=dummy_members[0].id)
]

def seed_stores(members_store, posts_store):
    models.Post.objects.all().delete()
    models.Member.objects.all().delete()
    for member in dummy_members:
        members_store.add(member)

    for post in dummy_posts:
        posts_store.add(post)