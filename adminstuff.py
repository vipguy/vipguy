if is_admin:
            cmd = chat_message.body.lower().split(' ')
            if cmd[0] == 'ban':
                user = cmd[1]
                self.client.send_chat_message(chat_message.group_jid, f"Attempting to ban \"{user}\" from the group...")
                jid = self.client.get_jid(user)
                if jid:
                    self.client.ban_member_from_group(chat_message.group_jid, jid)
                    self.client.send_chat_message(chat_message.group_jid, "User has been banned")
                else:
                    self.client.send_chat_message(chat_message.group_jid, "Ban did not work")

            elif cmd[0] == 'unban':
                user = cmd[1]
                self.client.send_chat_message(chat_message.group_jid, f"Attempting to unban \"{user}\" from the group...")
                jid = self.client.get_jid(user)
                if jid:
                    self.client.unban_member_from_group(chat_message.group_jid, jid)
                    self.client.send_chat_message(chat_message.group_jid, "User has been unbanned")
                else:
                    self.client.send_chat_message(chat_message.group_jid, "Unban did not work")

            elif cmd[0] == 'add':
                user = cmd[1]
                self.client.send_chat_message(chat_message.group_jid, f"Attempting to add \"{user}\" to the group...")
                jid = self.client.get_jid(user)
                if jid:
                    self.client.add_peer_to_group(chat_message.group_jid, jid)
                    self.client.send_chat_message(chat_message.group_jid, "User has been added")
                else:
                    self.client.send_chat_message(chat_message.group_jid, "Add attempt failed")

            elif cmd[0] == 'remove':
                user = cmd[1]
                self.client.send_chat_message(chat_message.group_jid, f"Attempting to remove \"{user}\" from the group...")
                jid = self.client.get_jid(user)
                if jid:
                    self.client.remove_peer_from_group(chat_message.group_jid, jid)
                    self.client.send_chat_message(chat_message.group_jid, "User has been removed")
                else:
                    self.client.send_chat_message(chat_message.group_jid, "Remove attempt failed")

            elif cmd[0] == 'promote':
                user = cmd[1]
                self.client.send_chat_message(chat_message.group_jid, f"Attempting to promote \"{user}\" ...")
                jid = self.client.get_jid(user)
                if jid:
                    self.client.promote_to_admin(chat_message.group_jid, jid)
                    self.client.send_chat_message(chat_message.group_jid, "User has been promoted to admin")
                else:
                    self.client.send_chat_message(chat_message.group_jid, "Promotion attempt failed")
