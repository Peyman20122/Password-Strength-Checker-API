from fastapi import FastAPI
import hashlib
import random
import string

app = FastAPI()

weak_passwords = ["123456", "password", "qwerty", "abc123", "letmein", "111111", "password1", "123123"]
weak_hashes = {hashlib.sha256(p.encode()).hexdigest(): p for p in weak_passwords}

def check_password_strength(password: str):
    score = 0
    if len(password) >= 8: score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c in "!@#$%^&*()-_+=" for c in password): score += 1
    return score

def generate_strong_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*()-_+="
    return ''.join(random.choice(chars) for _ in range(length))


@app.get("/check-password/{password}")
def check_password(password: str):
    password_hash = hashlib.sha256(password.encode()).hexdigest()

    if password_hash in weak_hashes:
        return {
            "password": password,
            "strength": "Very Weak",
            "suggested_password": generate_strong_password(),
            "message": "This password is weak and commonly used. Please choose a stronger one."
        }

    strength_score = check_password_strength(password)
    strength_levels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    strength = strength_levels[strength_score]

    return {
        "password": password,
        "strength": strength,
        "suggested_password": generate_strong_password() if strength_score < 3 else None,
        "message": "Consider using a stronger password." if strength_score < 3 else "Your password is strong!"
    }
