# 🎬 Rule-Based Movie Recommendation Engine

A Python-based **Rule-Based Movie Recommendation Engine** that recommends movies according to the user's preferred genre and minimum rating.

The project uses predefined filtering rules with Python and Pandas to analyze movie data and generate recommendations. It does not use Machine Learning or AI models.

## 📌 Features

- Display available movie genres.
- Accept the user's preferred genre.
- Filter movies based on minimum rating.
- Display matching movie recommendations.
- Calculate the average rating of recommended movies.
- Interactive command-line interface.
- Exit functionality.

## ⚙️ How It Works

The recommendation engine follows a predefined rule-based approach:

1. The user selects a preferred movie genre.
2. The user enters a minimum acceptable rating.
3. The system filters movies matching both conditions.
4. Matching movies are displayed as recommendations.
5. The average rating of the recommended movies is calculated.

**Recommendation Rules:**
- Genre must match the user's selection.
- Movie rating must be greater than or equal to the minimum rating entered by the user.

## 🛠️ Technologies Used

- Python
- Pandas
- CSV Dataset

## 📂 Project Structure

```text
Movie-Recommendation-Engine/
│
├── movies_dataset.csv
├── app.py
└── README.md
```

## 🚀 Installation and Setup

**1. Clone the repository**

```bash
git clone YOUR_REPOSITORY_URL
```

**2. Navigate to the project directory**

```bash
cd Movie-Recommendation-Engine
```

**3. Install dependencies**

```bash
pip install pandas
```

**4. Run the application**

```bash
python main.py
```

## 💻 Sample Output

```text
===== MOVIE RECOMMENDATION ENGINE =====

Available genres:
Sci-Fi, Action, Romance, Horror...

Enter your favourite genre: Sci-Fi
Enter the minimum rating: 8.0

===== RECOMMENDED MOVIES =====

1. Inception
   Rating: 8.8
   Year: 2010

Average recommendation rating: 8.75
```

## 📊 Dataset Information

The CSV dataset contains the following columns:

| Column | Description |
|---|---|
| name | Movie title |
| genre | Movie genre |
| rating | Movie rating |
| year | Release year |

## 🧠 Concepts Practiced

- Python programming fundamentals
- Pandas DataFrame operations
- CSV file handling
- Data filtering and conditional logic
- Loops and user input
- Basic data analysis
- Rule-based recommendation logic

## 🔮 Future Improvements

- Sort recommendations by rating.
- Display the top 5 recommended movies.
- Support multiple genre selection.
- Add movie release year filtering.
- Implement a personal movie watchlist.
- Explore content-based recommendation using cosine similarity.

## 🎯 Project Objective

To understand how a basic recommendation system works using predefined rules, while strengthening Python programming and data manipulation skills.

**Note:** This is a rule-based recommendation system, not a Machine Learning model.

---

**Author:** Azahar Patel

*Built as a hands-on Python learning project.*