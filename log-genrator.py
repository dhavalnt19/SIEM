# CREATING 100000 LOGS VIA SCRIPT FOR PRAQCTICING THE KQL LANGUAGE 
#python3
# pip install faker


import csv
import random
from datetime import datetime, timedelta
from faker import Faker

fake = Faker()

operations = [
    "MICROSOFT.COMPUTE/VIRTUALMACHINES/START/ACTION",
    "MICROSOFT.COMPUTE/VIRTUALMACHINES/DELETE",
    "MICROSOFT.NETWORK/NETWORKSECURITYGROUPS/WRITE",
    "MICROSOFT.KEYVAULT/VAULTS/DELETE",
    "MICROSOFT.STORAGE/STORAGEACCOUNTS/WRITE",
    "MICROSOFT.RESOURCES/DEPLOYMENTS/WRITE",
    "MICROSOFT.INSIGHTS/DIAGNOSTICSETTINGS/WRITE",
    "MICROSOFT.AUTHORIZATION/ROLEASSIGNMENTS/WRITE",
    "MICROSOFT.COMPUTE/VIRTUALMACHINES/RESTART/ACTION",
    "MICROSOFT.NETWORK/PUBLICIPADDRESSES/DELETE"
]

levels = ["Informational", "Warning", "Error"]
status = ["Succeeded", "Failed"]
users = [
    "admin@company.com",
    "security@company.com",
    "devops@company.com",
    "attacker@evil.com",
    "intern@company.com"
]

resources = [
    "VM-Prod01",
    "VM-Test01",
    "Storage-Prod",
    "KeyVault01",
    "NSG-Web",
    "VNET-Prod"
]

with open("AzureActivity.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([
        "TimeGenerated",
        "Caller",
        "OperationNameValue",
        "Resource",
        "ActivityStatusValue",
        "Level",
        "IPAddress"
    ])

    start = datetime.now() - timedelta(days=30)

    for _ in range(100000):

        start += timedelta(seconds=random.randint(1,120))

        writer.writerow([
            start.isoformat(),
            random.choice(users),
            random.choice(operations),
            random.choice(resources),
            random.choice(status),
            random.choice(levels),
            fake.ipv4_public()
        ])

print("Finished generating 100000 Azure Activity Logs.")
