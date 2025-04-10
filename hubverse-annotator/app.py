"""
A streamlit application for that loads hubverse formatted
tables and plots model forecasts for the end user to
compare and annotate models.

To run: poetry run streamlit run app.py
"""

import datetime

import streamlit as st


def main():
    st.title("Forecast Annotator")

    # ile upload section
    # st.subheader("Upload Hubverse File")
    uploaded_file = st.file_uploader(
        "Upload Hubverse File", type=["csv", "parquet"]
    )

    # two-column layout for reference Date and location
    col1, col2 = st.columns(2)
    with col1:
        reference_date = st.date_input(
            "Reference Date", value=datetime.date(2024, 1, 1)
        )
    with col2:
        location = st.selectbox(
            "Location", ["Arizona", "New York", "Nevada", "New Jersey"]
        )

    st.markdown(f"## Forecasts For: {location}")
    st.markdown(f"## Reference Date: {reference_date}")
    st.area_chart(
        {
            "Forecast A": [3, 6, 9, 2, 5],
            "Forecast B": [2, 4, 8, 3, 7],
            "Forecast C": [1, 7, 5, 6, 2],
            "Forecast D": [5, 4, 3, 2, 6],
        }
    )

    # forecasts annotation section
    st.markdown("#### Forecast A")
    st.selectbox("Status", ["Preferred", "Omitted", "None"], key="status_a")
    st.text_input("Comments", key="comments_a")

    st.markdown("#### Forecast B")
    st.selectbox("Status", ["Preferred", "Omitted", "None"], key="status_b")
    st.text_input("Comments", key="comments_b")

    st.markdown("#### Forecast C")
    st.selectbox("Status", ["Preferred", "Omitted", "None"], key="status_c")
    st.text_input("Comments", key="comments_c")

    st.markdown("#### Forecast D")
    st.selectbox("Status", ["Preferred", "Omitted", "None"], key="status_d")
    st.text_input("Comments", key="comments_d")

    # export button
    if st.button("Export forecasts"):
        col1, col2, col3 = st.columns([1, 3, 1])
        with col2:
            st.success("Need export")


if __name__ == "__main__":
    main()
