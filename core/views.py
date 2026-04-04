from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')

def about(request):
    # about = AboutUs.objects.first()

    # context = {
    #     'about': about,

    # }
    return render(request, 'about.html')


def whyus(request):
    # whyus = WhyUs.objects.first()
    # context = {
    #     'whyus': whyus,

    # }
    return render(request, 'why-us.html')


def legal(request):
    # legaldocs = Document.objects.all()

    # context = {
    #     'legaldocs': legaldocs,

    # }
    return render(request, 'legal-documents.html')


def contact(request):
    return render(request, 'contact.html')