from django.contrib import admin
from django.utils.html import format_html, mark_safe
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.urls import reverse

from bands.models import Musician, Band, Room, Venue, UserProfile

from datetime import date, datetime

class DecadeListFilter(admin.SimpleListFilter):
    title = "decade born"
    parameter_name = "decade"

    def lookups(self, request, model_admin):
        result = []
        this_year = datetime.today().year
        this_decade = (this_year // 10) * 10
        start = this_decade - 10
        for year in range(start, start - 100, -10):
            result.append((str(year), f"{year}-{year+9}"))

        return result

    def queryset(self, request, queryset):
        start = self.value()
        if start is None:
            return queryset
        start = int(start)
        result = queryset.filter(
            birth__gte=date(start, 1, 1),
            birth__lte=date(start + 9, 12, 31),
        )

        return result

@admin.register(Musician)
class MusicianAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "birth",  "show_weekday", "show_bands", )
    list_filter = (DecadeListFilter, )
    search_fields = ("last_name", "first_name")

    def show_weekday(self, obj):
        return obj.birth.strftime("%A")

    show_weekday.short_description = "Birth Weekday"

    def show_bands(self, obj):
        bands = obj.band_set.all()
        if len(bands) == 0:
            return format_html("<i>None</i>")
        
        plural = ""
        if len(bands) > 1:
            plural = "s"
        parm = "?id__in=" + ",".join([str(b.id) for b in bands])
        url = reverse("admin:bands_band_changelist") + parm

        return format_html('<a href="{}">Band{}</a>', url, plural)

    show_bands.short_description = "Bands"


@admin.register(Band)
class BandAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "show_members", )
    search_fields = ("name",)

    def show_members(self, obj):
        musicians = obj.musicians.all()
        links = []
        url = reverse ("admin:bands_musician_changelist")

        for musician in musicians:
            parm = f"?id={musician.id}"
            link = format_html('<a href="{}">{}</a>', url + parm, musician.last_name)
            links.append(link)

        return mark_safe(", ".join(links))

    show_members.short_description = "Members"


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "show_rooms",)
    search_fields = ("name",)

    def show_rooms(self, obj):
        rooms = obj.room_set.all()
        if len(rooms) == 0:
            return format_html("<i>None</i>")
        
        plural = ""
        if len(rooms) > 1:
            plural = "s"
        parm = "?id__in=" + ",".join([str(r.id) for r in rooms])
        url = reverse("admin:bands_room_changelist") + parm

        return format_html('<a href="{}">Room{}</a>', url, plural)

    show_rooms.short_description = "Rooms"


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)
    search_fields = ("name",)


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)