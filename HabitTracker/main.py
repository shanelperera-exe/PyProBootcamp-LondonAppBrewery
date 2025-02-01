import requests
from datetime import datetime

USERNAME = "shanelperera"
TOKEN = "R1DQ17TSKdwZ2drs86THOOb9bP0g"
GRAPH_ID = "graph1"

def main():
    print("""██╗  ██╗ █████╗ ██████╗ ██████╗ ██╗████████╗    ████████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ 
██║  ██║██╔══██╗██╔══██╗██╔══██╗██║╚══██╔══╝    ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
███████║███████║██████╔╝██████╔╝██║   ██║          ██║   ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
██╔══██║██╔══██║██╔══██╗██╔══██╗██║   ██║          ██║   ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██║  ██║██║  ██║██████╔╝██████╔╝██║   ██║          ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚═╝   ╚═╝          ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝""")


# pixela_endpoint = "https://pixe.la/v1/users"
#
# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
#
# # Creating Pixela account
# # response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# # response.raise_for_status()
# # print(response.text)
#
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
#
# graph_config = {
#     "id": GRAPH_ID,
#     "name": "Cycling Graph",
#     "unit": "Km",
#     "type": "float",
#     "color": "shibafu"
# }
#
# headers = {
#     "X-USER-TOKEN": TOKEN
# }
#
# # Creating the graph
# # response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# # response.raise_for_status()
# # print(response.text)
#
# pixel_creation_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
#
# today = datetime.now()
# formatted_date = today.strftime("%Y%m%d")
#
# # Get any date
# # today = datetime(year=2024, month=12, day=3)
#
# pixel_data = {
#     "date": formatted_date,
#     "quantity": "15.0"
# }
#
# # Add pixels to the graph
# # response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# # response.raise_for_status()
# # print(response.text)
#
# # Update Pixels
#
# update_pixel_endpoint = f"{pixel_creation_endpoint}/{formatted_date}"
#
# updated_pixel_data = {
#     "quantity": "12.0"
# }
#
# # response = requests.put(url=update_pixel_endpoint, json=updated_pixel_data, headers=headers)
# # response.raise_for_status()
# # print(response.text)
#
#
# # Delete pixels
#
# delete_pixel_endpoint = update_pixel_endpoint
#
# response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# response.raise_for_status()
# print(response.text)

if __name__ == "__main__":
    main()