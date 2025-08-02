from datetime import datetime

current_time = datetime.now()
timestamp = current_time.timestamp()

print(f'Seconds since January 1, 1970: {timestamp:,.4f} or {timestamp:.2e} in scientific notation')
print(current_time.strftime('%b %d %Y'))