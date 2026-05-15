import sys
import pathlib
import streamlit as st

PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from fuzzy.inference import run_system
from fuzzy.context import get_context_config


def confidence_label(value: float) -> str:
    if value >= 75:
        return "High"
    if value >= 40:
        return "Medium"
    return "Low"


st.set_page_config(page_title="Computer Diagnostic Expert", layout="wide")

if "flow_step" not in st.session_state:
    st.session_state.flow_step = "welcome"

if "context_config" not in st.session_state:
    st.session_state.context_config = None

if "inputs_collected" not in st.session_state:
    st.session_state.inputs_collected = {}

st.title("🖥️ Computer Diagnostic Expert")
st.write("A fuzzy-logic assistant for laptop diagnostics and performance evaluation.")
st.info("This system provides a preliminary assessment and is not a substitute for a technician.")

if st.session_state.flow_step == "welcome":
    st.header("Welcome!")
    st.write("""
    This diagnostic tool will guide you through a few questions about your laptop,
    then analyze its performance and health.
    """)
    if st.button(" Start Analysis", key="start_btn"):
        st.session_state.flow_step = "context"
        st.rerun()

if st.session_state.flow_step == "context":
    st.header("Step 1: Tell us about your laptop")
    
    col1, col2 = st.columns(2)
    
    with col1:
        brand = st.selectbox(
            "Brand",
            ["ASUS", "Lenovo", "HP", "Dell", "Apple", "Other"],
            key="brand_select"
        )
    
    with col2:
        laptop_type = st.selectbox(
            "Laptop Type",
            ["Gaming", "Office", "Ultrabook", "Professional", "Other"],
            key="type_select"
        )
    
    col3, col4 = st.columns(2)
    
    with col3:
        os_type = st.selectbox(
            "Operating System",
            ["Windows", "Linux", "macOS", "Other"],
            key="os_select"
        )
    
    with col4:
        usage_type = st.selectbox(
            "Primary Usage",
            ["Gaming", "Office", "Development", "Design", "Other"],
            key="usage_select"
        )
    
    col_a, col_b = st.columns([1, 1])
    with col_a:
        if st.button("Back", key="back_context"):
            st.session_state.flow_step = "welcome"
            st.rerun()
    
    with col_b:
        if st.button("Next: Choose analysis type", key="next_context"):
            st.session_state.context_config = get_context_config(brand, laptop_type, os_type, usage_type)
            st.session_state.flow_step = "analysis_type"
            st.rerun()

if st.session_state.flow_step == "analysis_type":
    st.header("Step 2: What would you like to evaluate?")
    
    analysis_mode = st.radio(
        "Select analysis type:",
        ["Diagnosis (Troubleshoot a problem)", 
         "Performance Evaluation (Check system speed)",
         "Full System Analysis (Complete health check)"],
        key="analysis_radio"
    )
    
    col_a, col_b = st.columns([1, 1])
    with col_a:
        if st.button("Back", key="back_analysis"):
            st.session_state.flow_step = "context"
            st.rerun()
    
    with col_b:
        if st.button(" Next: Provide system data", key="next_analysis"):
            st.session_state.analysis_mode = analysis_mode
            st.session_state.flow_step = "inputs"
            st.rerun()

if st.session_state.flow_step == "inputs":
    st.header("Step 3: System Metrics")
    st.write("Enter your system measurements below. Use Task Manager (Windows) or System Monitor (Linux/Mac) to get accurate values.")
    
    analysis_mode = st.session_state.get("analysis_mode", "Full System Analysis")
    
    with st.form("input_form"):
        st.subheader("Core Metrics")
        
        col1, col2 = st.columns(2)
        with col1:
            cpu = st.slider("CPU Usage (%)", 0, 100, 30, help="Current processor load")
            disk = st.slider("Disk Health (%)", 0, 100, 90, help="Disk integrity (100% = healthy)")
        
        with col2:
            ram = st.slider("RAM Usage (%)", 0, 100, 30, help="Memory utilization")
            boot = st.slider("Boot Time (seconds)", 0, 200, 30, help="Time to fully load OS")
        
        col3, col4 = st.columns(2)
        with col3:
            temp = st.slider("Temperature (°C)", 0, 120, 40, help="CPU core temperature")
        
        with col4:
            fan = st.slider("Fan Speed (0-100)", 0, 100, 40, help="Fan activity level")
        
        if "Full System" in analysis_mode:
            st.subheader("Additional Metrics (Full Analysis)")
            col5, col6, col7 = st.columns(3)
            
            with col5:
                disk_usage = st.slider("Disk Usage (%)", 0, 100, 50, help="How full the disk is")
            
            with col6:
                free_space = st.slider("Free Space (%)", 0, 100, 50, help="Available disk space")
            
            with col7:
                battery_health = st.slider("Battery Health (%)", 0, 100, 80, help="Battery capacity (0-100%)")
        else:
            disk_usage = 50
            free_space = 50
            battery_health = 80
        
        submitted = st.form_submit_button("Analyze System", use_container_width=True)
        
        if submitted:
            st.session_state.inputs_collected = {
                "cpu": cpu,
                "ram": ram,
                "temp": temp,
                "disk": disk,
                "boot": boot,
                "fan": fan,
                "disk_usage": disk_usage,
                "free_space": free_space,
                "battery_health": battery_health,
            }
            
            results = run_system(
                cpu_value=cpu,
                ram_value=ram,
                temp_value=temp,
                disk_value=disk,
                boot_value=boot,
                fan_value=fan,
                disk_usage_value=disk_usage,
                free_space_value=free_space,
                battery_health_value=battery_health,
                context_config=st.session_state.context_config,
            )
            st.session_state.results = results
            st.session_state.flow_step = "results"
            st.rerun()

