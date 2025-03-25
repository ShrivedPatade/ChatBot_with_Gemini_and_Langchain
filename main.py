import google.generativeai as genai

genai.configure(api_key="GRNAI_API_KEY_HERE")
confirmer = genai.GenerativeModel("gemini-1.5-flash")
model = genai.GenerativeModel("gemini-1.5-flash")

def chatMedical(prompt):
    if int(confirmer.generate_content("Return '1' if the question after ',' is medical field related else '0' , "+prompt).text):
        response = model.generate_content(prompt).text
    else:
        response = "Your response doesn't seem to be Medical Field related. \nI am a Medical Field based Chat Bot, ask me anything related to it 😁."
    return response
        
    
print(chatMedical("how are you"))
