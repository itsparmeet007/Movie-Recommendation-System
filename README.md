# CineMatch -- Content-Based Movie Recommendation System

CineMatch is a **content-based movie recommendation system** developed
as part of a Data Handling and Visualization (DHV) project. It
recommends five movies similar to a movie selected by the user by
comparing movie information such as its overview, genres, keywords,
cast, and director.

The project uses the TMDB 5000 Movies and Credits datasets and applies
text preprocessing, feature extraction, and cosine-based similarity to
find relevant recommendations.

## Project Overview

Traditional movie browsing can make it difficult to discover films that
match a viewer's interests. CineMatch builds a text profile for each
movie from selected metadata, converts that text into numerical
features, and compares movies using cosine-based similarity.

Given a movie title, the recommender finds the closest matches and
returns **five recommended movies**, excluding the selected movie
itself.

## Objectives

-   Explore and understand the TMDB movie datasets.
-   Clean and combine movie information from the two dataset files.
-   Extract useful information from genres, keywords, cast, and crew.
-   Combine selected movie attributes into a single text feature.
-   Preprocess text and convert it into numerical vectors.
-   Find movies with similar content.
-   Return five recommendations for a selected movie title.

## Dataset

This project uses the **TMDB 5000 Movie Dataset**, commonly distributed
as two CSV files:

1.  `tmdb_5000_movies.csv` -- movie information such as title, overview,
    genres, and keywords.
2.  `tmdb_5000_credits.csv` -- cast and crew information.

The two datasets are combined using the movie title (`title`).

Place both CSV files in the location expected by your notebook, or
update the file paths in the data-loading cells.

## Technologies and Libraries

  -----------------------------------------------------------------------
  Technology / Library                Purpose
  ----------------------------------- -----------------------------------
  **Python**                          Main programming language

  **Jupyter Notebook**                Interactive development and
                                      execution environment

  **Pandas**                          Loading, cleaning, selecting, and
                                      merging tabular movie data

  **NumPy**                           Numerical and array operations

  **Matplotlib**                      Data visualization during
                                      exploration

  **Seaborn**                         Statistical and exploratory data
                                      visualization

  **NLTK**                            Natural-language text preprocessing

  **Porter Stemmer (NLTK)**           Reducing words to their root/stem
                                      form

  **Scikit-learn**                    Text feature extraction and
                                      similarity-based recommendation

  **CountVectorizer**                 Converting movie text into
                                      word-count feature vectors

  **Cosine similarity / distance**    Measuring similarity between movie
                                      feature vectors

  **NearestNeighbors**                Finding movies closest to the
                                      selected movie using a cosine-based
                                      metric

  **Python `ast` module**             `ast.literal_eval()` parses string
                                      representations of Python literals,
                                      such as lists of dictionaries
  -----------------------------------------------------------------------

### Important concepts

-   **Content-based filtering:** recommends items based on their
    attributes.
-   **Feature engineering:** combines useful movie attributes into a
    single text field, commonly named `tags`.
-   **Bag of Words (BoW):** represents text using word-occurrence
    counts.
-   **Stemming:** reduces related word forms to a common stem.
-   **Cosine similarity:** compares the direction of two feature vectors
    to estimate how similar their content is.
-   **Nearest-neighbour search:** retrieves movies with the smallest
    cosine distance to the selected movie.

## How It Works

### 1. Load the datasets

Read the Movies and Credits CSV files using Pandas.

### 2. Merge the datasets

Combine the two DataFrames using the common `title` column so that movie
details and cast/crew information are available together.

### 3. Select relevant columns

The workflow uses fields such as `movie_id`, `title`, `overview`,
`genres`, `keywords`, `cast`, and `crew`.

### 4. Clean and preprocess the data

-   Handle missing values and remove duplicate records where required.
-   Parse string-formatted list data using `ast.literal_eval()`.
-   Extract names from the genres and keywords fields.
-   Extract selected cast members (the top three in the discussed
    workflow).
