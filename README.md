# Tietokanta Projekti

This project is a Python application that interacts with a SQL database to manage recipes.

### Prerequisites

- Docker

### Running the application

1. Clone the repository
2. Navigate to the project directory
3. Run the following commands

```sh
docker compose build
docker compose up -d mssql
docker compose run tietokanta-projekti
```

### Queries
The queries that are used within the application are located in the [queries.sql](./queries.sql)