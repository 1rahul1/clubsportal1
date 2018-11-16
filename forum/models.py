from django.db import models
# from registration.models import Users
# from propose_join.models import ExistingClub

# Create your models here.
# class Question(models.Model):
#     creater = models.ForeignKey(Users,on_delete=models.CASCADE,related_name="")
#     in_club = models.ForeignKey(Clubs,on_delete=models.CASCADE,related_name="")
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     text_content = models.TextField()
#     image = models.FilePathField()
#     video = models.FilePathField()
#
# class Answer(models.Model):
#     answer_to = models.ForeignKey(Question,on_delete=models.CASCADE,related_name="")
#     creater = models.ForeignKey(Users,on_delete=models.CASCADE,related_name="")
#     in_club = models.ForeignKey(Clubs,on_delete=models.CASCADE,related_name="")
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     text_content = models.TextField()
#     image = models.FilePathField()
#     video = models.FilePathField()
#
# class Comments(models.Model):
#     comment_to = models.ForeignKey(Answer,on_delete=models.CASCADE,related_name="")
#     creater = models.ForeignKey(Users,on_delete=models.CASCADE,related_name="")
#     in_club = models.ForeignKey(Clubs,on_delete=models.CASCADE,related_name="")
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     text_content = models.TextField()
#     image = models.FilePathField()
#     video = models.FilePathField()
