from django.db import models

# Create your models here.

class Bookmark(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField('url', unique=True)
    create_date = models.DateTimeField('Create date',
                                       auto_now_add=True,
                                       blank=True, null=True)

    modify_date = models.DateTimeField('Modify Date',
                                       auto_now=True,
                                       blank=True,null=True)

    def __str__(self):
        return self.title # print로 출력시 title이 나오도록

# 1. model이 새롭게 정의하면
# 1-1. admin.py에서 model을 관리자 템플릿에 등록
# 1-2. python manage.py makemigrations을 실행
# 2. 실제로 이 정보로 DB를 실행하려면 python manage.py migrate을 실행
#   - migrations 폴더에 있는 파이썬 파일을 읽어서 DB를 생성한다
# 3. 서버를 실행해서 확인하기 위해 python manage.py runserver