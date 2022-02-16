
# CLI APIThreads

This is a basic Python CLI app , specially made for developers to test their APIs suing concurrent or delayed server hit from their own machine.

This cli app is configured for GET and POST methods. To use this CLI app you need to pass some arguments.

## Arguments

To run this project, you will need to pass some arguments related to api

`-method`: HTTP method GET or POST

`-url`: URL string

`-threads`: Number of threads to run. Default value is 1 

`-resCode`: Response Code to check n Response for assertion. Run would pass if in response same code is returned. Default value is 200.

`-headers`: File path to headers. Headers file is in *.json format.

`-body`: File path to API body. Body file is in *.json format

`-delay`: Add delay to API run value is in seconds. Default value is 0 .

`-type`: Defines whether an API is JSON or XML. Expected values json or xml. Default value is json.

## Enironment variables

`${id}`: this is a unique id generator for any data in json or xml api body. Write ${id} in your json/xml that value would be  replaced by unique id in API request

```javascript
{
  id:${id},
  value:"data_"${id}
}
```
## Installation

`Windows`

Download and use like .\cli_apithreads.exe

`Linux`

 Download and use the cli app by typing `./cli_apithreads`

`Mac`

Download Mac files `Content.zip`, de-compress and do `cd MacOS/` then run cli tool using `./cli_apithreads`

You can add this app to ${PATH} or Environment Variables if you want to run from any folder.

Also Headers and Payload files can have any paths. Just define the path in -headers,-bodyData

Also `git clone https://github.com/gaurangbhatt19/CLI_apithreads/tree/master/` then delete other folders
## Syntax


```bash
  For Windows:

 #  .\cli_apithreads.exe -method <POST or GET> -url <URL> -threads <Number of threads> -resCode <Expected response code for assertion> -headers <filepath headers> -body <filepath body> -delay <Delay Seconds>
  
  For Mac/Linux:
  
 #  ./cli_apithreads -method <POST or GET> -url <URL> -threads <Number of threads> -resCode <Expected response code for assertion> -headers <filepath headers> -body <filepath body> -delay <Delay Seconds>
```
## Demo

 `Header.json (can use any file with *.json format for headers and *.json or *.xml file for API body )`

```json
{
    "Content-Type":"application/xml",
    "User-Agent": "Python",
    "Authorization":"Token"
}

```


```bash
GET method:

Windows

# .\cli_apithreads.exe -method GET -url https://api.github.com/users/gaurangbhatt19 -threads 4 -resCode 200 -headers /headers.json

Mac/Linux

# ./cli_apithreads -method GET -url https://api.github.com/users/gaurangbhatt19 -threads 4 -resCode 200 -headers /headers.json

POST method:

Windows

# .\cli_apithreads.exe -method POST -url https://api.github.com/users/gaurangbhatt19 -threads 4 -resCode 200 -bodyData .\data.json -headers .\headers.json -delay 2

Mac/Linux

# ./cli_apithreads -method POST -url https://api.github.com/users/gaurangbhatt19 -threads 4 -resCode 200 -bodyData .\data.json -headers .\headers.json -delay 2

```
## App Results

```javascript
Threads = 1

Url: https://api.github.com/users/gaurangbhatt19
Response: {"login": "gaurangbhatt19", "id": 44087367, "node_id": "MDQ6VXNlcjQ0MDg3MzY3", "avatar_url": "https://avatars.githubusercontent.com/u/44087367?v=4", 
"gravatar_id": "", "url": "https://api.github.com/users/gaurangbhatt19", "html_url": "https://github.com/gaurangbhatt19", "followers_url": "https://api.github.com/users/gaurangbhatt19/followers", "following_url": "https://api.github.com/users/gaurangbhatt19/following{/other_user}", "gists_url": "https://api.github.com/users/gaurangbhatt19/gists{/gist_id}", "starred_url": "https://api.github.com/users/gaurangbhatt19/starred{/owner}{/repo}", "subscriptions_url": "https://api.github.com/users/gaurangbhatt19/subscriptions", "organizations_url": "https://api.github.com/users/gaurangbhatt19/orgs", "repos_url": "https://api.github.com/users/gaurangbhatt19/repos", "events_url": "https://api.github.com/users/gaurangbhatt19/events{/privacy}", "received_events_url": "https://api.github.com/users/gaurangbhatt19/received_events", "type": "User", "site_admin": false, "name": "Gaurang Bhatt", "company": null, "blog": "", "location": "Haridwar", "email": null, "hireable": null, "bio": "Web Development, IT Cloud Automation, and Cybersecurity enthusiast with a good hand on efficient coding methods and Data Structures.", "twitter_username": null, "public_repos": 65, "public_gists": 0, "followers": 0, "following": 0, "created_at": "2018-10-12T09:58:01Z", "updated_at": "2022-01-08T11:12:41Z"}
Elapsed Time: 0:00:00.133479
Result: Passed

Total Pass: 1/1 Total Fail: 0/1
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

Total Pass: 2/2 Total Fail: 0/2
```
## Download

Linux

<a href="https://github.com/gaurangbhatt19/CLI_apithreads/blob/master/Linux/cli_apithreads" download>Download Linux File</a>

Mac

<a href="https://github.com/gaurangbhatt19/CLI_apithreads/blob/master/Linux/Contents.zip" download>Download Mac File</a>

Windows

<a href="https://github.com/gaurangbhatt19/CLI_apithreads/blob/master/Windows/cli_apithreads.exe" download>Download Windows File</a>

## Authors

- [@gaurangbhatt19](https://github.com/gaurangbhatt19)