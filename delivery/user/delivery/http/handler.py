from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
import hashlib

# External Architecture
from core.decoratos import login_required, admin_required
from user.forms import AuthForm, CreateForm
from user.repository.repository_django_orm import Repository
from user.usecases.usecase import UseCase


@csrf_exempt
def create(request):
    template = loader.get_template('new_user.html')
    form = CreateForm(request.POST)

    if form.is_valid():

        repository = Repository()
        use_case = UseCase(repository)

        password = form.cleaned_data.get('password').encode('utf8')
        encrypted_password = hashlib.sha1(password).hexdigest()

        result = use_case.create(form.cleaned_data.get('name'),
                                 form.cleaned_data.get('phone'),
                                 form.cleaned_data.get('email'),
                                 encrypted_password)

        context = {
            'saved': result,
            'form': form,
        }
        return HttpResponse(template.render(context, request))
    else:
        context = {
            'form': CreateForm(),
        }
        return HttpResponse(template.render(context, request))


@csrf_exempt
@login_required
@admin_required
def getAll(request):
    template = loader.get_template('users.html')

    repository = Repository()
    use_case = UseCase(repository)
    result = use_case.getAll()

    context = {
        'user_list': result,
    }
    return HttpResponse(template.render(context, request))


@csrf_exempt
@login_required
def getById(request, userId):
    template = loader.get_template('user_view.html')

    repository = Repository()
    use_case = UseCase(repository)
    result = use_case.getById(userId)

    context = {
        'user': result,
    }
    return HttpResponse(template.render(context, request))


@csrf_exempt
def authentication(request):
    template = loader.get_template('user_auth.html')
    form = AuthForm(request.POST)

    if form.is_valid():

        email = str(form.cleaned_data["email"]).lower()
        password = form.cleaned_data.get('password').encode('utf8')
        encrypted_password = hashlib.sha1(password).hexdigest()

        repository = Repository()
        use_case = UseCase(repository)
        user, error = use_case.authenticate(email, encrypted_password)

        if error is False:
            # Create Session
            request.session['userId'] = str(user.user_id)
            if user.admin:
                request.session['isAdmin'] = True

            response = redirect('/menu/today/')
            return response

        context = {
            'form': form,
            'error': True,
        }
        return HttpResponse(template.render(context, request))
    else:
        context = {
            'form': AuthForm(),
        }
        return HttpResponse(template.render(context, request))


@login_required
def logout(request):
    if "userId" in request.session.keys():
        del request.session['userId']

    if "isAdmin" in request.session.keys():
        del request.session['isAdmin']

    return redirect('/user/login/')
