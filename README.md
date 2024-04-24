# Tietokanta Projekti

This project is a Python application that interacts with a SQL database to manage recipes.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Docker

### Installation

1. Clone the repository
2. Navigate to the project directory
3. Run the following commands

```sh
docker compose build
docker compose up -d mssql
docker compose run tietokanta-projekti
```