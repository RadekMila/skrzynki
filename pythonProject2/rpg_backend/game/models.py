from django.db import models


class Character(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField(default=1)
    experience = models.IntegerField(default=0)
    health = models.IntegerField(default=100)
    max_health = models.IntegerField(default=100)
    mana = models.IntegerField(default=50)
    strength = models.IntegerField(default=0)
    agility = models.IntegerField(default=0)
    intelligence = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} (Lvl {self.level})"

class Monster(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField(default=1)
    health = models.IntegerField(default=50)
    attack = models.IntegerField(default=5)
    min_experience_required = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} (Lv {self.level})"

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    power = models.IntegerField(default=0)
    value = models.IntegerField(default=10)

    owner = models.ForeignKey(
        'Character',
        related_name='items',

        on_delete=models.CASCADE,

        null=True, blank=True
    )

    def __str__(self):
        return self.name