import psutil
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from io import BytesIO


if chat_message.body.strip().lower() == "battery":
            battery = psutil.sensors_battery()
            percent = battery.percent
            power_plugged = battery.power_plugged
            plugged = "Plugged In" if power_plugged else "Not Plugged In"
            message = f"Battery level: {percent}% ({plugged})"
    
            # Create a bar chart of the battery level
            fig, ax = plt.subplots()
            ax.bar(['Battery'], [percent])
            ax.set_ylim(0, 100)
            ax.set_ylabel('Battery Level (%)')
            ax.set_title('Battery Status')
            buffer = BytesIO()
            plt.savefig(buffer, format='png')
    
            # Send the message and image to the group chat
            buffer.seek(0)
            image_data = buffer.getvalue()
            self.client.send_chat_message(chat_message.group_jid, message)
            self.client.send_chat_image(chat_message.group_jid, image_data)
