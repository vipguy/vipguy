#LOCAL BOT BATTERY LVL #
#import psutil


if chat_message.body.strip().lower() == "battery":
            battery = psutil.sensors_battery()
            percent = battery.percent
            power_plugged = battery.power_plugged
            plugged = "Plugged In" if power_plugged else "Not Plugged In"
            message = f"Battery level: {percent}% ({plugged})"
            self.client.send_chat_message(chat_message.group_jid, message)
