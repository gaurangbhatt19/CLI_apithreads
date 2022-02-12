
# CLI APIThreads

This is a basic Python Cli app , specially made for developers to test their APIs suing concurrent or delayed server hit from their own machine.

This cli app is configured for GET and POST methods. To use this CLI app you need to pass some arguments.




## Arguments

To run this project, you will need to pass some arguments related to api

`-method`: HTTP method GET or POST

`-url`: URL string

`-threads`: Number of threads to run. Default value is 1 

`-resCode`: Response Code to check n Response for assertion. Run would pass if in response same code is returned. Default value is 200.

`-headers`: File path to headers. Headers file is in *.json format.

`-body`: File path to API body. Body file is in *.json format

`-delay`: Add delay to API run value is in seconds. Defualt value is 0 .

## Syntax


```bash
  For Windows:

 #   cd App/dist
 #   cli_apithreads.exe -method <POST or GET> -url <URL> -threads <Number of threads> -resCode <Expected response code for assertion> -headers <filepath headers> -body <filepath body> -delay <Delay Seconds>
  
  For Mac:
  
 #   cd App
 #   python cli_apithreads.pyc -method <POST or GET> -url <URL> -threads <Number of threads> -resCode <Expected response code for assertion> -headers <filepath headers> -body <filepath body> -delay <Delay Seconds>
```
## Demo

```bash
GET method:

Windows

# cli_apithreads.exe -method GET -url https://api.github.com/users/gaurangbhatt19 -threads 4 -resCode 200 -headers /headers.json

Mac

# python cli_apithreads.pyc -method GET -url https://api.github.com/users/gaurangbhatt19 -threads 4 -resCode 200 -headers /headers.json

POST method:

Windows

# cli_apithreads.exe -method POST -url https://api.github.com/users/gaurangbhatt19 -threads 4 -resCode 200 -bodyData .\data.json -headers .\headers.json -delay 2

Mac

# python cli_apithreads.pyc -method POST -url https://api.github.com/users/gaurangbhatt19 -threads 4 -resCode 200 -bodyData .\data.json -headers .\headers.json -delay 2

```
## App Results

```javascript
Threads = 1

Url: https://api.github.com/users/gaurangbhatt19
Response: {"login": "gaurangbhatt19", "id": 44087367, "node_id": "MDQ6VXNlcjQ0MDg3MzY3", "avatar_url": "https://avatars.githubusercontent.com/u/44087367?v=4", 
"gravatar_id": "", "url": "https://api.github.com/users/gaurangbhatt19", "html_url": "https://github.com/gaurangbhatt19", "followers_url": "https://api.github.com/users/gaurangbhatt19/followers", "following_url": "https://api.github.com/users/gaurangbhatt19/following{/other_user}", "gists_url": "https://api.github.com/users/gaurangbhatt19/gists{/gist_id}", "starred_url": "https://api.github.com/users/gaurangbhatt19/starred{/owner}{/repo}", "subscriptions_url": "https://api.github.com/users/gaurangbhatt19/subscriptions", "organizations_url": "https://api.github.com/users/gaurangbhatt19/orgs", "repos_url": "https://api.github.com/users/gaurangbhatt19/repos", "events_url": "https://api.github.com/users/gaurangbhatt19/events{/privacy}", "received_events_url": "https://api.github.com/users/gaurangbhatt19/received_events", "type": "User", "site_admin": false, "name": "Gaurang Bhatt", "company": null, "blog": "", "location": "Haridwar", "email": null, "hireable": null, "bio": "Web Development, IT Cloud Automation, and Cybersecurity enthusiast with a good hand on efficient coding methods and Data Structures.", "twitter_username": null, "public_repos": 65, "public_gists": 0, "followers": 0, "following": 0, "created_at": "2018-10-12T09:58:01Z", "updated_at": "2022-01-08T11:12:41Z"}
Elapsed Time: 0:00:00.133479
Result: Passed
```
```javascript
Threads = 2

Url: https://api.github.com/users/gaurangbhatt19
Response: {"login": "gaurangbhatt19", "id": 44087367, "node_id": "MDQ6VXNlcjQ0MDg3MzY3", "avatar_url": "https://avatars.githubusercontent.com/u/44087367?v=4", 
"gravatar_id": "", "url": "https://api.github.com/users/gaurangbhatt19", "html_url": "https://github.com/gaurangbhatt19", "followers_url": "https://api.github.com/users/gaurangbhatt19/followers", "following_url": "https://api.github.com/users/gaurangbhatt19/following{/other_user}", "gists_url": "https://api.github.com/users/gaurangbhatt19/gists{/gist_id}", "starred_url": "https://api.github.com/users/gaurangbhatt19/starred{/owner}{/repo}", "subscriptions_url": "https://api.github.com/users/gaurangbhatt19/subscriptions", "organizations_url": "https://api.github.com/users/gaurangbhatt19/orgs", "repos_url": "https://api.github.com/users/gaurangbhatt19/repos", "events_url": "https://api.github.com/users/gaurangbhatt19/events{/privacy}", "received_events_url": "https://api.github.com/users/gaurangbhatt19/received_events", "type": "User", "site_admin": false, "name": "Gaurang Bhatt", "company": null, "blog": "", "location": "Haridwar", "email": null, "hireable": null, "bio": "Web Development, IT Cloud Automation, and Cybersecurity enthusiast with a good hand on efficient coding methods and Data Structures.", "twitter_username": null, "public_repos": 65, "public_gists": 0, "followers": 0, "following": 0, "created_at": "2018-10-12T09:58:01Z", "updated_at": "2022-01-08T11:12:41Z"}
Elapsed Time: 0:00:00.399195
Result: Passed
Url: https://api.github.com/users/gaurangbhatt19
Response: {"login": "gaurangbhatt19", "id": 44087367, "node_id": "MDQ6VXNlcjQ0MDg3MzY3", "avatar_url": "https://avatars.githubusercontent.com/u/44087367?v=4", 
"gravatar_id": "", "url": "https://api.github.com/users/gaurangbhatt19", "html_url": "https://github.com/gaurangbhatt19", "followers_url": "https://api.github.com/users/gaurangbhatt19/followers", "following_url": "https://api.github.com/users/gaurangbhatt19/following{/other_user}", "gists_url": "https://api.github.com/users/gaurangbhatt19/gists{/gist_id}", "starred_url": "https://api.github.com/users/gaurangbhatt19/starred{/owner}{/repo}", "subscriptions_url": "https://api.github.com/users/gaurangbhatt19/subscriptions", "organizations_url": "https://api.github.com/users/gaurangbhatt19/orgs", "repos_url": "https://api.github.com/users/gaurangbhatt19/repos", "events_url": "https://api.github.com/users/gaurangbhatt19/events{/privacy}", "received_events_url": "https://api.github.com/users/gaurangbhatt19/received_events", "type": "User", "site_admin": false, "name": "Gaurang Bhatt", "company": null, "blog": "", "location": "Haridwar", "email": null, "hireable": null, "bio": "Web Development, IT Cloud Automation, and Cybersecurity enthusiast with a good hand on efficient coding methods and Data Structures.", "twitter_username": null, "public_repos": 65, "public_gists": 0, "followers": 0, "following": 0, "created_at": "2018-10-12T09:58:01Z", "updated_at": "2022-01-08T11:12:41Z"}
Elapsed Time: 0:00:00.123956
Result: Passed
```


## Authors

- [@gaurangbhatt19](https://github.com/gaurangbhatt19)

