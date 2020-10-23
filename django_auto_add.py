
from pygooglenews import GoogleNews
import time
from linkpreview import link_preview
import os
import django

gn = GoogleNews(lang='ar')
keyword_results = gn.search('أندرويد')
data = keyword_results['entries']

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news_feed.settings')
django.setup()

from articles.models import article as classy

all_news = []
test_counter = 0

for i in data:
    try:
        preview = link_preview(i.link)
        components = {
            'title' : i.title,
            'link' : i.link,
            'image' : preview.image
            }
            
        if str(components['image']) == 'None':
            pass
        else:
            new_data = classy(title=components['title'], link=components['link'], image=components['image'])
            new_data.save()
            print('\n')
        time.sleep(20)
    except:
        pass
