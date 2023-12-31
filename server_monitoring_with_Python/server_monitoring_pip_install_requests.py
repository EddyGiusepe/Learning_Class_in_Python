"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Aqui aprenderemos a MONITORAR SERVIÇOS. 
Para isso seguimos o exemplo de "IQDotNet Code"
"""
import requests
import json
import time
import logging

# Vamos usar cores:
GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m' # Restabelecer a cor

# Setup o logging para escrever o arquivo e também para printar no terminal:
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                               logging.FileHandler('server_monitor.log'),
                               logging.StreamHandler()
                             ]
                    )

def load_configuration(config_file):
    with open(config_file, 'r') as file:
        return json.load(file)
    

def check_servers(server_list):
    statuses = {}
    for server in server_list:
        try:
            response = requests.get(server, timeout=5)
            if response.status_code == 200:
                status = "Online"
                logging.info(f"{server}: {GREEN}{status}{RESET}")
            else:
                status = "Problems detected"
                logging.info(f"{server}: {RED}{status}{RESET}")
            statuses[server] = status

        except requests.ConnectionError:
            logging.error(f"{server}: {RED}Offline{RESET}")
            statuses[server] = 'Offline'
        except Exception as e:
            logging.error(f"{server}: {RED}Error - {e}{RESET}")
            statuses[server] = f'Error: {e}'
    return statuses


def main():
    config = load_configuration("config.json")
    servers = config["servers"]

    while True:
        logging.info("Starting server check.")
        server_statuses = check_servers(servers)

        logging.info("Waiting 60 seconds for the next check . . . \n")
        time.sleep(60)




if __name__ == "__main__":
    main()
