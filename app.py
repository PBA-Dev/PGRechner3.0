import os
import json
import logging
from flask import Flask, render_template, request, make_response, url_for, session, redirect, flash, Response, current_app, jsonify
from fpdf import FPDF
from fpdf.enums import XPos, YPos
from modules.module1 import module1
from modules.module2 import module2
from modules.module3 import module3
from modules.module4 import module4
from modules.module5 import module5
from modules.module6 import module6
from config.pflegegrad_config import pflegegrad_thresholds
from config.benefits_data import pflegegrad_benefits

app = Flask(__name__)
app.secret_key = os.urandom(24)

all_modules = {
    1: module1,
    2: module2,
    3: module3,
    4: module4,
    5: module5,
    6: module6,
}
TOTAL_MODULES = len(all_modules)

weighted_score_mapping_tables = {
    1: [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 10), (12, 10), (13, 10), (14, 10), (15, 10)],
    2: [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 15), (17, 15), (18, 15), (19, 15), (20, 15), (21, 15), (22, 15), (23, 15), (24, 15), (25, 15), (26, 15), (27, 15), (28, 15), (29, 15), (30, 15), (31, 15), (32, 15), (33, 15)],
    3: [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 5), (7, 5), (8, 5), (9, 5), (10, 10), (11, 10), (12, 10), (13, 10), (14, 10), (15, 15), (16, 15), (17, 15), (18, 15), (19, 15), (20, 15), (21, 15), (22, 15), (23, 15), (24, 15), (25, 15), (26, 15), (27, 15), (28, 15), (29, 15), (30, 15), (31, 15), (32, 15), (33, 15), (34, 15), (35, 15), (36, 15), (37, 15), (38, 15), (39, 15), (40, 15), (41, 15), (42, 15), (43, 15), (44, 15), (45, 15), (46, 15), (47, 15), (48, 15), (49, 15), (50, 15), (51, 15), (52, 15), (53, 15), (54, 15), (55, 15), (56, 15), (57, 15), (58, 15), (59, 15), (60, 15), (61, 15), (62, 15), (63, 15), (64, 15), (65, 15)],
    4: [(0, 0), (1, 2.5), (2, 5), (3, 7.5), (4, 10), (5, 12.5), (6, 15), (7, 17.5), (8, 20), (9, 22.5), (10, 25), (11, 27.5), (12, 30), (13, 32.5), (14, 35), (15, 37.5), (16, 40), (17, 40), (18, 40), (19, 40), (20, 40), (21, 40), (22, 40), (23, 40), (24, 40), (25, 40), (26, 40), (27, 40), (28, 40), (29, 40), (30, 40), (31, 40), (32, 40), (33, 40), (34, 40), (35, 40), (36, 40), (37, 40), (38, 40), (39, 40), (40, 40), (41, 40), (42, 40), (43, 40), (44, 40), (45, 40), (46, 40), (47, 40), (48, 40)],
    5: [(0, 0), (1, 5), (2, 10), (3, 15), (4, 20), (5, 20), (6, 20), (7, 20), (8, 20), (9, 20), (10, 20), (11, 20), (12, 20), (13, 20), (14, 20), (15, 20)],
    6: [(0, 0), (1, 1.25), (2, 2.5), (3, 3.75), (4, 5), (5, 6.25), (6, 7.5), (7, 8.75), (8, 10), (9, 11.25), (10, 12.5), (11, 13.75), (12, 15), (13, 15), (14, 15), (15, 15), (16, 15), (17, 15), (18, 15)]
}

# ... (rest of app setup: all_modules, TOTAL_MODULES, pflegegrad_thresholds) ...

# In app.py
# ... (imports, config, RAW_TO_WEIGHTED_MAPPING) ...

def map_raw_to_weighted_score(module_id, raw_score):
    """Maps raw score to weighted score based on predefined tables."""
    try:
        module_id = int(module_id)
    except (ValueError, TypeError):
        current_app.logger.error(f"Invalid module_id type for weighted score mapping: {module_id}")
        return 0.0

    if module_id not in weighted_score_mapping_tables:
        current_app.logger.warning(f"Weighted score mapping table not found for module_id: {module_id}")
        return 0.0

    mapping_table = weighted_score_mapping_tables[module_id]
    weighted_score = 0.0

    try:
        raw_score = float(raw_score)
    except (ValueError, TypeError):
         current_app.logger.warning(f"Invalid raw_score type for weighted score mapping (Module {module_id}): {raw_score}")
         return 0.0

    for table_raw, table_weighted in mapping_table:
        if raw_score >= table_raw:
            weighted_score = table_weighted
        else:
            break
    return float(weighted_score)

