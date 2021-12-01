import json
import csv


with open('Vulnerabilities.csv', newline='') as newCsvfile:
    newVulnerabilities = csv.reader(newCsvfile)
    for newVulnerability in newVulnerabilities:
        with open('OldVulnerabilities.csv', newline='') as oldCsvfile:
            oldVulnerabilities = csv.reader(oldCsvfile)
            if newVulnerability in oldVulnerabilities:
                with open('CommonVulnerabilities.csv', 'w', newline='') as commonFile:
                    commonWriter = csv.writer(commonFile)
                    commonWriter.writerow(newVulnerability)
                    commonFile.close()
            else:
                with open('AddedVulnerabilities.csv', 'w', newline='') as newFile:
                    newWriter = csv.writer(newFile)
                    newWriter.writerow(newVulnerability)
                    newFile.close()
            oldCsvfile.close()
    newCsvfile.close()
