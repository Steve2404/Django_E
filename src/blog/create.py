import json
import django
import os
from models import BlogPost

# configuration file
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings.py')
django.setup()
chemin = "blog_blogpost.json"


def insert_data():
    with open(chemin, "r", encoding='utf-8') as f:
        data = json.load(f)

    for bp in data:
        BlogPost.objects.create(title=bp["title"],
                                slug=bp["slug"],
                                published=bp["published"],
                                description=bp["description"],
                                date=bp["date"])


if __name__ == '__main__':
    insert_data()
    print("Blog post created")
