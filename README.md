# SQLBot

A natural language to SQL query generator powered by AI. Transform plain English questions into SQL queries effortlessly and presenting it back in natural language.

## Table of Contents
1. [Getting Started](#-getting-started)
2. [Prerequisites](#-prerequisites)
3. [Project Setup](#project-setup)
4. [Running the Application](#running-the-application)
5. [Usage](#usage)
6. [Author](#-author)
7. [Contributing](#-contributing)
8. [Contact](#-contact)

## 🚀 Getting Started

Follow the instructions below to set up and run the SQLBot application.

### 🐣 Prerequisites

Ensure you have the following installed:
- Python >= 3.10
- Database (MySQL, PostgreSQL, or SQLite)

### 🛠️ Project Setup

1. Clone the project repository:
    ```bash
    git clone https://github.com/aniket-7887/SQLBot.git
    ```
   
2. Navigate to the project directory:
    ```bash
    cd SQLBot/
    ```

3. Create and activate a virtual environment:
    ```bash
    # for mac or linux based system
    python3 -m venv env
    source env/bin/activate

    # for windows
    python -m venv .venv
    ./.venv/Scripts/activate
    ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Set up environment variables by copying the example configuration:
    ```bash
    cp .venv.example .venv
    ```

6. Configure your database connection in the `.venv` file with your database credentials.

## Running the Application

Start the application:
```bash
streamlit frontend.py
```

The application will be available at `http://localhost:8000`

## 💡Usage

### Basic Query Example

**User Input:**
```
# Example natural language query
Show me all customers who made purchases in the last 30 days
```

**Generated SQL:**
```sql
# Example database query
SELECT * FROM customers 
WHERE customer_id IN (
    SELECT DISTINCT customer_id 
    FROM orders 
    WHERE order_date >= DATE_SUB(CURRENT_DATE, INTERVAL 30 DAY)
);
```

## 👨‍💻 Author

**Aniket Mali**
- GitHub: [@aniket-7887](https://github.com/aniket-7887)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.


## 📧 Contact

For questions or suggestions, please open an issue or reach out through GitHub.

---

⭐ If you find this project useful, please consider giving it a star!