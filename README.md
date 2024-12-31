# Assignment Setup Guide

## Prerequisites
Before setting up the application, ensure that you have the following tools installed:
- **Node.js (v14.0 or higher)** — for running the frontend application.
- **Python (v3.7 or higher)** — for the scraping and backend services.
- **PostgreSQL** — for storing character data in the database.
- **pip** — Python package manager.

## Step 1: Clone the Repository
Start by cloning the repository to your local machine:
```bash
git clone https://github.com/odetacocaj/Assignment.git
```

## Step 2: Set Up the Backend (Python)

The backend handles data scraping and database insertion. It continuously scrapes data from external sources and stores it in a PostgreSQL database.

### 2.1 Install Python Dependencies
Ensure you are in the backend directory and install the necessary Python dependencies using pip:

```bash
cd backend
pip install -r requirements.txt
```

### 2.2 Set Up Environment Variables
Create a **.env** file in the backend directory to store sensitive environment variables like database credentials:

```env
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
```

### 2.3 Run the Scraping and Data Insertion

* Make sure that PostgreSQL is installed and running on your local machine or server.

* The scraping script continuously fetches character data and inserts it into the database.

#### Run the main.py script to begin scraping and inserting data:
```bash
Copy code
python main.py
```
_Important: The script will also create the necessary tables in the database if they don't already exist, so you don't need to manually create them._

### Step 3: Set Up the Frontend (React)
* The frontend is built with React and provides a user-friendly interface to interact with the character data stored in the database.

#### 3.1 Install Node.js and Dependencies
Make sure Node.js is installed, then install the necessary frontend dependencies:

```bash
cd frontend
npm install
```
#### 3.2 Configure API Endpoint
In the frontend project, configure the API endpoint that communicates with the backend to fetch character data. Ensure the API endpoint is set to the URL of your backend server (e.g., http://localhost:5000 or the live URL if deployed).

#### 3.3 Start the Development Server
Run the development server to view the frontend in your browser:

```bash
npm run dev
```

The app will be available at http://localhost:5173.

### Step 4: Run the Entire Application
* **Start the Backend Server**: In the backend directory, run the backend server.

```bash
python main.py
```
* **Start the Frontend Server**: In the frontend directory, run the frontend development server.

```bash
npm run dev
```
