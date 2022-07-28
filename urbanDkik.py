import json

import requests

#URBAN DICTIONARY
        if chat_message.body.lower() == ("ud"):
            word = chat_message.body[3:].replace(' ', '+')
            response = requests.get(f"http://api.urbandictionary.com/v0/define?term={word}")
        
            most_thumbs = -1
            best_definition = ""
            for definition in json.loads(response.text)['list']:
                if definition['thumbs_up']>most_thumbs:
                    most_thumbs = definition['thumbs_up']
                    best_definition = definition['definition']
                    self.client.send_chat_message(chat_message.group_jid,(f"{word}: {best_definition}"))
# get all list item 
            
            
# get index 0 of list


# get index 0 - word of list

