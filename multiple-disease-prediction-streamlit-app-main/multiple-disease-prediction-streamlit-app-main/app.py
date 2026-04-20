import os
import pickle
import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
from streamlit_option_menu import option_menu

# --- ১. পেজ কনফিগারেশন ---
st.set_page_config(page_title="Health Assistant", layout="wide", page_icon="🧑‍⚕️")

# --- ২. ডাটাবেস (YAML) সেটআপ ---
if not os.path.exists('config.yaml'):
    with open('config.yaml', 'w') as file:
        yaml.dump({'credentials': {'usernames': {}}}, file)

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# অথেন্টিকেটর অবজেক্ট
authenticator = stauth.Authenticate(
    config['credentials'],
    'health_assistant_cookie',
    'auth_key',
    cookie_expiry_days=30
)

# সাইডবারে অ্যাকশন মেনু
st.sidebar.title("User Portal")
auth_selection = st.sidebar.selectbox("Select Action", ["Login", "Sign Up"])

# --- ৩. সাইন আপ লজিক ---
if auth_selection == "Sign Up":
    try:
        result = authenticator.register_user(location='main')
        if result:
            email, username, name = result
            if email:
                with open('config.yaml', 'w') as file:
                    yaml.dump(config, file, default_flow_style=False)
                
                st.session_state["authentication_status"] = True
                st.session_state["name"] = name
                st.session_state["username"] = username
                st.success(f'Welcome {name}! Registration successful. Redirecting...')
                st.rerun() 
    except Exception as e:
        st.error(e)

# --- ৪. লগইন প্রসেস ---
elif auth_selection == "Login":
    authenticator.login(location='main')

# --- ৫. মেইন অ্যাপ ড্যাশবোর্ড ---
if st.session_state.get("authentication_status"):
    # লগআউট বাটন সাইডবারে
    authenticator.logout('Logout', 'sidebar')
    st.sidebar.success(f"Logged in as: {st.session_state['name']}")

    # কাজের ডিরেক্টরি এবং মডেল লোড (এরর হ্যান্ডলিং সহজ করা হয়েছে)
    working_dir = os.path.dirname(os.path.abspath(__file__))
    
    try:
        # এখানে 'saved_models' ফোল্ডার পাথ নিশ্চিত করা হয়েছে
        diabetes_model = pickle.load(open(f'{working_dir}/saved_models/diabetes_model.sav', 'rb'))
        heart_disease_model = pickle.load(open(f'{working_dir}/saved_models/heart_disease_model.sav', 'rb'))
        parkinsons_model = pickle.load(open(f'{working_dir}/saved_models/parkinsons_model.sav', 'rb'))
    except FileNotFoundError:
        st.error("Model files not found! Please ensure 'saved_models' folder exists with .sav files.")
    except Exception as e:
        st.error(f"Error loading models: {e}")

    # মেইন নেভিগেশন মেনু
    selected = option_menu(
        menu_title='Multiple Disease Prediction System',
        options=['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
        icons=['activity', 'heart', 'person'],
        menu_icon='hospital-fill',
        default_index=0,
        orientation="horizontal"
    )

    # --- Diabetes Prediction ---
    if selected == 'Diabetes Prediction':
        st.title('Diabetes Prediction using ML')
        col1, col2, col3 = st.columns(3)
        with col1: Pregnancies = st.text_input('Number of Pregnancies', value="0")
        with col2: Glucose = st.text_input('Glucose Level', value="0")
        with col3: BloodPressure = st.text_input('Blood Pressure value', value="0")
        with col1: SkinThickness = st.text_input('Skin Thickness value', value="0")
        with col2: Insulin = st.text_input('Insulin Level', value="0")
        with col3: BMI = st.text_input('BMI value', value="0")
        with col1: DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value', value="0")
        with col2: Age = st.text_input('Age', value="0")

        if st.button('Diabetes Test Result'):
            try:
                user_input = [float(x) for x in [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]
                prediction = diabetes_model.predict([user_input])
                if prediction[0] == 1:
                    st.error('The person is diabetic')
                else:
                    st.success('The person is not diabetic')
            except NameError:
                st.error("Model not loaded properly. Check the file path.")
            except Exception as e:
                st.error(f"Error: {e}")

    # --- Heart Disease Prediction ---
    elif selected == 'Heart Disease Prediction':
        st.title('Heart Disease Prediction using ML')
        col1, col2, col3 = st.columns(3)
        with col1: age = st.text_input('Age', value="0")
        with col2: sex = st.text_input('Sex (1=M, 0=F)', value="0")
        with col3: cp = st.text_input('Chest Pain types', value="0")
        with col1: trestbps = st.text_input('Resting Blood Pressure', value="0")
        with col2: chol = st.text_input('Serum Cholestoral', value="0")
        with col3: fbs = st.text_input('Fasting Blood Sugar > 120', value="0")
        with col1: restecg = st.text_input('Resting ECG results', value="0")
        with col2: thalach = st.text_input('Max Heart Rate', value="0")
        with col3: exang = st.text_input('Exercise Induced Angina', value="0")
        with col1: oldpeak = st.text_input('ST depression', value="0")
        with col2: slope = st.text_input('Slope of ST segment', value="0")
        with col3: ca = st.text_input('Major vessels (0-3)', value="0")
        with col1: thal = st.text_input('thal: 0=normal; 1=fixed; 2=reversable', value="0")

        if st.button('Heart Disease Test Result'):
            try:
                user_input = [float(x) for x in [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
                prediction = heart_disease_model.predict([user_input])
                if prediction[0] == 1:
                    st.error('The person has heart disease')
                else:
                    st.success('The person does not have heart disease')
            except Exception as e:
                st.error(f"Error: {e}")

    # --- Parkinson's Prediction ---
    elif selected == "Parkinsons Prediction":
        st.title("Parkinson's Disease Prediction using ML")
        features = ['MDVP:Fo(Hz)','MDVP:Fhi(Hz)','MDVP:Flo(Hz)','MDVP:Jitter(%)','MDVP:Jitter(Abs)','MDVP:RAP','MDVP:PPQ','Jitter:DDP','MDVP:Shimmer','MDVP:Shimmer(dB)','Shimmer:APQ3','Shimmer:APQ5','MDVP:APQ','Shimmer:DDA','NHR','HNR','RPDE','DFA','spread1','spread2','D2','PPE']
        cols = st.columns(5)
        user_vals = []
        for i, f in enumerate(features):
            with cols[i % 5]:
                user_vals.append(st.text_input(f, value="0"))

        if st.button("Parkinson's Test Result"):
            try:
                user_input = [float(x) for x in user_vals]
                prediction = parkinsons_model.predict([user_input])
                if prediction[0] == 1:
                    st.error("The person has Parkinson's")
                else:
                    st.success("The person does not have Parkinson's")
            except Exception as e:
                st.error(f"Error: {e}")

elif st.session_state.get("authentication_status") is False:
    st.error('Username or Password incorrect')
elif st.session_state.get("authentication_status") is None and auth_selection == "Login":
    st.info('Please enter your credentials.')