# enter your code below
import requests
url = "https://api.github.com/users/boyander/repos"
res = requests.get(url)
res

GET /repos/:owner/:repo/forks