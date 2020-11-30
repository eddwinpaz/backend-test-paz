from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import loader

from core.decoratos import login_required, admin_required
from order.forms import OrderCreateForm

# External Architecture
from order.repository.repository_django_orm import Repository
from order.usecases.usecase import UseCase


# This will allow users non admin to create menu orders


@csrf_exempt
@login_required
def placeOrder(request, menuId):
    template = loader.get_template('order_new.html')
    form = OrderCreateForm(request.POST)
    userId = request.session['userId']

    repository = Repository()
    use_case = UseCase(repository)
    menu = use_case.getMenuNameById(menuId)

    if form.is_valid():

        result = use_case.createOrder(userId,
                                      menuId,
                                      form.cleaned_data.get('customization'),
                                      )

        context = {
            'saved': result,
            'menu': menu,
            'form': form,
        }
        return HttpResponse(template.render(context, request))
    else:
        context = {
            'form': OrderCreateForm(),
            'menu': menu,
        }
        return HttpResponse(template.render(context, request))


# this will get all users in general, for Nora to
# see how to build and deliver food


@login_required
@admin_required
def getAll(request):
    template = loader.get_template('orders.html')

    repository = Repository()
    use_case = UseCase(repository)
    result = use_case.getAll()

    context = {
        'order_list': result,
    }
    return HttpResponse(template.render(context, request))


# this will return single order information by orderId


@login_required
def getById(request, orderId):
    template = loader.get_template('order_view.html')
    user_id = request.session.get('userId')

    repository = Repository()
    use_case = UseCase(repository)
    result = use_case.getById(orderId, user_id)

    context = {
        'order': result,
    }
    return HttpResponse(template.render(context, request))


@login_required
def getAllById(request):
    template = loader.get_template('orders.html')
    user_id = request.session.get('userId')

    repository = Repository()
    use_case = UseCase(repository)
    result = use_case.getAllById(user_id)

    context = {
        'order_list': result,
        'user': user_id,
    }
    return HttpResponse(template.render(context, request))
