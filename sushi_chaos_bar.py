import time
import random

class SushiChaosBar:
    def __init__(self):
        self.wellness_score = 100
        self.alien_ingredients = {
            "Neural Sticky Core": "sushi rice",
            "Void Shadow Veil": "nori seaweed",
            "Nebula Butter Slices": "avocado",
            "Aqua Snap Batons": "cucumber",
            "Sea Echo Flakes": "imitation crab",
            "Crimson Pulse Fin": "tuna",
            "Rose Dawn Sovereign": "salmon",
            "Golden Lightning Tail": "yellowtail",
            "Glazed Abyss Serpent": "eel",
            "Pink Tempest Prawn": "shrimp",
            "Armored Crunch Claw": "soft-shell crab tempura",
            "Sunrise Golden Silk": "tamago egg",
            "Velvet Dream Spread": "cream cheese",
            "Sinus Nova Blast": "wasabi",
            "Pink Palate Purifier": "pickled ginger",
            "Cosmic Pop Spheres": "fish roe",
            "Toasted Nebula Seeds": "sesame seeds",
            "Inferno Swirl Drizzle": "spicy mayo",
            "Emerald Tower Spears": "asparagus",
            "Golden Root Shards": "carrot",
            "Fire Ring Igniters": "jalapeño",
            "Sharp Green Blades": "green onion"
        }
        self.categories = {
            "Rice & Wrap Foundation": ["Neural Sticky Core", "Void Shadow Veil"],
            "Uramaki Dream Team": ["Nebula Butter Slices", "Aqua Snap Batons", "Sea Echo Flakes"],
            "Ocean Powerhouse": ["Crimson Pulse Fin", "Rose Dawn Sovereign", "Golden Lightning Tail", 
                                  "Glazed Abyss Serpent", "Pink Tempest Prawn", "Armored Crunch Claw"],
            "Sweet & Creamy Gems": ["Sunrise Golden Silk", "Velvet Dream Spread"],
            "Zing & Topper Squad": ["Sinus Nova Blast", "Pink Palate Purifier", "Cosmic Pop Spheres", 
                                    "Toasted Nebula Seeds", "Inferno Swirl Drizzle"],
            "Garden Crunch Crew": ["Emerald Tower Spears", "Golden Root Shards", "Fire Ring Igniters", "Sharp Green Blades"]
        }

    def grokko_chan_intro(self):
        print("\n" + "="*60)
        print("🌟 GROKKO-CHAN EXPLODES ONTO THE COUNTER 🌟")
        print("KYAAAAAAA\~!!! STOCK GUY-SENPAI IS HERE!!!")
        print("TIMER STARTS... NOW!!! ⏰ 60 SECONDS OF CHAOS!!!")
        print("="*60 + "\n")

    def serve_roll(self, chosen_aliens):
        print("\n🍣 **I SLAPPED THIS TOGETHER AS FAST AS I COULD...**")
        print("Ingredients I grabbed (they all feel the same to me):")
        for item in chosen_aliens:
            print(f"   • {item}")
        print("\nThe roll looks... weird. Alien. Kinda sticky on the outside, some shiny bits, some crunchy bits.")
        print("Taste test... everything just tastes like 'sushi-ish' but not the sushi I remember. Weird aftertaste.\n")

    def chef_reaction(self):
        if self.wellness_score < 60:
            print("😵‍💫 Chef (panicking): 'I... I have NO idea what I just made. This isn't right. Wellness dropping...'")
            self.wellness_score = max(0, self.wellness_score - 20)
        else:
            print("😎 Chef (trying to stay calm): 'I did the best with what I could. This has to be sushi... right?'")
        print(f"   Current Wellness Score: {self.wellness_score}/100\n")

    def grokko_chan_verdict(self, chosen_aliens):
        print("\n" + "="*60)
        print("GROKKO-CHAN POPS BACK IN!!!")
        real_roll = [self.alien_ingredients[a] for a in chosen_aliens]
        print("A REAL SUSHI ROLL HAS BEEN DISCOVERED!!!")
        print("Your alien combo translates to:")
        print(" → " + " + ".join(real_roll))
        print("\nThis actually makes a legit custom roll (no pre-made recipes — pure creation)!")
        if random.random() > 0.5:
            print("🎉 You did GREAT chef!!! We’re getting closer to the real sushi!!!")
        else:
            print("💥 You did great chef, we’ll get ‘em tomorrow!!!")
        print(f"   Wellness Score now: {self.wellness_score}/100")
        print("="*60 + "\n")

    def play_round(self):
        self.grokko_chan_intro()
        start_time = time.time()
        
        print("FRANTIC MODE ACTIVATED — throw me any combo of alien ingredients (space-separated)!")
        print("Example: Neural Sticky Core Void Shadow Veil Nebula Butter Slices Crimson Pulse Fin\n")
        
        user_input = input("Your frantic combo → ").strip()
        
        # Simulate timer ending even if you type fast
        elapsed = time.time() - start_time
        if elapsed < 60:
            print(f"⏰ Timer ran out after {int(elapsed)} seconds — sending whatever you gave me!")
        
        chosen = [item.strip() for item in user_input.split() if item.strip() in self.alien_ingredients]
        if not chosen:
            chosen = random.sample(list(self.alien_ingredients.keys()), 4)  # fallback
        
        self.serve_roll(chosen)
        self.chef_reaction()
        self.grokko_chan_verdict(chosen)

    def run(self):
        print("🍣 Grok's Alien Sushi Chaos Bar is NOW OPEN 🍣")
        print("Say the magic words to start a round!\n")
        
        while True:
            command = input("You: ").strip().lower()
            if "so what’s on the menu tonight" in command or "menu" in command:
                self.play_round()
            elif command == "quit" or command == "exit":
                print("GROKKO-CHAN: BYEEE\~!!! See you tomorrow for more chaos!!! ❤️")
                break
            else:
                print("GROKKO-CHAN (whisper): Just say the magic line when you're ready...")

if __name__ == "__main__":
    game = SushiChaosBar()
    game.run()
