if chat_message.body.lower().startswith("chuck"):
    # Get a Chuck Norris joke
            url = "https://api.chucknorris.io/jokes/random"
            response = requests.get(url)
            response_dict = response.json()
            joke = response_dict["value"]

    # Load image
            image_path = 'images\chuck7.jpeg'
            image = Image.open(image_path)
            draw = ImageDraw.Draw(image)
            font = ImageFont.truetype("arial.ttf", 70)

    # Add joke to image
            message_parts = []
            max_width = 25
            words = joke.split()
            line = ''
            for word in words:
                if len(line) + len(word) + 1 <= max_width:
                    line += word + ' '
                else:
                    message_parts.append(line)
                    line = word + ' '
            message_parts.append(line)
            message = '\n'.join(message_parts)
            text_width, text_height = draw.textsize(message, font=font)
            x = (image.width - text_width) / 2
            y = (image.height - text_height) / 2 + 50
            draw.text((x, y), message, font=font, fill=(255, 255, 255))
            image.save("chuck_norris_joke.jpg")
            self.client.send_chat_image(chat_message.group_jid, "chuck_norris_joke.jpg")
