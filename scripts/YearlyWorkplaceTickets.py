############################################################################################################################
##                                                                                                                        ##
##  Created     :   12.02.2024                                                                             By : SCHB      ##
##                                                                                                                        ##
##  Name        :   YearlyWorkpaceTickets.py                                                                              ##
##                                                                                                                        ##
##  Description :   export tickets in a csv file                                                                          ##
##                                                                                                                        ##
##  Rules       :      | Characteristics - Status | is | All                                                              ##
##                 AND |    | Characteristics - Entity | is | Root > Workplace > Loyco                                    ##
##                     | OR | Characteristics - Entity | is | Root > Workplace > CLDN                                     ##
##                     | OR | Characteristics - Entity | is | Root > Workplace > ISU                                      ##
##                     | OR | Characteristics - Entity | is | Root > Workplace > CCIH                                     ##
##                     | OR | Characteristics - Entity | is | Root > Workplace > Taurus Workplace                         ##
##                     | OR | Characteristics - Entity | is | Root > Workplace > Taurus - SecOps                          ##
##                 AND |    | Characteristics - Opening date | after | - 1 year                                           ##
##                                                                                                                        ##
############################################################################################################################

import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

from dotenv import load_dotenv
import requests
import csv
import threading
from tools.animation import loading_animation, TerminalColors

def main():

    load_dotenv()
    
    url = os.getenv('URL')
    app_token = os.getenv('APP_TOKEN')
    user_token = os.getenv('USER_TOKEN')

    # Rules
    params = {
        "is_deleted": 0,
        "as_map": 0,
        "browse": 0,
        "criteria[0][link]": "AND",
        "criteria[0][field]": 12,
        "criteria[0][searchtype]": "equals",
        "criteria[0][value]": "all",
        "criteria[1][link]": "AND",
        "criteria[1][criteria][0][link]": "AND",
        "criteria[1][criteria][0][field]": 80,
        "criteria[1][criteria][0][searchtype]": "equals",
        "criteria[1][criteria][0][value]": 182,
        "criteria[1][criteria][1][link]": "OR",
        "criteria[1][criteria][1][field]": 80,
        "criteria[1][criteria][1][searchtype]": "equals",
        "criteria[1][criteria][1][value]": 93,
        "criteria[1][criteria][2][link]": "OR",
        "criteria[1][criteria][2][field]": 80,
        "criteria[1][criteria][2][searchtype]": "equals",
        "criteria[1][criteria][2][value]": 48,
        "criteria[1][criteria][3][link]": "OR",
        "criteria[1][criteria][3][field]": 80,
        "criteria[1][criteria][3][searchtype]": "equals",
        "criteria[1][criteria][3][value]": 137,
        "criteria[1][criteria][4][link]": "OR",
        "criteria[1][criteria][4][field]": 80,
        "criteria[1][criteria][4][searchtype]": "equals",
        "criteria[1][criteria][4][value]": 210,
        "criteria[1][criteria][5][link]": "OR",
        "criteria[1][criteria][5][field]": 80,
        "criteria[1][criteria][5][searchtype]": "equals",
        "criteria[1][criteria][5][value]": 224,
        "criteria[2][link]": "AND",
        "criteria[2][criteria][0][link]": "AND",
        "criteria[2][criteria][0][field]": 15,
        "criteria[2][criteria][0][searchtype]": "morethan",
        "criteria[2][criteria][0][value]": "-1YEAR",
        "start": 0,
        "sort[]": 19,
        "order[]": "DESC",
    }

    try:

        # Init
        response = requests.get(f"{url}/initSession/", headers={"Content-Type": "application/json", "Authorization": f"user_token {user_token}", "App-Token": app_token})
        session_token = response.json()["session_token"]

        # Animation
        loading_animation.stop = False
        loading_animation_thread = threading.Thread(target=loading_animation)
        loading_animation_thread.start()
        
        start = 0
        total_tickets = float('inf')
        all_tickets = []

        while start < total_tickets:
            params["start"] = start
            response = requests.get(f"{url}/search/Ticket", params=params, headers={"session-token": session_token, "App-Token": app_token})
            tickets = response.json()
        
            if total_tickets == float('inf'):
                total_tickets = int(tickets['totalcount'])

            all_tickets.extend(tickets['data'])
            start += len(tickets['data'])

        # Stop animation
        loading_animation.stop = True
        loading_animation_thread.join()

        #################### Path / Name .csv ########################
        csv_file_path = 'yearly_tickets_data.csv'
        # configurer rafraichissement automatique dans Power BI
        ##############################################################

        with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
            # Ticket's fields
            fieldnames = ['ID', 'Title', 'Entity', 'Opening date', 'Priority', 'Last update', 'Last edit by', 'Status', 'Type', 'Requester - Requester', 'Category', 'Assigned to - Technician', 'Assigned to - Technician group', 'Approval - Approver', 'Satisfaction survey - Satisfaction', 'SLA - SLA Time to own', 'Resolution date', 'Tasks - Description', 'Cost - Total cost', 'SLA - SLA Time to resolve', 'Time to resolve', 'Tasks - Category', 'Total duration', 'Closing date', 'Time to resolve + Progress', 'Time to resolve exceeded', 'Urgency', 'Impact', 'Time to own']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)
    
            writer.writeheader()
            for ticket in all_tickets:
                writer.writerow({
                    'ID': ticket['2'],
                    'Title': ticket['1'],
                    'Entity': ticket['80'],
                    'Opening date': ticket['15'],
                    'Priority': ticket['3'],
                    'Last update': ticket['19'],
                    'Last edit by': ticket['64'],
                    'Status': ticket['12'],
                    'Type': ticket['14'],
                    'Requester - Requester': ticket['4'],
                    'Category': ticket['7'],
                    'Assigned to - Technician': ticket['5'],
                    'Assigned to - Technician group': ticket['8'],
                    'Approval - Approver': ticket['59'],
                    'Satisfaction survey - Satisfaction': ticket['62'],
                    'SLA - SLA Time to own': ticket['37'],
                    'Resolution date': ticket['17'],
                    'Tasks - Description': ticket['26'],
                    'Cost - Total cost': ticket['48'],
                    'SLA - SLA Time to resolve': ticket['30'],
                    'Time to resolve': ticket['18'],
                    'Tasks - Category': ticket['20'],
                    'Total duration': ticket['45'],
                    'Closing date': ticket['16'],
                    'Time to resolve + Progress': ticket['151'],
                    'Time to resolve exceeded': ticket['82'],
                    'Urgency': ticket['10'],
                    'Impact': ticket['11'],
                    'Time to own': ticket['155']
                })

        print(TerminalColors.GREEN + f"\nLes {len(all_tickets)} données ont été mises à jour dans : {csv_file_path}" + TerminalColors.END)

        # Kill session 
        response = requests.get(f"{url}/killSession/", headers={"Content-Type": "application/json", "Session-Token": session_token, "App-Token": app_token})

    except Exception as e:
        print(TerminalColors.RED + f"\nUne erreur s'est produite lors de l'exécution de la requête : {e}" + TerminalColors.END)

if __name__ == "__main__":
    main()
