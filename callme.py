        if chat_message.body.lower().startswith("call me "):
            newname = mssg.replace("call me ", "")
            split_string = newname.split(":", 0)
            self.client.send_chat_message(chat_message.group_jid, "Ok, {}".format(newname))
            Database("data.db").given_name(newname, chat_message.group_jid, chat_message.from_jid)
        
        
        elif mssg == 'hey vip' or mssg == 'hi':
            newname = Database("data.db").get_given_name(chat_message.group_jid, chat_message.from_jid)
            newname = '' if newname is None else newname
            self.client.send_chat_message(chat_message.group_jid, "Hello {}".format(newname))
