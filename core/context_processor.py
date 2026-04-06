from .models import *
from daytour.models import *
# from about.models import *
# from settings.models import *
# from page.models import *
from settings.models import Favicon, Logo, SiteInfo,PageBanner
# , CompanyProfile, SocialLinks, PageBanner, Seo as DefaultSEO


def default(request):
    favicon = Favicon.objects.first()
    logo = Logo.objects.first()
    site_info = SiteInfo.objects.first()
    pagebanner = PageBanner.objects.first()
    daytours=DayTour.objects.all().filter(is_active=True)
    # defaultseo = DefaultSEO.objects.first()

    # destinations = Destination.objects.prefetch_related(
    #     'activities').filter(is_active=True)
    # styles = Style.objects.all()
    # activities = Activity.objects.filter(destination__title="Nepal").distinct()
    # pages = Page.objects.all().filter(is_active=True)
    # social_links = SocialLinks.objects.first()

    # defaultseo = DefaultSEO.objects.first()
    # mountaineering = Tour.objects.all().filter(activity__title='Mountaineering')
    # trekking = Tour.objects.all().filter(activity__title='Trekking')
    # heightcat = HeightCategory.objects.all()
    # trekkingregions = Region.objects.all()
    # climbing = Tour.objects.all().filter(activity__title='Climbing')
    # skiing = Tour.objects.all().filter(activity__title='Skiing')
    # othertours = Tour.objects.all().filter(activity__title='Adventure Tours')
    # testimonials=Testimonial.objects.all()

    # upcomingtours=Tour.objects.all().filter(tour__)

    # blogs = Blog.objects.all()

    return {
        'favicon': favicon,
        'logo': logo,
        'site_info': site_info,
        'pagebanner': pagebanner,
        'daytours': daytours,
        # 'styles': styles,
        # 'activities': activities,
        # 'destinations': destinations,
        # 'pages': pages,
        # 'defaultseo': defaultseo,
        
        # 'social_links': social_links,
        # 'mountaineering': mountaineering,
        # 'heightcat': heightcat,
        # 'trekking': trekking,
        # 'trekkingregions':trekkingregions,
        # 'climbing': climbing,
        # 'skiing': skiing,
        # 'othertours': othertours,
        # 'blogs': blogs,
        # 'testimonials': testimonials,
    }
