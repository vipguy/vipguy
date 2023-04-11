emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)


if chat_message.body.lower().startswith('copy'):
    message_text = chat_message.body[5:].strip()  # extract the message after "copy" and remove leading/trailing whitespaces
    message_text = emoji_pattern.sub(r'\g<0> ', message_text)  # add a space between consecutive emojis
    self.client.send_chat_message(chat_message.group_jid, message_text)
       
