# Recipe API

## Overview

This CLI app allows you to interact with and modify a MySQL cookbook database using an API.

## **Getting started guide**

This API is _not_ hosted and thus will need to be installed on your local machine.

> [!IMPORTANT]
> You will need:
>
> -   [ ] MySQL

### Installing

#### 1. Clone the Repository

Using Git, copy these files into a folder.
Use this command:

```
git clone https://github.com/ChloeSAPage/Recipe-API.git
```

#### 2. Install the requirements

```
pip install -r requirements.txt
```

#### 3. Edit the config.py file in the root directory and add your SQL details.

> [!WARNING]
> **The file should be formatted as such, with the appropriate details. Otherwise it will _not_ work**

```
HOST = "localhost"
USER = ""
PASSWORD = ""
```

#### 4. Manually create a DB

> [!WARNING]
> Use the supplied code in the `/DB_SETUP` directory to manually create a MySQL database. **A DB will _not_ be automatically created**

#### 5. Run

> [!CAUTION]
> Running the files in a different order may cause issues.

1. Run app.py
2. Run main.py
3. Follow instructions in command line

## EndPoints

### Get all recipes

-   Endpoint: `/get-recipes`
-   Method: GET
-   Response: JSON

### Get one recipe

-   Endpoint: `/get-recipe/<name>`
-   Method: GET
-   Parameters: `recipe-name` (required).
-   Response: JSON

### Submit a recipe

-   Endpoint: `/submit-recipe/`
-   Method: PUT
-   Response: 201

## Error Handling

The API returns the appropriate HTTP status code.

# Example Usage

> [!CAUTION]
> Case sensitive

## Requesting all recipe names

![requesting all recipe names](/images/image9.png)

## Get a specific recipe by name

![alt text](images/image10.png)

## Adding a recipe

![alt text](images/image11.png)

