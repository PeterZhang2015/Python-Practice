import json
import csv

with open('Vulnerabilities.json') as f:
  data = json.load(f)

vulnerabilities = data["ScanResult"]["vulnerabilities"]
print(vulnerabilities)

with open('Vulnerabilities.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    startingRow = 2

    for vulnerability in vulnerabilities:
        writer.writerow(["landslide", "landslide/landslide", "LS_20_2_0_GA ", vulnerability["id"], vulnerability["severity"], "", "", data["ScanResult"]["generated_at"], vulnerability["description"]])
