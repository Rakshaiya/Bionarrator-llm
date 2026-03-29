"""
BioNarrator-LLM: A Retrieval-Augmented Framework for Interpreting
Real-Time Wet-Lab Sensor Data into Explainable Biological Insights

Based on the research paper by Rakshaiya Yadav G et al.
Sathyabama Institute of Science and Technology, Chennai

** No API key required — fully local execution **
"""

# ─────────────────────────────────────────────
# KNOWLEDGE BASE (RAG Simulation)
# ─────────────────────────────────────────────
KNOWLEDGE_BASE = [
    {
        "condition": "optimal_growth",
        "description": "Microbial growth is optimal when temperature is 30–37°C, pH is 6.5–7.5, and growth rate exceeds 0.8 OD/hr.",
    },
    {
        "condition": "heat_stress",
        "description": "Temperatures above 40°C denature proteins and disrupt cell membranes, leading to heat stress and reduced microbial activity.",
    },
    {
        "condition": "cold_stress",
        "description": "Temperatures below 25°C slow enzymatic reactions, reducing metabolic rate and growth.",
    },
    {
        "condition": "acidic_stress",
        "description": "pH below 5.5 causes proton toxicity and inhibits enzyme function, reducing cellular activity.",
    },
    {
        "condition": "alkaline_stress",
        "description": "pH above 8.0 disrupts membrane integrity and impairs nutrient transport in most microorganisms.",
    },
    {
        "condition": "low_growth",
        "description": "Growth rate below 0.4 OD/hr indicates nutrient limitation, environmental stress, or inhibitory conditions.",
    },
]

# ─────────────────────────────────────────────
# MODULE 1 — DATA PREPROCESSING
# ─────────────────────────────────────────────
def preprocess_sensor_data(temperature, ph, growth_rate):
    if temperature < 25:
        temp_label = "cold stress"
    elif 25 <= temperature <= 37:
        temp_label = "optimal range"
    elif 37 < temperature <= 40:
        temp_label = "slightly elevated"
    else:
        temp_label = "heat stress"

    if ph < 5.5:
        ph_label = "strongly acidic"
    elif 5.5 <= ph < 6.5:
        ph_label = "mildly acidic"
    elif 6.5 <= ph <= 7.5:
        ph_label = "neutral/optimal"
    elif 7.5 < ph <= 8.0:
        ph_label = "mildly alkaline"
    else:
        ph_label = "strongly alkaline"

    if growth_rate < 0.4:
        growth_label = "critically low"
    elif 0.4 <= growth_rate < 0.7:
        growth_label = "below optimal"
    elif 0.7 <= growth_rate <= 1.2:
        growth_label = "optimal"
    else:
        growth_label = "elevated"

    return {
        "temperature": temperature,
        "temperature_label": temp_label,
        "ph": ph,
        "ph_label": ph_label,
        "growth_rate": growth_rate,
        "growth_label": growth_label,
    }

# ─────────────────────────────────────────────
# MODULE 2 — RETRIEVAL MODULE
# ─────────────────────────────────────────────
def retrieve_knowledge(processed_data):
    retrieved = []
    temp_label = processed_data["temperature_label"]
    ph_label   = processed_data["ph_label"]
    growth     = processed_data["growth_rate"]

    if "heat stress" in temp_label:
        retrieved.append(KNOWLEDGE_BASE[1])
    elif "cold" in temp_label:
        retrieved.append(KNOWLEDGE_BASE[2])
    else:
        retrieved.append(KNOWLEDGE_BASE[0])

    if "acidic" in ph_label:
        retrieved.append(KNOWLEDGE_BASE[3])
    elif "alkaline" in ph_label:
        retrieved.append(KNOWLEDGE_BASE[4])

    if growth < 0.4:
        retrieved.append(KNOWLEDGE_BASE[5])

    return retrieved

