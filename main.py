import streamlit as st

# Page configuration
st.set_page_config(
    page_title="BMI Calculator",
    page_icon="🏥",
    layout="centered"
)

# Custom CSS for professional medical look
st.markdown("""
    <style>
    .main-header {
        text-align: center;
        color: #1e3a8a;
        padding: 20px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
        margin-bottom: 30px;
    }
    .main-header h1 {
        color: white;
        margin: 0;
        font-size: 2.5em;
    }
    .main-header p {
        color: #e0e7ff;
        margin: 10px 0 0 0;
    }
    .bmi-result {
        text-align: center;
        padding: 30px;
        border-radius: 10px;
        margin: 20px 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .bmi-value {
        font-size: 3em;
        font-weight: bold;
        margin: 10px 0;
    }
    .bmi-category {
        font-size: 1.5em;
        font-weight: 600;
        margin: 10px 0;
    }
    .recommendation-box {
        background-color: #f0f9ff;
        padding: 20px;
        border-radius: 10px;
        border-left: 4px solid #3b82f6;
        margin: 20px 0;
    }
    .disclaimer {
        background-color: #fef3c7;
        padding: 15px;
        border-radius: 8px;
        border-left: 4px solid #f59e0b;
        margin-top: 30px;
        font-size: 0.9em;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
    <div class="main-header">
        <h1>🏥 BMI Calculator</h1>
        <p>Body Mass Index Health Assessment Tool</p>
    </div>
""", unsafe_allow_html=True)

# Create two columns for inputs
col1, col2 = st.columns(2)

with col1:
    st.subheader("📏 Height")
    height_unit = st.radio("Unit", ["Centimeters (cm)", "Inches (in)"], key="height_unit")
    if height_unit == "Centimeters (cm)":
        height = st.number_input("Enter height", min_value=0.0, max_value=300.0, value=170.0, step=0.1)
        height_m = height / 100
    else:
        height = st.number_input("Enter height", min_value=0.0, max_value=120.0, value=67.0, step=0.1)
        height_m = height * 0.0254

with col2:
    st.subheader("⚖️ Weight")
    weight_unit = st.radio("Unit", ["Kilograms (kg)", "Pounds (lbs)"], key="weight_unit")
    if weight_unit == "Kilograms (kg)":
        weight = st.number_input("Enter weight", min_value=0.0, max_value=500.0, value=70.0, step=0.1)
        weight_kg = weight
    else:
        weight = st.number_input("Enter weight", min_value=0.0, max_value=1100.0, value=154.0, step=0.1)
        weight_kg = weight * 0.453592

# Calculate BMI button
if st.button("Calculate BMI", type="primary", use_container_width=True):
    if height_m > 0 and weight_kg > 0:
        # Calculate BMI
        bmi = weight_kg / (height_m ** 2)
        
        # Determine category and color
        if bmi < 18.5:
            category = "Underweight"
            color = "#3b82f6"
            bg_color = "#dbeafe"
            recommendation = """
            **Health Recommendations:**
            - Consult with a healthcare provider or nutritionist
            - Focus on nutrient-dense foods to gain weight healthily
            - Consider strength training exercises to build muscle mass
            - Ensure adequate calorie intake throughout the day
            - Monitor for any underlying health conditions
            """
        elif 18.5 <= bmi < 25:
            category = "Normal Weight"
            color = "#10b981"
            bg_color = "#d1fae5"
            recommendation = """
            **Health Recommendations:**
            - Maintain your current healthy lifestyle
            - Continue balanced nutrition and regular physical activity
            - Aim for 150 minutes of moderate exercise per week
            - Stay hydrated and get adequate sleep
            - Regular health check-ups for preventive care
            """
        elif 25 <= bmi < 30:
            category = "Overweight"
            color = "#f59e0b"
            bg_color = "#fef3c7"
            recommendation = """
            **Health Recommendations:**
            - Consider gradual weight loss through diet and exercise
            - Focus on whole foods and reduce processed food intake
            - Incorporate both cardio and strength training exercises
            - Set realistic weight loss goals (1-2 lbs per week)
            - Consult healthcare provider for personalized advice
            """
        else:
            category = "Obese"
            color = "#ef4444"
            bg_color = "#fee2e2"
            recommendation = """
            **Health Recommendations:**
            - Strongly recommend consultation with healthcare provider
            - Consider working with a registered dietitian
            - Develop a comprehensive weight management plan
            - Start with low-impact exercises and gradually increase intensity
            - Monitor blood pressure, cholesterol, and blood sugar levels
            - Consider joining a support group or weight management program
            """
        
        # Display result
        st.markdown(f"""
            <div class="bmi-result" style="background-color: {bg_color};">
                <p style="color: #64748b; margin: 0;">Your BMI is</p>
                <div class="bmi-value" style="color: {color};">{bmi:.1f}</div>
                <div class="bmi-category" style="color: {color};">{category}</div>
            </div>
        """, unsafe_allow_html=True)
        
        # BMI Range Reference
        st.markdown("### 📊 BMI Categories Reference")
        st.markdown("""
        - **Underweight:** BMI < 18.5
        - **Normal Weight:** BMI 18.5 - 24.9
        - **Overweight:** BMI 25 - 29.9
        - **Obese:** BMI ≥ 30
        """)
        
        # Display recommendations
        st.markdown(f"""
            <div class="recommendation-box">
                {recommendation}
            </div>
        """, unsafe_allow_html=True)
        
    else:
        st.error("Please enter valid height and weight values.")

# Disclaimer
st.markdown("""
    <div class="disclaimer">
        <strong>⚠️ Medical Disclaimer</strong><br>
        This BMI calculator is for educational and informational purposes only. 
        It should not be used as a substitute for professional medical advice, diagnosis, or treatment. 
        BMI is a general indicator and may not accurately reflect health status for athletes, pregnant women, 
        elderly individuals, or those with specific medical conditions. Always consult with a qualified 
        healthcare provider for personalized medical advice.
    </div>
""", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
    <p style="text-align: center; color: #64748b; font-size: 0.9em;">
        Made with ❤️ for health awareness | BMI Formula: weight(kg) / height(m)²
    </p>
""", unsafe_allow_html=True)
