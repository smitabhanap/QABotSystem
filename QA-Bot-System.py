import streamlit as st
# Function to answer questions
def get_answer(question):
    # You can implement more sophisticated logic here based on your use case
    if question.lower() == 'what is your college name?':
        return "Ajeenkya D.Y.Patil College of Engineering"
    elif question.lower() == 'What is average percentage of students who get campus placement?':
        return "70%"
    elif question.lower() == 'what is intake capacity?':
        return "120"
    elif question.lower() == 'what is highest placement package offered to student ?':
        return "12 Lacks per annum"
    elif question.lower() == 'what is NAAC grade of college':
        return "A"
    elif question.lower() == 'how many companies come for campus placement yearly?':
        return "50"
    else:
        return "Sorry, I don't understand that question."

# Streamlit UI
def main():
    st.title("Question-Answer Chatbot")
    st.write("Ask me anything!")

    # User input for question
    question = st.text_input("You:", "")

    # Button to submit question
    if st.button("Ask"):
        # Get answer and display
        answer = get_answer(question)
        st.text_area("Bot:", value=answer, height=100)

if __name__ == "__main__":
    main()
