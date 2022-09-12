from django.contrib.sitemaps import Sitemap
from .models import Post

# Custom site map
class PostSitemap(Sitemap):
    changefreq = 'weekly' # change freq of post pages
    priority = 0.9 # relevance in the website
    
    def items(self):
        return Post.published.all() # return queryset of object to include in this sitemap
    
    def lastmod(self, obj):
        return obj.updated