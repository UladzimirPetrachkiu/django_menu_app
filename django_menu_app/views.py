from django.shortcuts import render


def index(request):
    """
    This function handles the request and renders the 'index.html' template.
    """
    return render(request, 'index.html')


def about(request):
    """
    This function handles the request and renders the 'about.html' template.
    """
    return render(request, 'about.html')


def services(request):
    """
    This function handles the request and renders the 'services.html' template.
    """
    return render(request, 'services.html')


def contacts(request):
    """
    This function handles the request and renders the 'contacts.html' template.
    """
    return render(request, 'contacts.html')


def web_dev(request):
    """
    This function handles the request and renders the 'web_dev.html' template.
    """
    return render(request, 'web_dev.html')


def mobile_apps(request):
    """
    This function handles the request and renders the 'mobile_apps.html' template.
    """
    return render(request, 'mobile_apps.html')


def secondary(request):
    """
    This function handles the request and renders the 'secondary.html' template.
    """
    return render(request, 'secondary.html')


def news(request):
    """
    This function handles the request and renders the 'news.html' template.
    """
    return render(request, 'news.html')


def blog(request):
    """
    This function handles the request and renders the 'blog.html' template.
    """
    return render(request, 'blog.html')


def portfolio(request):
    """
    This function handles the request and renders the 'portfolio.html' template.
    """
    return render(request, 'portfolio.html')


def web_projects(request):
    """
    This function handles the request and renders the 'web_projects.html' template.
    """
    return render(request, 'web_projects.html')


def mobile_apps_portfolio(request):
    """
    This function handles the request and renders the 'mobile_apps_portfolio.html' template.
    """
    return render(request, 'mobile_apps_portfolio.html')
