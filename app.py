import streamlit as st
import difflib as dl
import os
from functionforDownloadButtons import download_button

st.set_page_config(page_title="Diff Checher ", page_icon="📑")


def _max_width_():
    max_width_str = f"max-width: 1000px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>    
    """,
        unsafe_allow_html=True,
    )


_max_width_()

c30, c31, c32 = st.columns([2.5, 1, 3])

with c30:
    st.image("logo.png", width=300)
    st.header("")

with c32:

    st.title("")
    st.title("")
    st.caption("")
    st.text("")
    st.caption("")
    st.caption("")
    st.caption("")
    st.caption("")
    st.caption("")
    st.caption("")

    st.write(
        "Made in [![this is an image link](https://i.imgur.com/iIOA6kU.png)](https://www.streamlit.io/)&nbsp, with :heart: by [@DataChaz](https://www.charlywargnier.com/) | [![this is an image link](https://i.imgur.com/thJhzOO.png)](https://www.buymeacoffee.com/cwar05)"
    )

st.write("")

st.markdown("### ** Compare your text snippets **")

s1 = ["Python", "Java", "C++", "PHP"]
s2 = ["Python", "JavaScript", "C", "PHP"]

with st.form("my_form"):

    c30, c31, c32 = st.columns([3, 0.5, 3])

    with c30:

        linesDeduped2 = []
        MAX_LINES = 200
        text = st.text_area("Text A", height=200, key="2")
        lines = text.split("\n")  # A list of lines
        linesList = []
        for x in lines:
            linesList.append(x)
        linesList = list(dict.fromkeys(linesList))  # Remove dupes
        linesList = list(filter(None, linesList))  # Remove empty

        if len(linesList) > MAX_LINES:
            st.warning(
                f"⚠️ Only the first 200 keywords will be reviewed. Increased allowance  is coming - Stay tuned! 😊)"
            )
            linesList = linesList[:MAX_LINES]

    with c32:
        linesDeduped2 = []
        MAX_LINES = 200
        text2 = st.text_area("Text B", height=200, key="1")
        lines2 = text2.split("\n")  # A list of lines
        linesList2 = []
        for x in lines2:
            linesList2.append(x)
        linesList2 = list(dict.fromkeys(linesList2))  # Remove dupes
        linesList2 = list(filter(None, linesList2))  # Remove empty

        if len(linesList2) > MAX_LINES:
            st.warning(
                f"⚠️ Only the first 200 keywords will be reviewed. Increased allowance  is coming - Stay tuned! 😊)"
            )
            linesList2 = linesList2[:MAX_LINES]

    submitted = st.form_submit_button("✨ Compare!")

if submitted:

    dl.context_diff(linesList2, linesList)

    for diff in dl.context_diff(linesList2, linesList):
        textFinal = st.text(diff)
        string = str(textFinal)

    downloadButton = download_button(string, "Diff_file.txt", "📥 Download Diff file")
