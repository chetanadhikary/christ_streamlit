# Student Setup Guide 

Follow these steps before starting the workshop.

---

## Step 1: Fork the Repository

1. Open this GitHub repository.
2. Click the **Fork** button.
3. Create your own copy.

Your repository should look like:

your-github-id/christ_streamlit

All your work will happen in your own fork.

---

## Step 2: Create a GitHub Codespace

Open your fork.

Click:

Code 

↓

Codespaces

↓

Create codespace on main

GitHub will automatically configure:

- Python 3.11
- Streamlit
- Pandas
- Plotly
- Required VS Code extensions


Wait until the setup completes.

---

## Step 3: Verify the Environment

Open the terminal inside Codespaces.

Run:

```bash
python --version
```

Expected:

```bash
Python 3.11.x
```

### Check Streamlit:

```bash
streamlit --version
```

## Step 4 : Run Your First Application

Run:

```bash
streamlit run streamlit_basics/01_hello_streamlit/app.py 
```

A browser preview should open

### You have successfully completed the setup !!!


# Working During the Workshop

For each module:
1. Open the module folder
2. Modify the Python file
3. Run the application
4. Test your changes
5. Commit your work

Example

```Bash
git add .
git commit -m "Completed Module 1"
git push
```
your changes are saved in your fork.

## Final Project Submission
At the end of the workshop:

Submit:
1. Your Github repository link
2. Screenshot of your dashboard
3. Brief explanation of your design choices

