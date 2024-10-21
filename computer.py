import random

names = ["Erik", "Liam", "Johan", "Vilmer", "Alex", "Elton"]# type: ignore
computers =["Laptop 1", "Laptop 2", "PC1", "PC2", "MAC1"] # type: ignore
serviced_computers = []

service_computer = random.choice(computers)


serviced_computers.append(service_computer)

computers.remove(service_computer)

print(f"Computer being serviced: {service_computer}")
print(f"Serviced computers: {serviced_computers}")
print(f"Remaining computers: {computers}")