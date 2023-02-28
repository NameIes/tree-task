from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class TreeMenu(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


def calculate_link(item):
    result = '/'
    while item.parent:
        result = '/' + str(item.id) + result
        item = item.parent

    return '/' + str(item.menu.id) + '/' + str(item.id) + result


class TreeItem(models.Model):
    name = models.CharField(max_length=80)
    link = models.CharField(max_length=250, blank=True, null=True, editable=False)
    menu = models.ForeignKey(TreeMenu, on_delete=models.CASCADE, related_name='childrens', blank=True, null=True)
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


@receiver(post_save, sender=TreeItem)
def treeitem_set_link(sender, instance, **kwargs):
    instance.link = calculate_link(instance)
    post_save.disconnect(treeitem_set_link, sender=TreeItem)
    instance.save()
    post_save.connect(treeitem_set_link, sender=TreeItem)
