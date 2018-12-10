from django.db import models


class User(models.Model):
    username = models.CharField(max_length=12, unique=True)
    password = models.CharField(max_length=12)
    create_time = models.TimeField(auto_now_add=True)

    class Meta:
        db_table = 'user'


class AType(models.Model):
    types = models.CharField(max_length=10)
    f_typeid = models.IntegerField(null=True)

    class Meta:
        db_table = 'article_type'


class Article(models.Model):
    title = models.CharField(max_length=30, null=False)
    types = models.ForeignKey(AType, null=False, on_delete=models.CASCADE)
    desc = models.CharField(max_length=100, null=True)
    content = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    icon = models.ImageField(upload_to='article', null=True)
    is_show = models.BooleanField(default=0)

    class Meta:
        db_table = 'article'



