import streamlit as st

def set_page():
    st.set_page_config(page_title="How an Email Client Works", layout="wide")
    st.title("How an Email Client Works")

def introduction():
    st.markdown("""
    An **email client** is an application that allows users to send, receive, and organize emails. It communicates with email servers using standard protocols such as **SMTP**, **IMAP**, and **POP3**. Below is an in-depth explanation of how an email client operates step by step.
    """)

def display_step(step, content):
    with st.expander(f"{step}. {content['title']}"):
        st.markdown(content['text'])

def summary_workflow():
    st.subheader("Summary Workflow")
    st.markdown("""
    **1.** Account Setup → **2.** Retrieving Emails (IMAP/POP3) → **3.** Sending Emails (SMTP) → **4.** Organizing Emails → 
    **5.** Handling Attachments → **6.** Notifications → **7.** Security → **8.** Advanced Features
    """)

def footer():
    st.info("An email client simplifies and secures the management of electronic communication, offering tools to enhance productivity and connectivity.")

def main():
    set_page()
    introduction()

    steps = [
        {"title": "User Interface and Account Setup", "text": "..."},
        {"title": "Retrieving Emails (IMAP/POP3)", "text": "..."},
        # ... other steps ...
    ]

    for step in steps:
        display_step(steps.index(step) + 1, step)

    summary_workflow()
    footer()

if __name__ == "__main__":
    main()



