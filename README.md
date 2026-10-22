# IqraSec Academy — Phase 2: Scripting & Automation

**Internship Project | Cybersecurity | Python & Bash**

**Developer:** Malini S  
**Project:** AutoRecon Lite  
**Repository:** [IqraSec-Phase-2-Scripting-Automation](https://github.com/malu-2707/IqraSec-Phase-2-Scripting-Automation)  
**Submission Deadline:** 25 October 2026

---

## 1. Project Overview

Scripting and automation are essential in cybersecurity because repetitive manual tasks can consume time and introduce errors.

**AutoRecon Lite** is a lightweight command-line reconnaissance automation tool designed to simplify basic network discovery, service enumeration, scan result collection, and report generation in authorized cybersecurity labs.

Developed using Python and integrated with Nmap, the project aims to provide a simple, organized, and efficient workflow for security learners and penetration-testing practitioners.

The tool emphasizes usability, input validation, error handling, maintainable code, and clear reporting.

## 2. Project Objectives

- Automate repetitive reconnaissance tasks.
- Reduce manual effort during authorized security assessments.
- Validate target input before scanning.
- Check required dependencies and handle missing tools.
- Automate port and service enumeration using Nmap.
- Save scan results for future analysis.
- Generate readable Markdown reports from actual scan results.
- Implement appropriate error handling and automated tests.
- Maintain clean, modular, and understandable source code.
- Publish an open-source project suitable for a cybersecurity portfolio.

## 3. Features

The following features define the intended functionality of AutoRecon Lite. Each feature should be marked as complete only after implementation and testing.

- **Target validation:** Validate target IP addresses or supported hostnames.
- **Dependency checking:** Check whether Python and Nmap are available.
- **Reachability checks:** Check whether a target appears reachable where supported.
- **Automated scanning:** Execute configured Nmap port and service enumeration.
- **Result collection:** Store scan output in an organized directory.
- **Report generation:** Create Markdown reports from collected scan results.
- **Error handling:** Handle invalid input, missing dependencies, and failed commands.
- **Command-line interface:** Provide usage instructions and clear error messages.
- **Testing:** Verify input validation and other supported functionality.

## 4. Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Main application and automation logic |
| Bash | Optional command-line automation |
| Nmap | Port scanning and service enumeration |
| Kali Linux | Security testing environment |
| Git | Version control |
| GitHub | Repository hosting and collaboration |
| Markdown | Documentation and report generation |
| Python unittest | Automated testing |

## 5. Project Structure

```text
IqraSec-Phase-2-Scripting-Automation/
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── autorecon.py
├── modules/
│   ├── __init__.py
│   ├── validator.py
│   ├── scanner.py
│   └── reporter.py
├── tests/
│   ├── __init__.py
│   └── test_validator.py
├── reports/
│   └── .gitkeep
└── examples/
    └── sample-report.md
```

This is the recommended structure. The repository should contain only files that actually exist and correspond to the implemented project.

## 6. System Requirements

- Kali Linux or a compatible Linux distribution.
- Python 3.10 or later.
- Nmap installed and available in the system PATH.
- Git, for repository management.
- An authorized target or isolated cybersecurity lab.

Check the installed tools:

```bash
python3 --version
nmap --version
git --version
```

## 7. Installation

### Step 1: Clone the repository

```bash
git clone https://github.com/malu-2707/IqraSec-Phase-2-Scripting-Automation.git
```

### Step 2: Navigate to the project directory

```bash
cd IqraSec-Phase-2-Scripting-Automation
```

### Step 3: Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Step 4: Install dependencies

If the project uses external Python packages, install them with:

```bash
python3 -m pip install -r requirements.txt
```

If the project uses only the Python standard library, `requirements.txt` can remain empty. Nmap must still be installed separately for scanning functionality.

## 8. Usage

The following commands describe the intended interface and should be used after the corresponding options have been implemented.

### Display help

```bash
python3 autorecon.py --help
```

### Run reconnaissance against an authorized lab target

```bash
python3 autorecon.py --target 192.168.56.101
```

### Save results to an output directory

```bash
python3 autorecon.py --target 192.168.56.101 --output reports/
```

**Note:** `192.168.56.101` is an example private-network address, not a verified target address. Replace it with the actual address of your authorized lab machine. The available command-line options must match the implemented script.

## 9. Testing and Quality Assurance

Testing helps ensure that the tool behaves correctly and handles unexpected situations.

The following test cases should be considered:

| Test case | Expected behavior |
|---|---|
| Valid target input | Accept supported target formats |
| Invalid target input | Display an error and reject invalid input |
| Missing Nmap | Explain that the required dependency is unavailable |
| Unreachable target | Report the result without crashing |
| Scan execution failure | Handle the error and return a meaningful status |
| Report generation | Generate a report from actual collected results |
| Invalid command-line arguments | Display usage instructions |

Run the automated test suite:

```bash
python3 -m unittest discover -s tests -v
```

Document the actual test results and fix any failures before submitting the project.

## 10. Example Report Contents

Reports generated by the tool should include relevant information such as:

- Assessment date and time.
- Target supplied by the user.
- Scan configuration.
- Discovered open ports.
- Detected services and versions, when available.
- Scan completion status.
- Output file locations.
- Limitations and observations.

The report must distinguish observed scan results from assumptions. Service detection alone does not prove that a vulnerability exists.

## 11. Ethical Use and Safety

AutoRecon Lite is intended for educational use and authorized cybersecurity assessments.

- Scan only systems you own or have explicit permission to assess.
- Prefer isolated virtual machines for vulnerable-target exercises.
- Do not expose vulnerable machines to public networks.
- Review scan parameters before execution.
- Do not use the tool to access systems without authorization.
- Avoid publishing credentials, sensitive logs, or private information.
- Ensure that reports accurately reflect the tests performed.

The developer is not responsible for unauthorized use of this software.

## 12. Future Improvements

Potential enhancements include:

- JSON and CSV report exports.
- Configurable scan profiles.
- Improved logging and debugging.
- More comprehensive unit and integration tests.
- Report summaries and evidence-based severity classification.
- Configuration files for reusable settings.
- Additional checks for authorized lab environments.
- Continuous integration for automated testing.

## 13. References

- [Kali Linux](https://www.kali.org/)
- [Nmap Official Documentation](https://nmap.org/book/man.html)
- [Python Documentation](https://docs.python.org/3/)
- [GNU Bash Reference Manual](https://www.gnu.org/software/bash/manual/)
- [Git Documentation](https://git-scm.com/doc)
- [GitHub Documentation](https://docs.github.com/)

## 14. Project Information

| Field | Details |
|---|---|
| Academy | IqraSec Academy |
| Internship Phase | Phase 2 — Scripting & Automation |
| Project Name | AutoRecon Lite |
| Developer | Malini S |
| Primary Language | Python |
| Supporting Language | Bash, where implemented |
| Platform | Kali Linux |
| Repository | [GitHub Repository](https://github.com/malu-2707/IqraSec-Phase-2-Scripting-Automation) |


## 15. License

This project is intended to be distributed under the MIT License. The repository must include a valid `LICENSE` file containing the complete license text.

---

**Developed by Malini S as part of the IqraSec Academy internship.**

*Learn. Practice. Secure.*
