from pipeline import pipeline
import streamlit as stm
from streamlit_app import helper
import streamlit.components.v1 as components 

def main():

    stm.title("Civic Meeting Minutes Generator")
    youtube_url = stm.text_input("Paste the Youtube Link Here")

    if stm.button("Generate Minutes"):
        with stm.spinner("Processing: This can take up to 5 minutes"):
            minutes = pipeline.generate_minutes_from_youtube(youtube_url)
            stm.success("Done")
            components.html(minutes, height=1600, scrolling=True)

            pdf_bytes = helper.convert_html_to_pdf(minutes)

            stm.download_button(
                label="📄 Download as PDF",
                data=pdf_bytes,
                file_name="meeting_minutes.pdf",
                mime="application/pdf"
            )

if __name__ == "__main__":
    main()
