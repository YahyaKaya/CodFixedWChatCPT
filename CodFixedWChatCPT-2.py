import requests
import openai

code = input("User: ")

def check_code(code):
    try:
        exec(code)
        return True
    except:
        return False

def fix_code(code):
    response = requests.post("https://api.openai.com/v1/engines/text-davinci-002/completions",
                             headers={
                                 "Content-Type": "application/json",
                                 "Authorization": "Bearer KEY"
                             },
                             json={
                                 "prompt": f"Fix the following code in python: {code} (Just write the fixed code)",
                                 "max_tokens": 2048,
                                 "n": 1,
                                 "stop": None,
                                 "temperature": 0.5,
                             })                      
    if response.status_code == 200:
        return response.json()["choices"][0]["text"]
    else:
        return "Failed"

if check_code(code):
    print("The code is correct")
else:
    fixed_code = fix_code(code)
    print("Fixed code:", fixed_code)
    exec(fixed_code)
