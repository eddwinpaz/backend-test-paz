import json

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

# External Architecture
from core.decoratos import login_required, admin_required
from core.tasks import send_slack_message, send_whatsapp_message
from menu.forms import MenuAddForm
from menu.repository.repository_django_orm import Repository
from menu.usecases.usecase import UseCase


@login_required
@admin_required
def getAll(request):
    template = loader.get_template('menus.html')

    repository = Repository()
    use_case = UseCase(repository)
    result = use_case.getAll()

    message = "Hello here is today's menu\n"
    for r in result:
        message += "-- {} {} \n".format(r.name, r.uuid)
    send_slack_message(message)

    context = {
        'menu_list': result,
    }
    return HttpResponse(template.render(context, request))


def getById(request, menuId):
    template = loader.get_template('menu_view.html')

    repository = Repository()
    use_case = UseCase(repository)
    result = use_case.getById(menuId)

    context = {
        'menu': result,
    }
    return HttpResponse(template.render(context, request))


def getTodayMenu(request):
    template = loader.get_template('menu_today_list.html')

    repository = Repository()
    use_case = UseCase(repository)
    exp_hour = 11
    result = use_case.getTodayMenu(exp_hour)

    context = {'menu_list': result}
    return HttpResponse(template.render(context, request))


@admin_required
@login_required
def addMenu(request):
    template = loader.get_template('menu_new.html')

    form = MenuAddForm(request.POST)
    # string_date = form.cleaned_data.get('expiration_date')
    # form_date.strftime("%d %b, %Y - %Ih%Mm%S %p")

    if form.is_valid():
        repository = Repository()
        use_case = UseCase(repository)
        saved = use_case.add(form.cleaned_data.get('name'),
                             form.cleaned_data.get('description'),
                             form.cleaned_data.get('expiration_date'),
                             )

        if saved:
            context = {
                'saved': True,
                'form': form,
            }
            return HttpResponse(template.render(context, request))
        else:
            context = {
                'saved': False,
                'form': form,
            }
            return HttpResponse(template.render(context, request))
    else:

        context = {
            'form': MenuAddForm(),
        }
        return HttpResponse(template.render(context, request))


@admin_required
@login_required
def updateMenu(request, menuId):
    template = loader.get_template('menu_update.html')

    repository = Repository()
    use_case = UseCase(repository)
    menu = use_case.getById(menuId)

    if menu is None:
        return HttpResponseRedirect("/menu/")

    form = MenuAddForm(request.POST)

    if form.is_valid():

        saved = use_case.update(menuId,
                                form.cleaned_data.get('name'),
                                form.cleaned_data.get('description'),
                                form.cleaned_data.get('expiration_date'),
                                )

        if saved:

            menu = use_case.getById(menuId)

            context = {
                'saved': True,
                'form': form,
                'menu': menu,
            }
            return HttpResponse(template.render(context, request))
        else:
            context = {
                'saved': False,
                'form': form,
                'menu': menu,
            }
            return HttpResponse(template.render(context, request))
    else:

        context = {
            'form': MenuAddForm(),
            'menu': menu,
        }
        return HttpResponse(template.render(context, request))


@admin_required
@login_required
def deleteMenu(request, menuId):
    repository = Repository()
    use_case = UseCase(repository)
    use_case.delete(menuId)
    return HttpResponseRedirect("/menu/")


@admin_required
@login_required
def broadcast_whatsapp_menu(request):
    repository = Repository()
    use_case = UseCase(repository)
    exp_hour = 11
    result = use_case.getTodayMenu(exp_hour)
    client_phone_list = use_case.clientsPhoneBook()

    message = "Hello! \n"
    message += "I share with you today's menu \n"

    if len(result) > 0 and len(client_phone_list) > 0:
        # Build message
        for item in result:
            message += "-- {}".format(item.name)
        # Broadcast each whatsapp phone number
        for client in client_phone_list:
            send_whatsapp_message(fromPhone="whatsapp:+56933375029",
                                  toPhone="whatsapp:{}".format(client.phone),
                                  message=message)
