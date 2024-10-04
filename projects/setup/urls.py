from django.urls import path
from . import views
from django.contrib.auth.models import User
urlpatterns = [
    path('setup/', views.setup_view, name='setup_view'),
]

def setup_view(request):
    global_preferences = global_preferences_registry.manager()

    if request.method == 'POST':
        form = SetupForm(request.POST, request.FILES)
        if form.is_valid():
            global_preferences['setup__app_name'] = form.cleaned_data['app_name']
            global_preferences['setup__is_setup_complete'] = True
            global_preferences['setup__app_logo'] = form.cleaned_data['app_logo']
            global_preferences['setup__app_favicon'] = form.cleaned_data['app_favicon']

            # Create admin user
            User.objects.create_superuser(
                # username=form.cleaned_data['admin_username'],
                email=form.cleaned_data['admin_email'],
                password=form.cleaned_data['admin_password']
            )

            return redirect('/')  # Redirect to some view after setup
    else:
        initial_data = {
            'app_name': global_preferences['setup__app_name'],
            'is_setup_complete': global_preferences['setup__is_setup_complete'],
        }
        form = SetupForm(initial=initial_data)

    context = {'form': form}
    return render(request, 'setup.html', context)