def calculate_frequency_score(count, unit):
    """Calculates a raw score based on frequency of need."""
    try:
        count = int(count)
        if count < 0: count = 0
    except (ValueError, TypeError):
        count = 0

    if count == 0: return 0

    unit = str(unit).lower()
    if 'tag' in unit or 'day' in unit: return 3
    elif 'woche' in unit or 'week' in unit: return 2
    elif 'monat' in unit or 'month' in unit: return 1
    else: return 0

def _freq_per_day(count, unit):
    """Convert a frequency specification to an average per day."""
    try:
        cnt = float(count)
        if cnt < 0:
            cnt = 0.0
    except (ValueError, TypeError):
        cnt = 0.0

    unit = str(unit).lower()
    if 'tag' in unit or 'day' in unit:
        return cnt
    if 'woche' in unit or 'week' in unit:
        return cnt / 7.0
    if 'monat' in unit or 'month' in unit:
        return cnt / 30.0
    return 0.0

def calculate_module5_raw_score(answers):
    """Calculate the raw score for module 5 according to the official guide."""
    answers = answers or {}

    # --- Part 1: F 4.5.1 bis F 4.5.7 ---
    part1_ids = [f'5.1.{i}' for i in range(1, 8)]
    sum_per_day = sum(_freq_per_day(answers.get(q, {}).get('count'),
                                    answers.get(q, {}).get('unit'))
                      for q in part1_ids)
    sum_per_day = round(sum_per_day, 4)
    if sum_per_day < 1:
        part1_score = 0
    elif sum_per_day <= 3:
        part1_score = 1
    elif sum_per_day <= 8:
        part1_score = 2
    else:
        part1_score = 3

    # --- Part 2: F 4.5.8 bis F 4.5.11 ---
    part2_ids = [f'5.2.{i}' for i in range(1, 5)]
    sum_per_day2 = sum(_freq_per_day(answers.get(q, {}).get('count'),
                                     answers.get(q, {}).get('unit'))
                       for q in part2_ids)
    sum_per_day2 = round(sum_per_day2, 4)
    if sum_per_day2 < 1/7:
        part2_score = 0
    elif sum_per_day2 < 1:
        part2_score = 1
    elif sum_per_day2 < 3:
        part2_score = 2
    else:
        part2_score = 3

    # --- Part 3: F 4.5.12 bis F 4.5.15 ---
    mapping = {
        '5.3.1': {'monthly': 2.0, 'weekly': 8.6, 'daily': 60.0},  # F 4.5.12
        '5.4.1': {'monthly': 1.0, 'weekly': 4.3},                 # F 4.5.13
        '5.4.2': {'monthly': 1.0, 'weekly': 4.3},                 # F 4.5.14
        '5.4.3': {'monthly': 2.0, 'weekly': 8.6}                  # F 4.5.15
    }

    total_points = 0.0
    for qid, rules in mapping.items():
        data = answers.get(qid, {})
        if not data:
            continue
        try:
            cnt = float(data.get('count', 0))
            if cnt <= 0:
                continue
        except (ValueError, TypeError):
            continue
        unit = str(data.get('unit', '')).lower()
        if 'tag' in unit and 'daily' in rules:
            total_points += rules.get('daily', 0.0)
        elif 'tag' in unit:
            # Daily values are not expected for the others; treat as weekly
            total_points += cnt * rules.get('weekly', 0.0)
        elif 'woche' in unit or 'week' in unit:
            total_points += cnt * rules.get('weekly', 0.0)
        elif 'monat' in unit or 'month' in unit:
            total_points += cnt * rules.get('monthly', 0.0)

    total_points = round(total_points, 4)
    if total_points < 4.3:
        part3_score = 0
    elif total_points < 8.6:
        part3_score = 1
    elif total_points < 12.9:
        part3_score = 2
    elif total_points < 60:
        part3_score = 3
    else:
        part3_score = 6

    # --- Part 4: F 4.5.16 ---
    part4_score = int(answers.get('5.5.1', {}).get('score', 0))

    return part1_score + part2_score + part3_score + part4_score



# --- Routes ---

@app.route('/')
def intro():
    """Displays the introduction page."""
    # Clear any previous session data at the start
    session.pop('answers', None)
    session.pop('results', None)
    return render_template('intro.html')

