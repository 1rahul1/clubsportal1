from django.contrib import admin
from .models import *


admin.site.register(CustomUser)
admin.site.register(ExistingClub)
admin.site.register(ProposedClub)
admin.site.register(ClubMember)

