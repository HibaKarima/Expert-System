import sys
import pathlib
import streamlit as st

PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from fuzzy.inference import run_inference


def confidence_label(value: float) -> str:
    if value >= 75:
        return "High"
    if value >= 40:
        return "Medium"
    return "Low"


st.set_page_config(page_title="Computer Diagnostic Expert", layout="centered")

# --- Header / Start Page ---
st.title("Computer Diagnostic Expert")
st.write("A tiny fuzzy-logic assistant that gives preliminary diagnosis and performance evaluation.")
if "step" not in st.session_state:
    st.session_state.step = "start"

st.info("This system provides a preliminary assessment and is not a substitute for a technician.")

if st.session_state.step == "start":
    if st.button("Start Analysis"):
        st.session_state.step = "choose"

# --- Choose analysis type ---
if st.session_state.step == "choose":
    st.header("Choose Analysis Type")
    analysis_mode = st.radio(
        "Select one:", ["Diagnosis", "Performance Evaluation", "Full System Analysis"]
    )
    if st.button("Continue"):
        st.session_state.analysis_mode = analysis_mode
        st.session_state.step = "inputs"

# --- Inputs page ---
if st.session_state.step == "inputs":
    st.header("System Inputs")
    st.write("Fill the sections below. Sections are shown based on the chosen analysis type.")

    # Diagnosis section (Yes/No questions)
    with st.expander("Diagnosis (symptoms)"):
        st.write("Answer simple yes/no questions about observable symptoms")
        black_screen = st.checkbox("Black screen")
        slow_boot = st.checkbox("Slow boot")
        system_freeze = st.checkbox("System freezes")
        fan_noise = st.checkbox("Fan noise")
        power_led = st.checkbox("Power LED on")

    # Performance section (sliders)
    with st.expander("Performance (numerical inputs)", expanded=True):
        cpu = st.slider("CPU Usage (%)", 0, 100, 30)
        ram = st.slider("RAM Usage (%)", 0, 100, 30)
        temp = st.slider("Temperature (°C)", 0, 120, 40)
        disk = st.slider("Disk Health (%)", 0, 100, 90)
        boot = st.slider("Boot Time (s)", 0, 200, 30)

    analyze = st.button("Analyze")

    # Save current inputs in session (for explanation)
    st.session_state.inputs = {
        "black_screen": black_screen,
        "slow_boot": slow_boot,
        "system_freeze": system_freeze,
        "fan_noise": fan_noise,
        "power_led": power_led,
        "cpu": cpu,
        "ram": ram,
        "temp": temp,
        "disk": disk,
        "boot": boot,
    }

    if analyze:
        # Call inference engine (uses fuzzy rules)
        results = run_inference(cpu, ram, temp, disk, boot)
        st.session_state.results = results
        st.session_state.step = "results"

# --- Results page ---
if st.session_state.step == "results":
    st.header("Results")
    results = st.session_state.get("results", {})
    inputs = st.session_state.get("inputs", {})

    # A) Main findings
    st.subheader("Main Findings")
    st.write("- Performance:", results.get("performance"))
    st.write("- Overheating risk:", results.get("overheating_risk"))
    st.write("- Stability:", results.get("stability"))

    # B) Confidence / human label
    st.subheader("Confidence / Severity")
    perf_label = confidence_label(float(results.get("performance", 0)))
    over_label = confidence_label(float(results.get("overheating_risk", 0)))
    stab_label = confidence_label(float(results.get("stability", 0)))
    st.write(f"Performance: {perf_label}")
    st.write(f"Overheating risk: {over_label}")
    st.write(f"Stability: {stab_label}")

    # C) Recommendations (simple rules based on outputs)
    st.subheader("Recommendations")
    recs = []
    if float(results.get("overheating_risk", 0)) >= 60:
        recs.append("Check cooling and fans; improve ventilation; clean dust.")
    if float(results.get("performance", 0)) <= 40:
        recs.append("Close heavy applications; consider upgrading RAM/CPU.")
    if float(results.get("stability", 0)) <= 40:
        recs.append("Run disk diagnostics and check for failing hardware.")
    if inputs.get("black_screen"):
        recs.append("Check power supply and display connections.")
    if not recs:
        recs.append("No urgent actions detected — monitor system.")
    for r in recs:
        st.write("- ", r)

    # Explanation
    st.subheader("Explanation")
    st.write("These facts influenced the decision:")
    facts = []
    if inputs.get("cpu", 0) >= 75:
        facts.append("CPU usage is high")
    if inputs.get("ram", 0) >= 75:
        facts.append("RAM usage is high")
    if inputs.get("temp", 0) >= 75:
        facts.append("Temperature is high")
    if inputs.get("disk", 100) <= 50:
        facts.append("Disk health is low")
    if inputs.get("boot", 0) >= 100:
        facts.append("Boot time is slow")
    if inputs.get("black_screen"):
        facts.append("User reported black screen")
    if inputs.get("system_freeze"):
        facts.append("User reported system freezes")

    if facts:
        for f in facts:
            st.write("- ", f)
    else:
        st.write("No strong contributing facts detected.")

    if st.button("Analyze another case"):
        st.session_state.step = "choose"