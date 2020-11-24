from django.db import models

# Create your models here.


class BlogPost(models.Model):
    post_title = models.CharField(max_length=40)
    post_date = models.DateTimeField(auto_now=False)
    post_image = models.ImageField(upload_to='blog_post_images/')
    post_text = models.TextField()

    def get_summary(self):
        return self.post_text[:70]

    def __str__(self):
        return self.post_title
