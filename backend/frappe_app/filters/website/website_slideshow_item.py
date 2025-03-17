import django_filters as filters
from frappe_app.models.website.website_slideshow_item import WebsiteSlideshowItem

class WebsiteSlideshowItemFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = WebsiteSlideshowItem
        fields = ['id']

