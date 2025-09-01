"""
Offline Training Manual Generator
No external APIs required — template & rules based.
"""

import json
from datetime import datetime
from jinja2 import Template

profile = {
    "company": "Acme Payments",
    "role": "Customer Support Associate",
    "level": "Junior",
    "department": "Support",
    "location": "Remote",
    "start_date": "2025-09-01",
    "learning_objectives": [
        "Resolve billing queries",
        "Use product dashboard effectively",
        "Follow escalation and compliance process"
    ],
    "prerequisites": [
        "Basic web knowledge",
        "Good communication skills"
    ],
    "duration_days": 7
}

manual_template = """
# {{ company }} - {{ role }} Training Manual

**Level**: {{ level }}
**Department**: {{ department }}
**Location**: {{ location }}
**Start Date**: {{ start_date }}

---

## Overview
Welcome to the training manual for the **{{ role }}** role at {{ company }}.  
This program is designed to help you get productive in your first {{ duration_days }} days.

---

## Learning Objectives
{% for obj in learning_objectives -%}
- {{ obj }}
{% endfor %}

---

## Prerequisites
{% for pre in prerequisites -%}
- {{ pre }}
{% endfor %}

---

## Training Modules
{% for i, obj in enumerate(learning_objectives, start=1) %}
### Module {{ i }}: {{ obj }}
- Duration: {{ 60 }} minutes  
- Objectives:  
  - Understand basics of {{ obj }}
  - Apply knowledge in real-world scenarios
- Activities:  
  - Read documentation  
  - Hands-on exercise  
  - Mini-assessment
{% endfor %}

---

## Daily Schedule
{% for day in range(1, duration_days+1) %}
Day {{ day }}: Training & practice on assigned module(s).
{% endfor %}

---

## Assessment Plan
- Quizzes after each module  
- Final case study project  
- Supervisor feedback

---

## Success Metrics
- Ability to independently handle key tasks  
- Accuracy above 95% in customer responses  
- Positive feedback in first performance review  

---

## Notes
Generated on {{ timestamp }}
"""

template = Template(manual_template)
manual_text = template.render(**profile, timestamp=datetime.now().strftime("%Y-%m-%d %H:%M"))

with open("manual_offline.md", "w", encoding="utf-8") as f:
    f.write(manual_text)

print("Manual generated -> manual_offline.md")
print("\nPreview:\n", manual_text[:500], "...")
