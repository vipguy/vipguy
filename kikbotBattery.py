import psutil
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from io import BytesIO


if chat_message.body.strip().lower() == "battery":  # Check if the chat message is asking for battery info
            battery = psutil.sensors_battery()  # Get the battery information using the psutil library
            percent = battery.percent  # Get the battery percentage
            power_plugged = battery.power_plugged  # Check if the power is plugged in or not
            plugged = "Plugged In" if power_plugged else "Not Plugged In"  # Set the "plugged" variable based on the power plugged status
            message = f"Battery level: {percent}% ({plugged})"  # Create a message with the battery percentage and power status
    
            # Create a bar chart of the battery level using matplotlib
            fig, ax = plt.subplots()
            ax.bar(['Battery'], [percent])
            ax.set_ylim(0, 100)
            ax.set_ylabel('Battery Level (%)')
            ax.set_title('Battery Status')
            buffer = BytesIO()
            plt.savefig(buffer, format='png')  # Save the bar chart as a PNG image in a BytesIO buffer
    
            # Send the message and image to the group chat
            buffer.seek(0)
            image_data = buffer.getvalue()
            self.client.send_chat_message(chat_message.group_jid, message)  # Send the battery info message to the group chat
            self.client.send_chat_image(chat_message.group_jid, image_data)  # Send the bar chart image to the group chat
