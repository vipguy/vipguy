if message == ("groupname"):
     is_admin  #admin
     icon =''
     vip = str(message.replace("groupname ", ""))
     self.client.change_group_name(chat_message.group_jid,chat_message.body.split(" ",maxsplit=1)[1])
     self.client.send_chat_message(chat_message.group_jid, icon,"Changing Group Name".format(vip))
