# Team 1 - HR Recruitment Analytics

## Problem Statement

HR teams have recruitment funnel data, interview feedback, and onboarding records, but no shared reporting system identifies which hiring stages contribute most to candidate drop-offs across departments.

This project aims to build an HR Recruitment Analytics system that helps HR teams analyze recruitment data, identify candidate drop-offs at different hiring stages, and compare recruitment performance across departments.

---

## Tech Stack

- Python
- Pandas
- PostgreSQL
- SQL
- Streamlit
- Docker
- Docker Compose
- Pytest
- GitHub Actions

---

## Project Setup

### Prerequisites

Make sure the following are installed on your system:

- Git
- Docker
- Docker Compose

Check the installations:

```bash
git --version
docker --version
docker compose version

1. Clone the Repository
git clone <repository-url>

Navigate into the project:

cd Team1_hr-analytics
2. Create the Environment File

Copy the example environment file:

cp .env.example .env

The .env file contains the PostgreSQL configuration.

Example:

POSTGRES_DB=hr_analytics
POSTGRES_USER=hr_user
POSTGRES_PASSWORD=change_me
POSTGRES_HOST=db
POSTGRES_PORT=5432

Do not commit the .env file to GitHub.

3. Build and Start the Project

Run:

docker compose up --build

This will start:

Streamlit application
PostgreSQL database
4. Open the Application

Once the containers are running, open:

http://localhost:8501
Running Tests

Run the tests inside the application container:

docker compose exec app pytest
Stopping the Project

To stop the containers:

docker compose down

To stop the containers and remove the database volume:

docker compose down -v

Warning: docker compose down -v will delete the PostgreSQL data stored in the Docker volume.