if st.session_state.flow_step == "results":
    st.header("Analysis Results")
    results = st.session_state.get("results", {})
    inputs = st.session_state.get("inputs_collected", {})
    context = st.session_state.get("context_config", {}).get("context", {})
    
    st.subheader("Main Findings")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        perf_val = float(results.get("performance", 0))
        perf_label = confidence_label(perf_val)
        st.metric("Performance Score", f"{perf_val:.0f}/100", delta=perf_label)
    
    with col2:
        over_val = float(results.get("overheating_risk", 0))
        over_label = confidence_label(over_val)
        st.metric("Overheating Risk", f"{over_val:.0f}/100", delta=over_label)
    
    with col3:
        stab_val = float(results.get("stability", 0))
        stab_label = confidence_label(stab_val)
        st.metric("System Stability", f"{stab_val:.0f}/100", delta=stab_label)
    
    st.subheader("Detailed Assessment")
    col_a, col_b, col_c = st.columns(3)
    
    if "storage_issue" in results:
        with col_a:
            st.write(f"**Storage Issue:** {results.get('storage_issue', 0):.0f}/100")
    
    if "battery_issue" in results:
        with col_b:
            st.write(f"**Battery Issue:** {results.get('battery_issue', 0):.0f}/100")
    
    if "boot_issue" in results:
        with col_c:
            st.write(f"**Boot Issue:** {results.get('boot_issue', 0):.0f}/100")
    
    st.subheader(" Recommendations")
    recs = results.get("recommendations", [])
    
    if recs:
        for idx, r in enumerate(recs, 1):
            st.write(f"✓ {r}")
    else:
        st.write(" No urgent actions detected — monitor system regularly.")
    
    st.subheader("Your System Profile")
    ctx_col1, ctx_col2 = st.columns(2)
    
    with ctx_col1:
        st.write(f"**Brand:** {context.get('brand', 'Unknown').title()}")
        st.write(f"**Type:** {context.get('laptop_type', 'Unknown').title()}")
    
    with ctx_col2:
        st.write(f"**OS:** {context.get('os_type', 'Unknown').title()}")
        st.write(f"**Primary Usage:** {context.get('usage_type', 'Unknown').title()}")
    
    st.subheader("What influenced this result?")
    explanations = []
    
    if float(inputs.get("cpu", 0)) >= 75:
        explanations.append("• CPU usage is high")
    elif float(inputs.get("cpu", 0)) >= 40:
        explanations.append("• CPU usage is moderate")
    else:
        explanations.append("• CPU usage is low")
    
    if float(inputs.get("ram", 0)) >= 75:
        explanations.append("• RAM usage is high")
    
    if float(inputs.get("temp", 0)) >= 75:
        explanations.append("• Temperature is elevated")
    
    if float(inputs.get("disk", 100)) <= 50:
        explanations.append("• Disk health is degraded")
    
    if float(inputs.get("boot", 0)) >= 100:
        explanations.append("• Boot time is slow")
    
    if float(inputs.get("fan", 0)) >= 75:
        explanations.append("• Fan is working hard (cooling demand)")
    
    if explanations:
        for e in explanations:
            st.write(e)
    else:
        st.write("System appears to be operating normally.")
    
    st.divider()
    col_nav1, col_nav2 = st.columns([1, 1])
    
    with col_nav1:
        if st.button("Analyze another system", use_container_width=True):
            st.session_state.flow_step = "context"
            st.session_state.context_config = None
            st.session_state.inputs_collected = {}
            st.rerun()
    
    with col_nav2:
        if st.button(" Back to Start", use_container_width=True):
            st.session_state.flow_step = "welcome"
            st.session_state.context_config = None
            st.session_state.inputs_collected = {}
            st.rerun()