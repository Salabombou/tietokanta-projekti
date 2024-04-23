#!/bin/bash
set -e

# Start SQL Server
/opt/mssql/bin/sqlservr &

# Wait for the SQL Server to come up
echo "Waiting for SQL Server to start..."
export STATUS=1
i=0
while [ $STATUS -ne 0 ] && [ $i -lt 30 ]; do
    i=$i+1
    /opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P Nakkikastike12 -Q "SELECT 1" >> /dev/null
    STATUS=$?
    sleep 1
done

# Define the path of the flag file
FLAGFILE="/var/opt/mssql/.setup_complete"

# Check if the flag file exists
if [ ! -f "$FLAGFILE" ]; then
    # Set up the database
    echo "Setting up the database..."
    /opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P Nakkikastike12 -q "CREATE DATABASE RecipeDB"
    /opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P Nakkikastike12 -d RecipeDB -i ./db/schema.sql
    /opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P Nakkikastike12 -d RecipeDB -i ./db/populate.sql

    # Create the flag file
    touch $FLAGFILE
    echo "SQL Server started."
else
    echo "Setup already completed. Skipping..."
fi

# Keep the container running
tail -f /dev/null