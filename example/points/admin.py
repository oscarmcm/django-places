from django.conf import settings
from django.contrib import admin

from .models import Place, RoutePoint, Route

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('position_map', 'location')

    def position_map(self, instance):
        if instance.location is not None:
            return '<img src="http://maps.googleapis.com/maps/api/staticmap?center=%(latitude)s,%(longitude)s&zoom=%(zoom)s&size=%(width)sx%(height)s&maptype=roadmap&markers=%(latitude)s,%(longitude)s&sensor=false&visual_refresh=true&scale=%(scale)s&key=%(key)s" width="%(width)s" height="%(height)s">' % {
                'latitude': instance.location.latitude,
                'longitude': instance.location.longitude,
                'key': getattr(settings, 'PLACES_MAPS_API_KEY'),
                'zoom': 15,
                'width': 100,
                'height': 100,
                'scale': 2
            }
    position_map.allow_tags = True


class RoutePointInline(admin.StackedInline):
    '''Stacked Inline View for RoutePoint model'''

    model = RoutePoint
    min_num = 1
    extra = 1


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    inlines = [RoutePointInline, ]

