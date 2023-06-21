# Candidates App

The Candidates App is a Streamlit web application for collecting candidate information and storing it using a backend API. This repository contains the source code and necessary files to run the app.

## Usage

You can access the live version of the Candidates App by visiting [https://candidates-form.streamlit.app](https://candidates-form.streamlit.app).

To run the app locally, follow the steps below:

1. Clone the repository:  
    ```bash
    git clone git clone https://github.com/your-username/candidates_App.git
    
2. Navigate to the repository directory:  
    ```bash
    cd candidates_App

3. Install the required packages:  
    ```bash
    pip install -r requirements.txt

4. Set the `API_URL` environment variable. The value of this variable should be the URL of the backend API where the candidate data will be stored. For example:
    ```bash
    export API_URL=http://localhost:8000/candidates

5. Navigate to the `src` folder:
    ```bash
    cd src

6. Run the app:
    ```bash
    streamlit run index.py


The app will be accessible locally at [http://localhost:8501](http://localhost:8501).

## Repository Structure

- `.env`: Environment file for setting up environment variables. You should define your `API_URL` here.
- `.gitignore`: Specifies the files and directories to be ignored by Git version control.
- `index.py`: The main Streamlit app file containing the form and submission logic.
- `LICENSE`: The license file for your project.
- `README.md`: This file you are currently reading.
- `requirements.txt`: Lists the required Python packages and their versions.

## License

This project is licensed under the terms of the [MIT License](LICENSE).

