import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

## FAKE POP SCRIPT
import random
from first_app.models import AccessRecord, Webpage, Topic
from faker import Faker

fakegen = Faker()
topics=['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
  t = Topic.objects.get_or_create(top_name=random.choice(topics))[0] # Returns a tuple por eso agarramos el 0
  t.save()
  return t

def populate(N=5):
  for entry in range(N):
    # get the topic for the entry
    top = add_topic()

    # Create fake data for that entry
    fake_url = fakegen.url()
    fake_date = fakegen.date()
    fake_name = fakegen.company()

    # Create new webpage entry
    webpage = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

    # Create a fake access record for that webpage
    # Usamos name=webpage porque en el modelo name esta especificado como Foreign Key
    acc_rec = AccessRecord.objects.get_or_create(name=webpage, date=fake_date)[0]

if __name__ == '__main__':
  print('Populating script!')
  populate(20)
  print('Populating compleate!')


# To run this script
# python populate_first_app.py
