

import streamlit as st
import pandas as pd

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="PathForge|Career Builder",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# UI STYLING
# ONLY MARKDOWN IS USED FOR CSS
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap');

* {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #070b14;
    color: #f8fafc;
}

.block-container {
    max-width: 1450px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

section[data-testid="stSidebar"] {
    background: #0a0f1c;
    border-right: 1px solid #1e293b;
}

section[data-testid="stSidebar"] .block-container {
    padding-top: 1.5rem;
}

.sidebar-logo {
    font-size: 42px;
    text-align: center;
}

.sidebar-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 27px;
    font-weight: 800;
    text-align: center;
    color: white;
}

.sidebar-subtitle {
    text-align: center;
    color: #64748b;
    font-size: 12px;
    line-height: 1.5;
    margin-bottom: 25px;
}

h1, h2, h3 {
    font-family: 'Space Grotesk', sans-serif !important;
}

h1 {
    font-weight: 800 !important;
}

h2 {
    font-weight: 700 !important;
}

.hero-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 55px;
    font-weight: 800;
    line-height: 1.05;
    margin-bottom: 15px;
}

.gradient {
    background: linear-gradient(
        90deg,
        #818cf8,
        #a78bfa,
        #22d3ee
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-text {
    color: #94a3b8;
    font-size: 17px;
    line-height: 1.8;
    max-width: 750px;
}

.badge {
    display: inline-block;
    padding: 6px 12px;
    border-radius: 30px;
    background: #111827;
    border: 1px solid #312e81;
    color: #a5b4fc;
    font-size: 12px;
    font-weight: 700;
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(15, 23, 42, 0.65);
    border: 1px solid rgba(148, 163, 184, 0.12);
    border-radius: 18px;
}

div[data-testid="stMetric"] {
    background: #0f172a;
    padding: 18px;
    border-radius: 16px;
    border: 1px solid #1e293b;
}

div[data-testid="stMetricValue"] {
    color: #818cf8;
}

div[data-baseweb="select"] > div {
    background: #0f172a;
    border-color: #334155;
    border-radius: 12px;
}

input {
    background: #0f172a !important;
    color: white !important;
}

.stButton > button,
.stLinkButton > a {
    border-radius: 11px;
    font-weight: 700;
    border: 1px solid #3730a3;
    background: linear-gradient(
        135deg,
        #4f46e5,
        #7c3aed
    );
    color: white;
    transition: .2s ease;
}

.stButton > button:hover,
.stLinkButton > a:hover {
    transform: translateY(-2px);
    border-color: #818cf8;
}

button[data-baseweb="tab"] {
    color: #64748b;
    font-weight: 700;
}

button[data-baseweb="tab"][aria-selected="true"] {
    color: #a5b4fc;
}

img {
    border-radius: 18px;
}

.footer {
    text-align: center;
    padding: 35px 0;
    color: #64748b;
    border-top: 1px solid #1e293b;
    margin-top: 50px;
}

@media(max-width: 768px) {

    .hero-title {
        font-size: 40px;
    }

}

</style>
""", unsafe_allow_html=True)

projects = {

    "AI Engineer": [
        ("🤖 AI Resume Analyzer",
         "Analyze resumes using NLP and AI.",
         "https://github.com/landedjobs/ai-engineer-portfolio-projects"),

        ("📚 RAG Document Chatbot",
         "Ask questions about uploaded documents.",
         "https://github.com/landedjobs/ai-engineer-portfolio-projects"),

        ("🤝 Multi-Agent Research Assistant",
         "Multiple AI agents collaborate to research a topic.",
         "https://github.com/landedjobs/ai-engineer-portfolio-projects"),
    ],

    "Machine Learning Engineer": [
        ("📈 House Price Prediction",
         "Predict house prices using regression models.",
         "https://github.com/ageron/handson-ml3"),

        ("❤️ Disease Prediction",
         "Build a classification model for disease prediction.",
         "https://github.com/ageron/handson-ml3"),

        ("🚗 Car Price Prediction",
         "Predict used-car prices using machine learning.",
         "https://github.com/ageron/handson-ml3"),
    ],

    "Data Scientist": [
        ("📊 Customer Churn Prediction",
         "Predict customers who are likely to leave.",
         "https://github.com/ageron/handson-ml3"),

        ("🛒 Customer Segmentation",
         "Group customers using clustering algorithms.",
         "https://github.com/ageron/handson-ml3"),

        ("📈 Sales Prediction",
         "Forecast future sales using historical data.",
         "https://github.com/ageron/handson-ml3"),
    ],

    "Data Analyst": [
        ("📊 Sales Dashboard",
         "Create an interactive business analytics dashboard.",
         "https://github.com/plotly/dash"),

        ("🛍️ E-Commerce Analysis",
         "Analyze customer and product sales data.",
         "https://github.com/IBM/employee-attrition-aif360"),

        ("📈 Marketing Analytics",
         "Analyze marketing campaign performance.",
         "https://github.com/plotly/dash"),
    ],

    "Data Engineer": [
        ("🔄 ETL Data Pipeline",
         "Build an automated ETL pipeline.",
         "https://github.com/awesomedata/awesome-public-datasets"),

        ("🏗️ Data Warehouse",
         "Create a warehouse for business analytics.",
         "https://github.com/awesomedata/awesome-public-datasets"),

        ("⚡ Real-Time Data Pipeline",
         "Process streaming data in real time.",
         "https://github.com/streamsets"),
    ],

    "Generative AI Engineer": [
        ("✍️ AI Content Generator",
         "Generate articles and summaries using LLMs.",
         "https://github.com/langchain-ai/langchain"),

        ("📚 RAG Knowledge Assistant",
         "Build a knowledge assistant using RAG.",
         "https://github.com/langchain-ai/langchain"),

        ("🎨 AI Image Assistant",
         "Build a multimodal AI application.",
         "https://github.com/openai/openai-cookbook"),
    ],

    "NLP Engineer": [
        ("💬 Sentiment Analyzer",
         "Classify text as positive or negative.",
         "https://github.com/huggingface/transformers"),

        ("📰 News Classifier",
         "Automatically classify news articles.",
         "https://github.com/huggingface/transformers"),

        ("🤖 Text Summarizer",
         "Generate summaries from long documents.",
         "https://github.com/huggingface/transformers"),
    ],

    "Computer Vision Engineer": [
        ("👤 Face Detection System",
         "Detect faces from images or video.",
         "https://github.com/opencv/opencv"),

        ("🚗 Object Detection",
         "Detect vehicles and objects in images.",
         "https://github.com/ultralytics/ultralytics"),

        ("🩻 Medical Image Classifier",
         "Classify medical images using deep learning.",
         "https://github.com/pytorch/pytorch"),
    ],

    "MLOps Engineer": [
        ("🚀 ML Model Deployment",
         "Deploy a machine learning model as an API.",
         "https://github.com/mlflow/mlflow"),

        ("📊 ML Monitoring System",
         "Monitor model performance and data drift.",
         "https://github.com/evidentlyai/evidently"),

        ("🔄 ML CI/CD Pipeline",
         "Automate model testing and deployment.",
         "https://github.com/mlflow/mlflow"),
    ],

    "AI Research Scientist": [
        ("🧠 Transformer From Scratch",
         "Implement a transformer architecture.",
         "https://github.com/karpathy/nanoGPT"),

        ("🔬 Neural Network From Scratch",
         "Build a neural network without frameworks.",
         "https://github.com/karpathy/micrograd"),

        ("📚 LLM From Scratch",
         "Understand and implement an LLM.",
         "https://github.com/rasbt/LLMs-from-scratch"),
    ],

    "Software Engineer": [
        ("💻 Task Management System",
         "Full-stack task management application.",
         "https://github.com/vercel/next.js"),

        ("🛒 E-Commerce Application",
         "Build a complete online shopping platform.",
         "https://github.com/medusajs/medusa"),

        ("💬 Real-Time Chat App",
         "Build a real-time messaging application.",
         "https://github.com/socketio/socket.io"),
    ],

    "Full Stack Developer": [
        ("🛒 E-Commerce Website",
         "Full-stack shopping website.",
         "https://github.com/medusajs/medusa"),

        ("💼 Job Portal",
         "Create a job searching and recruitment platform.",
         "https://github.com/vercel/next.js"),

        ("📱 Social Media App",
         "Build a social networking application.",
         "https://github.com/vercel/next.js"),
    ],

    "Backend Developer": [
        ("🔐 Authentication API",
         "JWT-based authentication backend.",
         "https://github.com/fastapi/fastapi"),

        ("🛒 E-Commerce API",
         "REST API for products, users and orders.",
         "https://github.com/fastapi/fastapi"),

        ("💬 Chat Backend",
         "Real-time messaging backend.",
         "https://github.com/socketio/socket.io"),
    ],

    "Frontend Developer": [
        ("🎨 Portfolio Website",
         "Create a modern developer portfolio.",
         "https://github.com/facebook/react"),

        ("🛒 Shopping UI",
         "Build an e-commerce frontend.",
         "https://github.com/facebook/react"),

        ("📊 Analytics Dashboard",
         "Interactive frontend dashboard.",
         "https://github.com/facebook/react"),
    ],

    "Mobile App Developer": [
        ("📱 Expense Tracker",
         "Track personal expenses through a mobile app.",
         "https://github.com/flutter/flutter"),

        ("🏋️ Fitness Tracker",
         "Track workouts and fitness goals.",
         "https://github.com/flutter/flutter"),

        ("📝 Notes App",
         "Cloud-connected mobile notes application.",
         "https://github.com/flutter/flutter"),
    ],

    "Cloud Engineer": [
        ("☁️ Cloud File Storage",
         "Build cloud-based file storage.",
         "https://github.com/aws/aws-cli"),

        ("🌐 Serverless API",
         "Build a serverless REST API.",
         "https://github.com/aws/aws-lambda-java-libs"),

        ("📊 Cloud Monitoring",
         "Monitor cloud infrastructure.",
         "https://github.com/prometheus/prometheus"),
    ],

    "Cloud Architect": [
        ("🏗️ Cloud Architecture",
         "Design a scalable web application architecture.",
         "https://github.com/aws-samples"),

        ("🌐 Multi-Region Application",
         "Design highly available infrastructure.",
         "https://github.com/aws-samples"),

        ("🔄 Disaster Recovery System",
         "Build a cloud disaster recovery architecture.",
         "https://github.com/aws-samples"),
    ],

    "DevOps Engineer": [
        ("🚀 CI/CD Pipeline",
         "Automate testing and deployment.",
         "https://github.com/actions"),

        ("🐳 Dockerized Application",
         "Containerize and deploy a web application.",
         "https://github.com/docker/awesome-compose"),

        ("☸️ Kubernetes Deployment",
         "Deploy an application using Kubernetes.",
         "https://github.com/kubernetes/kubernetes"),
    ],

    "Site Reliability Engineer (SRE)": [
        ("📊 Service Monitoring",
         "Monitor application health and uptime.",
         "https://github.com/prometheus/prometheus"),

        ("🚨 Alerting System",
         "Create automated infrastructure alerts.",
         "https://github.com/prometheus/alertmanager"),

        ("⚡ Load Testing System",
         "Test application performance under load.",
         "https://github.com/grafana/k6"),
    ],

    "Platform Engineer": [
        ("⚙️ Internal Developer Platform",
         "Build tools for developer self-service.",
         "https://github.com/backstage/backstage"),

        ("🚀 Deployment Platform",
         "Create a platform for automated deployments.",
         "https://github.com/backstage/backstage"),

        ("📦 Container Platform",
         "Manage containerized applications.",
         "https://github.com/kubernetes/kubernetes"),
    ],

    "Cybersecurity Engineer": [
        ("🔐 Security Monitoring System",
         "Monitor systems for suspicious activity.",
         "https://github.com/wazuh/wazuh"),

        ("🛡️ Vulnerability Scanner",
         "Scan applications for common vulnerabilities.",
         "https://github.com/projectdiscovery/nuclei"),

        ("🔑 Password Security Checker",
         "Analyze password security practices.",
         "https://github.com/zxcvbn-ts/zxcvbn"),
    ],

    "Cybersecurity Analyst": [
        ("🚨 SIEM Dashboard",
         "Analyze security events and alerts.",
         "https://github.com/wazuh/wazuh"),

        ("🔍 Log Analyzer",
         "Detect suspicious patterns in logs.",
         "https://github.com/wazuh/wazuh"),

        ("📊 Security Dashboard",
         "Visualize security events.",
         "https://github.com/grafana/grafana"),
    ],

    "Cloud Security Engineer": [
        ("☁️ Cloud Security Monitor",
         "Monitor cloud resources for security issues.",
         "https://github.com/prowler-cloud/prowler"),

        ("🔐 IAM Audit Tool",
         "Audit cloud identity permissions.",
         "https://github.com/prowler-cloud/prowler"),

        ("🛡️ Cloud Compliance Scanner",
         "Check cloud infrastructure against security standards.",
         "https://github.com/prowler-cloud/prowler"),
    ],

    "Security Architect": [
        ("🏰 Zero Trust Architecture",
         "Design a zero-trust security architecture.",
         "https://github.com/GoogleCloudPlatform/zero-trust-architecture"),

        ("🔐 Secure Cloud Architecture",
         "Design a secure cloud environment.",
         "https://github.com/aws-samples"),

        ("🛡️ Enterprise Security Design",
         "Design enterprise security controls.",
         "https://github.com/OWASP"),
    ],

    "Database Administrator": [
        ("🗄️ Database Monitoring",
         "Monitor database health and performance.",
         "https://github.com/prometheus-community/postgres_exporter"),

        ("💾 Database Backup System",
         "Automate database backups.",
         "https://github.com/postgres/postgres"),

        ("📊 Database Performance Analyzer",
         "Analyze database performance.",
         "https://github.com/postgres/postgres"),
    ],

    "Solutions Architect": [
        ("🏗️ Scalable Web Architecture",
         "Design scalable cloud architecture.",
         "https://github.com/aws-samples"),

        ("🌐 Microservices Architecture",
         "Design a microservices-based application.",
         "https://github.com/microservices-demo/microservices-demo"),

        ("📦 Event-Driven Architecture",
         "Build an event-driven application.",
         "https://github.com/aws-samples"),
    ],

    "Blockchain Developer": [
        ("⛓️ Voting DApp",
         "Build a decentralized voting application.",
         "https://github.com/OpenZeppelin/openzeppelin-contracts"),

        ("💰 Token Application",
         "Create and interact with blockchain tokens.",
         "https://github.com/OpenZeppelin/openzeppelin-contracts"),

        ("🗳️ Decentralized Identity",
         "Build a blockchain identity system.",
         "https://github.com/ethereum/ethereum-org-website"),
    ],

    "Web3 Developer": [
        ("🌐 Web3 Wallet",
         "Build a blockchain wallet interface.",
         "https://github.com/ethereum/ethereum-org-website"),

        ("🖼️ NFT Marketplace",
         "Build a decentralized NFT marketplace.",
         "https://github.com/OpenZeppelin/openzeppelin-contracts"),

        ("💰 DeFi Dashboard",
         "Display decentralized finance data.",
         "https://github.com/ethereum/ethereum-org-website"),
    ],

    "IoT Engineer": [
        ("🏠 Smart Home",
         "Control home devices through IoT.",
         "https://github.com/home-assistant/core"),

        ("🌡️ Smart Weather Station",
         "Collect temperature and environmental data.",
         "https://github.com/esphome/esphome"),

        ("🚗 Vehicle Monitoring",
         "Monitor vehicle data using IoT sensors.",
         "https://github.com/esphome/esphome"),
    ],

    "Embedded Systems Engineer": [
        ("🌡️ Temperature Monitor",
         "Build a microcontroller temperature monitor.",
         "https://github.com/arduino/Arduino"),

        ("🚗 Smart Parking System",
         "Detect available parking spaces.",
         "https://github.com/arduino/Arduino"),

        ("🚦 Smart Traffic Light",
         "Build an automated traffic control prototype.",
         "https://github.com/arduino/Arduino"),
    ],

    "QA Automation Engineer": [
        ("🧪 Web Automation Framework",
         "Automate browser testing.",
         "https://github.com/SeleniumHQ/selenium"),

        ("🔄 API Testing Framework",
         "Automate REST API testing.",
         "https://github.com/karatelabs/karate"),

        ("🚀 CI Test Automation",
         "Run automated tests through CI/CD.",
         "https://github.com/pytest-dev/pytest"),
    ],

    "Test Engineer": [
        ("🧪 Automated Test Suite",
         "Create automated software tests.",
         "https://github.com/pytest-dev/pytest"),

        ("🔍 API Test System",
         "Test APIs automatically.",
         "https://github.com/karatelabs/karate"),

        ("📱 Mobile Testing",
         "Automate mobile application testing.",
         "https://github.com/appium/appium"),
    ],

    "Technical Product Manager": [
        ("📱 AI Product Prototype",
         "Create an AI-powered product prototype.",
         "https://github.com/landedjobs/ai-engineer-portfolio-projects"),

        ("📊 Product Analytics Dashboard",
         "Track product KPIs and user behavior.",
         "https://github.com/plotly/dash"),

        ("🤖 AI Feature Prototype",
         "Prototype an AI-powered product feature.",
         "https://github.com/langchain-ai/langchain"),
    ],

    "Technology Consultant": [
        ("🏢 Digital Transformation Dashboard",
         "Analyze technology transformation metrics.",
         "https://github.com/plotly/dash"),

        ("☁️ Cloud Migration Planner",
         "Create a cloud migration planning tool.",
         "https://github.com/aws-samples"),

        ("📊 Technology Assessment Tool",
         "Assess technology infrastructure and maturity.",
         "https://github.com/grafana/grafana"),
    ],

    "Database Engineer": [
        (
            "🗄️ Database Management System",
            "Build a system for managing databases, tables and queries.",
            "https://github.com/postgres/postgres"
        ),
        (
            "📊 Database Performance Monitor",
            "Monitor database queries, performance and resource usage.",
            "https://github.com/percona/pmm"
        )
    ],

    "API Developer": [
        (
            "🔌 REST API Platform",
            "Build a scalable REST API with authentication and documentation.",
            "https://github.com/fastapi/fastapi"
        ),
        (
            "📡 API Gateway",
            "Create an API gateway for routing and managing services.",
            "https://github.com/Kong/kong"
        )
    ],

    "System Administrator": [
        (
            "🖥️ Server Monitoring System",
            "Monitor CPU, memory, disk and server health.",
            "https://github.com/prometheus/prometheus"
        ),
        (
            "⚙️ Linux Server Automation",
            "Automate common Linux administration tasks.",
            "https://github.com/ansible/ansible"
        )
    ],

    "Network Engineer": [
        (
            "🌐 Network Monitoring Dashboard",
            "Monitor network devices, traffic and availability.",
            "https://github.com/librenms/librenms"
        ),
        (
            "📡 Network Automation",
            "Automate network configuration and management.",
            "https://github.com/ansible/ansible"
        )
    ],

    "Network Security Engineer": [
        (
            "🛡️ Network Intrusion Detection",
            "Detect suspicious network traffic and activity.",
            "https://github.com/zeek/zeek"
        ),
        (
            "🔍 Network Security Monitor",
            "Analyze network traffic for security events.",
            "https://github.com/suricata/suricata"
        )
    ],

    "Penetration Tester": [
        (
            "🔎 Web Security Lab",
            "Build a legal local environment for practicing web security testing.",
            "https://github.com/WebGoat/WebGoat"
        ),
        (
            "🧪 Vulnerability Testing Lab",
            "Practice identifying vulnerabilities in intentionally vulnerable applications.",
            "https://github.com/juice-shop/juice-shop"
        )
    ],

    "SOC Engineer": [
        (
            "🚨 SOC Monitoring Dashboard",
            "Create a dashboard for security events and alerts.",
            "https://github.com/wazuh/wazuh"
        ),
        (
            "🔔 Security Alert Automation",
            "Automate detection and notification of security events.",
            "https://github.com/wazuh/wazuh"
        )
    ],

    "Forensic Analyst": [
        (
            "🔬 Digital Forensics Lab",
            "Create a controlled environment for analyzing forensic evidence.",
            "https://github.com/volatilityfoundation/volatility3"
        ),
        (
            "💾 Memory Analysis Tool",
            "Analyze memory dumps for forensic investigation.",
            "https://github.com/volatilityfoundation/volatility3"
        )
    ],

    "Privacy Engineer": [
        (
            "🔐 Privacy Audit Tool",
            "Analyze an application's handling of sensitive data.",
            "https://github.com/privacylab/yappl"
        ),
        (
            "🛡️ Data Privacy Dashboard",
            "Track privacy-related application settings and controls.",
            "https://github.com/privacylab/yappl"
        )
    ],

    "Blockchain Security Engineer": [
        (
            "🔐 Smart Contract Analyzer",
            "Analyze smart contracts for common security issues.",
            "https://github.com/crytic/slither"
        ),
        (
            "🛡️ Solidity Security Lab",
            "Practice secure smart-contract development.",
            "https://github.com/ConsenSys/smart-contract-best-practices"
        )
    ],

    "Database Reliability Engineer": [
        (
            "💾 Automated Backup System",
            "Automate database backups and recovery workflows.",
            "https://github.com/postgres/postgres"
        ),
        (
            "🚨 Database Health Monitor",
            "Monitor database availability and performance.",
            "https://github.com/prometheus-community/postgres_exporter"
        )
    ],

    "Observability Engineer": [
        (
            "📊 Observability Platform",
            "Collect metrics, logs and traces from applications.",
            "https://github.com/grafana/grafana"
        ),
        (
            "🔭 Distributed Tracing System",
            "Track requests across multiple services.",
            "https://github.com/open-telemetry/opentelemetry-collector"
        )
    ],

    "Performance Engineer": [
        (
            "⚡ Website Performance Tester",
            "Measure web application performance under different loads.",
            "https://github.com/grafana/k6"
        ),
        (
            "📈 Load Testing Platform",
            "Build automated performance and load tests.",
            "https://github.com/locustio/locust"
        )
    ],

    "Release Engineer": [
        (
            "🚀 Automated Release Pipeline",
            "Automate application builds, testing and releases.",
            "https://github.com/actions"
        ),
        (
            "📦 Package Release System",
            "Automate versioning and software package releases.",
            "https://github.com/python-poetry/poetry"
        )
    ],

    "Build Engineer": [
        (
            "🔨 Build Automation System",
            "Create automated software build workflows.",
            "https://github.com/bazelbuild/bazel"
        ),
        (
            "⚙️ Build Dependency Manager",
            "Manage dependencies and reproducible builds.",
            "https://github.com/gradle/gradle"
        )
    ],

    "Firmware Engineer": [
        (
            "🔌 IoT Device Firmware",
            "Develop firmware for connected embedded devices.",
            "https://github.com/zephyrproject-rtos/zephyr"
        ),
        (
            "📡 Wireless Sensor Firmware",
            "Create firmware for a wireless sensor device.",
            "https://github.com/zephyrproject-rtos/zephyr"
        )
    ],

    "Hardware Design Engineer": [
        (
            "🔧 Open Hardware Board",
            "Design and document an open-source hardware board.",
            "https://github.com/KiCad/kicad-source-mirror"
        ),
        (
            "⚡ PCB Design Project",
            "Design a PCB for an embedded electronics project.",
            "https://github.com/KiCad/kicad-source-mirror"
        )
    ],

    "FPGA Engineer": [
        (
            "⚡ FPGA CPU",
            "Implement a simple CPU architecture on an FPGA.",
            "https://github.com/YosysHQ/picorv32"
        ),
        (
            "📡 FPGA Signal Processor",
            "Build a digital signal-processing system on FPGA.",
            "https://github.com/YosysHQ/yosys"
        )
    ],

    "Computer Graphics Engineer": [
        (
            "🎨 3D Renderer",
            "Build a basic 3D graphics rendering engine.",
            "https://github.com/ssloy/tinyrenderer"
        ),
        (
            "🌐 WebGL 3D Scene",
            "Create an interactive 3D scene in the browser.",
            "https://github.com/mrdoob/three.js"
        )
    ],

    "Technical Writer": [
        (
            "📚 Developer Documentation",
            "Create professional documentation for an open-source project.",
            "https://github.com/withastro/starlight"
        ),
        (
            "📖 API Documentation Portal",
            "Build a searchable documentation website for an API.",
            "https://github.com/Redocly/redoc"
        )
    ],

    "Developer Advocate": [
        (
            "🎤 Developer Community Portal",
            "Build a platform for tutorials, events and developer resources.",
            "https://github.com/docusaurus/docusaurus"
        ),
        (
            "📚 Interactive Developer Tutorials",
            "Create an interactive learning website for developers.",
            "https://github.com/freeCodeCamp/freeCodeCamp"
        )
    ]
}

# ============================================================
# PLATFORMS
# ============================================================

platforms = [
    "Internshala",
    "AICTE National Internship Portal",
    "LinkedIn",
    "Indeed",
    "Glassdoor",
    "Wellfound",
    "Handshake",
    "Forage",
    "Unstop",
    "Naukri",
    "LetsIntern",
    "Chegg Internships",

    "Google Careers",
    "Microsoft Careers",
    "Amazon Jobs",
    "Meta Careers",
    "Apple Jobs",
    "IBM Careers",
    "Oracle Careers",
    "Adobe Careers",
    "NVIDIA Careers",
    "Intel Careers",
    "Cisco Careers",
    "Salesforce Careers",
    "SAP Careers",
    "Deloitte Careers",
    "Accenture Careers",
    "TCS Careers",
    "Infosys Careers",
    "Wipro Careers",
    "Cognizant Careers",
    "Capgemini Careers",
    "HCLTech Careers",
    "Tech Mahindra Careers",

    "Coursera",
    "edX",
    "Udemy",
    "Udacity",
    "Great Learning",
    "Simplilearn",
    "DataCamp",
    "Codecademy",
    "Pluralsight",
    "LinkedIn Learning",
    "Khan Academy",
    "freeCodeCamp",

    "NPTEL",
    "SWAYAM",
    "IIT Madras Online",
    "IIT Bombay",
    "IIT Delhi",
    "IIT Kanpur",
    "IIT Kharagpur",
    "IIT Roorkee",
    "AICTE",
    "UGC",

    "LeetCode",
    "HackerRank",
    "CodeChef",
    "Codeforces",
    "AtCoder",
    "GeeksforGeeks",
    "HackerEarth",
    "Exercism",
    "Coding Ninjas",
    "InterviewBit",

    "Kaggle",
    "Google AI",
    "Google Machine Learning",
    "DeepLearning.AI",
    "fast.ai",
    "Hugging Face",
    "DataCamp",
    "MIT OpenCourseWare",
    "IBM SkillsBuild",

    "AWS Skill Builder",
    "Microsoft Learn",
    "Google Cloud Skills Boost",
    "Oracle University",
    "Cisco Networking Academy",
    "Red Hat Learning",
    "Linux Foundation",
    "Docker",
    "Kubernetes",

    "TryHackMe",
    "Hack The Box",
    "PortSwigger Web Security Academy",
    "Cybrary",
    "Cisco Networking Academy",
    "EC-Council",

    "MDN Web Docs",
    "freeCodeCamp",
    "The Odin Project",
    "W3Schools",
    "Frontend Mentor",
    "Full Stack Open",

    "GitHub",
    "GitLab",
    "Open Source Guides",
    "Google Summer of Code",
    "Outreachy",
    "Linux Foundation",

    "AWS Certification",
    "Microsoft Certifications",
    "Google Cloud Certification",
    "Cisco Certifications",
    "Oracle Certification",
    "IBM Certification",
    "CompTIA",
    "Red Hat Certification",

    "GitHub",
    "LinkedIn",
    "Stack Overflow",
    "Reddit",
    "Discord",
    "Dev.to",
    "Hashnode",

    "LinkedIn Jobs",
    "Indeed",
    "Naukri",
    "Glassdoor",
    "Wellfound",
    "Hired",
    "Dice",
    "Cutshort",
    "Instahyre",

    "Unstop",
    "Devpost",
    "MLH",
    "Kaggle",
    "Hackathon.com",
    "HackerEarth",
    "CodeChef",
    "Codeforces"
]

# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        '<div class="sidebar-logo">🧭</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-title">PathForge</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-subtitle">'
        'Build Skills. Build Projects.<br>'
        'Build Your Career.'
        '</div>',
        unsafe_allow_html=True
    )

    st.divider()

    st.subheader("🎯 Career Target")

    role = st.selectbox(
        "Choose your tech role",
        [
            "Select a role",
            "AI Engineer",
            "Machine Learning Engineer",
            "Generative AI Engineer",
            "AI Research Scientist",
            "Data Scientist",
            "Data Engineer",
            "Data Analyst",
            "MLOps Engineer",
            "Software Engineer",
            "Full Stack Developer",
            "Backend Developer",
            "Frontend Developer",
            "Mobile App Developer",
            "Cloud Engineer",
            "Cloud Architect",
            "DevOps Engineer",
            "Site Reliability Engineer (SRE)",
            "Cybersecurity Engineer",
            "Cybersecurity Analyst",
            "Cloud Security Engineer",
            "Penetration Tester",
            "Database Administrator",
            "Database Engineer",
            "Blockchain Developer",
            "Web3 Developer",
            "IoT Engineer",
            "Embedded Systems Engineer",
            "QA Automation Engineer",
            "Technical Product Manager",
            "Technology Consultant"
        ]
    )

    st.divider()

    st.subheader("📊 Your Progress")

    st.metric(
        "Projects Built",
        "0",
        "+1 target"
    )

    st.progress(0.15)

    st.caption("Career preparation: 15%")

# ============================================================
# NAVIGATION
# ============================================================

home, api_tab, projects_tab, internship_tab, about_tab = st.tabs(
    [
        "🏠 Home",
        "🔌 APIs",
        "🚀 Projects",
        "🎓 Internships",
        "ℹ️ About"
    ]
)

# ============================================================
# HOME
# ============================================================

with home:

    st.markdown(
        '<span class="badge">🧭 YOUR TECH CAREER COMPASS</span>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="hero-title">
        Build Your <span class="gradient">Future.</span>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="hero-text">
        PathForge helps students discover technology careers,
        build portfolio projects, explore useful APIs and find
        opportunities that turn learning into real-world experience.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    if role != "Select a role":

        st.success(
            f"🎯 Your selected career: **{role}**"
        )

    st.divider()

    st.subheader("📊 PathForge at a Glance")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Career Roles",
            "80+"
        )

    with c2:
        st.metric(
            "Projects",
            "100+"
        )

    with c3:
        st.metric(
            "Free APIs",
            "13+"
        )

    with c4:
        st.metric(
            "Resources",
            "100+"
        )

    st.divider()

    st.subheader("🗺️ Your Career Journey")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        with st.container(border=True):
            st.subheader("📚 Learn")
            st.write(
                "Master the fundamentals and develop strong technical skills."
            )

    with c2:
        with st.container(border=True):
            st.subheader("🛠️ Build")
            st.write(
                "Turn your knowledge into practical portfolio projects."
            )

    with c3:
        with st.container(border=True):
            st.subheader("🐙 Publish")
            st.write(
                "Put your projects on GitHub and build proof of work."
            )

    with c4:
        with st.container(border=True):
            st.subheader("📈 Grow")
            st.write(
                "Apply for internships, jobs and continuously improve."
            )

    st.divider()

    st.subheader("✨ Why PathForge?")

    left, right = st.columns(2)

    with left:

        with st.container(border=True):
            st.subheader("🎯 Career Discovery")
            st.write(
                "Explore modern technology roles and identify "
                "the skills required for each career."
            )

        with st.container(border=True):
            st.subheader("🚀 Project-Based Learning")
            st.write(
                "Build real applications instead of relying only "
                "on tutorials and certificates."
            )

        with st.container(border=True):
            st.subheader("🐙 Open Source")
            st.write(
                "Explore GitHub repositories and learn from real "
                "software projects."
            )

    with right:

        with st.container(border=True):
            st.subheader("🔌 Useful APIs")
            st.write(
                "Discover free APIs that can make your projects "
                "more powerful."
            )

        with st.container(border=True):
            st.subheader("🎓 Opportunities")
            st.write(
                "Explore internship, learning and career platforms."
            )

        with st.container(border=True):
            st.subheader("🔥 Build for the Future")
            st.write(
                "Develop skills around modern technologies such as "
                "AI, cloud, cybersecurity and software engineering."
            )

# ============================================================
# APIs
# ============================================================

with api_tab:

    st.title("🔌 Free APIs")

    st.caption(
        "Useful APIs for building real-world student projects."
    )

    api_search = st.text_input(
        "🔎 Search APIs",
        placeholder="Try weather, books, users, games..."
    )

    api_data = [
        (
            "🧪",
            "JSONPlaceholder",
            "Fake REST API for testing and practice.",
            "https://jsonplaceholder.typicode.com/"
        ),
        (
            "🛍️",
            "DummyJSON",
            "Products, users, carts and sample data.",
            "https://dummyjson.com/"
        ),
        (
            "🌍",
            "REST Countries",
            "Countries, currencies, languages and flags.",
            "https://restcountries.com/"
        ),
        (
            "🌦️",
            "Open-Meteo",
            "Weather and forecast data.",
            "https://open-meteo.com/"
        ),
        (
            "📚",
            "Open Library",
            "Books and author information.",
            "https://openlibrary.org/developers/api"
        ),
        (
            "🎮",
            "PokéAPI",
            "Pokémon information and game data.",
            "https://pokeapi.co/"
        ),
        (
            "💱",
            "Frankfurter",
            "Currency exchange rates.",
            "https://www.frankfurter.app/"
        ),
        (
            "🐱",
            "The Cat API",
            "Cat images and information.",
            "https://thecatapi.com/"
        ),
        (
            "🐶",
            "Dog CEO",
            "Dog images and breed information.",
            "https://dog.ceo/dog-api/"
        ),
        (
            "👤",
            "Random User",
            "Generate random user profiles.",
            "https://randomuser.me/"
        ),
        (
            "🚀",
            "NASA API",
            "Space and astronomy data.",
            "https://api.nasa.gov/"
        )
    ]

    if api_search:

        api_data = [
            item for item in api_data
            if (
                api_search.lower() in item[1].lower()
                or api_search.lower() in item[2].lower()
            )
        ]

    for start in range(0, len(api_data), 3):

        cols = st.columns(3)

        for col, item in zip(
            cols,
            api_data[start:start + 3]
        ):

            icon, name, description, url = item

            with col:

                with st.container(border=True):

                    st.subheader(
                        f"{icon} {name}"
                    )

                    st.write(description)

                    st.link_button(
                        "Open API →",
                        url,
                        use_container_width=True
                    )

# ============================================================
# PROJECTS
# ============================================================

with projects_tab:

    st.title("🚀 Project Explorer")

    st.caption(
        "Build projects that prove your technical skills."
    )

    project_search = st.text_input(
        "🔎 Search projects",
        placeholder="AI, ML, Python, Cloud, Security..."
    )

    project_roles = sorted(projects.keys())

    selected_project_role = st.selectbox(
        "🎯 Filter by role",
        ["All Roles"] + project_roles
    )

    st.divider()

    results = []

    for project_role, role_projects in projects.items():

        if (
            selected_project_role != "All Roles"
            and project_role != selected_project_role
        ):
            continue

        for project in role_projects:

            project_name, description, github = project

            if not project_search:

                results.append(
                    (project_role, project)
                )

            else:

                query = project_search.lower()

                if (
                    query in project_role.lower()
                    or query in project_name.lower()
                    or query in description.lower()
                ):
                    results.append(
                        (project_role, project)
                    )

    st.caption(
        f"Showing {len(results)} project(s)"
    )

    for start in range(0, len(results), 3):

        cols = st.columns(3)

        for col, item in zip(
            cols,
            results[start:start + 3]
        ):

            project_role, project = item

            project_name, description, github = project

            with col:

                with st.container(border=True):

                    st.caption(project_role)

                    st.subheader(project_name)

                    st.write(description)

                    st.link_button(
                        "🐙 View GitHub",
                        github,
                        use_container_width=True
                    )

    if not results:

        st.warning(
            "No projects found. Try another search."
        )

# ============================================================
# INTERNSHIPS
# ============================================================

with internship_tab:

    st.title("🎓 Internships & Learning")

    st.caption(
        "Discover platforms for internships, courses and career development."
    )

    # ========================================================
    # VERIFICATION
    # ========================================================

    with st.container(border=True):

        st.subheader("🛡️ Platform Verification")

        st.write(
            "Check whether a platform exists in the PathForge "
            "curated resource list."
        )

        platform_name = st.text_input(
            "Platform name",
            placeholder="Example: Coursera"
        )

        verify = st.button(
            "🔍 Verify Platform",
            use_container_width=True
        )

        if verify:

            if not platform_name.strip():

                st.warning(
                    "Please enter a platform name."
                )

            else:

                clean_name = platform_name.strip().lower()

                verified = False

                # ====================================================
                # FIXED: platforms is a LIST, not a DICTIONARY
                # ====================================================

                for platform in platforms:

                    if clean_name == platform.lower():
                        verified = True
                        break

                if verified:

                    st.success(
                        f"✅ {platform_name.strip()} "
                        "is listed in PathForge."
                    )

                else:

                    st.error(
                        f"❌ {platform_name.strip()} "
                        "is not currently in the curated list."
                    )

    st.divider()

    # ========================================================
    # RESOURCE EXPLORER
    # ========================================================

    st.subheader("🌐 Resource Explorer")

    # ====================================================
    # FIXED: platforms is a LIST, so there are no .keys()
    # ====================================================

    category = "All Resources"

    resources = platforms

    st.caption(
        f"{len(resources)} resources available"
    )

    for start in range(0, len(resources), 3):

        cols = st.columns(3)

        for col, resource in zip(
            cols,
            resources[start:start + 3]
        ):

            with col:

                with st.container(border=True):

                    st.subheader(resource)

                    st.caption(category)

                    st.write(
                        "Explore this resource for learning, "
                        "career development or opportunities."
                    )

# ============================================================
# ABOUT
# ============================================================

with about_tab:

    st.title("ℹ️ About PathForge")

    st.caption(
        "A student-focused platform for building technology careers."
    )

    left, right = st.columns([1.5, 1])

    with left:

        with st.container(border=True):

            st.caption("CREATED BY AKHIL")

            st.header("Kurapati Akhil")

            st.write(
                """
                I am a developer interested in building useful
                and innovative applications.

                PathForge brings career resources, projects,
                APIs, internships and developer opportunities
                together in one place.
                """
            )

            st.subheader("🚀 What I Do")

            st.write("💻 Build web applications and developer tools")
            st.write("🔗 Explore APIs and developer platforms")
            st.write("🐙 Work with GitHub and open-source projects")
            st.write("📚 Learn emerging technologies")
            st.write("🚀 Build useful applications")

            st.link_button(
                "🔗 Connect on LinkedIn",
                "https://www.linkedin.com/in/akhil-kurapati-0b8b3b3b3/",
                use_container_width=True
            )

    with right:

        with st.container(border=True):

            st.header("🧭 PathForge")

            st.write(
                "Built around one simple philosophy:"
            )

            st.success("📚 Learn")

            st.info("🛠️ Build")

            st.warning("🐙 Publish")

            st.success("📈 Grow")

    st.divider()

    st.subheader("✨ Our Principles")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        with st.container(border=True):
            st.subheader("🎯 Clarity")
            st.write(
                "Know what career you're building toward."
            )

    with c2:
        with st.container(border=True):
            st.subheader("🛠️ Practice")
            st.write(
                "Learn by building real applications."
            )

    with c3:
        with st.container(border=True):
            st.subheader("🐙 Proof")
            st.write(
                "Show your skills through projects."
            )

    with c4:
        with st.container(border=True):
            st.subheader("📈 Growth")
            st.write(
                "Keep improving as technology evolves."
            )

# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">

    🧭 <strong>PathForge</strong>

    <br><br>

    Build Skills. Build Projects. Build Your Career.

    <br><br>

    Made with ❤️ using Streamlit · © 2026

    </div>
    """,
    unsafe_allow_html=True
)
