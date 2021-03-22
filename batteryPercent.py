import psutil
battery = psutil.sensors_battery()
percent =str(battery.percent)

print('Your system has been running on '+ percent+'% battery')