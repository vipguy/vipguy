#LOCAL BOT BATTERY LVL #
#import psutil


if ("battery"== chat_message.body.lower()):
            battery_detecting = psutil.sensors_battery()
            plugged = battery_detecting.power_plugged
            percent_battery = str(battery_detecting.percent)
            plugged = "Plugged In" if plugged else "Not Plugged In"
            self.client.send_chat_message(chat_message.group_jid,f"{(percent_battery+'% | '+plugged)}")
