# In admin.py
from django.contrib import admin
from .models import Login, Register, sellphone, iphone, samsung, Tecno, itel, google_pixel, huawei, opoo, redmi, sony

admin.site.register(Login)
admin.site.register(Register)
admin.site.register(sellphone)
admin.site.register(iphone)
admin.site.register(samsung)

admin.site.register(Tecno)
admin.site.register(itel)
admin.site.register(google_pixel)
admin.site.register(huawei)
admin.site.register(opoo)
admin.site.register(redmi)
admin.site.register(sony)