@app.route('/start', methods=['POST'])
def start():
    """Stores Berater and Klient information then starts the questionnaire."""
    session['user_info'] = {
        'berater_name': request.form.get('berater_name', '').strip(),
        'client_name': request.form.get('client_name', '').strip(),
        'insurance_number': request.form.get('insurance_number', '').strip(),
        'dob': request.form.get('dob', '').strip(),
        'address': request.form.get('address', '').strip(),
        'phone': request.form.get('phone', '').strip(),
    }
    return redirect(url_for('module_page', module_id=1))




# --- Update module_page_submit function ---
# --- Route for DISPLAYING module page (GET requests) ---
@app.route('/module/<int:module_id>', methods=['GET'], endpoint='module_page') # Explicit endpoint name
def module_page(module_id):
    if module_id not in all_modules or module_id < 1 or module_id > TOTAL_MODULES:
        flash("Ungültiges Modul angefordert.", "error")
        # Redirect to intro or the first module if session exists
        if 'module_answers' in session and session['module_answers']:
             first_answered = min(int(k) for k in session['module_answers'].keys() if k.isdigit())
             return redirect(url_for('module_page', module_id=first_answered))
        return redirect(url_for('intro'))

    module_data = all_modules[module_id]
    module_id_str = str(module_id)

    # Get current answers for this module to pre-fill form
    current_answers = session.get('module_answers', {}).get(module_id_str, {})

    # --- Calculate Estimated Score for Progress Bar ---
    # This logic needs to be here for GET requests too
    current_estimated_score = 0.0
    temp_module_scores_raw = {}
    temp_module_scores_weighted = {}
    temp_which_module_contributed_m2_m3 = None

    # Recalculate based on session data up to the *previous* module
    # Or include current module if answers exist? Let's recalculate all answered.
    all_session_answers = session.get('module_answers', {})
    for mid_str, answers in all_session_answers.items():
        mid = int(mid_str)
        if mid not in all_modules: continue

        raw_score = 0.0
        for q_key, answer_data in answers.items():
             if q_key not in ['notes', 'visited'] and isinstance(answer_data, dict):
                 raw_score += answer_data.get('score', 0)
        temp_module_scores_raw[mid_str] = raw_score
        temp_module_scores_weighted[mid_str] = map_raw_to_weighted_score(mid, raw_score)

    # Calculate estimated total based on weighted scores found
    m1_s = temp_module_scores_weighted.get('1', 0.0)
    m2_s = temp_module_scores_weighted.get('2', 0.0)
    m3_s = temp_module_scores_weighted.get('3', 0.0)
    m4_s = temp_module_scores_weighted.get('4', 0.0)
    m5_s = temp_module_scores_weighted.get('5', 0.0)
    m6_s = temp_module_scores_weighted.get('6', 0.0)

    current_estimated_score += m1_s
    if m2_s >= m3_s:
        current_estimated_score += m2_s
        temp_which_module_contributed_m2_m3 = 2
    else:
        current_estimated_score += m3_s
        temp_which_module_contributed_m2_m3 = 3
    current_estimated_score += m4_s
    current_estimated_score += m5_s
    current_estimated_score += m6_s
    # --- End Estimated Score Calculation ---

    # Define max_score for the progress bar (adjust if needed)
    max_score = 100

    return render_template(
        'module_page.html',
        module=module_data,
        module_id=module_id,
        TOTAL_MODULES=TOTAL_MODULES, # Pass TOTAL_MODULES
        current_answers=current_answers, # Pass current answers for pre-filling
        # Pass data needed for progress bar
        current_estimated_score=current_estimated_score,
        max_score=max_score,
        pflegegrad_thresholds=pflegegrad_thresholds,
        all_modules=all_modules # Pass all_modules if needed by template logic
    )


