with open('csaidinput.txt', 'r') as f:
    alert_ids = f.read().splitlines()

with open('csaidoutput.txt', 'w') as f:
    f.write(','.join(alert_ids))
