from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    '''
        Post モデル
    '''
    # 他のモデルへのリンク
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # 文字列が制限されているフィールド
    title = models.CharField(max_length=200)
    # 文字数制限なしのフィールド
    text = models.TextField()
    # 日付と時間
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title
