# Growth Mindset App

A Streamlit-based web application designed to provide insights and interactive tools to cultivate a growth mindset.

## Features
- **Interactive UI** built with Streamlit.
- **Enhanced UI Components** using `streamlit-extras`.
- **Visualization & Insights** to develop a positive growth mindset.
- **Easy Deployment** on Streamlit Cloud.

## Installation

### 1. Clone the repository:
```sh
git clone https://github.com/Tahasaif3/Growth-Mindset.git
cd Growth-Mindset
```

### 2. Create a virtual environment (optional but recommended):
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### 3. Install dependencies:
```sh
pip install -r requirements.txt
```

## Running the App Locally
```sh
streamlit run growth.py
```

## Deploying to Streamlit Cloud
1. Ensure `requirements.txt` contains:
   ```
   streamlit
   streamlit-extras
   ```
2. Push your code to GitHub.
3. Deploy on Streamlit Cloud by linking your GitHub repository.

## Troubleshooting
If you encounter a `ModuleNotFoundError`, ensure:
- `streamlit-extras` is installed.
- The correct import statement is used:
  ```python
  from streamlit_extras.colored_header import colored_header
  ```
- Your `requirements.txt` is correctly set up and included in your deployment.

## Contributing
Feel free to fork this repository and submit a pull request with improvements!

## License
This project is licensed under the MIT License.

---

### Author: [Taha Saif](https://github.com/Tahasaif3)

