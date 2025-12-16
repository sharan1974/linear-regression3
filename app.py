## app.py

```python
import streamlit as st
import pandas as pd

st.set_page_config(page_title="My Streamlit App", layout="wide")

st.title("🚀 My First Streamlit App")
st.write("This is a simple Streamlit app template.")

# Sidebar
st.sidebar.header("Options")
show_data = st.sidebar.checkbox("Show sample data", value=True)

# Main content
if show_data:
    st.subheader("Sample Data")
    df = pd.DataFrame({
        "Name": ["Alice", "Bob", "Charlie"],
        "Score": [85, 90, 78]
    })
    st.dataframe(df)

    st.subheader("Chart")
    st.bar_chart(df.set_index("Name"))

st.success("App loaded successfully!")
```

---

## requirements.txt

```txt
streamlit
pandas
```

---

### How to run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```
