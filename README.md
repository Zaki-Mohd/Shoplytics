# Customer Segmentation Project

This project is a web application for customer segmentation using K-Means clustering. It allows users to input a customer's annual income and spending score to predict which customer segment they belong to.

## Features

- **Interactive Frontend:** A user-friendly interface for inputting customer data.
- **K-Means Clustering:** The backend uses a trained K-Means model to segment customers into one of five clusters.
- **Data Visualization:** A scatter plot visualizes the customer data, cluster centroids, and the predicted location of a new customer.
- **Glassmorphism UI:** A modern and visually appealing user interface.

## Technologies Used

- **Frontend:**
    - HTML
    - CSS
    - JavaScript
    - [Chart.js](https://www.chartjs.org/) for data visualization
- **Backend:**
    - [Flask](https://flask.palletsprojects.com/): A lightweight web framework for Python.
    - [scikit-learn](https://scikit-learn.org/): For K-Means clustering.
    - [pandas](https://pandas.pydata.org/): For data manipulation.
    - [NumPy](https://numpy.org/): For numerical operations.

## Setup and Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/Zaki-Mohd/Shoplytics.git
    ```

2.  **Install the required Python libraries:**

    ```bash
    pip install Flask pandas scikit-learn numpy threejs
    ```

3.  **Run the application:**

    ```bash
    python main.py
    ```

4.  Open your web browser and navigate to `http://127.0.0.1:5000/` to view the application.

## How to Use

1.  Enter the customer's **Annual Income (k$)** in the designated input field.
2.  Enter the customer's **Spending Score (1-100)** in the designated input field.
3.  Click the **"Predict"** button.
4.  The application will display the predicted customer cluster and an insight based on that cluster.
5.  The scatter plot will update to show the location of the new customer.
