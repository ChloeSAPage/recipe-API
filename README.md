# Recipe API

## Overview

With this recipe API, you can retrieve (in JSON format), and submit recipes into a database.

## **Getting started guide**

This API is *not* hosted and thus will need to be installed on your local machine.

> [!IMPORTANT]
> You will need:

- [ ]  MySQL database

### Installing

#### 1. Clone the Repository

Using Git, copy these files into a folder.
Use this command:

```
git clone https://github.com/ChloeSAPage/Rat-Bot.git
```

#### 2. Install the requirements

```
pip install -r requirements.txt
```

#### 3. Create a config file in the root directory and add your SQL details.

> [!WARNING]
> **The file should be formatted as such, with the appropriate details. Otherwise this will _not_ work **

```
HOST = "localhost"
USER = ""
PASSWORD = ""
```

#### 5. Manually create a DB

Use the supplied code in the `/DB_SETUP` directory to create a MySQL database.


#### 4. Run

1. Run app.py
2. Run main.py
3. Follow instructions in command line

## EndPoints

### Get all recipes

- Endpoint: `/get-recipes`
- Method: GET
- Response: JSON

### Get one recipe

- Endpoint: `/get-recipe/<id>`
- Method: GET
- Parameters: `recipe-id` (required).
- Response: JSON


### Submit a recipe

- Endpoint: `/submit-recipe/`
- Method: PUT
- Response: 201

## Error Handling

The API returns the appropriate HTTP status code.

# Git Section [^1]

## Checking the status

![Checking the status](/images/image.png)

## Creating the branch

![Creating the branch](/images/image-1.png)

## Adding files to branch

![Adding files to branch](/images/image-2.png)


## Commits

![Commits](/images/image-3.png)


## Pull request

https://github.com/ChloeSAPage/Recipe-API/pull/1

![Pull request](/images/image-4.png)


## Merging with main

### Request

![Request merge](/images/image-5.png)

### Confirm Merge

![Confirm Merge](/images/image-6.png)

### Merge Success and branch deleted

![Merge Success and branch deleted](/images/image-7.png)

## Git ignore

The .gitignore file is used to ensure files you don't wish to be shared (such as the config.py file) are not accidentally added in a commit. The files will be ignored when staging files even when using `git add .`

## Requirements.txt

This file is used to show what dependencies a repository has, for example this repo uses the following packages:

- requests
- mysql
- flask


The requirements file can be easily installed using the following command `pip install -r requirements.txt`

[^1]: This section will be removed after the pull request is confirmed.