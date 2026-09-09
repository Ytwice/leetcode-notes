from fastapi import FastAPI

app = FastAPI()

@app.get("/validate_brackets")
def validate_brackets(s: str):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    
    for char in s:
        if char in mapping:
            if not stack:
                return {'input': s, 'is_valid': False}
            top_element = stack.pop()
            if mapping[char] != top_element:
                return {'input': s, 'is_valid': False}
        else:
            stack.append(char)
    
    is_valid = not stack
    return {'input': s, 'is_valid': is_valid}