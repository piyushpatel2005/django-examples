from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import Http404
from bands.models import Band, Musician, Venue

from bands.models import Musician

def _get_page_num(request, paginator):
    # Get current page number for Pagination, using reasonable defaults
    page_num = int(request.GET.get("page", 1))

    if page_num < 1:
        page_num = 1
    elif page_num > paginator.num_pages:
        page_num = paginator.num_pages

    return page_num

def _get_items_per_page(request):
    # Determine how many items to show per page, disallowing <1 or >50
    items_per_page = int(request.GET.get("items_per_page", 10))
    if items_per_page < 1:
        items_per_page = 10
    if items_per_page > 50:
        items_per_page = 50

    return items_per_page


def musicians(request):
    all_musicians = Musician.objects.all().order_by("last_name")
    items_per_page = _get_items_per_page(request)
    paginator = Paginator(all_musicians, items_per_page)
    page_num = _get_page_num(request, paginator)
    page = paginator.page(page_num)

    data = {
        "musicians": page.object_list,
        "page": page,
    }

    return render(request, "musicians.html", data)

def musician(request, musician_id):
    musician = get_object_or_404(Musician, id=musician_id)
    data = {
        'musician': musician
    }

    return render(request, 'musician.html', data)

def band (request, band_id):
    data = {
        "band": get_object_or_404(Band, id=band_id)
    }
    return render(request, "band.html", data)

def bands(request):
    all_bands = Band.objects.all().order_by("name")
    items_per_page = _get_items_per_page(request)
    paginator = Paginator(all_bands, items_per_page)
    page_num = _get_page_num(request, paginator)
    page = paginator.page(page_num)

    data = {
        "bands": page.object_list,
        "page": page,
    }

    return render(request, "bands.html", data)

def venues(request):
    all_venues = Venue.objects.all().order_by("name")
    items_per_page = _get_items_per_page(request)
    paginator = Paginator(all_venues, items_per_page)
    page_num = _get_page_num(request, paginator)
    page = paginator.page(page_num)

    data = {
        "venues": page.object_list,
        "page": page,
    }

    return render(request, "venues.html", data)


@login_required
def restricted_page(request):
    data = {
        'title': "Restricted Page",
        'content': '<h1>You are logged in</h1>',
    }

    return render (request, "general.html", data)

@login_required
def musician_restricted(request, musician_id):
    musician = get_object_or_404(Musician, id=musician_id)
    profile = request.user.userprofile
    allowed = False

    if profile.musician_profiles.filter(id=musician_id).exists():
        allowed = True
    else:
        musician_profiles = set (profile.musician_profiles.all())
        for band in musician.band_set.all():
            band_musicians = set (band.musicians.all())
            if musician_profiles.intersection(band_musicians):
                allowed = True
                break

    if not allowed:
        raise Http404("Permission denied")
    
    content = f"""
        <h1>Musician Page: {musician.last_name}, {musician.first_name}</h1>
        """

    data = {
        'title': "Restricted Page",
        'content': content,
    }

    return render (request, "general.html", data)

def has_venue(user):
    try:
        return user.userprofile.venues_controlled.count() > 0
    except AttributeError:
        return False


@user_passes_test(has_venue)
def venues_restricted(request):
    return venues(request)