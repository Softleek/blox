import django_filters as filters
from frappe_app.models.website.web_page_view import WebPageView

class WebPageViewFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = WebPageView
        fields = ['id']

