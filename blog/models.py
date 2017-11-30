from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
	'''
    Django 要求模型必须继承 models.Model 类
    Category 只需要一个简单的分类名 name 就可以了
    CharField 指定了分类名 name 的数据类型，CharField是字符串类型
    CharField 的 max_length 参数指定其最大长度，超过这个长度的name就不能写入数据库
    当然 Django 还为我们提供了多种其它的数据类型，如日期时间类型 DateTimeField、整数类型 IntegerField 等等。
    Django 内置的全部类型可查看文档：
    https://docs.djangoproject.com/en/1.10/ref/models/fields/#field-types
	'''
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
	'''
    标签Tag
    '''
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    """文章数据库"""
    # 文章标签
    title = models.CharField(max_length=70)

    # 文章正文。使用的是TextField类型
    # 存储比较短的字符串可以使用CharField，长的用TextField
    body = models.TextField()

    # 这两个列分别表示文章的创建时间和最后一次修改时间，存储时间的字段用 DateTimeField 类型。
    create_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    def __str__(self):
        return self.title

    # 自定义 get_absolute_url 方法
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    class Meta(object):
        ordering = ['-create_time']

    # 文章摘要，可以没有文章摘要，但默认情况下CharField要求我们必须存入数据，否则报错
    # 指定CharField的blank=True参数值后就可以允许空值了。
    excerpt = models.CharField(max_length=200, blank=True)

    # 我们规定一篇文章只能对应一个分类，但是一个分类下可以有多篇文章，所以我们使用的是 ForeignKey，即一对多的关联关系。
    # 而对于标签来说，一篇文章可以有多个标签，同一个标签下也可能有多篇文章，所以我们使用 ManyToManyField，表明这是多对多的关联关系。
    # 同时我们规定文章可以没有标签，因此为标签 tags 指定了 blank=True。
    # 如果你对 ForeignKey、ManyToManyField 不了解，请看教程中的解释，亦可参考官方文档：
    # https://docs.djangoproject.com/en/1.10/topics/db/models/#relationships
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)

    # 文章作者，这里 User 是从 django.contrib.auth.models 导入的。
    # django.contrib.auth 是 Django 内置的应用，专门用于处理网站用户的注册、登录等流程，User 是 Django 为我们已经写好的用户模型。
    # 这里我们通过 ForeignKey 把文章和 User 关联了起来。
    # 因为我们规定一篇文章只能有一个作者，而一个作者可能会写多篇文章，因此这是一对多的关联关系，和 Category 类似。
    author = models.ForeignKey(User)
