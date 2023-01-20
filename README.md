# streamlit-app-template

This is a template repository for creating Streamlit apps

Write your Streamlit app to the [`main.py`](./main.py) file. Add any additional files to the [`pages`](./pages) directory.

Add any additional dependencies to the [`requirements.txt`](./requirements.txt) file. Streamlit Cloud will install the dependencies when deploying your app.

App configurations are in [`config.toml`](./.streamlit/config.toml).

If you want to use `st.secrets`, you can create a file called `secrets.toml` in the folder [`.streamlit`](./.streamlit). This file will be ignored by git.
