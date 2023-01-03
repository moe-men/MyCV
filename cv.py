from pathlib import Path
import streamlit as st
from PIL import Image

# --- Path settings ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
cv_file =  current_dir / "documents" / "CV_Moemen.pdf"
profile_picture = current_dir / "documents" / "pic.png"


# --- GENERAL SETTING ---
PAGE_TITLE = "Digital CV | Moemen Ebdelli"
PAGE_ICON = ":man:"
NAME = "Moemen Ebdelli"
DESCRIPTION = """
Junior Data Engineer at [RAYLYTIC]("https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjLor7w4an8AhX3RvEDHSlbCiIQFnoECA0QAQ&url=https%3A%2F%2Fwww.raylytic.com%2Fen%2F&usg=AOvVaw3bAOO6vCvUO2DWRmWPGPAM") and contributer at [NAAS](https://www.naas.ai
)
"""
EMAIL = "moemenebdelli7@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/moemen-ebdelli/",
    "GitHub": "https://github.com/moe-men"
}
PROJECTS = {
    "🏆 Data Modeling With pstgress"  : ["https://github.com/moe-men/data-modeling-with-pstgress","Design a relational DB to optimize queries on songs data"],
    "🏆 Data Modeling With Cassandra" : ["https://github.com/moe-men/data-modeling-with-Cassandra", "Data Modeling with NoSQL DB"],
    "🏆 ETL Data Warehouse On Redshift" : ["https://github.com/moe-men/ETL-Data-Warehouse-with-AWS-RedShift","Extract music data from S3 - Stage in Redshift - Transforms data into dimensional tables"],
    "🏆 Tunisia" : ["https://github.com/moe-men/Tunisia_Demographics", "scrap data about Tuninisa and web page using Streamlit"]
}
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- load css, pdf & profil pic ---
with open(css_file) as f:
    st.markdown("<style>{}</style>". format(f.read()), unsafe_allow_html=True)
with open(cv_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_picture)


# --- hero section --- 
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label = " 📄 Download My CV",
        data = PDFbyte,
        file_name=cv_file.name,
        mime="applicaion/octet-stream",
    )
    st.write("📫", EMAIL)


# -- social links ---
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform,link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader(":orange[Experience & Qulifications]")
st.write(
    """
- ✔️ 2 years experience in handeling Healthcare data
- ✔️ Strong hands on experience and knowledge in Python
- ✔️ Good understanding of Data modeling with Relational DB
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader(":orange[Hard Skills]")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas, Pyspark), SQL
- 📊 Data Visulization: Stzreamlit, Superset, Plotly
- 🗄️ Databases: Postgres, MongoDB, MySQL, MariaDB
- ⚙  ETL : Airflow
- 💻 OS & Containerization : Linux-Ubuntu, Windows, Docker
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader(":orange[Work History]")
st.write("---")


# --- JOB 1
st.write("🚧", "**Junior Data Engineer | [RAYLYTIC](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjLor7w4an8AhX3RvEDHSlbCiIQFnoECA0QAQ&url=https%3A%2F%2Fwww.raylytic.com%2Fen%2F&usg=AOvVaw3bAOO6vCvUO2DWRmWPGPAM)**")
st.write("03/2023 - Present")
st.write(
    """
- ► Build ETL jobs in Apache Airﬂow to automate medical questionnaires exporting to different registries
- ► Data Modeling with MariaDB
- ► Worked in a +5 members team
- ► Redesigned data model through iterations that improved predictions by 12%
"""
)


# --- JOB 2
st.write('\n')
st.write("🚧", "**Working Student-Data Engineeing | [RAYLYTIC](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjLor7w4an8AhX3RvEDHSlbCiIQFnoECA0QAQ&url=https%3A%2F%2Fwww.raylytic.com%2Fen%2F&usg=AOvVaw3bAOO6vCvUO2DWRmWPGPAM)**")
st.write("07/2021 - 02/2023")
st.write(
    """
- ► Use Apache Superset to create dashboards
- ► Refactoring +1.2K line code-base using OOP
- ► Extract, and process FHIR data
- ► Creation and validation of test units
"""
)


# --- JOB 3 
st.write('\n')
st.write("🚧", "**Working Student - Data Science/Python development | [Universitätsmedizin Greifswald Greifswald](https://www.medizin.uni-greifswald.de/de/home/)**")
st.write("04/2015 - 01/2018")
st.write(
    """
- ► Translate SQL queries to pandas operations
- ► Analysing Medical Data
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader(":orange[Projects & Accomplishments]")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link[0]}) : {link[1]}")
