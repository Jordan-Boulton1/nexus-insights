import os
import json
from champions.models import ChampionData, SkinData, SpellData

# Path to the folder containing individual champion JSON files
champion_folder = r'D:\Nexus Insights\data\league\dragontail-14.23.1\14.23.1\data\en_GB\champion'

# Loop through each JSON file in the directory
for filename in os.listdir(champion_folder):
    if filename.endswith('.json'):  # Ensure it's a JSON file
        file_path = os.path.join(champion_folder, filename)

        # Open and parse the JSON file
        with open(file_path, 'r', encoding='utf-8') as file:
            champ_data = json.load(file)

        # Extract champion data
        champ_info = champ_data['data'][list(champ_data['data'].keys())[0]]

        # Use update_or_create to handle duplicates
        champion, created = ChampionData.objects.update_or_create(
            id=champ_info['id'],  # Use the unique identifier for the champion
            defaults={
                'key': int(champ_info['key']),
                'name': champ_info['name'],
                'title': champ_info['title'],
                'lore': champ_info.get('lore', ''),
                'image_url': f"http://ddragon.leagueoflegends.com/cdn/14.23.1/img/champion/{champ_info['image']['full']}",
            }
        )

        # Add skins
        for skin in champ_info.get('skins', []):
            SkinData.objects.update_or_create(
                champion=champion,
                skin_id=skin['id'],
                defaults={
                    'name': skin['name'],
                }
            )

        # Add spells
        for spell in champ_info.get('spells', []):
            SpellData.objects.update_or_create(
                champion=champion,
                spell_id=spell['id'],
                defaults={
                    'name': spell['name'],
                    'description': spell['description'],
                    'tooltip': spell.get('tooltip', ''),
                    'image_url': f"http://ddragon.leagueoflegends.com/cdn/14.23.1/img/spell/{spell['image']['full']}",
                }
            )

print("All champions have been processed successfully!")
