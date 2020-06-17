from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'office/index.html')



"""
Error Handling
"""


def bad_request(request, exception):
    """
    400 Bad Request
    """
    return render(request, 'error/bad_request.html', {})


def not_authorized(request, exception):
    """
    403 Not Autorized Error
    """
    return render(request, 'error/not_autorized.html', {})


def page_not_found(request, exception):
    """
    404 Page not found
    """
    return render(request, 'error/not_found.html', {})


def internal_error(request, exception):
    """
    500 Internal Server Error
    """
    return render(request, 'error/server_error.html', {})
