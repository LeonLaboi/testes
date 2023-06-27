import uuid
from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Scan(BaseModel):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)

    last_run = models.DateTimeField(null=True, blank=True)
    auto_run = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Result(BaseModel):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)

    scan = models.ForeignKey('Scan', on_delete=models.CASCADE)

    BAR_SIZE_CHOICES = (
        ('tick', 'Tick'),
        ('minute', 'Minute'),
    )
    bar_size = models.CharField(max_length=16, choices=BAR_SIZE_CHOICES, default='minute')

    def __str__(self):
        return str(self.name)
