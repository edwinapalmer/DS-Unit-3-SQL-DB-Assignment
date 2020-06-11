# import requests

# download_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00476/buddymove_holidayiq.csv"
# target_csv_path = "buddymove_holidayiq.csv"

# response = requests.get(download_url)
# response.raise_for_status() # Check that the request was successful
# with open(target_csv_path, 'wb') as f:
#     f.write(response.content)
# print("Download ready.")


import pandas as pd
buddymove = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/00476/buddymove_holidayiq.csv")
type(buddymove)

len(buddymove)

buddymove.shape

print(buddymove.shape)