import django_filters as filters
from frappe_app.models.website.website_slideshow import WebsiteSlideshow

class WebsiteSlideshowFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = WebsiteSlideshow
        fields = ['id']

