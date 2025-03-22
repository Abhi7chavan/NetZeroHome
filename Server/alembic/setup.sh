#!/bin/bash

# Path to config.ini
CONFIG_FILE="configuration/config.ini"

# Function to extract value from INI file
get_config_value() {
    section=$1
    key=$2
    value=$(grep -A 10 "^\[$section\]" "$CONFIG_FILE" | grep "^$key" | sed 's/.*= *//; s/ *$//')
    echo "$value"
}

# Extract values
USERNAME=$(get_config_value "database" "username")
PASSWORD=$(get_config_value "database" "password")
HOST=$(get_config_value "database" "host")
PORT=$(get_config_value "database" "port")
DBNAME=$(get_config_value "database" "dbname")

# Set PGPASSWORD for psql
export PGPASSWORD="$PASSWORD"

# Create database if it doesn’t exist
psql -U "$USERNAME" -h "$HOST" -p "$PORT" -c "CREATE DATABASE $DBNAME;" 2>/dev/null || echo "Database $DBNAME already exists or error occurred"

# Run Alembic migrations
# Assuming alembic.ini uses the same credentials or you update it dynamically
chdir alembic

alembic upgrade head