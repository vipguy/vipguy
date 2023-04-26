 if is_user_admin(chat_message.from_jid, chat_message.group_jid):
            is_admin = True
            is_superadmin = False
        else:
            is_admin = False
            is_superadmin = False


         ##########################################
        #Enable variable answring captca 
        ##########################################
        
        prefix = "/"
        if is_admin:
            commands = {
                "enable captcha": (enable_captcha, "Captchas enabled."),
                "disable captcha": (disable_captcha, "Captchas disabled.")
            }
            command = commands.get(chat_message.body.lower())
            if command:
                function, response = command
                function(chat_message.group_jid)
                self.client.send_chat_message(chat_message.group_jid, response)
        ##########################################
        #Censoring words commands
        ##########################################
        
        if is_admin:
            commands = {
                "censor": (censor, "Now censoring '{arg}'"),
                "uncensor": (uncensor, "Uncensored '{arg}'")
            }
            for cmd, (function, response) in commands.items():
                if chat_message.body.lower().startswith(prefix + cmd + " "):
                    arg = chat_message.body[len(prefix + cmd + " "):]
                    function(chat_message.group_jid, arg)
                    self.client.send_chat_message(chat_message.group_jid, response.format(arg=arg))


         ##########################################
        #Delete trigers
        ##########################################        

        if chat_message.body.lower().startswith(prefix):
            command = chat_message.body.lower()[len(prefix):].strip()
            censored = []
            triggers = []
            response = ""
            if command.startswith("censor "):
                censor(chat_message.group_jid, command[7:])
                response = f"Now censoring '{command[7:]}'"
            elif command.startswith("uncensor "):
                uncensor(chat_message.group_jid, command[9:])
                response = f"Uncensored '{command[9:]}'"
            elif command.startswith("delete "):
                remove_trigger(chat_message.group_jid, command[7:])
                response = 'Trigger deleted!'
            elif command == "censored":
                censored = get_censored(chat_message.group_jid)
                if censored:
                    response = "[Censored Words]\n" + " \ ".join(censored)[-2048:]
                else:
                    response = "No words censored!"
            elif command == "triggers":
                triggers = get_triggers(chat_message.group_jid)
                if triggers:
                    response = "[Saved Triggers]\n" + " \ ".join(triggers)[-2048:]
                else:
                    response = "No triggers saved!"
            self.client.send_chat_message(chat_message.group_jid, response)



        
         ##########################################
        #Lock Group commands
        ##########################################
        if is_admin:
            commands = {
                "lock": (toggle_group_lock, "Group locked!"),
                "unlock": (toggle_group_lock, "Group unlocked!")
            }
            command = commands.get(chat_message.body.lower().replace(prefix, ''))
            if command:
                function, response = command
                arg = "True" if chat_message.body.lower().startswith(prefix+"lock") else "False"
                function(chat_message.group_jid, arg)
                self.client.send_chat_message(chat_message.group_jid, response)
