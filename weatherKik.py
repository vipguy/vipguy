
##from bs4 import BeautifulSoup
import requests


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}           
        if chat_message.body.lower().startswith("weather"):
            city = chat_message.body.lower().split(maxsplit=1)[1]
            city=city+" weather"
            res = requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',headers=headers)
            soup = BeautifulSoup(res.text,'html.parser')   
            location = soup.select('#wob_loc')[0].getText().strip()  
            timezone = soup.select('#wob_dts')[0].getText().strip()       
            info = soup.select('#wob_dc')[0].getText().strip() 
            weather = soup.select('#wob_tm')[0].getText().strip()
            self.client.send_chat_message(chat_message.group_jid,f"{(location)} {(timezone)}")
        
            self.client.send_chat_message(chat_message.group_jid,f"{(info)} {(weather)}°C")
            celsius = float(weather)
            

            # calculate fahrenheit
            fahrenheit = (celsius * 1.8) + 32
            self.client.send_chat_message(chat_message.group_jid,('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius,fahrenheit)))
