from accounts.forms import UserLoginForm


def Login_User(request):
    login_form = UserLoginForm()   
    return {'login_form': login_form}