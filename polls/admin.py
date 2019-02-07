from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':  ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes':['collapse']}),
        ]
    inlines = [ChoiceInline]
    # 后台选项list_display更改列表页中以列的形式展示这个对象
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


# 注册时增加新参数，注入类名
# 创建一个模型后台类，接着将其作为第二个参数传给 admin.site.register()
# ——在你需要修改模型的后台管理选项时这么做
admin.site.register(Question, QuestionAdmin)
