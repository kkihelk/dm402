"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from mysite.views import IndexView
from bookmark.views import BookmarkLV, BookmarkDV
from blog.views import PostLV, PostDV

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls), # 기본적으로 관리자 페이지 url이 적혀있다
    url(r'^$', IndexView.as_view(), name='index'),

    url(r'^bookmark/$', BookmarkLV.as_view(), name="bookmark_index"),
    url(r'^bookmark/(?P<pk>\d+)$', BookmarkDV.as_view(), name="detail"),
    #PK는 Primary Key 객체간의 구분하는 일종의 id 장고에서 자동으로 숫자로 생성

    url(r'^blog/$', PostLV.as_view(), name='blog_index'),
    url(r'^blog/(?P<pk>\d+)$', PostDV.as_view(), name="blog_detail"),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)


# r'^$' 는 추가적으로 입력하지 않은 상태인 메인페이지
# url(url 주소 패턴, 관련된 views.py의 클래스.as_view(), name="html파일명")