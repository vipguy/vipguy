
with open("jokes.json","r",encoding="utf8") as f:
    jokes = json.load(f)





#CHUCK J
        if chat_message.body.lower() == "jokes":
            fp = open("jokes.json")
            jokes = (json.load(fp)['value'])
            rand = random.randint(1,len(jokes))
            self.client.send_chat_message(chat_message.group_jid, jokes[rand-1]['joke'])
