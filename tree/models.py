from django.core.exceptions import ValidationError
from django.db import models


class TreeMenu(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class TreeItem(models.Model):
    name = models.CharField(max_length=80)
    menu = models.ForeignKey(TreeMenu, on_delete=models.CASCADE, related_name='tree_items', blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='childrens', blank=True, null=True)

    def __str__(self):
        return self.name

    def clean(self):
        menu = bool(self.menu)
        parent = bool(self.parent)

        if not ((not menu and parent) or (menu and not parent)):
            raise ValidationError({
                'menu': 'Only one of "menu" and "parent" must be filled.'
            })
