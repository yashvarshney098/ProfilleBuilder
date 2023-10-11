
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# fields = list(UserAdmin.fieldsets)
# fields[0] = (None, {'fields': })
# UserAdmin.fieldsets = tuple(fields)
# admin.site.register(User, UserAdmin)

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm

class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User

class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('firstname','lastname','phone','gradyear','posprimary','possecondary','instagram','twitter','facebook','school','city','state','ncaa','height','weight','vertical','time40','gpa','actscore','classrank','satscore','url1','url2','sbp1','sbp2','sbp3','sbp4','abp1','abp2','abp3','abp4','s1date','s1event','s1location','s2date','s2event','s2location','s3date','s3event','s3location','coachmessage','profileimage')}),
    )


admin.site.register(User, MyUserAdmin)