# def login(func):
#     def wrapper():
#         print("checking login")
#         func()
#     return wrapper
# @login
# def dashboard():
#     print("dashboard page")
# dashboard()
# def message(func):
#     def wrapper():
#         print("function started")
#         func()
#         print("function ended")
#     return wrapper
# @message
# def hello():
#     print("hello python")
# hello()

# {
#   "login": "python",
#   "id": 1525981,
#   "node_id": "MDEyOk9yZ2FuaXphdGlvbjE1MjU5ODE=",
#   "avatar_url": "https://avatars.githubusercontent.com/u/1525981?v=4",
#   "gravatar_id": "",
#   "url": "https://api.github.com/users/python",
#   "html_url": "https://github.com/python",
#   "followers_url": "https://api.github.com/users/python/followers",
#   "following_url": "https://api.github.com/users/python/following{/other_user}",
#   "gists_url": "https://api.github.com/users/python/gists{/gist_id}",
#   "starred_url": "https://api.github.com/users/python/starred{/owner}{/repo}",
#   "subscriptions_url": "https://api.github.com/users/python/subscriptions",
#   "organizations_url": "https://api.github.com/users/python/orgs",
#   "repos_url": "https://api.github.com/users/python/repos",
#   "events_url": "https://api.github.com/users/python/events{/privacy}",
#   "received_events_url": "https://api.github.com/users/python/received_events",
#   "type": "Organization",
#   "user_view_type": "public",
#   "site_admin": false,
#   "name": "Python",
#   "company": null,
#   "blog": "https://www.python.org/",
#   "location": null,
#   "email": null,
#   "hireable": null,
#   "bio": "Repositories related to the Python Programming language",
#   "twitter_username": null,
#   "public_repos": 92,
#   "public_gists": 0,
#   "followers": 31578,
#   "following": 0,
#   "created_at": "2012-03-11T15:56:37Z",
#   "updated_at": "2026-07-09T15:19:30Z"
# }

import requests
response =requests.get(
    "https://api.github.com/users/python"
)
data=response.json()
print(data)