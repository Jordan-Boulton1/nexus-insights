from django.db import models

class ChampionData(models.Model):
    key = models.IntegerField(unique=True)
    id = models.CharField(max_length=100, primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    lore = models.TextField()
    image_url = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class SkinData(models.Model):
    champion = models.ForeignKey(ChampionData, related_name="skins", on_delete=models.CASCADE)
    skin_id = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.name} ({self.champion.name})"


class SpellData(models.Model):
    champion = models.ForeignKey(ChampionData, related_name="spells", on_delete=models.CASCADE)
    spell_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField()
    tooltip = models.TextField(null=True, blank=True)
    image_url = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} ({self.champion.name})"