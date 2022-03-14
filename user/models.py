from django.db import models

class Usuario(models.Model):
    user_id = models.CharField(max_length=5)
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    user_password = models.CharField(max_length=20)

    class Meta:
        db_table = "usuario"