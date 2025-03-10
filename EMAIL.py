import streamlit as st
import google.generativeai as genai

# Configure Gemini API Key (Replace with your actual key)
GEMINI_API_KEY = "AIzaSyDXQR1Sq9kiEtEChOBEYfzcs76tGq16rJQ"
genai.configure(api_key=GEMINI_API_KEY)

# Function to generate personalized email using Gemini AI
def generate_email(recipient_name, event_name, special_instructions):
    prompt = f"Write a professional and personalized email to {recipient_name} about the upcoming {event_name}. Include these special instructions: {special_instructions}."

    try:
        model = genai.GenerativeModel("gemini-1.5-pro-latest")
        response = model.generate_content(prompt)
        return response.text.strip() if response else "Error: No response from AI."
    except Exception as e:
        return f"⚠ Error generating email: {str(e)}"

# Streamlit app layout
def main():
    st.title("📧 AI Personalized Email Generator")
    st.write("Generate professional, AI-powered emails instantly!")

    # Input fields for user data
    recipient_name = st.text_input("Recipient's Name")
    event_name = st.text_input("Event Name")
    special_instructions = st.text_area("Special Instructions (Optional)")

    if st.button("Generate Email"):
        if recipient_name and event_name:
            # Generate the personalized email
            email_body = generate_email(recipient_name, event_name, special_instructions)
            
            # Display the generated email
            st.subheader("Generated Email:")
            st.text_area("Your Email", value=email_body, height=300)
        else:
            st.error("⚠ Please enter both recipient's name and event name.")

# Run the Streamlit app
if __name__ == "__main__":
    main()