# --- Route for HANDLING module submission (POST requests) ---
@app.route('/module/<int:module_id>', methods=['POST'], endpoint='module_page_submit') # Explicit endpoint name
def module_page_submit(module_id):
    # Keep the entire logic from the previous step here
    # (Checking module_id, initializing session, storing answers for M5,
    # storing answers for other modules, storing notes, redirecting)
    if module_id not in all_modules:
        flash("Ungültiges Modul.", "error")
        return redirect(url_for('intro'))

    module_data = all_modules[module_id]
    module_id_str = str(module_id)

    # Initialize session storage if not present
    if 'module_answers' not in session:
        session['module_answers'] = {}
    if module_id_str not in session['module_answers']:
        session['module_answers'][module_id_str] = {}

    # --- Store answers ---
    if module_id == 5:
        # --- Module 5: Handle parts, frequency and standard questions ---
        for part in module_data.get('parts', []):
            for question in part.get('questions', []):
                question_key = question['id'] # Use the unique question ID (e.g., '5.1.1')

                if question.get('type') == 'frequency':
                    count_key = f'freq_count_{question_key}'
                    unit_key = f'freq_unit_{question_key}'
                    answered_key = f'answered_{question_key}' # Check if user interacted

                    # Only process if the hidden 'answered' field was sent
                    if answered_key in request.form:
                        count = request.form.get(count_key, 0)
                        unit = request.form.get(unit_key, '')
                        score = calculate_frequency_score(count, unit)
                        answer_text = f"{count}x pro {unit}" if score > 0 else "Entfällt/Selbständig"

                        session['module_answers'][module_id_str][question_key] = {
                            'question': question['text'],
                            'answer_text': answer_text,
                            'score': score,
                            'count': count,
                            'unit': unit
                        }
                    else:
                         session['module_answers'][module_id_str].pop(question_key, None)

                elif question.get('type') == 'standard':
                    answer_key = f'answer_{module_id}_{question_key}'
                    selected_option_index = request.form.get(answer_key)
                    if selected_option_index is not None:
                        try:
                            option_index = int(selected_option_index)
                            if 0 <= option_index < len(question['options']):
                                selected_option = question['options'][option_index]
                                session['module_answers'][module_id_str][question_key] = {
                                    'question': question['text'],
                                    'answer_text': selected_option['text'],
                                    'score': selected_option.get('score', 0),
                                    'option_index': option_index
                                }
                            else: session['module_answers'][module_id_str].pop(question_key, None)
                        except ValueError: session['module_answers'][module_id_str].pop(question_key, None)
                    else: session['module_answers'][module_id_str].pop(question_key, None)

                else: # Fallback/Default
                    answer_key = f'answer_{module_id}_{question_key}'
                    selected_option_index = request.form.get(answer_key)
                    if selected_option_index is not None:
                        try:
                            option_index = int(selected_option_index)
                            if 0 <= option_index < len(question['options']):
                                selected_option = question['options'][option_index]
                                session['module_answers'][module_id_str][question_key] = {
                                    'question': question['text'],
                                    'answer_text': selected_option['text'],
                                    'score': selected_option.get('score', 0),
                                    'option_index': option_index
                                }
                            else: session['module_answers'][module_id_str].pop(question_key, None)
                        except ValueError: session['module_answers'][module_id_str].pop(question_key, None)
                    else: session['module_answers'][module_id_str].pop(question_key, None)

    else: # Standard handling for modules 1, 2, 3, 4, 6
        for i, question in enumerate(module_data.get('questions', [])):
            question_index_str = str(i)
            # Use .get() for question text with a default value
            question_text = question.get('text', f'Unbekannte Frage {i+1}')
            answer_key = f'answer_{module_id}_{i}'
            selected_option_index = request.form.get(answer_key)
            if selected_option_index is not None:
                try:
                    option_index = int(selected_option_index)
                    options = question.get('options', [])
                    if 0 <= option_index < len(options):
                        selected_option = options[option_index]
                        if isinstance(selected_option, dict):
                            session['module_answers'][module_id_str][question_index_str] = {
                                'question': question_text,
                                'answer_text': selected_option.get('text', 'N/A'),
                                'score': selected_option.get('score', 0),
                                'option_index': option_index,
                                'type': 'standard'
                            }
                        else:
                            current_app.logger.error(f"Invalid option format for M{module_id} Q{i} Opt{option_index}: {selected_option}")
                            session['module_answers'][module_id_str].pop(question_index_str, None)
                    else:
                         session['module_answers'][module_id_str].pop(question_index_str, None)
                except ValueError:
                     session['module_answers'][module_id_str].pop(question_index_str, None)
                except TypeError:
                     current_app.logger.error(f"Invalid options format for M{module_id} Q{i}: {options}")
                     session['module_answers'][module_id_str].pop(question_index_str, None)
            else:
                 session['module_answers'][module_id_str].pop(question_index_str, None)

    # --- Store Notes ---
    notes_key = f'module_{module_id}_notes'
    notes_text = request.form.get(notes_key, '').strip()
    if notes_text:
        session['module_answers'][module_id_str]['notes'] = notes_text
    else:
        session['module_answers'][module_id_str].pop('notes', None)

    session.modified = True

    # --- Determine next step ---
    next_module_id = module_id + 1
    if next_module_id > TOTAL_MODULES:
        return redirect(url_for('calculate'))
    else:
        # Redirect to the GET endpoint for the next module
        return redirect(url_for('module_page', module_id=next_module_id))