-   Extract the director's name from the crew information.

### 5. Create movie tags

Combine the overview, genres, keywords, cast, and director information
into one text feature, commonly called `tags`. This gives each movie a
text representation that captures several aspects of its content.

### 6. Text preprocessing

Convert text to lowercase and apply the NLTK Porter Stemmer so that
related word forms are represented more consistently.

### 7. Convert text into numerical vectors

Use Scikit-learn's `CountVectorizer` to create Bag-of-Words vectors from
the movie tags.

The discussed configuration uses: - `max_features=5000` -
`stop_words='english'`

This creates a numerical representation that can be compared
mathematically.

### 8. Find similar movies

Use cosine-based comparison to identify movies whose feature vectors are
closest to the selected movie. The nearest-neighbour search uses a
cosine metric.

### 9. Generate recommendations

The recommendation function accepts a movie title, finds the
corresponding movie in the processed dataset, retrieves its nearest
neighbours, excludes the selected movie itself, and displays five
recommended movie titles.

If the entered title is not present in the dataset, the function can
display `Movie not found.`

## Project Workflow

``` text
TMDB Movies CSV + Credits CSV
              |
              v
       Load data with Pandas
              |
              v
      Merge datasets by title
              |
              v
       Data cleaning and parsing
              |
              v
 Extract genres, keywords, cast, director
              |
              v
       Combine information into tags
              |
              v
     Lowercase text and stemming
              |
              v
       CountVectorizer (BoW)
              |
              v
       Numerical feature vectors
              |
              v
       Cosine-based nearest neighbours
              |
              v
        Top 5 movie recommendations
```

## Installation

### 1. Clone the repository

``` bash
git clone <your-repository-url>
cd <your-repository-folder>
```

### 2. Create a virtual environment (recommended)

``` bash
python -m venv venv
```

Activate it on Windows:

``` bash
venv\Scripts\activate
```

### 3. Install dependencies

``` bash
pip install pandas numpy matplotlib seaborn scikit-learn nltk jupyter
```

## How to Run

1.  Obtain the TMDB 5000 Movies and Credits CSV files.
2.  Place the files in the dataset folder expected by the notebook.
3.  Start Jupyter Notebook:

``` bash
jupyter notebook
```

4.  Open the movie recommendation notebook.
5.  Run the notebook cells in order, from data loading and preprocessing
    through recommendation generation.
6.  Enter a movie title supported by the dataset to retrieve
    recommendations.

## Example

If a user selects a movie such as `The Dark Knight`, the system searches
for movies with similar metadata and returns up to five recommendations.
The exact results depend on the dataset, preprocessing, and similarity
results.

## Limitations

-   Recommendations depend on the movie metadata available in the
    dataset.
-   The system may not recommend a movie that is absent from the
    dataset.
-   Content-based filtering does not directly learn from users' ratings
    or viewing behaviour.
-   Similarity in metadata does not guarantee that a viewer will enjoy a
    recommended movie.
-   Recommendation quality has not been established through user studies
    or a production-scale evaluation.

## Future Improvements

-   Build a web interface using a framework such as Streamlit.
-   Add movie posters and additional movie details using a movie
    database API.
-   Explore TF-IDF as an alternative to raw word counts.
-   Add collaborative filtering or a hybrid recommendation approach.
-   Evaluate recommendations using suitable ranking metrics and user
    feedback.
-   Improve title matching to handle spelling differences and partial
    searches.

## Project Information

-   **Project:** CineMatch -- Movie Recommendation System
-   **Project type:** Data Handling and Visualization (DHV)
-   **Recommendation approach:** Content-based filtering
-   **Dataset:** TMDB 5000 Movies and Credits
-   **Output:** Five similar movie recommendations for a selected title

------------------------------------------------------------------------

*This README describes the notebook-based project workflow. Add your
actual repository URL, notebook filename, screenshots, and any
deployment details before publishing it on GitHub.*
