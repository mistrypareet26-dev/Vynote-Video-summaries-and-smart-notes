
import streamlit as st
import requests


st.set_page_config(
    page_title="Vynote",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

API_URL = "http://127.0.0.1:8000"



st.markdown("""
<style>
.stApp {
    background-color: #0F172A;
}

[data-testid="stHeader"] {
    background-color: #1E293B;
}

.block-container {
    padding-top: 1rem;
}

h1 {
    color: #A78BFA;
}

p {
    color: #E2E8F0;
}
</style>
""", unsafe_allow_html=True)


st.sidebar.title("🎬 Vynote")
st.sidebar.write("Your personal video notes workspace")

page = st.sidebar.radio(
    "Navigation",
    ["Home", "My Notes"]
)



if page == "Home":

    st.title("Generate Video Summary")

    st.subheader("Convert videos into summaries like notes")

    st.write("Paste a YouTube video link to get started.")

    youtube_url = st.text_input(
        "YouTube Video URL",
        placeholder="Paste your YouTube link here..."
    )

    if st.button("Generate Summary", type="primary"):

        if not youtube_url.strip():
            st.error("Please enter a YouTube URL.")

        else:
            try:
                with st.spinner("Generating your summary..."):

                    response = requests.post(
                        f"{API_URL}/summarize",
                        json={"youtube_url": youtube_url},
                        timeout=180
                    )

                    response.raise_for_status()

                    data = response.json()

                    st.session_state.summary = data["summary"]

                st.success("Summary generated successfully!")

            except requests.exceptions.RequestException as e:
                st.error(f"Backend error: {e}")


    if "summary" in st.session_state:

        with st.container(border=True):

            st.subheader("Your Video Summary")

            st.write(st.session_state.summary)


elif page == "My Notes":

    st.title("My Saved Notes")

    try:
        response = requests.get(
            f"{API_URL}/notes",
            timeout=15
        )

        response.raise_for_status()

        notes = response.json()

        if notes:

            for note in notes:

                with st.expander(
                    f"Note #{note['id']} - {note['youtube_url']}"
                ):

                    st.write(note["summary"])

                    st.caption(
                        f"Created at: {note['created_at']}"
                    )

        else:
            st.info("No saved notes available yet.")

    except requests.exceptions.RequestException as e:
        st.error(f"Could not fetch notes: {e}")