# --- Update calculate function ---
@app.route('/calculate')
def calculate():
    if 'module_answers' not in session or not session['module_answers']:
        flash("Bitte füllen Sie zuerst die Module aus.", "warning")
        return redirect(url_for('intro'))

    all_answers = session.get('module_answers', {})
    module_scores_raw = {}
    module_scores_weighted = {}
    all_detailed_answers = {} # To store text and score for results page/PDF

    # --- Calculate Raw Scores and Collect Detailed Answers ---
    for module_id_str, answers in all_answers.items():
        module_id = int(module_id_str)
        if module_id not in all_modules: continue

        module_data = all_modules[module_id]
        current_module_raw_score = 0.0
        current_detailed_answers = {}

        # Iterate through the stored answers for the module
        # Exclude 'notes' and 'visited' keys from score calculation
        for q_key, answer_data in answers.items():
            if q_key not in ['notes', 'visited'] and isinstance(answer_data, dict):
                current_module_raw_score += answer_data.get('score', 0)
                current_detailed_answers[q_key] = answer_data # Store details (question text, answer text, score)

        module_scores_raw[module_id_str] = current_module_raw_score
        all_detailed_answers[module_id_str] = current_detailed_answers


    # --- Map Raw Scores to Weighted Scores (using mapping function) ---
    # (Keep existing logic)
    for module_id_str, raw_score in module_scores_raw.items():
         module_id = int(module_id_str)
         if module_id in all_modules:
             module_scores_weighted[module_id_str] = map_raw_to_weighted_score(module_id, raw_score)
         else:
             module_scores_weighted[module_id_str] = 0.0

    # --- Calculate Final Total Score ---
    # (Keep existing logic)
    final_total_score = 0
    which_module_contributed_m2_m3 = None
    m1_score = module_scores_weighted.get('1', 0.0)
    m2_score = module_scores_weighted.get('2', 0.0)
    m3_score = module_scores_weighted.get('3', 0.0)
    m4_score = module_scores_weighted.get('4', 0.0)
    m5_score = module_scores_weighted.get('5', 0.0) # Now uses calculated M5 score
    m6_score = module_scores_weighted.get('6', 0.0)

    final_total_score += m1_score
    if m2_score >= m3_score:
        final_total_score += m2_score
        which_module_contributed_m2_m3 = 2
    else:
        final_total_score += m3_score
        which_module_contributed_m2_m3 = 3
    final_total_score += m4_score
    final_total_score += m5_score
    final_total_score += m6_score

    # --- Determine Pflegegrad ---
    # (Keep existing logic)
    pflegegrad = 0
    for grad, threshold in sorted(pflegegrad_thresholds.items(), key=lambda item: item[1]['min_points']):
        if final_total_score >= threshold['min_points']:
            pflegegrad = grad
        else:
            break

    # --- Aggregate Notes ---
    # (Keep existing logic)
    aggregated_notes = {
        mid: data.get('notes', '')
        for mid, data in all_answers.items()
        if data.get('notes')
    }

    # --- Get Benefits Data ---
    # (Keep existing logic - maybe add date check)
    from datetime import date
    today = date.today()
    # Determine period based on date - adjust cutoff as needed
    current_period_key = "period_2" if today >= date(today.year, 7, 1) else "period_1"
    # Fallback if period key doesn't exist for some reason
    benefits_for_pg = pflegegrad_benefits.get(pflegegrad, {})
    benefits = benefits_for_pg.get(current_period_key)
    if not benefits: # If current period missing, try the other one
        fallback_period = "period_1" if current_period_key == "period_2" else "period_2"
        benefits = benefits_for_pg.get(fallback_period, {})


    # --- Prepare results for template ---
    # (Keep existing structure)
    results = {
        'final_total_score': round(final_total_score, 2),
        'pflegegrad': pflegegrad,
        'module_scores_raw': module_scores_raw,
        'module_scores_weighted': module_scores_weighted,
        'which_module_contributed_m2_m3': which_module_contributed_m2_m3,
        'answers': all_detailed_answers, # Pass detailed answers for display/PDF
        'notes': aggregated_notes,       # Pass aggregated notes
        'benefits': benefits             # Pass benefits data
    }

    session['results'] = results # Keep storing in session if needed elsewhere

    # Pass necessary variables to the template
    return render_template(
        'result.html',
        results=results,
        all_modules=all_modules,
        pflegegrad_thresholds=pflegegrad_thresholds,
        user_info=session.get('user_info', {})
        # Add TOTAL_MODULES if used in result.html
        # TOTAL_MODULES=TOTAL_MODULES
    )


