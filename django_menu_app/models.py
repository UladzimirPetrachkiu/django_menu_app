from django.db import models


class MenuItem(models.Model):
    """
    A model representing a menu item with a name, URL, and optional parent.
    """
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', null=True, blank=True)

    def __str__(self):
        """
        Return a string representation of the object.
        """
        return self.name
