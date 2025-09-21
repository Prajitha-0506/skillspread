import pandas as pd
import random


job_roles = {
    "Data Analyst": ["SQL", "Excel", "Power BI", "Python", "Statistics", "Tableau", "Data Cleaning", "Visualization", "ETL", "Business Intelligence"],
    "Software Engineer": ["Java", "Spring Boot", "REST APIs", "Git", "Unit Testing", "Microservices", "OOP", "Data Structures", "Algorithms", "CI/CD"],
    "Web Developer": ["HTML", "CSS", "JavaScript", "React", "Bootstrap", "AJAX", "SEO", "JSON", "DOM", "Responsive Design"],
    "Data Scientist": ["Python", "Pandas", "Scikit-learn", "Machine Learning", "EDA", "XGBoost", "Seaborn", "Data Pipelines", "Model Evaluation", "Matplotlib"],
    "Machine Learning Engineer": ["Python", "TensorFlow", "Keras", "Deployment", "MLflow", "Hyperparameter Tuning", "ONNX", "Pipelines", "PyTorch", "Numpy"],
    "UI/UX Designer": ["Figma", "Adobe XD", "User Research", "Wireframing", "Prototyping", "Accessibility", "Design Systems", "Sketch", "Usability Testing", "Interaction Design"],
    "DevOps Engineer": ["Docker", "Kubernetes", "CI/CD", "Jenkins", "Bash", "Terraform", "AWS", "Prometheus", "Monitoring", "GitHub Actions"],
    "Cloud Engineer": ["AWS", "Azure", "GCP", "EC2", "S3", "IAM", "VPC", "CloudFormation", "Lambda", "Networking"],
    "Mobile App Developer": ["Flutter", "Kotlin", "Dart", "Android", "iOS", "Firebase", "UI Design", "API Integration", "React Native", "Navigation"],
    "Cybersecurity Analyst": ["Firewalls", "SIEM", "Kali Linux", "Vulnerability Scanning", "Penetration Testing", "Encryption", "Network Security", "Incident Response", "IDS/IPS", "SOC Tools"],
    "Business Analyst": ["Excel", "SQL", "Power BI", "Stakeholder Analysis", "User Stories", "Requirement Gathering", "Process Mapping", "JIRA", "Gap Analysis", "Data Interpretation"],
    "Product Manager": ["Agile", "Scrum", "Backlogs", "Roadmaps", "User Personas", "Market Research", "Metrics", "Feature Prioritization", "Stakeholder Management", "MVP Planning"],
    "Network Engineer": ["TCP/IP", "Switching", "Routing", "BGP", "NAT", "Cisco", "Firewall", "Subnetting", "LAN/WAN", "VPN"],
    "Database Administrator": ["SQL", "MySQL", "Oracle", "Backup", "Recovery", "Indexing", "Replication", "Triggers", "Performance Tuning", "Permissions"],
    "AI Engineer": ["Deep Learning", "NLP", "Neural Networks", "Transformer Models", "BERT", "TensorFlow", "PyTorch", "Model Optimization", "Computer Vision", "GANs"],
    "System Administrator": ["Linux", "Bash Scripting", "Active Directory", "DNS", "System Monitoring", "Virtualization", "User Management", "Security Policies", "Patch Management", "Shell"],
    "Technical Writer": ["Markdown", "API Documentation", "Git", "Diagrams", "User Manuals", "Proofreading", "Technical Research", "Tutorials", "Style Guides", "Version Control"],
    "QA Engineer": ["Manual Testing", "Selenium", "Bug Reporting", "Test Plans", "Regression Testing", "JIRA", "Postman", "Automation Frameworks", "Agile Testing", "Unit Tests"],
    "Blockchain Developer": ["Solidity", "Ethereum", "Smart Contracts", "Web3.js", "Remix", "Truffle", "Gas Optimization", "IPFS", "Decentralized Apps", "EVM"],
    "Full Stack Developer": ["React", "Node.js", "MongoDB", "Express", "REST APIs", "HTML", "CSS", "JavaScript", "Redux", "JWT Auth"],
    "Game Developer": ["Unity", "C#", "Game Physics", "3D Modeling", "Animations", "Scripting", "Game Engines", "Shader Programming", "Level Design", "UI Systems"],
    "Digital Marketer": ["SEO", "Google Analytics", "AdWords", "Email Marketing", "Content Strategy", "Social Media", "Funnel Building", "A/B Testing", "Copywriting", "Marketing Automation"],
    "Content Writer": ["Blogging", "SEO", "Grammar", "Editing", "Proofreading", "Research", "WordPress", "Copywriting", "Creative Writing", "Headline Crafting"],
    "IT Support Specialist": ["Troubleshooting", "Hardware Support", "Software Installation", "Ticketing Systems", "Windows", "Networking", "Customer Service", "Printers", "VPN", "Remote Desktop"],
    "Graphic Designer": ["Photoshop", "Illustrator", "InDesign", "Branding", "Typography", "Layout Design", "Color Theory", "Mockups", "Canva", "Figma"],
    "Financial Analyst": ["Excel", "Forecasting", "Financial Modeling", "Valuation", "Budgeting", "Power BI", "Scenario Analysis", "Dashboards", "Cash Flow", "Variance Analysis"],
    "HR Manager": ["Recruitment", "Payroll", "Performance Reviews", "Compliance", "Training", "HRIS", "Employee Engagement", "Onboarding", "Policy Making", "Compensation"],
    "Legal Advisor": ["Legal Research", "Contracts", "Compliance", "Litigation", "Corporate Law", "Risk Management", "Client Consultation", "Drafting", "Case Analysis", "Intellectual Property"],
    "Operations Manager": ["Inventory", "Supply Chain", "Logistics", "Process Optimization", "Team Management", "Scheduling", "Resource Allocation", "KPI Monitoring", "Vendor Management", "Reporting"],
    "Project Manager": ["Agile", "Waterfall", "Gantt Charts", "Scrum", "Risk Management", "Budgeting", "Communication", "Stakeholder Management", "Milestones", "JIRA"],
    "Accountant": ["Tally", "Excel", "Tax Filing", "GST", "Auditing", "Financial Reporting", "Bank Reconciliation", "Ledger Maintenance", "Cash Flow", "Budgeting"],
    "UX Researcher": ["User Interviews", "Persona Building", "Surveys", "Usability Testing", "Affinity Mapping", "Competitor Analysis", "User Flows", "Ethnographic Research", "Prototyping", "Journey Maps"],
    "Biotech Researcher": ["PCR", "ELISA", "DNA Extraction", "Cell Culture", "Gel Electrophoresis", "Spectrophotometry", "Western Blot", "Microscopy", "Data Analysis", "Sterile Techniques"],
    "Mechanical Engineer": ["AutoCAD", "SolidWorks", "Thermodynamics", "Manufacturing", "GD&T", "CNC", "ANSYS", "Material Science", "CAM", "Machine Design"],
    "Electrical Engineer": ["Circuit Design", "MATLAB", "PCB Design", "Control Systems", "Power Electronics", "Embedded Systems", "Multisim", "Signal Processing", "Load Flow", "Simulink"],
    "Civil Engineer": ["AutoCAD", "Construction Management", "Surveying", "Concrete Technology", "Soil Mechanics", "Estimating", "Project Scheduling", "Building Codes", "Site Supervision", "Reinforcement"],
    "Chemist": ["Titration", "Chromatography", "Lab Safety", "Spectroscopy", "NMR", "pH Measurement", "Sample Preparation", "Analytical Chemistry", "Chemical Handling", "Wet Lab Techniques"],
    "Physicist": ["Quantum Mechanics", "Mathematical Modeling", "Research Design", "Simulations", "Optics", "Thermodynamics", "Statistical Physics", "Experimental Setup", "Data Analysis", "Lab Instruments"],
    "Teacher": ["Lesson Planning", "Assessment", "Classroom Management", "Curriculum Design", "Educational Technology", "Student Engagement", "Grading", "Subject Expertise", "Communication", "Differentiated Instruction"],
    "Librarian": ["Cataloging", "Dewey Decimal", "Archiving", "Library Management", "Metadata", "Reference Services", "Research Help", "Classification", "Circulation", "Library Systems"],
    "Translator": ["Fluent Speaking", "Editing", "Proofreading", "Cultural Sensitivity", "Translation Software", "Localization", "Grammar", "Terminology Management", "Subtitling", "Writing Skills"],
    "Psychologist": ["Counseling", "Behavioral Assessment", "Psychotherapy", "Diagnosis", "Mental Health Evaluation", "Case Studies", "Ethical Guidelines", "Testing Tools", "Treatment Planning", "Interpersonal Skills"],
    "Sociologist": ["Survey Design", "Data Collection", "Interviewing", "Social Theory", "Cultural Analysis", "Statistical Tools", "Report Writing", "Field Research", "Trend Analysis", "Research Ethics"],
    "Economist": ["Forecasting", "Economic Modeling", "Data Analysis", "Inflation Trends", "Policy Research", "GDP Calculation", "Market Research", "Excel", "Time Series", "Game Theory"],
    "Geologist": ["Field Mapping", "GIS", "Mineralogy", "Seismic Analysis", "Core Sampling", "Petrology", "Remote Sensing", "Hydrology", "Stratigraphy", "Geochemistry"],
    "Astronomer": ["Astrophysics", "Telescope Handling", "Spectroscopy", "Sky Mapping", "Observational Astronomy", "Data Reduction", "Image Processing", "Star Charts", "Stellar Physics", "Space Science"],
    "Environmental Scientist": ["Impact Assessment", "Water Sampling", "Soil Analysis", "GIS", "Lab Techniques", "EIA", "Waste Management", "Climate Studies", "Policy Compliance", "Reporting"],
    "Statistician": ["R", "SPSS", "Hypothesis Testing", "Probability Models", "Regression Analysis", "Surveys", "Data Cleaning", "Statistical Inference", "Sampling Techniques", "Data Visualization"],
    "Frontend Developer": ["HTML", "CSS", "JavaScript", "React", "TypeScript","Responsive Design", "Tailwind CSS", "Webpack", "Redux", "UI Components"],
    "Human Resources Executive": ["Recruitment", "Onboarding", "Employee Relations", "Payroll Management", "HRIS","Compliance", "Performance Management", "HR Analytics", "Conflict Resolution", "Talent Management"],
    "Software Architect": ["System Design", "Microservices", "UML", "Cloud Architecture", "Design Patterns","DevOps", "Security Best Practices", "Database Design", "Scalability", "CI/CD Pipelines"],
    "Systems Analyst": ["Requirement Analysis", "SDLC", "UML", "Business Process Modeling", "Documentation","Testing Strategies", "Problem Solving", "Stakeholder Communication", "System Integration", "SQL"],
    "Data Engineer": ["SQL", "ETL", "Data Warehousing", "Apache Spark", "Kafka","Airflow", "BigQuery", "Python", "Data Lakes", "Cloud Platforms (AWS/GCP)"],
    "SEO Specialist": ["Keyword Research", "Google Analytics", "Content Strategy", "On-Page SEO", "Off-Page SEO","Backlinking", "Technical SEO", "SEMRush", "Ahrefs", "Search Engine Algorithms"],
    "API Developer": ["REST APIs", "JSON", "Swagger", "Node.js", "Express.js","Authentication", "Rate Limiting", "Error Handling", "API Testing", "OAuth 2.0"]
}


# Generate dataset
rows = []
for role, skills in job_roles.items():
    unique_combinations = set()
    while len(unique_combinations) < 100:
        selected = tuple(sorted(random.sample(skills, 5)))
        if selected not in unique_combinations:
            unique_combinations.add(selected)
            rows.append({
                "Job Role": role,
                "Skills": ", ".join(selected)
            })

# Save to CSV
df = pd.DataFrame(rows)
df.to_csv("realistic_unique_job_roles_dataset.csv", index=False)
print("✅ Saved: realistic_unique_job_roles_dataset.csv with", len(df), "rows.")
