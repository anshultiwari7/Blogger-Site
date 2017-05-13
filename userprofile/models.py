from django.db import models


class user(models.Model):
    # userid = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    type = models.CharField(max_length=1)
    def __str__(self):
        return (self.name)

class blog2(models.Model):
    title = models.CharField(max_length=500)
    content = models.CharField(max_length=5000)
    created = models.DateTimeField(auto_now_add=False)
    modified = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id)

class blog1(models.Model):
    author_id = models.ForeignKey(user,on_delete=models.CASCADE)
    blog_id = models.ForeignKey(blog2,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.blog_id)