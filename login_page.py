import streamlit as st
import streamlit.components.v1 as components
import time

st.set_page_config(page_title="Secure Access", page_icon="✨", layout="centered")

# --- BACKGROUND COMPONENT ---
molten_html = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body, html { margin: 0; padding: 0; width: 100vw; height: 100vh; overflow: hidden; background-color: #050510; }
        canvas { display: block; width: 100vw; height: 100vh; }
    </style>
</head>
<body>
    <div id="molten-container" style="width: 100%; height: 100%;"></div>
    
    <script>
        // Break out of the iframe and style it to be a full-screen fixed background
        try {
            const frame = window.frameElement;
            if (frame) {
                frame.style.position = 'fixed';
                frame.style.top = '0';
                frame.style.left = '0';
                frame.style.width = '100vw';
                frame.style.height = '100vh';
                frame.style.zIndex = '-1';
                frame.style.border = 'none';
                
                // Also remove padding from its parent container in Streamlit
                frame.parentElement.style.padding = '0';
                frame.parentElement.style.margin = '0';
            }
        } catch (e) {
            console.error(e);
        }
    </script>
    
    <script type="module">
        // Import OGL from unpkg
        import { Renderer, Program, Mesh, Triangle } from 'https://unpkg.com/ogl@1.0.11/src/index.mjs';

        const hexToRgb = hex => {
          const result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
          if (!result) return [1, 1, 1];
          return [parseInt(result[1], 16) / 255, parseInt(result[2], 16) / 255, parseInt(result[3], 16) / 255];
        };

        const vertex = `#version 300 es
        in vec2 position;
        void main() {
          gl_Position = vec4(position, 0.0, 1.0);
        }`;

        const fragment = `#version 300 es
        precision highp float;
        uniform vec2 iResolution;
        uniform float iTime;
        uniform float uSpeed;
        uniform float uScale;
        uniform float uDetail;
        uniform float uGlow;
        uniform float uCoreSize;
        uniform float uSwirl;
        uniform float uFold;
        uniform float uBlackPoint;
        uniform float uBrightness;
        uniform float uColorMode;
        uniform float uGrain;
        uniform float uGrainIntensity;
        uniform float uOpacity;
        uniform vec2 uMouse;
        uniform float uMouseStrength;
        uniform bool uEnableMouse;
        uniform vec3 uColor1;
        uniform vec3 uColor2;
        uniform vec3 uColor3;
        out vec4 fragColor;

        float hash(vec2 p) {
          return fract(sin(dot(p, vec2(12.9898, 78.233))) * 43758.5453);
        }

        void main() {
          float time = iTime * uSpeed;
          vec2 p = uScale * ((gl_FragCoord.xy - 0.5 * iResolution.xy) / iResolution.y) - 0.5;

          vec2 drift = vec2(0.0);
          if (uEnableMouse) {
            drift = (uMouse - 0.5) * uMouseStrength * 2.0;
          }
          p += drift;

          vec2 i = p;
          float c = 0.0;
          float r = length(p + vec2(sin(time), sin(time * 0.3 + 5.0)) * 0.5);
          float d = length(p);
          float rot = d + time + p.x * uSwirl;

          float cosRot = cos(rot);
          mat2 warp = mat2(cos(rot - sin(time / 5.0)), sin(rot), -sin(cosRot - time), cosRot) * uFold;
          float glowCore = uGlow * uCoreSize;

          for (float n = 0.0; n < 8.0; n++) {
            if (n >= uDetail) break;
            p *= warp;
            float t = r - time / (n + 3.0);
            i -= p + vec2(cos(t - i.x - r) + sin(t + i.y), sin(t - i.y) + cos(t + i.x) + r);
            c += glowCore / length(vec2(sin(i.x + t), cos(i.y + t)));
          }

          c /= 6.0;
          float intensity = max(c - uBlackPoint, 0.0) * uBrightness;
          float g = clamp(intensity, 0.0, 1.0);

          float mid = 0.5;
          if (uColorMode > 1.5) {
            mid = 0.65;
          } else if (uColorMode > 0.5) {
            mid = 0.35;
          }

          vec3 col = mix(uColor1, uColor2, smoothstep(0.0, mid, g));
          col = mix(col, uColor3, smoothstep(mid, 1.0, g));

          float a = g;
          if (uGrain > 0.5) {
            float gr = hash(gl_FragCoord.xy + iTime);
            a += (gr - 0.5) * uGrainIntensity;
          }
          a = clamp(a, 0.0, 1.0) * uOpacity;
          fragColor = vec4(col * a, a);
        }`;

        const container = document.getElementById('molten-container');
        const renderer = new Renderer({
          webgl: 2,
          alpha: true,
          premultipliedAlpha: true,
          antialias: false,
          dpr: Math.min(window.devicePixelRatio || 1, 2)
        });

        const gl = renderer.gl;
        gl.clearColor(0, 0, 0, 0);
        container.appendChild(gl.canvas);

        const geometry = new Triangle(gl);
        
        // Setup configuration based on React props defaults
        const c1 = hexToRgb('#5227FF');
        const c2 = hexToRgb('#FF9FFC');
        const c3 = hexToRgb('#FFFFFF');

        const program = new Program(gl, {
          vertex,
          fragment,
          uniforms: {
            iTime: { value: 0 },
            iResolution: { value: new Float32Array([1, 1]) },
            uSpeed: { value: 0.35 },
            uScale: { value: 4 },
            uDetail: { value: 3 },
            uGlow: { value: 1.6 },
            uCoreSize: { value: 0.1 },
            uSwirl: { value: 1 },
            uFold: { value: -0.2 },
            uBlackPoint: { value: 0.05 },
            uBrightness: { value: 1.3 },
            uColorMode: { value: 0 },
            uGrain: { value: 1 },
            uGrainIntensity: { value: 0.05 },
            uOpacity: { value: 1.0 },
            uMouse: { value: new Float32Array([0.5, 0.5]) },
            uMouseStrength: { value: 0.3 },
            uEnableMouse: { value: true },
            uColor1: { value: new Float32Array(c1) },
            uColor2: { value: new Float32Array(c2) },
            uColor3: { value: new Float32Array(c3) }
          }
        });

        const mesh = new Mesh(gl, { geometry, program });

        const setSize = () => {
          const w = window.innerWidth;
          const h = window.innerHeight;
          renderer.setSize(w, h);
          program.uniforms.iResolution.value[0] = gl.drawingBufferWidth;
          program.uniforms.iResolution.value[1] = gl.drawingBufferHeight;
        };
        window.addEventListener('resize', setSize);
        setSize();

        const targetMouse = [0.5, 0.5];
        const currentMouse = [0.5, 0.5];

        document.addEventListener('mousemove', e => {
          targetMouse[0] = e.clientX / window.innerWidth;
          targetMouse[1] = 1.0 - (e.clientY / window.innerHeight);
        });

        const t0 = performance.now();
        const loop = t => {
          program.uniforms.iTime.value = (t - t0) * 0.001;
          currentMouse[0] += 0.05 * (targetMouse[0] - currentMouse[0]);
          currentMouse[1] += 0.05 * (targetMouse[1] - currentMouse[1]);
          program.uniforms.uMouse.value[0] = currentMouse[0];
          program.uniforms.uMouse.value[1] = currentMouse[1];
          renderer.render({ scene: mesh });
          requestAnimationFrame(loop);
        };
        requestAnimationFrame(loop);
    </script>
</body>
</html>
"""

# Inject the background
components.html(molten_html, height=0, width=0)
# ----------------------------

# Initialize state
if 'users' not in st.session_state:
    st.session_state['users'] = {
        "admin": "password123",
        "genz": "vibes"
    }

if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

if 'view' not in st.session_state:
    st.session_state['view'] = 'login'

if 'loaded' not in st.session_state:
    st.session_state['loaded'] = False

# Stable CSS for Glassmorphism + Cursor + Hide instructions
css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;500;700&display=swap');

/* Apply custom cursor globally */
* {
    cursor: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32"><polygon points="3,3 3,25 8,20 12,28 16,26 12,18 19,18" fill="%23ff66b2"/><polygon points="0,0 0,22 5,17 9,25 13,23 9,15 16,15" fill="white" stroke="black" stroke-width="2" stroke-linejoin="miter"/></svg>') 0 0, auto !important;
}

.stApp {
    background-color: transparent !important;
    font-family: 'Inter', sans-serif;
}

/* Hide top padding for a cleaner look */
.block-container {
    padding-top: 2rem !important;
}

#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}

/* HIDE THE INPUT INSTRUCTIONS OVERLAP (e.g. "Press Enter to submit form") */
div[data-testid="InputInstructions"] {
    display: none !important;
}

/* Ensure padding on inputs accommodates the eye icon without overlap */
div[data-testid="stTextInput"] input {
    padding-right: 2.5rem !important;
}

/* Apply Glassmorphism cleanly to the st.form container itself */
[data-testid="stForm"] {
    background: rgba(255, 255, 255, 0.05) !important;
    border: 1px solid rgba(255, 255, 255, 0.15) !important;
    border-radius: 20px !important;
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37) !important;
    backdrop-filter: blur(20px) !important;
    -webkit-backdrop-filter: blur(20px) !important;
    padding: 2.5rem !important;
    margin-top: 10vh !important;
}

/* Loading container */
.loading-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 60vh;
}

@keyframes pulse {
    0% { opacity: 0.5; transform: scale(0.95); }
    50% { opacity: 1; transform: scale(1.05); }
    100% { opacity: 0.5; transform: scale(0.95); }
}

.loading-text {
    color: white;
    font-size: 2rem;
    font-weight: 700;
    letter-spacing: 4px;
    animation: pulse 1.5s infinite;
    text-transform: uppercase;
}

/* Input Fields */
div[data-testid="stTextInput"] input {
    background-color: rgba(255, 255, 255, 0.08) !important;
    border: 1px solid rgba(255, 255, 255, 0.2) !important;
    border-radius: 8px !important;
    color: #fff !important;
    padding: 0.75rem !important;
}

div[data-testid="stTextInput"] input:focus {
    border: 1px solid rgba(255, 255, 255, 0.5) !important;
    box-shadow: 0 0 10px rgba(255, 255, 255, 0.1) !important;
}

div[data-testid="stTextInput"] label {
    color: rgba(255, 255, 255, 0.9) !important;
    font-weight: 500 !important;
    font-size: 0.9rem !important;
}

/* Primary Submit Button inside Form */
div[data-testid="stFormSubmitButton"] button {
    background: linear-gradient(135deg, rgba(204, 0, 255, 0.8), rgba(0, 255, 255, 0.8)) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 8px !important;
    font-weight: 700 !important;
    font-size: 1rem !important;
    padding: 0.75rem 2rem !important;
    width: 100% !important;
    transition: all 0.3s ease !important;
    margin-top: 1rem !important;
    box-shadow: 0 4px 15px rgba(204, 0, 255, 0.4) !important;
}

div[data-testid="stFormSubmitButton"] button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(0, 255, 255, 0.6) !important;
}

/* Secondary Toggle Buttons */
div[data-testid="stButton"] button {
    background: transparent !important;
    color: #00ffff !important;
    border: 1px solid rgba(0, 255, 255, 0.5) !important;
    border-radius: 20px !important;
    font-size: 0.9rem !important;
    padding: 0.5rem 1.5rem !important;
    margin-top: -1rem !important;
    display: block !important;
    margin-left: auto !important;
    margin-right: auto !important;
}

div[data-testid="stButton"] button:hover {
    background: rgba(0, 255, 255, 0.1) !important;
    border-color: #00ffff !important;
}

h2, p {
    color: white !important;
}
</style>
"""
st.markdown(css, unsafe_allow_html=True)

if not st.session_state['loaded']:
    # Show loading screen
    st.markdown("""
    <div class="loading-container">
        <div class="loading-text">LOADING MAINFRAME...</div>
    </div>
    """, unsafe_allow_html=True)
    
    time.sleep(2)
    st.session_state['loaded'] = True
    st.rerun()

elif st.session_state['authenticated']:
    st.markdown("<h1 style='color: white;'>Welcome to the Mainframe 🚀</h1>", unsafe_allow_html=True)
    st.write("You have successfully logged in.")
    if st.button("Logout"):
        st.session_state['authenticated'] = False
        st.rerun()

else:
    # Use columns for layout control
    col1, col2, col3 = st.columns([1, 6, 1])
    
    with col2:
        if st.session_state['view'] == 'login':
            with st.form("login_form"):
                st.markdown("<h2 style='text-align: center;'>Sign In</h2>", unsafe_allow_html=True)
                username = st.text_input("Username")
                password = st.text_input("Password", type="password")
                
                submitted = st.form_submit_button("LOGIN")
                if submitted:
                    if not username or not password:
                        st.error("Fields cannot be empty.")
                    elif username in st.session_state['users'] and st.session_state['users'][username] == password:
                        st.session_state['authenticated'] = True
                        st.rerun()
                    else:
                        st.error("Invalid credentials.")
            
            st.write("")
            if st.button("Need an account? Register here"):
                st.session_state['view'] = 'register'
                st.rerun()
                
        else:
            with st.form("register_form"):
                st.markdown("<h2 style='text-align: center;'>Create Account</h2>", unsafe_allow_html=True)
                new_user = st.text_input("Choose Username")
                new_pass = st.text_input("Choose Password", type="password")
                confirm_pass = st.text_input("Confirm Password", type="password")
                
                registered = st.form_submit_button("REGISTER")
                if registered:
                    if not new_user or not new_pass:
                        st.error("Fields cannot be empty.")
                    elif new_user in st.session_state['users']:
                        st.error("Username already exists!")
                    elif new_pass != confirm_pass:
                        st.error("Passwords do not match!")
                    else:
                        st.session_state['users'][new_user] = new_pass
                        st.success("Account created successfully! Please log in.")
                        time.sleep(1.5)
                        st.session_state['view'] = 'login'
                        st.rerun()

            st.write("")
            if st.button("Already have an account? Log in"):
                st.session_state['view'] = 'login'
                st.rerun()
