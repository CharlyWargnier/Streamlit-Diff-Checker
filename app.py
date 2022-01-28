import streamlit as st
import difflib as dl
import os
from functionforDownloadButtons import download_button

import streamlit as st
from streamlit_elements import Elements

st.set_page_config(page_title="Diff Checher ", page_icon="📑")


# Creating a list of numbers from 0 to 99.
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


st.write(
    "<style>div.row-widget.stRadio > div{flex-direction:row;}</style>",
    unsafe_allow_html=True,
)
# We create a streamlit widget that contains a radio button.

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
        "Made in [![this is an image link](https://i.imgur.com/iIOA6kU.png)](https://www.streamlit.io/)&nbsp, with :heart: by [@DataChaz](https://www.charlywargnier.com/) | [![this is an image link](https://i.imgur.com/thJhzOO.png)](https://www.buymeacoffee.com/cwar05)"
    )

# st.write(
#     """
#
# Works well with lists, less well with paragraphs! :)
#
# 	    """
# )

col1, col2 = st.columns([1.05, 1])

with col1:
    # st.header("A dog")
    radio_buttons = st.radio("Boxes size", ["small", "medium", "large"])

with col2:
    # st.header("A cat")
    st.write("")
    st.write("")
    render_side_by_side = st.checkbox("Render side-by-side", False)

if radio_buttons == "small":
    height_text_area = 200
elif radio_buttons == "medium":
    height_text_area = 400
elif radio_buttons == "large":
    height_text_area = 600

# height_text_area = st.slider("slider 1", min_value=200, max_value=600, value=200)


with st.form("my_form"):

    c30, c31, c32 = st.columns([3, 0.2, 3])

    with c30:

        linesDeduped2 = []
        MAX_LINES = 50
        text = st.text_area(
            "List A",
            "'Python', 'Cava', 'C++', 'PLP'",
            height=height_text_area,
            key="2",
            placeholder="'Python', 'Cava', 'C++', 'PLP'",
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
            "'Mython', 'Java', 'C++', 'PHP'",
            height=height_text_area,
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

Works well with lists, less well with paragraphs! :)

	    """
    )

    st.write(
        """     
            """
    )

    st.markdown("")

# Create a new element context
mt = Elements()

# original="".join(linesList2)
original = "".join(text)
# modified="".join(linesList)
modified = "".join(text2)


if render_side_by_side:
    # mt.render_side_by_side(original, modified)
    Options = {"renderSideBySide": True}
else:
    Options = {"renderSideBySide": False}


# Example taken from https://material-ui.com/components/data-grid/
if submitted:
    with mt.paper:
        mt.monaco.diff(
            # options={"automaticLayout": True},
            # Does not work
            # options={"wordWrap": "on"},
            # options={"wordWrapBreakAfterCharacters": "."},
            # wordWrapBreakAfterCharacters?: string
            # options={"diffWordWrap": "on"},
            # WORKS! keep for horizontal scroll
            options=Options,
            # options={"renderSideBySide": False},
            height=height_text_area,
            # original="Hello there!",
            original=original,
            # original=linesList2,
            # modified="Goodbye there!",
            # modified=linesList,
            modified=modified,
        )

    mt.show()