from django.shortcuts import render


def index(request):
    template_name = 'index.html'
    return render(request, template_name)


def _list(request):
    template_name = '_list.html'
    return render(request, template_name)


def _create(request):
    template_name = '_form.html'
    return render(request, template_name)


def breadcrumb(request):
    template_name = 'base/breadcrumb.html'
    return render(request, template_name)


def cards(request):
    template_name = 'base/cards.html'
    return render(request, template_name)


def carousel(request):
    template_name = 'base/carousel.html'
    return render(request, template_name)


def collapse(request):
    template_name = 'base/collapse.html'
    return render(request, template_name)


def forms(request):
    template_name = 'base/forms.html'
    return render(request, template_name)


def jumbotron(request):
    template_name = 'base/jumbotron.html'
    return render(request, template_name)


def list_group(request):
    template_name = 'base/list-group.html'
    return render(request, template_name)


def navs(request):
    template_name = 'base/navs.html'
    return render(request, template_name)


def pagination(request):
    template_name = 'base/pagination.html'
    return render(request, template_name)


def popovers(request):
    template_name = 'base/popovers.html'
    return render(request, template_name)


def progress(request):
    template_name = 'base/progress.html'
    return render(request, template_name)


def scrollspy(request):
    template_name = 'base/scrollspy.html'
    return render(request, template_name)


def switches(request):
    template_name = 'base/switches.html'
    return render(request, template_name)


def tables(request):
    template_name = 'base/tables.html'
    return render(request, template_name)


def tabs(request):
    template_name = 'base/tabs.html'
    return render(request, template_name)


def tooltips(request):
    template_name = 'base/tooltips.html'
    return render(request, template_name)


def brand_buttons(request):
    template_name = 'buttons/brand-buttons.html'
    return render(request, template_name)


def button_group(request):
    template_name = 'buttons/button-group.html'
    return render(request, template_name)


def buttons(request):
    template_name = 'buttons/buttons.html'
    return render(request, template_name)


def dropdowns(request):
    template_name = 'buttons/dropdowns.html'
    return render(request, template_name)


def charts(request):
    template_name = 'charts.html'
    return render(request, template_name)


def colors(request):
    template_name = 'colors.html'
    return render(request, template_name)


def coreui_icons(request):
    template_name = 'icons/coreui-icons.html'
    return render(request, template_name)


def flags(request):
    template_name = 'icons/flags.html'
    return render(request, template_name)


def font_awesome(request):
    template_name = 'icons/font-awesome.html'
    return render(request, template_name)


def simple_line_icons(request):
    template_name = 'icons/simple-line-icons.html'
    return render(request, template_name)


def alerts(request):
    template_name = 'notifications/alerts.html'
    return render(request, template_name)


def badge(request):
    template_name = 'notifications/badge.html'
    return render(request, template_name)


def modals(request):
    template_name = 'notifications/modals.html'
    return render(request, template_name)


def typography(request):
    template_name = 'typography.html'
    return render(request, template_name)


def widgets(request):
    template_name = 'widgets.html'
    return render(request, template_name)


def login(request):
    template_name = 'login.html'
    return render(request, template_name)


def register(request):
    template_name = 'register.html'
    return render(request, template_name)


def error404(request):
    template_name = '404.html'
    return render(request, template_name)


def error500(request):
    template_name = '500.html'
    return render(request, template_name)


def invoice(request):
    template_name = 'invoice.html'
    return render(request, template_name)
