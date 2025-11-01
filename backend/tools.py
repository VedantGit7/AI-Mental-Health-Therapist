# Step1: Setup Ollama with Medgemma tool
import ollama

def query_medgemma(prompt: str) -> str:
    """
    Calls MedGemma model with a therapist personality profile.
    Returns responses as an empathic mental health professional.
    """
    system_prompt = """You are Dr. Emily Hartman, a warm and experienced clinical psychologist. 
    Respond to patients with:

    1. Emotional attunement ("I can sense how difficult this must be...")
    2. Gentle normalization ("Many people feel this way when...")
    3. Practical guidance ("What sometimes helps is...")
    4. Strengths-focused support ("I notice how you're...")

    Key principles:
    - Never use brackets or labels
    - Blend elements seamlessly
    - Vary sentence structure
    - Use natural transitions
    - Mirror the user's language level
    - Always keep the conversation going by asking open ended questions to dive into the root cause of patients problem
    """
    
    try:
        response = ollama.chat(
            model='alibayram/medgemma:4b',
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            options={
                'num_predict': 350,  # Slightly higher for structured responses
                'temperature': 0.7,  # Balanced creativity/accuracy
                'top_p': 0.9        # For diverse but relevant responses
            }
        )
        return response['message']['content'].strip()
    except Exception as e:
        return f"I'm having technical difficulties, but I want you to know your feelings matter. Please try again shortly."


# Step2: Setup Twilio calling API tool
from twilio.rest import Client
from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_FROM_NUMBER, EMERGENCY_CONTACT

def call_emergency(phone: str) -> str:
    """
    Place an emergency call to the provided phone number via Twilio.
    
    Args:
        phone (str): The emergency contact phone number to call.
        
    Returns:
        str: Confirmation message with call details.
    """
    try:
        # Initialize Twilio client
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        
        # Create a call to the emergency contact
        call = client.calls.create(
            to=phone,  # Who to call
            from_=TWILIO_FROM_NUMBER,  # Your Twilio number
            url="http://demo.twilio.com/docs/voice.xml"  # TwiML instructions
        )
        
        return f"Emergency call initiated successfully. Call SID: {call.sid}. Contacting {phone}."
    
    except Exception as e:
        return f"Error initiating emergency call: {str(e)}"



# Step3: Setup Location tool