# ─────────────────────────────────────────────
# MODULE 3 — LOCAL REASONING ENGINE
# Replaces LLM API with intelligent rule-based narrative generation
# ─────────────────────────────────────────────
def generate_interpretation(processed_data, knowledge_snippets):
    temp        = processed_data["temperature"]
    ph          = processed_data["ph"]
    growth      = processed_data["growth_rate"]
    temp_label  = processed_data["temperature_label"]
    ph_label    = processed_data["ph_label"]
    growth_label= processed_data["growth_label"]

    lines = []

    # --- State summary ---
    lines.append("BIOLOGICAL STATE SUMMARY")
    lines.append("-" * 40)

    if temp_label == "optimal range" and ph_label == "neutral/optimal" and growth_label == "optimal":
        lines.append(
            f"The experimental conditions are optimal for microbial growth. "
            f"Temperature ({temp}°C), pH ({ph}), and growth rate ({growth} OD/hr) "
            f"are all within ideal ranges, supporting healthy cellular metabolism."
        )
    elif temp_label == "heat stress" and "acidic" in ph_label:
        lines.append(
            f"The organism is under severe combined stress. "
            f"Elevated temperature ({temp}°C) is causing protein denaturation, "
            f"while the acidic pH ({ph}) is inducing proton toxicity. "
            f"This dual stress is reflected in the critically suppressed growth rate of {growth} OD/hr."
        )
    elif temp_label == "cold stress":
        lines.append(
            f"Cold stress conditions detected at {temp}°C. "
            f"Low temperatures reduce enzymatic activity and slow membrane fluidity, "
            f"leading to reduced metabolic output. "
            f"Growth rate of {growth} OD/hr reflects this thermal inhibition."
        )
    elif "acidic" in ph_label:
        lines.append(
            f"Acidic conditions (pH {ph}) are disrupting normal cellular function. "
            f"Proton accumulation is inhibiting key metabolic enzymes. "
            f"Growth rate of {growth} OD/hr suggests the organism is under significant pH stress."
        )
    elif "alkaline" in ph_label:
        lines.append(
            f"Alkaline conditions (pH {ph}) are impairing membrane integrity "
            f"and nutrient transport. The organism is compensating but growth "
            f"rate ({growth} OD/hr) is suboptimal as a result."
        )
    elif temp_label == "slightly elevated":
        lines.append(
            f"Temperature ({temp}°C) is slightly above optimal range. "
            f"Moderate heat is accelerating some metabolic reactions but may "
            f"begin stressing the organism if sustained. "
            f"Current growth rate of {growth} OD/hr is still within acceptable range."
        )
    else:
        lines.append(
            f"Conditions are within tolerable range. "
            f"Temperature: {temp}°C ({temp_label}), pH: {ph} ({ph_label}), "
            f"Growth Rate: {growth} OD/hr ({growth_label})."
        )

    # --- Cause analysis ---
    lines.append("")
    lines.append("LIKELY CAUSE")
    lines.append("-" * 40)
    causes = []
    if temp > 40:
        causes.append("excessive incubation temperature causing thermal denaturation")
    if temp < 25:
        causes.append("insufficient heating leading to cold inhibition of enzymes")
    if ph < 5.5:
        causes.append("acid accumulation possibly from fermentation byproducts")
    if ph > 8.0:
        causes.append("alkaline drift possibly from ammonia release or buffer imbalance")
    if growth < 0.4:
        causes.append("nutrient depletion or toxic metabolite accumulation")

    if causes:
        lines.append("Probable cause(s): " + ", ".join(causes) + ".")
    else:
        lines.append("No significant stress cause identified. Conditions support normal growth.")

    # --- Recommendation ---
    lines.append("")
    lines.append("RECOMMENDED ACTION")
    lines.append("-" * 40)
    recs = []
    if temp > 40:
        recs.append(f"Reduce incubation temperature to 35–37°C (currently {temp}°C)")
    if temp < 25:
        recs.append(f"Increase temperature to optimal range of 30–37°C (currently {temp}°C)")
    if ph < 5.5:
        recs.append(f"Add buffer solution to raise pH towards 6.5–7.5 (currently {ph})")
    if ph > 8.0:
        recs.append(f"Add acidifying agent to lower pH towards 6.5–7.5 (currently {ph})")
    if growth < 0.4:
        recs.append("Check nutrient availability and replenish growth medium")

    if recs:
        for r in recs:
            lines.append(f"  → {r}")
    else:
        lines.append("  → Maintain current conditions. No corrective action needed.")

    # --- Retrieved knowledge ---
    lines.append("")
    lines.append("RETRIEVED BIOLOGICAL KNOWLEDGE")
    lines.append("-" * 40)
    for k in knowledge_snippets:
        lines.append(f"  • {k['description']}")

    return "\n".join(lines)

