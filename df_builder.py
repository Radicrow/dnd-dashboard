import requests
import pandas as pd

monster_api = requests.get('https://www.dnd5eapi.co/api/monsters/')

monsters = monster_api.json()['results']

monster_stats = []
print(monsters)
for monster in monsters:

    monster_url = requests.get(f"https://www.dnd5eapi.co{monster['url']}")
    monster_data = monster_url.json()

    armor_class_value = monster_data.get("armor_class")
    if isinstance(armor_class_value, list):
        armor_class_value = armor_class_value[0].get("value", "N/A")

    monster_stats.append({
        "Name": monster_data.get("name"),
        "Size": monster_data.get("size"),
        "Alignment": monster_data.get("alignment"),
        "Challenge Rating": monster_data.get("challenge_rating"),
        "Proficiency Bonus": monster_data.get("proficiency_bonus"),
        "XP": monster_data.get("xp"),
        "Type": monster_data.get("type"),
        "Hit Points": monster_data.get("hit_points"),
        "Armor Class": armor_class_value,
        "Strength": monster_data.get("strength"),
        "Dexterity": monster_data.get("dexterity"),
        "Constitution": monster_data.get("constitution"),
        "Intelligence": monster_data.get("intelligence"),
        "Wisdom": monster_data.get("wisdom"),
        "Charisma": monster_data.get("charisma"),
        "Damage Vulnerabilities": monster_data.get("damage_vulnerabilities"),
        "Damage Immunities": monster_data.get("damage_immunities"),
        "Damage Resistances": monster_data.get("damage_resistances"),
        "Languages": monster_data.get("languages"),
        })

    print(f"{monster_data.get('name')} adicionado a database.")

monster_df = pd.DataFrame(monster_stats)

monster_df.to_csv('dnd_monsters.csv', index=False)

print("Arquivo .CSV criado com sucesso!!")
