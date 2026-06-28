# Movie API Client

A strictly type-hinted Python CLI application that fetches and formats movie data from the OMDB API. This project demonstrates modern Python architecture, static type checking, and clean separation of concerns.

## 📂 Repository Structure

```text
movie_api_client/
│
├── .env                # Stores your sensitive API keys (Ignored by git)
├── .gitignore          # Prevents pushing cache and .env to version control
├── api_client.py       # Handles networking and OMDB API requests
├── input_handler.py    # Manages terminal interactions and data casting
├── main.py             # Driver code and main application loop
├── models.py           # Dataclasses defining the Movie structure (DTO)
├── requirements.txt    # List of project dependencies
└── README.md           # Project documentation

```

## 🛠️ Dependencies Explained

* **`requests`**: Used to make HTTP GET calls to the OMDB API and handle network responses.
* **`python-dotenv`**: Securely loads environment variables from the `.env` file at the project level, ensuring the `API_KEY` is never hardcoded.
* **`mypy`**: A static type checker. It analyzes the code before runtime to catch any data type mismatches (e.g., passing a `str` when an `int` is expected).
* **`types-requests`**: Provides type stubs for the `requests` library. Without this, `mypy` wouldn't know how to verify the types coming out of network calls.
* **`pydantic`**: Used for rigorous, dynamic runtime data validation (ensuring the incoming JSON exactly matches our required formats).

## 🛡️ Static Type Checking

This codebase strictly enforces type hinting. You can verify the integrity of the code by running `mypy` before execution.

```bash
PS O:\git\movie_api_client> python -m mypy .
Success: no issues found in 5 source files

```

## 🚀 Setup Instructions

1. **Install the requirements:**
```bash
pip install -r requirements.txt

```


*(Alternatively: `pip install requests python-dotenv mypy pydantic types-requests`)*

2. **Configure your environment:**
Create a file named `.env` in the root folder and add your API key:
```env
API_KEY=your_omdb_api_key_here

```


3. **Run the application:**
```bash
python main.py

```



## 💻 Sample Output

```text
Movie API Menu
1. Search Movie
2. Exit
Enter choice: 1
Enter movie title to search: titanic

Movie Details
==================================
Title     : Titanic
Year      : 1997
Director  : James Cameron
Genre     : ['Drama', 'Romance']
Actors    : ['Leonardo DiCaprio', 'Kate Winslet', 'Billy Zane']
IMDb Rating: 8.0
Runtime (in mins)   : 194
Plot       : A seventeen-year-old aristocrat falls in love with a kind but poor artist aboard the luxurious, ill-fated R.M.S. Titanic.
==================================
```