# ─────────────────────────────────────────────
# MODULE 4 — RULE-BASED VALIDATION
# ─────────────────────────────────────────────
def validate_output(processed_data):
    flags = []
    confidence = 1.0

    temp = processed_data["temperature"]
    ph   = processed_data["ph"]
    gr   = processed_data["growth_rate"]

    if temp > 42:
        flags.append("CRITICAL: Temperature exceeds lethal threshold for most microorganisms.")
        confidence -= 0.2
    if ph < 4.5 or ph > 8.5:
        flags.append("WARNING: pH outside survivable range for standard lab organisms.")
        confidence -= 0.15
    if gr < 0.1:
        flags.append("WARNING: Growth rate critically low — possible cell death or contamination.")
        confidence -= 0.2
    if temp > 37 and ph < 6.0 and gr < 0.5:
        flags.append("ALERT: Multiple stress conditions detected simultaneously.")
        confidence -= 0.1

    confidence = max(0.0, round(confidence, 2))

    return {
        "flags": flags if flags else ["All parameters within acceptable biological ranges."],
        "confidence_score": confidence,
        "reliability": "High" if confidence >= 0.8 else "Moderate" if confidence >= 0.6 else "Low",
    }

# ─────────────────────────────────────────────
# MODULE 5 — FEATURE IMPORTANCE
# ─────────────────────────────────────────────
def compute_feature_importance(processed_data):
    temp_score = abs(processed_data["temperature"] - 33) / 20
    ph_score   = abs(processed_data["ph"] - 7.0) / 3.5
    gr_score   = abs(processed_data["growth_rate"] - 0.85) / 0.85
    total      = temp_score + ph_score + gr_score + 1e-9

    return {
        "Temperature": round(temp_score / total * 100, 1),
        "pH Level":    round(ph_score   / total * 100, 1),
        "Growth Rate": round(gr_score   / total * 100, 1),
    }

# ─────────────────────────────────────────────
# MAIN PIPELINE
# ─────────────────────────────────────────────
def run_bionarrator(temperature, ph, growth_rate):
    print("\n" + "=" * 60)
    print("  BioNarrator-LLM — Biological Insight Generator")
    print("=" * 60)
    print(f"\n[INPUT] Temperature: {temperature}°C | pH: {ph} | Growth Rate: {growth_rate} OD/hr")

    print("\n[1/5] Preprocessing sensor data...")
    processed = preprocess_sensor_data(temperature, ph, growth_rate)

    print("[2/5] Retrieving relevant biological knowledge...")
    knowledge = retrieve_knowledge(processed)
    print(f"      Retrieved {len(knowledge)} knowledge snippet(s)")

    print("[3/5] Engineering structured prompt...")
    print("[4/5] Generating biological interpretation...")
    interpretation = generate_interpretation(processed, knowledge)

    print("[5/5] Running rule-based validation...")
    validation = validate_output(processed)
    importance = compute_feature_importance(processed)

    print("\n" + "─" * 60)
    print("BIOLOGICAL INTERPRETATION")
    print("─" * 60)
    print(interpretation)

    print("\n" + "─" * 60)
    print("VALIDATION & CONFIDENCE")
    print("─" * 60)
    for flag in validation["flags"]:
        print(f"  • {flag}")
    print(f"\n  Confidence Score : {validation['confidence_score']}")
    print(f"  Reliability      : {validation['reliability']}")

    print("\n" + "─" * 60)
    print("FEATURE IMPORTANCE (% contribution to deviation)")
    print("─" * 60)
    for param, score in importance.items():
        bar = "█" * int(score / 5)
        print(f"  {param:<15} {bar} {score}%")

    print("\n" + "=" * 60 + "\n")

# ─────────────────────────────────────────────
# RUN EXAMPLES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    print("\nExample 1 — Optimal conditions")
    run_bionarrator(temperature=35, ph=7.0, growth_rate=0.95)

    print("\nExample 2 — Heat and acid stress")
    run_bionarrator(temperature=42, ph=5.2, growth_rate=0.3)

    print("\nExample 3 — Cold and alkaline stress")
    run_bionarrator(temperature=22, ph=8.3, growth_rate=0.45)
