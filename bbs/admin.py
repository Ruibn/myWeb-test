from django.contrib import admin
from bbs import models


class BbsAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary', 'author', 'signature', 'view_count', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'author__user__username')

    def signature(self, obj):
        return obj.author.signature
    signature.short_description = 'hash'


admin.site.register(models.BBS, BbsAdmin)
admin.site.register(models.Category)
admin.site.register(models.BBS_user)
