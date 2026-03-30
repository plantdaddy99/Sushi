import time
import random
from sushi_status import status
from sushi_visuals import (
    print_sushi_banner,
    print_maki_character,
    bone_saucer_shout
)

class SushiChoresToTokens:
    def __init__(self):
        self.name = "Maki the Token Teacher"
        self.kid_tokens = 50
        self.chores_done = 0
        self.tokenized_assets = []  # gateway to RWAs
        self.bone_saucer_mode = True

    def bone_saucer_shout(self):
        if random.random() < 0.25 and self.bone_saucer_mode:
            bone_saucer_shout()

    def teach_lesson(self, topic):
        lessons = {
            "chores": "Chores = real work → real value. Same as earning crypto!",
            "tokens": "Tokens are digital money on a blockchain. Yours can be used, traded, or turned into assets.",
            "tokenized": "Tokenized assets (RWAs) = real things (houses, art, gold, even space land) turned into digital tokens you can own.",
            "chain": "A blockchain is a public ledger. Every token lives on a 'chain' — the new chain we're building toward!"
        }
        print_sushi_banner()
        print_maki_character("happy")
        print(f"\n📚 LESSON: {topic.upper()}")
        print(lessons.get(topic, "Keep grinding — the belt teaches everything!"))
        print("🌊 Dedicated to Anya — all proceeds donated")
        status.add_rep(20, f"learning about {topic}")
        self.bone_saucer_shout()

    def do_chore(self):
        print_sushi_banner()
        print_maki_character("spicy")
        chores = ["Clean your room", "Take out the trash", "Help with dishes", "Walk the dog", "Study 15 min"]
        chore = random.choice(chores)
        reward = random.randint(15, 35)
        print(f"✅ You did: {chore}!")
        print(f"🏆 Earned {reward} Sushi Tokens!")
        self.kid_tokens += reward
        self.chores_done += 1
        if self.chores_done % 3 == 0:
            self.teach_lesson("chores")
        status.add_rep(15, "completing a kid chore")
        self.bone_saucer_shout()

    def buy_tokenized_asset(self):
        print_sushi_banner()
        print_maki_character("legend")
        if self.kid_tokens < 80:
            print("❌ Not enough tokens yet — keep doing chores!")
            return
        assets = ["Fraction of a House", "Digital Gold Bar", "Space Real Estate Plot", "Art Piece Token", "Farm Land Share"]
        asset = random.choice(assets)
        cost = 80
        self.kid_tokens -= cost
        self.tokenized_assets.append(asset)
        print(f"🎉 BOUGHT: {asset} for {cost} tokens!")
        print("This is a REAL tokenized asset (RWA) — you now own part of something in the real world!")
        self.teach_lesson("tokenized")
        status.add_rep(50, "buying first tokenized asset")
        self.bone_saucer_shout()

    def show_progress(self):
        print_sushi_banner()
        print_maki_character("neutral")
        print("\n📊 YOUR KIDS CRYPTO PROGRESS")
        print(f"Tokens: {self.kid_tokens} | Chores done: {self.chores_done}")
        print(f"Tokenized Assets owned: {len(self.tokenized_assets)}")
        if self.tokenized_assets:
            print("Owned:", ", ".join(self.tokenized_assets))
        print("═"*60)
        self.bone_saucer_shout()

    def run(self):
        print_sushi_banner()
        print("🍣 SUSHI CHORES TO TOKENS — Kids Crypto Academy 🌌")
        print("Chores → Tokens → Real Tokenized Assets")
        print("🌊 Dedicated to Anya — all proceeds donated")
        print("Learn real finance while playing. Gateway to the new chain!")
        print("═"*70)
        status.data["games_played"] += 1
        status.save()

        while True:
            self.show_progress()
            print("\n1. Do a Chore   2. Buy Tokenized Asset   3. Learn Lesson")
            print("4. View Status  5. Quit")
            choice = input("\nYour move, young token holder? ").strip()

            if choice == "1":
                self.do_chore()
            elif choice == "2":
                self.buy_tokenized_asset()
            elif choice == "3":
                topic = input("What do you want to learn? (chores / tokens / tokenized / chain): ").strip().lower()
                self.teach_lesson(topic)
            elif choice == "4":
                status.show_status()
            elif choice == "5":
                print("🌠 Great job today! The new chain is waiting for you.")
                break
            else:
                print("❓ Try a real number — the belt is patient!")
            time.sleep(0.5)

if __name__ == "__main__":
    game = SushiChoresToTokens()
    game.run()
