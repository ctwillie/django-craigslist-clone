from django.db import models


class Search(models.Model):
    text = models.CharField(max_length=200)
    created_at = models.DateTimeField('searched on')

    def __str__(self):
        return self.text

    # def was_published_recently(self):
    #     now = timezone.now()
    #     return now - datetime.timedelta(days=1) <= self.pub_date <= now
