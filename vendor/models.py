from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Food(models.Model):
    image = models.ImageField(upload_to='static/images/%Y/%m/%d', verbose_name='mahsulot surati', blank=True)
    name = models.CharField(max_length=50, null=False, verbose_name='mahsulot nomi')
    price = models.DecimalField(max_digits=20, decimal_places=2,verbose_name='maxsulot narxi', db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created',)
        index_together = (('id'),)

    def __str__(self):
        return self.name