# Ensure pflegegrad_thresholds is defined or imported
pflegegrad_thresholds = {
    1: {'min_points': 12.5, 'max_points': 26.9},
    2: {'min_points': 27, 'max_points': 47.4},
    3: {'min_points': 47.5, 'max_points': 69.9},
    4: {'min_points': 70, 'max_points': 89.9},
    5: {'min_points': 90, 'max_points': 100}
}
# ... (generate_pdf route) ...


# d:\Users\SSH\OneDrive\1_-_SunState_Health,_LLC\.-Optimum_Pflege\ProgFold\PGRechner\PGRechner\app.py
# ... (imports and other code remain the same) ...

# --- PDF Generation Route ---
# d:\Users\SSH\OneDrive\1_-_SunState_Health,_LLC\.-Optimum_Pflege\ProgFold\PGRechner\PGRechner\app.py

# --- PDF Generation Route ---
@app.route('/generate_pdf', methods=['POST'])
def generate_pdf():
    """
    Generates a PDF document based on the calculation results provided in the request body.
    Handles M5 frequency, notes, benefits. Uses updated FPDF2 syntax.
    Includes type checking for pdf.output() result.
    """
    data = None
    try:
        data = request.get_json(silent=True)
        if data is None:
            raw_data = request.data.decode('utf-8', errors='ignore')
            current_app.logger.error(f"Invalid or empty JSON received for PDF. Raw data received: '{raw_data}'")
            return jsonify({"error": "Invalid or empty JSON data received."}), 400

        current_app.logger.info(f"Successfully parsed JSON data for PDF generation. Keys: {list(data.keys())}")

        # --- Extract data safely ---
        detailed_results = data.get('detailed_results', {})
        final_total_score = float(data.get('final_total_score', 0.0))
        pflegegrad = int(data.get('pflegegrad', 0))
        benefits_data = data.get('benefits', {})
        notes_data = data.get('notes', {}) # Aggregated notes { '1': 'note', ... }
        user_info = data.get('user_info', {})


        # --- PDF Generation Logic ---
        pdf = FPDF()
        pdf.add_page()
        usable_width = pdf.w - pdf.l_margin - pdf.r_margin
        pdf.set_font("Arial", size=12) # Using core font

        # Company Header
        pdf.set_font("Arial", 'B', 14)
        pdf.multi_cell(usable_width, 8, "Optimum Pflegeberatung".encode('latin-1', 'replace').decode('latin-1'),
                       align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.set_font("Arial", size=10)
        pdf.multi_cell(usable_width, 5, "Verena Campbell - Pflegeberaterin".encode('latin-1', 'replace').decode('latin-1'),
                       align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.multi_cell(usable_width, 5, "verena.campbell@optimum-pflegeberatung.de".encode('latin-1', 'replace').decode('latin-1'),
                       align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.ln(5)


        # --- Title ---
        pdf.set_font("Arial", 'B', 16)
        pdf.multi_cell(usable_width, 10, "Pflegegradrechner - Ergebnisbericht".encode('latin-1', 'replace').decode('latin-1'),
                       align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.ln(10)

        # --- Summary ---
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(usable_width, 10, "Zusammenfassung".encode('latin-1', 'replace').decode('latin-1'),
                 new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.set_font("Arial", size=12)
        score_text = f"Gesamtpunktzahl (fuer Pflegegrad): {final_total_score:.2f}"
        pdf.cell(usable_width, 8, score_text.encode('latin-1', 'replace').decode('latin-1'),
                 new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pg_text = f"Ermittelter Pflegegrad: {pflegegrad}" if pflegegrad > 0 else "Ermittelter Pflegegrad: Kein Pflegegrad (unter 12.5 Punkte)"
        pdf.cell(usable_width, 8, pg_text.encode('latin-1', 'replace').decode('latin-1'),
                 new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.ln(5)

                # User / Client Information
        if user_info:
            pdf.set_font("Arial", 'B', 12)
            pdf.cell(usable_width, 8, "Daten".encode('latin-1', 'replace').decode('latin-1'), new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            pdf.set_font("Arial", size=10)
            if user_info.get('berater_name'):
                pdf.cell(usable_width, 5, f"Pflegeberater/in: {user_info.get('berater_name')}".encode('latin-1', 'replace').decode('latin-1'), new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            if user_info.get('client_name'):
                pdf.cell(usable_width, 5, f"Klient/in: {user_info.get('client_name')}".encode('latin-1', 'replace').decode('latin-1'), new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            if user_info.get('insurance_number'):
                pdf.cell(usable_width, 5, f"Krankenversicherungsnummer: {user_info.get('insurance_number')}".encode('latin-1', 'replace').decode('latin-1'), new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            if user_info.get('dob'):
                pdf.cell(usable_width, 5, f"Geburtsdatum: {user_info.get('dob')}".encode('latin-1', 'replace').decode('latin-1'), new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            if user_info.get('address'):
                pdf.cell(usable_width, 5, f"Adresse: {user_info.get('address')}".encode('latin-1', 'replace').decode('latin-1'), new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            if user_info.get('phone'):
                pdf.cell(usable_width, 5, f"Telefon: {user_info.get('phone')}".encode('latin-1', 'replace').decode('latin-1'), new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            pdf.ln(5)


        # --- Benefits Display ---
        if benefits_data and benefits_data.get('leistungen'):
             pdf.set_font("Arial", 'B', 12)
             benefit_title = f"Wichtige Leistungen bei Pflegegrad {pflegegrad}"
             date_range = benefits_data.get('date_range')
             if date_range:
                 benefit_title += f" ({date_range})"
             pdf.cell(usable_width, 10, benefit_title.encode('latin-1', 'replace').decode('latin-1'),
                      new_x=XPos.LMARGIN, new_y=YPos.NEXT)
             pdf.set_font("Arial", size=10)
             for item_dict in benefits_data.get('leistungen', []):
                 item_name = item_dict.get('name', '')
                 item_value = item_dict.get('value', '')
                 pdf.multi_cell(usable_width, 6, f"- {item_name}: {item_value}".encode('latin-1', 'replace').decode('latin-1'),
                                new_x=XPos.LMARGIN, new_y=YPos.NEXT)
             pdf.ln(5)

        # --- Detailed Results ---
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(usable_width, 10, "Detailergebnisse nach Modulen".encode('latin-1', 'replace').decode('latin-1'),
                 new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        module_answers_all = detailed_results.get('answers', {})
        module_scores_raw = detailed_results.get('module_scores_raw', {})
        module_scores_weighted = detailed_results.get('module_scores_weighted', {})
        which_module_contributed = detailed_results.get('which_module_contributed_m2_m3')

        if isinstance(module_answers_all, dict):
            for module_id_str in sorted(module_answers_all.keys(), key=lambda x: int(x) if x.isdigit() else 999):
                if not module_id_str.isdigit(): continue

                module_id = int(module_id_str)
                module_info = all_modules.get(module_id)
                module_answers = module_answers_all.get(module_id_str, {})

                if not module_info: continue

                pdf.set_font("Arial", 'B', 11)
                module_name = module_info.get('name', f'Modul {module_id}')
                pdf.cell(usable_width, 8, f"--- {module_name.encode('latin-1', 'replace').decode('latin-1')} ---",
                         new_x=XPos.LMARGIN, new_y=YPos.NEXT)
                pdf.set_font("Arial", size=10)

                raw_score = module_scores_raw.get(module_id_str, 0.0)
                weighted_score = module_scores_weighted.get(module_id_str, 0.0)

                pdf.cell(usable_width, 6, f"Rohpunkte: {float(raw_score):.1f}".encode('latin-1', 'replace').decode('latin-1'),
                         new_x=XPos.LMARGIN, new_y=YPos.NEXT)
                pdf.cell(usable_width, 6, f"Gewichtete Punkte: {float(weighted_score):.2f}".encode('latin-1', 'replace').decode('latin-1'),
                         new_x=XPos.LMARGIN, new_y=YPos.NEXT)

                if module_id_str in ['2', '3']:
                    note_text = "(Nicht fuer Gesamtpunktzahl beruecksichtigt)"
                    if which_module_contributed is not None and module_id == which_module_contributed:
                        note_text = "(Dieser Wert zaehlt fuer die Gesamtpunktzahl)"
                    pdf.set_font("Arial", 'I', 9)
                    pdf.cell(usable_width, 5, note_text.encode('latin-1', 'replace').decode('latin-1'),
                             new_x=XPos.LMARGIN, new_y=YPos.NEXT)
                    pdf.set_font("Arial", size=10)

                pdf.ln(2)
                pdf.set_font("Arial", 'B', 10)
                pdf.cell(usable_width, 6, "Antworten:".encode('latin-1', 'replace').decode('latin-1'),
                         new_x=XPos.LMARGIN, new_y=YPos.NEXT)
                pdf.set_font("Arial", size=9)

                if isinstance(module_answers, dict) and module_answers:
                    try:
                        sorted_q_keys = sorted(module_answers.keys(), key=lambda k: int(k) if k.isdigit() else float('inf'))
                    except ValueError:
                         sorted_q_keys = sorted(module_answers.keys())

                    for q_key in sorted_q_keys:
                        if q_key == 'notes': continue

                        answer_data = module_answers[q_key]
                        if isinstance(answer_data, dict):
                            q_text = answer_data.get('question', f'Frage {q_key}')
                            a_text = answer_data.get('answer_text', 'N/A')
                            a_score = answer_data.get('score', 'N/A')

                            if answer_data.get('type') == 'frequency':
                                count = answer_data.get('count', 'N/A')
                                unit = answer_data.get('unit', 'N/A')
                                full_text = f"- {q_text}: {count}x pro {unit} ({a_score} Rohpunkte)"
                            else:
                                full_text = f"- {q_text}: {a_text} ({a_score} Rohpunkte)"

                            pdf.multi_cell(usable_width, 5, full_text.encode('latin-1', 'replace').decode('latin-1'),
                                           new_x=XPos.LMARGIN, new_y=YPos.NEXT)
                        else:
                             pdf.multi_cell(usable_width, 5, f"- Frage {q_key}: Ungültige Antwortdaten".encode('latin-1', 'replace').decode('latin-1'),
                                            new_x=XPos.LMARGIN, new_y=YPos.NEXT)
                else:
                     pdf.cell(usable_width, 5, "- Keine Antworten fuer dieses Modul vorhanden.".encode('latin-1', 'replace').decode('latin-1'),
                              new_x=XPos.LMARGIN, new_y=YPos.NEXT)

                # Display Notes for Module
                module_note = notes_data.get(module_id_str, '')
                if module_note:
                    pdf.ln(2)
                    pdf.set_font("Arial", 'B', 10)
                    pdf.cell(usable_width, 6, "Notizen:".encode('latin-1', 'replace').decode('latin-1'),
                             new_x=XPos.LMARGIN, new_y=YPos.NEXT)
                    pdf.set_font("Arial", size=9)
                    pdf.multi_cell(usable_width, 5, module_note.encode('latin-1', 'replace').decode('latin-1'),
                                   new_x=XPos.LMARGIN, new_y=YPos.NEXT)

                pdf.ln(4)
        else:
            pdf.set_font("Arial", 'I', 10)
            pdf.multi_cell(usable_width, 6, "Fehler: Detaillierte Antworten konnten nicht geladen werden.".encode('latin-1', 'replace').decode('latin-1'),
                           new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        # --- Output the PDF ---
        # pdf.output() should return bytes. Add checks and conversion.
        pdf_data = pdf.output()
        current_app.logger.info(f"Type returned by pdf.output(): {type(pdf_data)}") # Log the type

        # Ensure it's bytes before returning
        if isinstance(pdf_data, bytes):
            pdf_output_bytes = pdf_data
        elif isinstance(pdf_data, bytearray):
             pdf_output_bytes = bytes(pdf_data) # Convert bytearray to bytes
        else:
            # This case should ideally not happen with modern fpdf2
            current_app.logger.error(f"pdf.output() returned unexpected type: {type(pdf_data)}. Attempting encoding.")
            # Fallback: try encoding if it's somehow a string (less likely)
            try:
                pdf_output_bytes = str(pdf_data).encode('latin-1', 'replace')
            except Exception as enc_err:
                 current_app.logger.error(f"Fallback encoding failed: {enc_err}", exc_info=True)
                 # Raise an error that will be caught by the outer try/except
                 raise ValueError("Failed to get PDF output as bytes")

        # Log the type *after* potential conversion
        current_app.logger.info(f"Type being passed to Response: {type(pdf_output_bytes)}")

        return Response(
            pdf_output_bytes, # Pass the verified/converted bytes
            mimetype='application/pdf',
            headers={'Content-Disposition': 'attachment;filename=pflegegrad_results.pdf'}
        )

    except Exception as e:
        current_app.logger.error(f"Error generating PDF: {e}", exc_info=True)
        return jsonify({"error": f"An internal server error occurred during PDF generation: {e}"}), 500

# ... (rest of app.py, including if __name__ == '__main__':) ...
# ... (rest of app.py, including if __name__ == '__main__':) ...

if __name__ == '__main__':
    app.run(debug=True, port=5001)