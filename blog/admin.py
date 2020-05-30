from django.contrib import admin
from blog.models import Post

# Register your models here.
# 1.관리자 페이지에서 볼 템플릿에 대한 클래스 생성
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'description', 'create_date', 'modify_date')

# 2.관리자 페이지에서 보여줄 DB 템플릿을 등록한다.
admin.site.register(Post, PostAdmin)
