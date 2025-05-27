#!/bin/bash

# Load environment variables from .env file
load_env() {
  if [ -f .env ]; then
    echo "Loading environment variables from .env..."
    set -a
    source .env
    set +a
  else
    echo ".env file not found. Exiting."
    exit 1
  fi
}

# Function to initialize Airflow DB
init_airflow_db() {
  echo "Initializing Airflow database..."
  airflow db init
}

# Function to create Airflow admin user using .env variables
create_new_user() {
  echo "Creating Airflow admin user..."

  # Ensure required env variables are present
  if [[ -z "$AIRFLOW_USER_USERNAME" || -z "$AIRFLOW_USER_FIRSTNAME" || -z "$AIRFLOW_USER_LASTNAME" || -z "$AIRFLOW_USER_ROLE" || -z "$AIRFLOW_USER_EMAIL" || -z "$AIRFLOW_USER_PASSWORD" ]]; then
    echo "Missing one or more required AIRFLOW_USER_* variables in .env. Exiting."
    exit 1
  fi

  airflow users create \
    --username "$AIRFLOW_USER_USERNAME" \
    --firstname "$AIRFLOW_USER_FIRSTNAME" \
    --lastname "$AIRFLOW_USER_LASTNAME" \
    --role "$AIRFLOW_USER_ROLE" \
    --email "$AIRFLOW_USER_EMAIL" \
    --password "$AIRFLOW_USER_PASSWORD"
}

# Main
load_env

case "$1" in
  0)
    init_airflow_db
    ;;
  1)
    create_new_user
    ;;
  *)
    echo "Usage: $0 {0|1}"
    echo "  0 = Initialize Airflow DB"
    echo "  1 = Add new user"
    exit 1
    ;;
esac
