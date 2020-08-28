from django.db import models
from django.urls import reverse


class Blog(models.Model):
    title = models.CharField("Название", max_length=120)
    text = models.TextField("Текст")
    file = models.ImageField("Изображение", 
                            upload_to="blog_detail_image/", 
                            default="blog_detail_image.jpg")
    created = models.DateTimeField("Добавлен", auto_now_add=True)

    def get_absolute_url(self):
        return reverse('blog_detail',args=[self.pk])

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ['-created']
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
