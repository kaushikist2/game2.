import random

def play_game():
    choices = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0

    print("✊📄✂️ Welcome to Rock Paper Scissors!")
    print("Type rock, paper, or scissors to play.")
    print("Type 'exit' to quit.\n")

    while True:
        user_choice = input("Your choice: ").lower()

        if user_choice == "exit":
            print("\n👋 Game Over!")
            print(f"Final Score → You: {user_score} | Computer: {computer_score}")
            break

        if user_choice not in choices:
            print("⚠️ Invalid choice. Try again.\n")
            continue

        computer_choice = random.choice(choices)
        print(f"🤖 Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("😐 It's a tie!\n")
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "paper" and computer_choice == "rock") or
            (user_choice == "scissors" and computer_choice == "paper")
        ):
            print("🎉 You win this round!\n")
            user_score += 1
        else:
            print("💀 Computer wins this round!\n")
            computer_score += 1

if __name__ == "__main__":
    play_game()
