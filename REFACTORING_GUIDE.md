"""
Documentation for the refactored FamilyAIDoc structure.
"""

# FamilyAIDoc Refactored Architecture

## Project Structure

```
health-predict/
├── app_refactored.py                 # Main entry point (refactored)
├── app.py                            # Original app (can be archived)
├── config/                           # Configuration modules
│   ├── __init__.py
│   ├── styles.py                    # All CSS styling
│   └── settings.py                  # Configuration constants and model paths
├── components/                       # Reusable UI components
│   ├── __init__.py
│   ├── gauges.py                    # Confidence gauge visualization
│   └── sidebar.py                   # Sidebar navigation
├── pages/                           # Page-specific logic
│   ├── __init__.py
│   ├── home.py                      # Home page
│   ├── kidney.py                    # Kidney disease prediction
│   ├── liver.py                     # Liver disease prediction
│   ├── parkinsons.py                # Parkinson's disease prediction
│   └── about_models.py              # Model information
├── models_utils/                    # Model-related utilities
│   ├── __init__.py
│   ├── model_loader.py              # Model loading utilities
│   └── sample_data.py               # Sample data for testing
├── utils/                           # General utilities
│   ├── __init__.py
│   ├── encoding.py                  # Categorical encoding functions
│   └── prediction_helper.py         # Helper functions for predictions
├── models/                          # (Existing) Trained models directory
├── data/                            # (Existing) Datasets directory
├── training_scripts/                # (Existing) Training scripts directory
├── requirements.txt
├── README.md
└── LICENSE
```

## Key Improvements

### 1. **Modular Architecture**
   - Each page is a separate module with its own render function
   - Components are reusable and loosely coupled
   - Easy to add new pages or features

### 2. **Configuration Management**
   - `config/settings.py` - Centralized constants, model paths, and thresholds
   - `config/styles.py` - All CSS styling in one place
   - Easy to modify without touching application logic

### 3. **Component-Based Design**
   - **Gauges** - Reusable confidence visualization
   - **Sidebar** - Centralized navigation
   - Easy to extend with more components (charts, tables, etc.)

### 4. **Utility Modules**
   - **Model Loader** - Handles model loading with caching
   - **Sample Data** - All sample data in one place
   - **Encoding** - Categorical variable encoding
   - **Prediction Helper** - Common prediction logic

### 5. **Code Reusability**
   - Encoding functions shared across pages
   - Prediction helpers prevent code duplication
   - Consistent styling applied globally

### 6. **Easier Testing & Maintenance**
   - Individual modules can be tested independently
   - Clear separation of concerns
   - Easier to debug specific functionality
   - Simple to refactor individual components

## File Size Comparison

**Before Refactoring:**
- `app.py`: 1045 lines (monolithic)

**After Refactoring:**
- `app_refactored.py`: ~35 lines (main entry point)
- Multiple focused modules, each < 300 lines

## Migration Guide

### To use the refactored version:

1. **Run the refactored app:**
   ```bash
   streamlit run app_refactored.py
   ```

2. **Keep the original app.py for reference** or archive it

### To extend the application:

#### Adding a new disease prediction:

1. Create a new file in `pages/` directory:
   ```python
   # pages/new_disease.py
   def render_new_disease_page():
       # Your disease page logic
       pass
   ```

2. Add sample data to `models_utils/sample_data.py`

3. Import and add navigation in `config/settings.py`:
   ```python
   PAGES = [..., "🩺 New Disease"]
   MODEL_INFO['new_disease'] = {...}
   ```

4. Add routing in `app_refactored.py`:
   ```python
   elif page == "🩺 New Disease":
       from pages.new_disease import render_new_disease_page
       render_new_disease_page()
   ```

#### Adding a new component:

1. Create new file in `components/` directory:
   ```python
   # components/new_component.py
   def render_new_component(...):
       # Component logic
       pass
   ```

2. Import and use in relevant pages

## Benefits Summary

✅ **Modularity** - Each file has single responsibility  
✅ **Maintainability** - Easier to locate and fix bugs  
✅ **Scalability** - Simple to add new features  
✅ **Reusability** - Components and utilities shared across pages  
✅ **Testability** - Individual modules can be tested in isolation  
✅ **Readability** - Smaller focused files are easier to understand  
✅ **Configuration** - Centralized settings for easy modifications  
✅ **Performance** - Model caching with @st.cache_resource  

## Notes

- The original `app.py` is kept unchanged for reference
- All imports use relative paths (from config, utils, etc.)
- Streamlit caching is applied to model loading for performance
- Session state is used to preserve user inputs (kidney_values, liver_values, parkinsons_values)
- CSS is applied globally via `st.markdown()` in main app

---
**Created:** January 2025  
**Project:** FamilyAIDoc - AI Disease Detection  
**Status:** Refactored and Ready for Production
