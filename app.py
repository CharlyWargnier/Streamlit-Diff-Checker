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

c30, c31, c32 = st.columns([2.5, 1.4, 3])

with c30:
    st.image("logo.png", width=280)
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

    st.caption(
        "&nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp Made in [![this is an image link](https://i.imgur.com/iIOA6kU.png)](https://www.streamlit.io/)&nbsp, with :heart: by [@DataChaz](https://www.charlywargnier.com/) | [![this is an image link](https://i.imgur.com/thJhzOO.png)](https://www.buymeacoffee.com/cwar05)"
    )

st.write("")

with st.form("my_form"):

    c30, c31, c32 = st.columns([3, 0.2, 3])

    with c30:

        linesDeduped2 = []
        MAX_LINES = 50
        text = st.text_area(
            "List A",
            height=200,
            key="2",
            placeholder="'Python', 'Java', 'C++', 'PHP'",
        )
        lines = text.split("\n")  # A list of lines
        linesList = []
        for x in lines:
            linesList.append(x)

        if len(linesList) > MAX_LINES:
            st.warning(f"⚠️ Only the first 50 lines will be reviewed.")
            linesList = linesList[:MAX_LINES]

    with c32:
        linesDeduped2 = []
        MAX_LINES = 50
        text2 = st.text_area(
            "List B",
            height=200,
            key="1",
            placeholder="'Mython', 'Java', 'C++', 'PHP'",
        )
        lines2 = text2.split("\n")  # A list of lines
        linesList2 = []
        for x in lines2:
            linesList2.append(x)

        if len(linesList2) > MAX_LINES:
            st.warning(f"⚠️ Only the first 50 lines will be reviewed.")
            linesList2 = linesList2[:MAX_LINES]

    st.write("")

    c30, c31, c32 = st.columns([1.5, 0.1, 3])

    with c30:

        rowLevel = st.checkbox(
            "Compare character by character",
            value=False,
            key="3",
            help="Ticking this option will indicate the differences more accurately, showing different character by character. We will see letters that have been changed via the ^ indicator.",
        )

    with c32:

        UnifyDiffs = st.checkbox(
            "Unify diffs",
            value=False,
            key="4",
            help="By ticking this option, the unified_diff() function will “unify” the two lists together can generate the outputs as above-shown, which is more readable in my opinion.",
        )

    st.write("")

    submitted = st.form_submit_button("✨ Compare!")

if not submitted:

    st.stop()

with st.expander("ℹ️ - How to read the results", expanded=False):

    st.write(
        """     

** Default settings **

	    """
    )

    st.write(
        """     

The diff checker app will show what has been changed (with a minus plus sign) and not changed ("tree" is not changed, so there is no indicator at all)

	    """
    )

    st.image("https://i.imgur.com/0Z3H7Tq.png")

    st.write(
        """     
            """
    )
    st.write(
        """     
** Compare character by character**

	    """
    )
    st.write(
        """     
Ticking the **'Compare character by character'** option will display the differences more accurately, character by character. You will see the letters that have been changed via the ^ indicator.

	    """
    )

    st.write(
        """     
            """
    )
    st.write(
        """     

** Unify diffs**

	    """
    )

    st.write(
        """     

Ticking the **'Unify diffs'** option will unify the two lists together, which is more readable in my opinion.

	    """
    )
    st.write(
        """     
            """
    )
    st.write(
        """     

** Known limitations**

	    """
    )

    st.write(
        """     

Works well with lists, less well with paragraphs! :)

	    """
    )

    st.write(
        """     
            """
    )

    # https://i.imgur.com/0Z3H7Tq.png

    st.markdown("")

# No options selected
if submitted and not rowLevel and not UnifyDiffs:

    st.write("")

    dl.context_diff(linesList, linesList2)

    for diff in dl.context_diff(linesList, linesList2):
        textFinal = st.text(diff)
        string = str(textFinal)

    st.write("")

    downloadButton = download_button(string, "Diff_file.txt", "Download diff file")

# Row level analysis ---------------------------
elif submitted and UnifyDiffs and not rowLevel:

    st.write("")

    dl.context_diff(linesList, linesList2)

    for diff in dl.unified_diff(linesList, linesList2):
        textFinal = st.text(diff)
        string = str(textFinal)

    st.write("")

    downloadButton = download_button(string, "Diff_file.txt", "Download diff file")

# UnifyDiffs analysis ---------------------------
elif submitted and rowLevel and not UnifyDiffs:

    st.write("")

    dl.ndiff(linesList, linesList2)

    for diff in dl.ndiff(linesList, linesList2):
        textFinal = st.text(diff)
        string = str(textFinal)

    st.write("")

    downloadButton = download_button(string, "Diff_file.txt", "Download diff file")

elif submitted and rowLevel and UnifyDiffs:

    st.warning("⚠️ You can't select both options, please tick only one")
    st.stop()