from django.db import models

# Create your models here.


class Kid(models.Model):
    class Meta:
        verbose_name = 'شرکت کننده'
        verbose_name_plural = 'شرکت کنندگان'

    GENDER = (
        ('1', 'پسر'),
        ('2', 'دختر'),
    )

    codmeli = models.CharField(max_length=10 ,blank=False, null=False, verbose_name='کد ملی')    
    phone = models.CharField(max_length=11, blank=False, null=False, verbose_name='تلفن همراه')
    name = models.CharField(max_length=20, blank=False, null=False, verbose_name='نام')
    lastname = models.CharField(max_length=20, blank=False, null=False, verbose_name='نام خانوادگی')
    age  = models.IntegerField(null=False, blank=False, verbose_name='سن')
    gender = models.CharField(choices=GENDER,max_length=6,null=False, blank=False, verbose_name='جنسیت')

    def __str__(self):
        return f'{self.codmeli} | {self.name}  {self.lastname} | {self.age} | {self.get_gender_display()} | {self.phone}'
    