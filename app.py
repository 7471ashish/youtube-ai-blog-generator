import streamlit as st
from crew import crew

st.set_page_config(
    page_title="YouTube AI Blog Generator",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 YouTube AI Blog Generator")
st.write("Generate a blog from a YouTube video transcript using CrewAI.")

topic = st.text_input(
    "Enter Topic",
    placeholder="Example: LangChain Krish Naik"
)

if st.button("Generate Blog"):
    if topic.strip() == "":
        st.warning("Please enter a topic.")
    else:
        with st.spinner("Researching YouTube and writing blog..."):

            try:
                result = crew.kickoff(
                    inputs={
                        "topic": topic
                    }
                )

                st.success("Blog Generated Successfully!")

                st.subheader("Generated Blog")

                st.markdown(str(result))

                with open("generated_blog.md", "w", encoding="utf-8") as f:
                    f.write(str(result))

                st.download_button(
                    "📥 Download Blog",
                    str(result),
                    file_name="generated_blog.md",
                    mime="text/markdown"
                )

            except Exception as e:
                st.error(e)