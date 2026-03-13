# UMES_Tech_031326
This repository serves as the storage for the UMES team's tech solution. 
VeridAI – AI Product Visibility & Trust Monitoring Platform

**What Our Application Does**

VeridAI is a platform designed to help companies understand how their products appear in AI-powered shopping recommendations. As more consumers ask AI assistants questions like “What are the best laptops under $500?”, businesses risk losing visibility if their products are not mentioned or are described incorrectly. 
Our application solves this problem by monitoring AI responses and providing companies with analytics and recommendations to improve their product visibility, accuracy, and customer trust.

**The platform contains two main components:**

Consumer Interface (Testing Environment)

This portion simulates real customer behavior.
Consumers can search for products the same way they would interact with an AI assistant.

The system then:

Analyzes the search query
Generates AI responses
Tracks which companies and products appear in the results
Detects missing products or inaccurate information
This serves as a testing environment to simulate real-world AI shopping queries.

Company Dashboard (Analytics & Insights)

Companies submit information about their products and brand.

The system then provides analytics reports based on consumer searches, including:

Product visibility in AI responses
Product ranking in recommendations
Consumer search trends
Product engagement signals
Profit/loss opportunity insights
Market demand trends
Detection of AI hallucinations or incorrect product facts
Based on this analysis, VeridAI suggests actionable solutions to help companies:

Improve product visibility in AI answers
Optimize product descriptions and metadata
Correct misinformation about their products
Increase engagement and customer trust
Our primary target users are minority business owners and underserved companies that often struggle to gain visibility in AI-driven marketplaces.



**2. Technologies & Frameworks Used**

Our solution integrates AI, analytics, and web technologies to monitor and improve AI product discovery.

**Main technologies include:**

**Frontend****
HTML / CSS
JavaScript
UI wireframes for consumer search and company dashboards

**Backend
**
Python
API-based architecture

**AI / Machine Learning**
Natural Language Processing (NLP) to analyze consumer queries
AI response analysis to track product mentions
Machine learning models to detect hallucinations and incorrect product data
Data Processing

Product database
Search query analytics
Trend analysis models
Infrastructure

Cloud-based processing environment
Automated scripts for running the application


**3. How Judges Should Navigate the Application**

To understand the system, judges should explore the two main sections:

**Step 1 – Consumer Interface**
Open the Consumer Search Page
Enter a product-related question
Example:
“Best budgeting software for small businesses”
The system will:

Generate AI-style responses
Identify which companies/products appear
Log the search for analytics
Step 2 – Company Dashboard

Navigate to the Company Portal
Enter company or product information
View generated analytics reports
Reports will show:

Product visibility scores
Search queries that trigger product mentions
Trends in consumer demand
Hallucination detection alerts
Suggested improvements to increase visibility


4. How to Run the Application

We provide a script to automatically start the system.

Run the following command in the project directory:



./run.sh



This script will:

Install dependencies
Start the backend server
Launch the web interface
Initialize the analytics engine


5. Example Startup Output

If the application starts successfully, the terminal should display something similar to:



./run.sh

Initializing VeridAI Platform...



Starting Backend Server...

Server running on http://localhost:5000



Loading AI Query Monitoring Engine...

Connected to Product Database



Launching Consumer Interface...

Launching Company Dashboard...



System Status: RUNNING

VeridAI ready to monitor AI product visibility.



You can verify the system is running by opening:



http://localhost:5000





6. How to Verify the System Works

After launching the app:

Open the Consumer Search Interface
Enter a sample query such as:


What are the best accounting tools for small businesses?



The system will return:

AI-generated recommendations
Logged product visibility data
Then open the Company Dashboard to see:

Visibility analytics
Product exposure metrics
Suggested optimization strategies


7. Ethical AI Monitoring

A core feature of VeridAI is AI trust and accuracy monitoring.

The system automatically detects:

Hallucinated product features
Incorrect pricing
Outdated availability
Misleading product comparisons
When issues are found, the platform alerts companies and recommends content updates or corrections to improve AI accuracy and consumer trust.



8. Business Impact

VeridAI helps companies:

Increase product visibility in AI assistants
Detect and correct AI misinformation
Understand consumer demand trends
Improve engagement and conversions
Our mission is to empower minority business owners with the insights needed to compete in AI-driven marketplaces.
