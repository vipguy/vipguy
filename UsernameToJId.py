#ADD USERNAME TH USERNAME.TXT IT WILL  AUTO CONVERT TO JID
        if '/n' in mssg:
            is_superadmin
            f, l = mssg.split('/n', maxsplit=1)
            responses[f.lower().strip()] = l.strip()
            self.client.get_jid(username)
            self.client.send_chat_message(chat_message.group_jid, f'{f}JIdUserNames:{l}')
            black = open('usernames.txt', 'a')
            rom = chat_message.body.split('/n')[0]
            self.client.send_chat_message(chat_message.from_jid, f"{f} was added to the database").format(rom)
            for rom in mssg.lower().split(maxsplit=1)[1].split(","):
                black.write(self.client.get_jid(rom))
                black.write('\n')
            black.close() 
