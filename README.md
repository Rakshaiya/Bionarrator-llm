# BioNarrator-LLM

A Python-based framework that interprets real-time wet-lab sensor data into explainable biological insights using Retrieval-Augmented Generation (RAG), structured prompt engineering, rule-based validation, and explainability modules.

> Based on the research paper: **"BioNarrator-LLM: A Retrieval-Augmented Framework for Interpreting Real-Time Wet-Lab Sensor Data into Explainable Biological Insights"**
> Rakshaiya Yadav G, Niranjana P
> Sathyabama Institute of Science and Technology, Chennai

---

## What It Does

Takes raw wet-lab sensor readings (temperature, pH, microbial growth rate) and produces:
- A human-readable biological interpretation of the experimental state
- Likely cause of current conditions
- Recommended corrective action
- Rule-based validation with confidence scores
- Feature importance showing which parameter is driving the biological state

---

## Sample Output

```
[INPUT] Temperature: 42°C | pH: 5.2 | Growth Rate: 0.3 OD/hr

BIOLOGICAL STATE SUMMARY
The organism is under severe combined stress. Elevated temperature (42°C)
is causing protein denaturation, while the acidic pH (5.2) is inducing
proton toxicity. This dual stress is reflected in the critically suppressed
growth rate of 0.3 OD/hr.

LIKELY CAUSE
Probable cause(s): excessive incubation temperature causing thermal
denaturation, acid accumulation possibly from fermentation byproducts,
nutrient depletion or toxic metabolite accumulation.

RECOMMENDED ACTION
  → Reduce incubation temperature to 35–37°C (currently 42°C)
  → Add buffer solution to raise pH towards 6.5–7.5 (currently 5.2)
  → Check nutrient availability and replenish growth medium

VALIDATION & CONFIDENCE
  • ALERT: Multiple stress conditions detected simultaneously.
  Confidence Score : 0.9
  Reliability      : High

FEATURE IMPORTANCE
  Temperature     █████ 27.9%
  pH Level        ██████ 31.9%
  Growth Rate     ████████ 40.2%
```

---

## System Architecture

The framework consists of 5 core modules:

| Module | Function |
|--------|----------|
| Data Preprocessing | Normalizes and classifies raw sensor values |
| Retrieval Module | Fetches relevant biological knowledge from knowledge base |
| Reasoning Engine | Generates structured biological narrative |
| Validation Layer | Rule-based checks with confidence scoring |
| Explainability Module | Feature importance and reliability assessment |

---

## Tech Stack

- **Python** — core language, no external dependencies
- **Rule-based RAG** — domain knowledge retrieval simulation
- **Structured prompt engineering** — converts sensor data to biological context
- **Statistical validation** — confidence scoring and anomaly flagging

---

## Setup & Run

**1. Clone the repository:**
```bash
git clone https://github.com/Rakshaiya/Bionarrator-llm.git
cd Bionarrator-llm
```

**2. No installations needed — pure Python**

**3. Run the framework:**
```bash
python bionarrator_llm_local.py
```

---

## Input Parameters

| Parameter | Range | Unit |
|-----------|-------|------|
| Temperature | 20 – 45 | °C |
| pH Level | 4.5 – 8.5 | — |
| Growth Rate | 0.1 – 1.5 | OD/hr |

---

## Use Cases

- Automated wet-lab monitoring
- Research analytics and data interpretation
- Smart healthcare and biomedical systems
- Educational tool for computational biology

---

## Research Paper

This project is a working implementation of the BioNarrator-LLM framework proposed in our research paper, which achieved:
- **99.93% accuracy** on simulated wet-lab dataset
- **BLEU Score: 0.91 | ROUGE Score: 0.94**
- Outperformed rule-based (85.4%) and statistical models (91.75%)

---

## Author

**Rakshaiya Yadav G**
- GitHub: [@Rakshaiya](https://github.com/Rakshaiya)
- Email: rakshaiya115@gmail.com
