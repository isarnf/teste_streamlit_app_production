import streamlit as st
import hashlib

# Set page config
st.set_page_config(page_title="Protected App", page_icon="🔒")

# Password configuration (you can change this)
CORRECT_PASSWORD = "123admin321"  # Change this to your desired password

def hash_password(password):
    """Hash password for security"""
    return hashlib.sha256(password.encode()).hexdigest()

def check_password():
    """Returns True if the user entered the correct password"""
    def password_entered():
        """Checks whether a password entered by the user is correct"""
        if hash_password(st.session_state["password"]) == hash_password(CORRECT_PASSWORD):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the password
        else:
            st.session_state["password_correct"] = False

    # Return True if the password is validated
    if st.session_state.get("password_correct", False):
        return True

    # Show input for password
    st.markdown("## 🔒 Login Required")
    st.markdown("Please enter the password to access the application:")
    
    st.text_input(
        "Password", 
        type="password", 
        on_change=password_entered, 
        key="password",
        placeholder="Enter password..."
    )
    
    if "password_correct" in st.session_state:
        if not st.session_state["password_correct"]:
            st.error("❌ Incorrect password. Please try again.")
    
    st.markdown("---")
    
    
    return False

# Main app logic
if check_password():
    # Show logout button in sidebar
    with st.sidebar:
        st.markdown("### Welcome! 👋")
        if st.button("🚪 Logout"):
            # Clear session state to logout
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
    
    # Your main app content here
    st.title("Hello World! 🌍")
    st.markdown("Welcome to the protected application!")

    name = st.text_input("What's your name?")

    if name:
        st.write(f"Hello, {name}! 👋")

    if st.button("Click me"):
        st.write("Button clicked! 🎉")
        
    # Additional protected content
    with st.expander("📊 Protected Content"):
        st.write("This content is only visible to authenticated users!")
        st.success("You have successfully logged in!")
