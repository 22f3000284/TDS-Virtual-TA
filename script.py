import requests
import json
url = "https://discourse.onlinedegree.iitm.ac.in/t/176077/posts.json?post_ids%5B%5D=637872&post_ids%5B%5D=637869&post_ids%5B%5D=637867&post_ids%5B%5D=637862&post_ids%5B%5D=637855&post_ids%5B%5D=637851&post_ids%5B%5D=637837&post_ids%5B%5D=637831&post_ids%5B%5D=637830&post_ids%5B%5D=637828&post_ids%5B%5D=637827&post_ids%5B%5D=637821&post_ids%5B%5D=637815&post_ids%5B%5D=637813&post_ids%5B%5D=637810&post_ids%5B%5D=637809&post_ids%5B%5D=637808&post_ids%5B%5D=637800&post_ids%5B%5D=637796&post_ids%5B%5D=637794&include_suggested=false"
with open('cookies.txt', 'r') as file:
    cookie = file.read().strip()
headers ={
    'cookie':cookie
}   
response= requests.get(url, headers=headers)

with open('response1.json', 'w') as file:
    json.dump(response.json(), file, indent=4)
