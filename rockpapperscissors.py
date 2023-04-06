if (chat_message.body.lower() == "🪨" or chat_message.body.lower() == "📃" or chat_message.body.lower() == "✂️"):
                possible_actions = ["🪨", "📃", "✂️"]
                computer_action = random.choice(possible_actions)
                self.client.send_chat_message(chat_message.group_jid, f"\nYou chose {chat_message.body.lower()}, computer chose {computer_action}.\n")
                if chat_message.body.lower() == computer_action:
                    self.client.send_chat_message(chat_message.group_jid, f"Both players selected {chat_message.body.lower()}. It's a tie!")
                elif chat_message.body.lower() == "🪨":
                    if computer_action == "✂️":
                        self.client.send_chat_message(chat_message.group_jid, "🪨 smashes ✂️! You win!")
                    else:
                        self.client.send_chat_message(chat_message.group_jid, "📃 covers 🪨! You lose.")
                elif chat_message.body.lower() == "📃":
                    if computer_action == "🪨":
                        self.client.send_chat_message(chat_message.group_jid, "📃 covers 🪨! You win!")
                    else:
                        self.client.send_chat_message(chat_message.group_jid, "✂️ cuts 📃! You lose.")
                elif chat_message.body.lower() == "✂️":
                    if computer_action == "📃":
                        self.client.send_chat_message(chat_message.group_jid, "✂️ cuts 📃! You win!")
                    else:
                        self.client.send_chat_message(chat_message.group_jid, "🪨 smashes ✂️! You lose.")
