if chat_message.body.lower() == "random monkey":
            monkey_image_url = "https://www.placemonkeys.com/500?random"  # 500 is the width, height is automatically adjusted
            # Download the monkey image and save it temporarily
            image_response = requests.get(monkey_image_url)
            if image_response.status_code == 200:
                temp_image_path = 'temp_monkey_image.jpg'
                with open(temp_image_path, 'wb') as image_file:
                    image_file.write(image_response.content)

                # Send the image in the chat
                self.client.send_chat_image(chat_message.group_jid, temp_image_path)

                # Delete the temporary image file
                os.remove(temp_image_path)
            else:
                self.client.send_chat_message(chat_message.group_jid, "Failed to retrieve monkey image.")

        elif chat_message.body.lower() == "monkey":
            response = requests.get('https://source.unsplash.com/1600x900/?monkey').content
            image_file_name = 'monkey_image.jpg'
            with open(image_file_name, 'wb') as f:
                f.write(response)
            self.client.send_chat_message(chat_message.group_jid, "Here's a random monkey image!")
            self.client.send_chat_image(chat_message.group_jid, image_file_name)
            time.sleep(5)
            os.remove(image_file_name)

        elif chat_message.body.lower() == "cat":
            response = requests.get('https://api.thecatapi.com/v1/images/search').json()
            image_url = response[0].get('url')
            image_file_name = 'cat_image.jpg'
            response = requests.get(image_url)
            with open(image_file_name, 'wb') as f:
                f.write(response.content)
            self.client.send_chat_message(chat_message.group_jid, "Here's a random cat image!")
            self.client.send_chat_image(chat_message.group_jid, image_file_name)
            time.sleep(5)
            os.remove(image_file_name)
        
        elif chat_message.body.lower() == "duck":
            response = requests.get('https://random-d.uk/api/v2/random').json()
            image_url = response['url']
            image_file_name = 'duck_image.jpg'
            response = requests.get(image_url)
            with open(image_file_name, 'wb') as f:
                f.write(response.content)
            self.client.send_chat_message(chat_message.group_jid, "Here's a random duck image!")
            self.client.send_chat_image(chat_message.group_jid, image_file_name)
            time.sleep(5)
            os.remove(image_file_name)
        
        elif chat_message.body.lower() == "panda":
            response = requests.get('https://some-random-api.ml/img/panda').json()
            image_url = response['link']
            image_file_name = 'panda_image.jpg'
            response = requests.get(image_url)
            with open(image_file_name, 'wb') as f:
                f.write(response.content)
            self.client.send_chat_message(chat_message.group_jid, "Here's a random panda image!")
            self.client.send_chat_image(chat_message.group_jid, image_file_name)
            time.sleep(5)
            os.remove(image_file_name)

        elif chat_message.body.lower() == "dog":
            response = requests.get('https://dog.ceo/api/breeds/image/random').json()
            image_url = response.get('message')
            image_file_name = 'dog_image.jpg'
            response = requests.get(image_url)
            with open(image_file_name, 'wb') as f:
                f.write(response.content)
            self.client.send_chat_message(chat_message.group_jid, "Here's a random dog image!")
            self.client.send_chat_image(chat_message.group_jid, image_file_name)
            time.sleep(5)
            os.remove(image_file_name)

        elif chat_message.body.lower() == "wolf":
    # retrieve a random wolf image
            response = requests.get('https://source.unsplash.com/random/800x600/?wolf')
            image_file_name = 'wolf_image.jpg'
            with open(image_file_name, 'wb') as f:
                f.write(response.content)
        
    # define 10 random facts about wolves
            facts = [
                "Wolves are the largest members of the dog family.",
                "Wolves can run up to 40 miles per hour.",
                "Wolves have excellent hearing and can hear sounds up to 6 miles away.",
                "Wolves are social animals that live in packs.",
                "Wolves can communicate with each other using howls, whines, and barks.",
                "Wolves mate for life and usually have a litter of 4-6 pups.",
                "Wolves have powerful jaws that can exert up to 1,500 pounds of pressure per square inch.",
                "Wolves play an important role in maintaining healthy ecosystems by controlling prey populations.",
                "Wolves are often misunderstood and feared, but they rarely pose a threat to humans.",
                "Wolves have been a part of human mythology and folklore for thousands of years."
            ]
    
    # choose a random fact from the list
            fact = random.choice(facts)
    
    # send the image and the fact
            self.client.send_chat_message(chat_message.group_jid, "Here's a random wolf image!")
            self.client.send_chat_image(chat_message.group_jid, image_file_name)
            self.client.send_chat_message(chat_message.group_jid, f"Did you know? {fact}")
            time.sleep(5)
            os.remove(image_file_name)

        elif chat_message.body.lower() == "random fox":
            url = "https://randomfox.ca/floof/"
            response = requests.get(url).json()
            fox_image_url = response['image']

            # Download the image and save it temporarily
            image_response = requests.get(fox_image_url)
            if image_response.status_code == 200:
                # Save the image temporarily
                temp_image_path = 'temp_fox_image.jpg'
                with open(temp_image_path, 'wb') as image_file:
                    image_file.write(image_response.content)

                # Send the image in the chat
                self.client.send_chat_image(chat_message.group_jid, temp_image_path)

                # Delete the temporary image file
                os.remove(temp_image_path)
            else:
                self.client.send_chat_message(chat_message.group_jid, "Failed to retrieve fox image.")
