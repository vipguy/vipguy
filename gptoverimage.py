if chat_message.body.lower().startswith("ai"):
            # Generate a response using OpenAI API
            completions = openai.Completion.create(
                engine="text-davinci-003",
                prompt=chat_message.body.lower() + "\n",
                max_tokens=100,
                temperature=0.5,
                stop="stop!",
            )
            response = completions.choices[0].text.strip()

            # Load a random image
            image_paths = ['images/ai.jpeg', 'images/ai2.jpeg']
            image_path = random.choice(image_paths)
            image = Image.open(image_path)
            draw = ImageDraw.Draw(image)
            font = ImageFont.truetype("arial.ttf", 70)

            # Add response to image
            message_parts = []
            max_width = 25
            words = response.split()
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
            y = 20
            draw.text((x, y), message, font=font, fill=(255, 255, 255))
            image.save("ai_response.jpg")
