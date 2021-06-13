from django.db import models

# Create your models here.
class User(models.Model):
    gender = [
        ("m", "男"),
        ("f", "女")
    ]
    user_id= models.CharField(max_length=50, verbose_name="id",unique=True)
    name = models.CharField(max_length=50, verbose_name="姓名")
    gender = models.CharField(max_length=10, choices=gender, default='m', verbose_name="性别")
    email = models.EmailField(unique=True,verbose_name="邮箱")
    password = models.CharField(max_length=30, verbose_name="密码")
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s (%s)" % (self.id, self.name)

    class Meta:
            db_table = 'User'
            ordering = ['c_time']
            verbose_name = '用户'
            verbose_name_plural = '用户'

class Game(models.Model):
    id = models.AutoField(primary_key=True)
    owner_id = models.CharField(max_length=50, verbose_name="id")
    opponent_id = models.CharField(max_length=50, verbose_name="id",null=True, blank=True)
    owner_side= models.CharField(max_length=10, default="white")
    owner_online = models.BooleanField(default=False)
    opponent_online = models.BooleanField(default=False)
    fen = models.CharField(max_length=92, default="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
    pgn = models.TextField(null=True, blank=True)
    time = models.CharField(max_length=10,null=True, blank=True)
    winner = models.CharField(max_length=50, verbose_name="id",null=True, blank=True)
    CHOICES=(
        (1,"等待对手"),
        (2,"游戏开始"),
        (3,"游戏结束"))
    status = models.IntegerField(default=1,choices=CHOICES)