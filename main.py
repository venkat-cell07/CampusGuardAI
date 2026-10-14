import os
import json
from google import genai
from google.genai import types

# Initialize the Gemini Client
client = genai.Client()

def analyze_school_zone_video(video_path: str, telemetry_data: dict) -> dict:
    print(f"Uploading {video_path} to Gemini API...")
    video_file = client.files.upload(file=video_path)
    
    prompt = f"""
    You are an advanced AI vision system for CampusGuard AI. 
    Analyze this video snippet captured from a vehicle driving through a school zone.
    Identify any infrastructure hazards like faded crosswalks, broken flashing signs, or blocked paths.
    Context data: {json.dumps(telemetry_data)}
    
    Return your analysis strictly following this JSON structure:
    {{
        "hazard_detected": true/false,
        "hazard_type": "faded_crosswalk" | "obscured_sign" | "broken_signal" | "sidewalk_damage" | "other",
        "severity": "low" | "medium" | "high",
        "description": "Short description.",
        "recommended_action": "What needs to be fixed."
    }}
    """
    
    response = client.models.generate_content(
        model='gemini-1.5-flash',
        contents=[video_file, prompt],
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            temperature=0.1
        ),
    )
    client.files.delete(name=video_file.name)
    return json.loads(response.text)

if __name__ == "__main__":
    sample_telemetry = {
        "current_gps": "16.4253, 80.5312",
        "nearest_school": "Oakridge International School Zone",
        "timestamp": "2026-10-14T08:34:00Z"
    }
    print("Backend ready. Run with your video file.")
