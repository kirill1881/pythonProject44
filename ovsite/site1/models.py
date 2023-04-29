from django.db import models

class Task(models.Model):
    name = models.CharField('task_name', max_length=255)
    text = models.CharField('task_text', max_length=255)
    time = models.IntegerField('task_add_time')

    def info(self):
        print(f'{self.name}, {self.text}, {self.time}')