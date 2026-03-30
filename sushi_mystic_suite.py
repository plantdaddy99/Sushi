import time
import random
from sushi_status import status
from sushi_visuals import (          # ← NEW: using the official visuals
    print_sushi_banner,
    print_maki_character,
    print_tarot_card,
    bone_saucer_shout
)

class SushiMysticSuite:
    def __init__(self):
        self.name = "Maki the Mystic Roll"
        self.bone_saucer_mode = True

    def bone_saucer_shout(self):
        if random.random() < 0.25 and self.bone_saucer_mode:
            bone_saucer_shout()   # now using the shared visual shout

    def astrology_reading(self):
        print_sushi_banner()
        print_maki_character("spicy")
        print("\n🌌 WASABI CONSTELLATIONS — Sushi Astrology")
        signs = ["Spicy Tuna", "Avocado Dreamer", "Salmon Warrior", "Wasabi Mystic", "Ginger Joker", "Rice Sage"]
        sign = random.choice(signs)
        print(f"Your current star: {sign}")
        print("The Great Conveyor Belt aligns in your favor today.")
        status.add_rep(25, "wasabi astrology reading")
        self.bone_saucer_shout()

    def tarot_reading(self):
        print_sushi_banner()
        print_maki_character("legend")
        print("\n🃏 TAROT BY MAKI — 3-Card Sushi Spread")
        deck = [
            "The Spicy Fool", "The Rice Empress", "The Wasabi Tower",
            "The Salmon Chariot", "The Avocado Lovers", "The Nigiri Hermit"
        ]
        spread = [random.choice(deck) for _ in range(3)]
        for i, card in enumerate(["Past", "Present", "Future"]):
            print_tarot_card(f"{card}: {spread[i]}")
        print("Karen-style wisdom: The cards speak through the rice.")
        status.add_rep(40, "tarot by maki 3-card spread")
        self.bone_saucer_shout()

    def numerology_reading(self):
        print_sushi_banner()
        print_maki_character()
        print("\n🔢 NUMEROLOGY + GEMATRIA — Sushi Soul Math")
        name = input("Enter your name (or any word): ").strip().upper()
        value = sum((ord(c) - 64) % 26 or 26 for c in name if c.isalpha())
        life_path = value % 9 or 9
        print(f"Name Gematria: {value} → reduces to {life_path}")
        print("Tau Math Note: This number vibrates with the sacred conveyor geometry.")
        status.add_rep(35, "sushi numerology & language science")
        self.bone_saucer_shout()

    def iching_reading(self):
        print_sushi_banner()
        print_maki_character("neutral")
        print("\n☯️  I CHING — Tao of the Conveyor Belt")
        print("Toss 3 coins 6 times (simulated)...")
        time.sleep(1.5)
        hexagram = random.randint(1, 64)
        print(f"Hexagram #{hexagram}")
        print("Wisdom: The belt teaches patience and flow.")
        status.add_rep(45, "I Ching tao math consultation")
        self.bone_saucer_shout()

    def tau_math_science(self):
        print_sushi_banner()
        print_maki_character("happy")
        print("\n📐 TAU MATH + LANGUAGE + SCIENCE — Sacred Wasabi Field")
        pattern = random.choice(["Golden Ratio Roll", "Fibonacci Conveyor", "Wasabi Wave Function"])
        print(f"Current pattern: {pattern}")
        print("Science note: Your rep is entangled with the entire Sushi Society.")
        status.add_rep(30, "tau math language science insight")
        self.bone_saucer_shout()

    def open_mystic_mode(self):
        print_sushi_banner()
        print_maki_character("legend")
        print("\n🌟 OPEN MYSTIC MODE — Ask the Belt Anything")
        question = input("What mystical question burns in your rice? ").strip()
        answers = [
            "The Guardian of the Best Salmon smiles upon you.",
            "Bone & Saucer energy says: keep rolling.",
            "Futstat squad + Gotchi pet = cosmic team-up incoming."
        ]
        print(f"The Conveyor Belt replies: {random.choice(answers)}")
        status.add_rep(50, "open mystic oracle")
        self.bone_saucer_shout()

    def run(self):
        print_sushi_banner()
        print("🍣 SUSHI MYSTIC SUITE — Full Tarot-by-Maki Oracle Belt 🌌")
        print("🌊 Dedicated to Anya — all proceeds donated")
        print("═"*70)
        status.data["games_played"] += 1
        status.save()

        while True:
            print("\n1. Astrology   2. Tarot (3-Card)   3. Numerology + Gematria")
            print("4. I Ching     5. Tau Math/Science  6. Open Mystic Mode")
            print("7. View Status 8. Quit")
            choice = input("\nChoose your oracle, Mystic Roll: ").strip()

            if choice == "1": self.astrology_reading()
            elif choice == "2": self.tarot_reading()
            elif choice == "3": self.numerology_reading()
            elif choice == "4": self.iching_reading()
            elif choice == "5": self.tau_math_science()
            elif choice == "6": self.open_mystic_mode()
            elif choice == "7": status.show_status()
            elif choice == "8":
                print("🌠 The mystic belt thanks you… return anytime, legend.")
                break
            else:
                print("❓ The stars are confused — pick a real number!")
            time.sleep(0.5)

if __name__ == "__main__":
    game = SushiMysticSuite()
    game.run()
