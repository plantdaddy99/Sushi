import random

# =============================================
# SUSHI VISUALS — Official Text Image Language
# Consistent ASCII + emoji + pixel style for ALL games
# 🌊 Dedicated to Anya — all proceeds donated
# =============================================

def print_sushi_banner():
    """Big header image for every game"""
    print("\n" + "═"*70)
    print("🍣🌊 SUSHI SOCIETY — WASABI ISLAND DREAM REALM 🌊🍣")
    print("The Great Conveyor Belt spins for Anya")
    print("═"*70)

def print_maki_character(mood="neutral"):
    """Maki the Mystic Roll — reusable character art"""
    art = {
        "neutral": "🧭 (🍣‿🍣) 🧭",
        "happy":  "🧭 (🍣‿🍣)✧ 🧭",
        "spicy":  "🧭 (🌶️🍣🌶️) 🧭",
        "legend": "🧭 ᕕ(🍣‿🍣)ᕗ💎 🧭",
        "sad":    "🧭 (🍣﹏🍣) 🧭"
    }
    print(art.get(mood, art["neutral"]))

def print_wasabi_map(size=6, player_pos=(2,2), guardian_pos=(5,5)):
    """Pixel-style map used in Awakening / any exploration game"""
    print("\n🌊 WASABI ISLAND — DREAM MAP 🌊")
    for y in range(size):
        row = "║ "
        for x in range(size):
            if (x, y) == player_pos:
                row += "🧭 "
            elif (x, y) == guardian_pos:
                row += "👑 "
            else:
                row += random.choice(["🍣 ", "🌿 ", "❓ "])
        row += "║"
        print(row)
    print("═"*40)

def print_tarot_card(card_name):
    """Tarot-by-Maki style card visual"""
    print(f"\n🃏 {card_name}")
    print("━━━━━━━━━━━━━━━━━━")
    print("   🍣  🌊  🍣")
    print("━━━━━━━━━━━━━━━━━━")

def print_gotchi_pet(happiness=80):
    """Reusable pet art for sushi_gotchi (or any pet game)"""
    if happiness > 70:
        print("🐾 (🍣‿🍣)✧ 🐾  ← LEGEND ROLL")
    elif happiness > 40:
        print("🐾 (🍣‿🍣) 🐾")
    else:
        print("🐾 (🍣﹏🍣) 🐾  ← needs love")

def print_howlbox_soundwave():
    """HowlBox Sound Studio visual (ready for audio integration)"""
    print("\n🎵 HOWLBOX SOUND STUDIO — WASABI WAVES 🎵")
    print("🌊 \~ \~ \~ \~ \~ \~ \~ \~ \~ \~ \~ \~ \~ \~ \~ \~ 🌊")
    print("   🔊 Bone & Saucer approved audio belt spinning...")

def bone_saucer_shout():
    """Occasional Bone & Saucer visual shout"""
    if random.random() < 0.3:
        print("🍣🔥 Bone & Saucer approved — this visual hits different! 🌊")

# 🌊 Dedicated to Anya — all proceeds donated
