# =========================================
# ENGLISH REPORT COMMENT GENERATOR - End of Year
# Year 7, British National Curriculum
# =========================================

import random
import streamlit as st
from docx import Document

TARGET_CHARS = 499

from eoy_statements import (
    eoy_opening_phrases,
    eoy_attitude_bank,
    eoy_reading_bank,
    eoy_writing_bank,
    eoy_reading_target_bank,
    eoy_writing_target_bank,
    eoy_closer_bank
)


# ---------- HELPERS ----------
def get_pronouns(gender):
    gender = gender.lower()
    if gender == "male":
        return "he", "his"
    elif gender == "female":
        return "she", "her"
    return "they", "their"

def lowercase_first(text):
    return text[0].lower() + text[1:] if text else ""

def truncate_comment(comment, target=TARGET_CHARS):
    if len(comment) <= target:
        return comment
    truncated = comment[:target].rstrip(" ,;.")
    if "." in truncated:
        truncated = truncated[:truncated.rfind(".")+1]
    return truncated

def replace_name_placeholder(text, name):
    return text.replace("{name}", name)

def fix_gender(text, p):
    if p == "he":
        text = text.replace(" she ", " he ").replace(" her ", " his ").replace(" her.", " him.")
        text = text.replace("her own", "his own").replace("her progress", "his progress")
        text = text.replace("her engagement", "his engagement").replace("her confidence", "his confidence")
        text = text.replace("her ability", "his ability").replace("her approach", "his approach")
    elif p == "they":
        text = text.replace(" she ", " they ").replace(" her ", " their ").replace(" her.", " them.")
        text = text.replace("her own", "their own").replace("her progress", "their progress")
        text = text.replace("her engagement", "their engagement").replace("her confidence", "their confidence")
        text = text.replace("her ability", "their ability").replace("her approach", "their approach")
    return text

def generate_eoy_comment(name, att, read, write, read_t, write_t, pronouns, attitude_target=None):
    p, p_poss = pronouns
    opening = random.choice(eoy_opening_phrases)

    attitude_sentence    = f"{opening} {name} {fix_gender(eoy_attitude_bank[att], p)}."
    reading_sentence     = f"In reading, {p} {fix_gender(eoy_reading_bank[read], p)}."
    writing_sentence     = f"In writing, {p} {fix_gender(eoy_writing_bank[write], p)}."
    reading_target_sentence = f"Going into Year 8, {p} should {lowercase_first(eoy_reading_target_bank[read_t])}."
    writing_target_sentence = f"In writing, {p} should {lowercase_first(eoy_writing_target_bank[write_t])}."
    closer_sentence      = replace_name_placeholder(random.choice(eoy_closer_bank), name)

    comment_parts = [
        attitude_sentence,
        reading_sentence,
        writing_sentence,
        reading_target_sentence,
        writing_target_sentence,
    ]

    if attitude_target:
        at = attitude_target.strip()
        if not at.endswith("."):
            at += "."
        comment_parts.append(at)

    comment_parts.append(closer_sentence)

    return truncate_comment(" ".join(comment_parts), TARGET_CHARS)


# ---------- APP ----------
st.title("Year 7 English — End of Year Report Comment Generator")
st.markdown("Fill in the student details and click **Generate Comment**.")

EOY_BANDS = [100, 90, 80, 70, 60, 50, 40, 30]

if 'eoy_comments' not in st.session_state:
    st.session_state['eoy_comments'] = []

with st.form("eoy_form"):
    name        = st.text_input("Student Name")
    gender      = st.selectbox("Gender", ["Female", "Male"])
    att         = st.selectbox("Attitude band", EOY_BANDS)
    read        = st.selectbox("Reading achievement band", EOY_BANDS)
    write       = st.selectbox("Writing achievement band", EOY_BANDS)
    read_t      = st.selectbox("Reading target band", EOY_BANDS)
    write_t     = st.selectbox("Writing target band", EOY_BANDS)
    att_target  = st.text_input("Optional Attitude Next Steps (appears last)")
    submitted   = st.form_submit_button("Generate Comment")

if submitted and name:
    pronouns = get_pronouns(gender)
    comment  = generate_eoy_comment(name, att, read, write, read_t, write_t, pronouns, att_target)
    st.text_area("Generated Comment", comment, height=200)
    st.write(f"Character count: {len(comment)} / {TARGET_CHARS}")
    st.session_state['eoy_comments'].append(f"{name}: {comment}")

if st.session_state['eoy_comments']:
    st.markdown("### All Generated Comments")
    for c in st.session_state['eoy_comments']:
        st.write(c)

    if st.button("Download as Word Document"):
        doc = Document()
        for c in st.session_state['eoy_comments']:
            doc.add_paragraph(c)
        file_name = "EOY_English_Report_Comments.docx"
        doc.save(file_name)
        with open(file_name, "rb") as f:
            st.download_button(
                label="Download Word File",
                data=f,
                file_name=file_name,
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )
