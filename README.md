# 🏥 FamilyAIDoc - Clinical AI Inference Engine

FamilyAIDoc is an enterprise-grade, highly-performant clinical decision support system. Built entirely on **Python 3.12** and **Streamlit**, it implements robust Machine Learning inference pipelines alongside a Retrieval-Augmented Generation (RAG) architecture to provide real-time, explainable diagnostic predictions for chronic diseases.

---

## 🏛️ System Architecture

```mermaid
graph TD
    subgraph Frontend [Streamlit UI Client]
        A[UI Router: app.py] --> B(Diagnostic Modules)
        A --> C(Medical Assistant)
        B --> D{Feature Encoders}
    end

    subgraph Inference Layer [Machine Learning Engine]
        D --> E[Kidney: ExtraTreesClassifier]
        D --> F[Liver: RandomForestClassifier]
        D --> G[Neuro: XGBoostClassifier]
        E & F & G --> H[Prediction Aggregator & Calibrator]
        H --> I[Clinical Threshold Override]
    end

    subgraph RAG Pipeline [Medical Chatbot]
        C --> J[NLP Query Processor]
        J --> K[(Convex Vector Store)]
        K -- Retrieve Top-K -->> L[Context Builder]
        L --> M[Groq: Llama-3-8B-Instant]
    end

    subgraph Output Generation
        I --> N[Plotly Gauge Generation]
        M --> O[Streamlit Chat Interface]
        O --> P[ReportLab PDF Engine]
    end
```

---

## 🧠 Diagnostic Inference Models

The core of FamilyAIDoc relies on heavily optimized, pre-trained ensemble models serialized via `joblib`. The underlying engine relies on `scikit-learn==1.8.0` and `xgboost>=1.7.6`.

### 🫘 Chronic Kidney Disease (CKD) Pipeline
- **Algorithm:** `ExtraTreesClassifier` (Extremely Randomized Trees)
- **Hyperparameters:** `n_estimators=100`, `random_state=42`, `criterion='gini'`
- **Feature Space:** $N=24$ clinical parameters.
- **Preprocessing:** 
  - Mode imputation for categorical features (e.g., `rbc`, `pc`, `ba`).
  - Median imputation for continuous variables (e.g., `bu`, `sc`).
  - `MinMaxScaler(feature_range=(-1, 1))` applies uniform scaling across the feature vector.
- **Clinical Override:** Predictions are subjected to a secondary hardcoded rule-engine (`utils/prediction_helper.py`). If $Serum\_Creatinine > 1.8$ or $Albumin \ge 3$, the system forces a high-risk flag, mitigating false negatives from the ML output.

### 🫀 Liver Disease Pipeline
- **Algorithm:** `RandomForestClassifier`
- **Feature Space:** $N=10$ biomarkers, focusing heavily on hepatobiliary enzymes (SGPT, SGOT, Alkaline Phosphatase).
- **Evaluation:** Evaluated against baseline Logistic Regression and SVMs; selected for its robust handling of non-linear enzyme relationships and resilience to overfitting.

### 🧠 Parkinson's Acoustic Analysis Pipeline
- **Algorithm:** `XGBClassifier` (Extreme Gradient Boosting)
- **Feature Space:** $N=22$ extracted speech signal features (Multi-Dimensional Voice Program parameters).
- **Optimization Metric:** `eval_metric='logloss'`.
- **Feature Importance:** SHAP and Gini importance metrics identify `PPE` (Pitch Period Entropy) and `spread1` as the highest-weight features governing the decision boundary.

---

## 🤖 RAG Architecture (Retrieval-Augmented Generation)

To prevent severe AI hallucinations in clinical contexts, the chatbot implements a strict RAG pipeline:
1. **Semantic Triage:** User inputs are transmitted to the **Convex HTTP API** (`/api/search_diseases`).
2. **Context Retrieval:** The backend performs a search against a verified database of clinical definitions, symptoms, and contraindications.
3. **Prompt Injection:** The retrieved JSON payloads are compiled into a zero-shot system prompt.
4. **LLM Inference:** The query and contextual prompt are passed to **Groq's LPU inference engine** using the `llama-3.1-8b-instant` model. The temperature is strictly clamped at `T=0.3` to ensure deterministic, low-variance clinical outputs.

---

## 🚀 Environment Initialization

### Prerequisites
- Python `3.10` - `3.12`
- `pip` package manager

### 1. Repository Setup
```bash
git clone <repository_url>
cd health-predict
```

### 2. Dependency Resolution
Strict version locking is enforced for `scikit-learn` to prevent unpickling corruption (e.g., the `monotonic_cst` attribute mismatch bug).
```bash
pip install -r requirements.txt
```

### 3. Environment Configuration
Create a `.env` file for backend integrations:
```env
# Required for LLM Inference
GROQ_API_KEY=gsk_...

# Required for RAG Database
CONVEX_URL=https://...
```

### 4. Server Execution
```bash
streamlit run app.py --server.port=8501 --server.address=0.0.0.0
```

---

## 🔄 Retraining & Continuous Integration

If the underlying datasets (`data/*.csv`) are updated, the serialized model binaries must be regenerated to prevent dimensional mismatch during inference.

The training pipelines use Stratified K-Folds (80/20 splits) and evaluate arrays of models sequentially. Run the specific pipeline from the root directory:

```bash
# CKD Retraining Pipeline
python training_scripts/train_kidney_extratrees.py

# Hepatic Retraining Pipeline
python training_scripts/train_liver_randomforest.py

# Neuro Acoustic Retraining Pipeline
python training_scripts/train_parkinsons_xgboost.py
```

*Note: The script will automatically overwrite the `.pkl` binaries in the `models/` subdirectory. A manual clear of Streamlit's `@st.cache_resource` or a server restart is required to load the updated weights into RAM.*

---

## ⚠️ Regulatory & Compliance Notice

**FamilyAIDoc is not an FDA-approved medical device.** The inference engine is designed strictly as a clinical decision support system (CDSS) for educational and research operations. It is not intended for live patient diagnosis, treatment formulation, or emergency triage. Output probabilities are uncalibrated estimates and must be verified by a board-certified physician.
