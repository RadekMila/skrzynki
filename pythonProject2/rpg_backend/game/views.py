from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Character, Monster, Item
from .serializers import CharacterSerializer, MonsterSerializer, ItemSerializer
import random


class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

class MonsterViewSet(viewsets.ModelViewSet):
    queryset = Monster.objects.all()
    serializer_class = MonsterSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


def play_page(request, character_id):
    return render(request, "game/play.html", {"character_id": character_id})


@api_view(['GET', 'POST'])
def play_game_api(request, character_id):
    character = get_object_or_404(Character, id=character_id)
    battle_text = ""
    game_over = False
    monster_data = request.session.get("current_monster")

    if not monster_data:
        available_monsters = Monster.objects.filter(min_experience_required__lte=character.experience)
        if not available_monsters.exists():
            available_monsters = Monster.objects.all()
        monster = random.choice(available_monsters)
        monster_data = {
            "id": monster.id,
            "name": monster.name,
            "health": monster.health,
            "attack": monster.attack,
            "experience_reward": getattr(monster, "experience_reward", 50)
        }
        request.session["current_monster"] = monster_data


    if request.method == "POST":
        action = request.data.get("action")

        if character.health <= 0:
            battle_text = "Nie możesz walczyć — Twoja przygoda dobiegła końca! ⚰️"
            game_over = True

        elif action == "attack":
            monster_data["health"] -= character.strength
            if monster_data["health"] <= 0:
                battle_text = f"Pokonałeś {monster_data['name']}! Zdobywasz {monster_data['experience_reward']} expa!"
                character.experience += monster_data["experience_reward"]
                request.session.pop("current_monster", None)
            else:
                character.health -= monster_data["attack"]
                battle_text = f"Zadajesz {character.strength} obrażeń. {monster_data['name']} zadaje {monster_data['attack']} obrażeń!"

            if character.health <= 0:
                character.health = 0
                game_over = True
                battle_text += " 💀 Zostałeś pokonany!"

            character.save()
            if monster_data["health"] > 0:
                request.session["current_monster"] = monster_data

        elif action == "potion":
            if character.mana >= 10:
                character.mana -= 10
                character.health += 10
                if character.health > character.max_health:
                    character.health = character.max_health
                battle_text = "Użyłeś mikstury! +10 HP, -10 many."
                character.save()
            else:
                battle_text = "Masz za mało many!"

        elif action == "new":
            if character.health <= 0:
                battle_text = "Nie możesz przywołać nowego potwora, jesteś martwy. ⚰️"
                game_over = True
            else:
                request.session.pop("current_monster", None)
                available_monsters = Monster.objects.filter(min_experience_required__lte=character.experience)
                if not available_monsters.exists():
                    available_monsters = Monster.objects.all()
                monster = random.choice(available_monsters)
                monster_data = {
                    "id": monster.id,
                    "name": monster.name,
                    "health": monster.health,
                    "attack": monster.attack,
                    "experience_reward": getattr(monster, "experience_reward", 50)
                }
                request.session["current_monster"] = monster_data
                battle_text = f"Nowy potwór: {monster_data['name']} pojawił się!"


    return Response({
        "character": CharacterSerializer(character).data,
        "monster": monster_data,
        "message": battle_text,
        "game_over": game_over,
        "stats": {
            "character_attack": character.strength,
            "monster_attack": monster_data["attack"] if monster_data else 0
        }
    })

