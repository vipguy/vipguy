if chat_message.body.lower().startswith("monkey"):
            response = requests.get('https://source.unsplash.com/1600x900/?monkey').content
            image_file_name = 'monkey_image.jpg'
            with open(image_file_name, 'wb') as f:
                f.write(response)
            self.client.send_chat_message(chat_message.group_jid, "Here's a random monkey image!")
            self.client.send_chat_image(chat_message.group_jid, image_file_name)
            time.sleep(5)
            os.remove(image_file_name)

        
        if chat_message.body.lower().startswith("cat"):
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
        
        
        
        
        if chat_message.body.lower().startswith("duck"):
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
        
       
        if chat_message.body.lower().startswith("panda"):
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

        if chat_message.body.lower().startswith("dog"):
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

        elif chat_message.body.lower().startswith("fox"):
            # retrieve a random fox image
            response = requests.get('https://some-random-api.ml/img/fox').json()
            image_url = response['link']
            image_file_name = 'fox_image.jpg'
            response = requests.get(image_url)
            with open(image_file_name, 'wb') as f:
                f.write(response.content)
        
            # send the image
            self.client.send_chat_message(chat_message.group_jid, "Here's a random fox image!")
            self.client.send_chat_image(chat_message.group_jid, image_file_name)
    
            # generate and send a random fox fact
            fox_facts = [
                "Foxes have excellent hearing and can even hear low-frequency sounds that are inaudible to humans!",
                "Foxes are incredibly adaptable and can be found in a wide range of habitats, from forests to cities.",
                "A group of foxes is called a 'skulk' or a 'leash'.",
                "Foxes have a unique communication style that involves a variety of vocalizations, body language, and scent marking.",
                "Foxes have vertically oriented pupils that help them see in low light.",
                "The scientific name for the red fox is Vulpes vulpes.",
                "Foxes have a keen sense of smell and can detect prey buried under snow or leaves.",
                "Foxes are solitary animals and typically only come together during mating season.",
                "Foxes are omnivores and will eat a variety of foods, including small mammals, birds, insects, and berries.",
                "In some cultures, foxes are seen as symbols of cunning and trickery."
            ]
    
            random_fox_fact = random.choice(fox_facts)
            self.client.send_chat_message(chat_message.group_jid, random_fox_fact)
    
            # wait 5 seconds and then remove the image file
            time.sleep(5)
            os.remove(image_file_name)
    
        elif chat_message.body.lower().startswith("kangaroo"):
            # retrieve a random fact
            response = requests.get('https://some-random-api.ml/animal/kangaroo').json()
            fact = response['fact']
    
            # retrieve a random image
            response = requests.get('https://some-random-api.ml/animal/kangaroo').json()
            image_url = response['image']
            image_file_name = 'kangaroo_image.jpg'
            response = requests.get(image_url)
            with open(image_file_name, 'wb') as f:
                f.write(response.content)
        
            # send the fact and the image
            self.client.send_chat_message(chat_message.group_jid, f"Here's a random kangaroo fact: {fact}")
            self.client.send_chat_image(chat_message.group_jid, image_file_name)
            time.sleep(5)
            os.remove(image_file_name)
    
        elif chat_message.body.lower().startswith("wolf"):
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
