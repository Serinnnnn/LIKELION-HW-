from django.db import models
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()

    def __str__(self):
        return self.content

    #CASCADE 참조대상인 Post가 삭제되면, 해당 포스트 팜조하고 있던 comment 들도 따라서 삭제!
    