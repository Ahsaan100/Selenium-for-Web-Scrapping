# import os
# from bs4 import BeautifulSoup

# # Loop through all files in the 'data' directory
# for file in os.listdir("data"):
#     try:
#         with open(f"data/{file}") as f:
#             html_doc = f.read()
    
#     # Parse the HTML content
#     soup = BeautifulSoup(html_doc, "html.parser")
    
#     # Find the first h2 tag
#     t = soup.find("h2")

#     l = t.find("a")

#     p = soup.find("span", attrs={"class": "a-price-whole"})

#     i = soup.find("img", class_="s-image")
    
#     # Check if h2 tag was found
#     if t is not None:
#         title = t.get_text()
#         link = "https://amazon.com" + l['href']
#         image = i.get("src")
#         price = p.get_text()
#         print("Title: \n", title)
#         print("Link: \n", link)
#         print("Price: \n", price)
#         print("Image url: \n", image)

#     else:
#         print(f"No <h2> tag found in {file}")
#     except Exception as e:
    

#     break  # Remove this break if you want to process all files

import os
import pandas as pd
from bs4 import BeautifulSoup

d = {'title': [], 'link': [], 'price': [], 'image': []}

# Loop through all files in the 'data' directory
for file in os.listdir("data"):
    try:
        with open(f"data/{file}") as f:
            html_doc = f.read()
    
        # Parse the HTML content
        soup = BeautifulSoup(html_doc, "html.parser")
        
        # Find the first h2 tag and associated elements
        t = soup.find("h2")
        l = t.find("a") if t else None
        p = soup.find("span", attrs={"class": "a-price-whole"})
        i = soup.find("img", class_="s-image")
        
        # Extract the required information
        title = t.get_text() if t else "No title found"
        link = "https://amazon.com" + l['href'] if l else "No link found"
        price = p.get_text() if p else "No price found"
        image = i.get("src") if i else "No image found"
        
        # Print the extracted information
        print("Title: \n", title)
        print("Link: \n", link)
        print("Price: \n", price)
        print("Image URL: \n", image)
    
        d["title"].append(title)
        d["link"].append(link)
        d["price"].append(price)
        d["image"].append(image)
    
    except Exception as e:
        print(f"Error processing file {file}: {e}")

df = pd.DataFrame(data = d)
df.to_csv("data.csv")
