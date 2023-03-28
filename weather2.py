headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'} 
        if chat_message.body.lower().startswith("tempnow "):
            city = chat_message.body.lower().split(maxsplit=1)[1]
            city=city+" temp"
            res = requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',headers=headers)
            soup = BeautifulSoup(res.text,'html.parser')    
            timezone = soup.select('#wob_dts')[0].getText().strip()       
            info = soup.select('#wob_dc')[0].getText().strip() 
            weather = soup.select('#wob_tm')[0].getText().strip()
            self.client.send_chat_message(chat_message.group_jid,("Please wait, fetching the weather."))
            if weather <= str(32):
                image_path = 'images/under32.png'
            elif weather <= str(50):
                image_path = 'images/under50.png'
            elif weather <= str(67):
                image_path = 'images/over67.png'
            elif weather <= str(79):
                image_path = 'images/over79.png'
            else:
                image_path = 'images/over80.png'
            image = Image.open(image_path)
            draw = ImageDraw.Draw(image)
            font = ImageFont.truetype("arial.ttf", 70)
            celsius = float(weather)
            # calculate fahrenheit
            fahrenheit = (celsius * 1.8) + 32
            message_parts = [f"{(timezone)}"]
            if timezone is not None:
                message_parts.append(f"{(info)}  {(weather)}°C")
            if fahrenheit is not None:
                message_parts.append(f"{(fahrenheit)}°f")
            message = "\n".join(message_parts)
            text_width, text_height = draw.textsize(message, font)
            x = (image.width - text_width) / 2
            y = (image.height - text_height) / 1.5
            draw.text((x, y), message, font=font, fill=(255, 0, 0))
            image.save("weather.png")
            self.client.send_chat_image(chat_message.group_jid, "weather.png")
            
            #self.client.send_chat_message(chat_message.group_jid,('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius,fahrenheit)))
       
        
