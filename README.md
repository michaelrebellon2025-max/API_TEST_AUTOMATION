# API Automation Testing with PyTest 🚀

![PyTest](https://img.shields.io/badge/tests-passing-brightgreen)  
![Python](https://img.shields.io/badge/python-3.x-blue)

A professional API automation test suite demonstrating **scalable QA automation** using Python and PyTest. 
Validates multiple users and deeply nested JSON fields in the **JSONPlaceholder Users API**.



## 🔹 Key Highlights

- **150+ Tests Passing** ✅  
- Multi-level nested field validation (e.g., `address.geo.lat`, `company.name`)  
- Dynamic user ID testing – automatically adapts as new users are added  
- Data type validation (`str`, `int`) and non-empty field checks  
- Fully parameterized and reusable test design  

---

## 🛠 Tech Stack

- Python 3.x  
- [PyTest](https://docs.pytest.org/) – parameterization, assertions  
- [Requests](https://docs.python-requests.org/) – API calls  

---

## 💻 Quick Start

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
pip install -r requirements.txt
pytest -v
