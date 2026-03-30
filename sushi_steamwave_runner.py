import time
import random
from sushi_status import status
from sushi_visuals import (
    print_sushi_banner,
    print_maki_character,
    print_wasabi_map,
    bone_saucer_shout
)

class SushiSteamwaveRunner:
    def __init__(self):
        self.name = "Maki the Steamwave Phantom"
        self.speed = 0
        self.distance = 0
        self.aether_orbs = 0
        self.bone_saucer_mode = True

    def bone_saucer_shout(self):
        if random.random() < 0.25 and self.bone_saucer_mode:
            bone_saucer_shout()

    def teach_mystical_lesson(self):
        lessons = [
            "🌌 ASTRONOMY: The constellation 'Wasabi Orion' points to the Best Salmon & Rice Orbit.",
            "🧭 EXPLORATION: Victorian cyber explorers used brass sextants and quantum compasses.",
            "🔮 MYSTICAL: Every wave you ride carries echoes of the Great Conveyor Belt across dimensions.",
            "📡 REWARDED LEARNING: Collect Aether Orbs = unlock real knowledge about the stars."
        ]
        print_sushi_banner()
        print_maki_character("legend")
        print("\n📚 MYSTICAL LESSON UNLOCKED!")
        print(random.choice(lessons))
        print("🌊 Dedicated to Anya — all proceeds donated")
        status.add_rep(30, "rewarded mystical learning")
        self.bone_saucer_shout()

    def race_tick(self):
        self.distance += self.speed
        event = random.random()
        if event < 0.3:
            print("🌊 PERFECT WAVE — speed +2!")
            self.speed += 2
        elif event < 0.5:
            print("⚡ CYBER-GEAR GLITCH — speed -1!")
            self.speed = max(1, self.speed - 1)
        elif event < 0.7 and self.aether_orbs < 5:
            print("✨ AETHER ORB COLLECTED!")
            self.aether_orbs += 1
            if self.aether_orbs % 2 == 0:
                self.teach_mystical_lesson()
        else:
            print("🌀 Smooth Victorian cyber-wave...")

    def run(self):
        print_sushi_banner()
        print("🍣 SUSHI STEAMWAVE RUNNER — Cybernetic Victorian Wave Race 🌊")
        print("Ride the Ethereal Wasabi Waves in a brass-and-neon jet-ski!")
        print("Collect Aether Orbs → rewarded learning in astronomy, exploration, mysticism")
        print("🌊 Dedicated to Anya — all proceeds donated")
        print("═"*70)
        status.data["games_played"] += 1
        status.save()

        self.speed = 5
        self.distance = 0
        self.aether_orbs = 0

        while self.distance < 200:
            print_sushi_banner()
            print_maki_character("spicy")
            print(f"\n🌊 DISTANCE: {self.distance}/200 | SPEED: {self.speed} knots | Orbs: {self.aether_orbs}")
            print_wasabi_map(size=8, player_pos=(3, 3))  # pixel-style ocean map

            choice = input("\n1. BOOST (risky)  2. Steady Cruise  3. Mystic Dodge  4. Quit : ").strip()

            if choice == "1":
                self.speed += random.randint(3, 6)
                print("🚀 BRASS BOOST ENGAGED!")
            elif choice == "2":
                self.speed = max(3, self.speed - 1)
                print("🛠️ Victorian steady cruise...")
            elif choice == "3":
                print("🔮 MYSTICAL DODGE — you weave through nebula waves!")
                self.aether_orbs += 1
            elif choice == "4":
                print("🌠 You dock the Phantom… great run, captain.")
                break
            else:
                print("The waves wait for no one!")

            self.race_tick()
            self.bone_saucer_shout()
            time.sleep(0.6)

        print_sushi_banner()
        print_maki_character("legend")
        print(f"\n🏁 RACE COMPLETE! Total distance: {self.distance} | Orbs collected: {self.aether_orbs}")
        status.add_rep(60 + self.aether_orbs * 20, "finishing a cyber-Victorian wave run")
        if self.aether_orbs >= 4:
            print("🌟 ASTRONOMY/EXPLORATION MASTER UNLOCKED — you’re ready for the stars!")
        print("The Great Conveyor Belt honors your ride, legend.")

if __name__ == "__main__":
    game = SushiSteamwaveRunner()
    game.run()
