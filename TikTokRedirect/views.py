from django.http import HttpResponseRedirect

URL = 'https://example.com'

def redirect_to_external_website(request, my_path):

    return HttpResponseRedirect(URL)


def redirect_to_external_website2(request):
    return HttpResponseRedirect(URL)
