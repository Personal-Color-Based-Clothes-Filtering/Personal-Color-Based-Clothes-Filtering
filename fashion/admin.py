from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Collar
from .models import Hoodie
from .models import Longsleeve
from .models import Shirt
from .models import Shortsleeve
from .models import Sleeveless
from .models import Sweat
from .models import Sweater

admin.site.register(Collar)
admin.site.register(Hoodie)
admin.site.register(Longsleeve)
admin.site.register(Shirt)
admin.site.register(Shortsleeve)
admin.site.register(Sleeveless)
admin.site.register(Sweat)
admin.site.register(Sweater)

# 업로드
