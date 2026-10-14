# 🏫 CampusGuard AI: Autonomous School Zone Safety Panel

CampusGuard AI is an innovative crowd-sourced infrastructure auditing solution engineered to protect students during their daily commutes. The application transforms standard smartphone dashcams or transit vehicle cameras into passive 24/7 public asset safety inspectors. By streaming localized video data blocks directly to Google's multimodal **Gemini 1.5 Flash** model, the platform automatically converts raw visual telemetry feeds into clean, structured asset-repair directives on a live municipal command dashboard—completely removing manual driver reporting friction.

## 🚀 Key Innovation Highlights
- 📍 **Live Geospatial GIS Mapping:** Integrates dynamic map views via Leaflet to plot active infrastructure anomaly locations in real-time.
- ⚙️ **Frictionless Crowd-Sourced Auditing:** Shifts structural field reporting from active manual forms to fully automated background tracking.
- 🤖 **Structured Gemini Inference Data:** Leverages low-variance Gemini JSON mapping schemas to extract high-accuracy technical public works repair commands.

## 🛠️ Software Infrastructure Stack
- **Frontend Layer:** HTML5, CSS3 Grid Architectures, JavaScript ES6 Async Engine, Leaflet GIS Scripting.
- **Backend Frame:** Node.js Web App Stack environment running on Express.
- **AI Core integration:** Official Google GenAI SDK linking straight to Gemini 1.5 Flash API models.

## 💻 Local Workspace Launch Instructions

Follow these configuration rules to boot the prototype hub live on your computer:

1. **Install Module Dependencies:**
   Run this inside your project folder directory space to download all required code assets:
   ```bash
   npm install
   ```

2. **Inject Your Google AI Studio API Secret Token Key:**
   Configure your secure authentication variables inside your terminal terminal line:
   ```powershell
   \$env:GEMINI_API_KEY="YOUR_ACTUAL_GOOGLE_STUDIO_KEY_HERE"
   ```

3. **Fire Up the Engine Web Server:**
   Launch the microservices runtime thread locally:
   ```bash
   node server.js
   ```

4. **Access the Operations Portal Layout Dashboard:**
   Open your default internet web browser app grid and navigate to the web route address line:
   👉 http://localhost:3000
