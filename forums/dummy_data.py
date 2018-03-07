from . import models, stores
from time import sleep

dummy_members = [
	models.Member("Manar", 23),
	models.Member("Nour", 21),
	models.Member("Zein", 21),
	models.Member("Rayan", 21)
]

dummy_posts = [
    models.Post("1st Post", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", dummy_members[0].id),
    models.Post("2nd Post", "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.", dummy_members[2].id),
    models.Post("3rd Post", "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.", dummy_members[1].id),
    models.Post("4th Post", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", dummy_members[3].id),
    models.Post("5th Post", "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.", dummy_members[0].id),
    models.Post("6th Post", "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.", dummy_members[2].id),
    models.Post("7th Post", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", dummy_members[0].id),
    models.Post("8th Post", "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.", dummy_members[3].id),
    models.Post("9th Post", "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.", dummy_members[0].id)
]

def seed_stores(members_store, posts_store):
    for member in dummy_members:
        members_store.add(member)

    for post in dummy_posts:
        posts_store.add(post)