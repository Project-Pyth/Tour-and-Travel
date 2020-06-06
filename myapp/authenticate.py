from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend


class EmailBackend(ModelBackend):
    def authenticate(self,request,username,password):
        try:
            user = User.objects.get(email=username)
            sucess = user.check_password(password)
            if sucess:
                if user.check_password(password):
                    return user
        except:
            pass
        return None