from django.contrib import admin
from bookmark.models import Bookmark

# Register your models here.
#관리자 페이지에서 볼 모델(DB 모델)을 정의한다

# 1. 관리자 페이지에서 볼 템플릿에 대한 클래스 생성
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'create_date', 'modify_date')

# 2. 관리자 페이지에서 보여줄 DB 펨플릿에 등록한다
admin.site.register(Bookmark, BookmarkAdmin)