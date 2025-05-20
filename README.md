# Fake-Social-Media-Profile-Detection-and-Reporting-Using-Machine-Learning-and-Blockchain
Introduction​:
Fake social media profiles have become a significant threat, leading to misinformation, fraud, and security risks. Traditional detection methods, such as manual reporting and rule-based systems, often fail to accurately identify fraudulent accounts.​
This project aims to detect and report fake social media profiles using a combination of Machine Learning (ML) and Blockchain technology. ​
Machine learning models such as Random Forest, Support Vector Machines (SVM), Artificial Neural Networks (ANN) and XGBoost analyze profile features (e.g., follower count, bio length, profile picture) to classify accounts as real or fake.​
Blockchain ensures secure, immutable storage of detected fake profiles and user reports, preventing data manipulation and enhancing transparency. By integrating ML for detection and blockchain for security, this project provides an efficient, automated, and trustworthy solution for combating fake profiles on social media platforms.​
Problem Statement: Fake social media profiles contribute to misinformation, fraud, and security risks.​
Project Objective: To detect and report fake social media profiles using Machine Learning (ML) and Blockchain technology.​
Machine Learning Approach: Models such as Random Forest, Support Vector Machines (SVM), and Artificial Neural Networks (ANN) and XGBoost analyze profile features (e.g., follower count, bio length, isPrivate and has Profile photo) to classify accounts as real or fake.​
Blockchain for Security: Ensures secure, immutable storage of detected fake profiles and user reports, preventing data manipulation and enhancing transparency.​
Outcome: Provides an efficient, automated, and trustworthy solution for combating fake profiles on social media platforms.​

Literature Review​:
Fake Profile and Bot Detection:​
Research in the field has focused on detecting fake social media profiles and bots using machine learning techniques. Studies have shown that features derived from user behavior, textual content, and network structure are highly effective for classification.​
Random Forest & SVM in Social Media Analysis:​
Several studies have compared ensemble methods (such as RF) and kernel-based methods (such as SVM) for detecting anomalies in social media data. Both have demonstrated high accuracy and robustness in experimental settings.​
Blockchain for Data Integrity:​
Recent work explores the integration of blockchain with machine learning to ensure the integrity and trustworthiness of data. Blockchain provides a decentralized mechanism to record and verify detection outcomes.​

Existing method Drawback​:
Lack of Scalability: Manual reporting cannot efficiently handle the vast number of fake profiles on large social media platforms.​
Data Manipulation Risks: Centralized storage of fake profile reports can be altered or removed, reducing credibility.​
Slow Detection Process: Traditional methods rely on user reporting, making fake profile detection reactive rather than proactive.​
Limited Adaptability: Rule-based detection struggles to keep up with evolving tactics used by fake accounts.​
Lack of Transparency: Users have no way to verify reported fake profiles, leading to distrust in detection mechanisms.​
No Secure Audit Trail: Without blockchain, there is no immutable record of reported fake profiles, making tracking difficult.​

Proposed Method​:
This project proposes a hybrid approach that integrates machine learning models with blockchain technology to improve the detection and verification of fake social media profiles.​
Key Components of the Proposed System:​
Machine Learning-Based Fake Profile Detection​
Three machine learning models (Random Forest, SVM, XGBoost, and ANN) are used to classify profiles as real or fake based on extracted features. ​
Features such as follower count, following count, bio length, profile photo presence, and privacy status are used for classification.​
A dataset with labeled fake and real profiles is used to train the models.​
Blockchain Integration for Security and Transparency​
Ethereum blockchain is used to store flagged fake profiles in an immutable ledger.​
Smart contracts automate the verification and reporting of fraudulent accounts.​
InterPlanetary File System (IPFS) is used for decentralized storage of reported profiles.​
User Interface for Profile Verification​
A Django-based web application allows users to input profile data and receive real-time predictions.​
A fraudulent profile reporting system enables users to report suspicious accounts, with all reports being securely stored on the blockchain.​

Technologies Used:​
Frontend Technologies:​
HTML & CSS: Structure and design of the web interface.​
JavaScript: Enhances interactivity and handles dynamic updates.​
Backend Technologies:​
Django (Python Web Framework): Handles user interactions, machine learning model integration, and blockchain transactions.​
Python: Used for backend logic, machine learning model execution, and blockchain communication.​
Machine Learning Technologies:​
scikit-learn: Implements classification algorithms such as Random Forest, Support Vector Machine (SVM), and Artificial Neural Networks (ANN) for detecting fake profiles.​
pandas & numpy: Process and structure user data for model prediction.​
pickle: Saves and loads trained models for efficient execution.​
Blockchain Technologies:​
Ethereum Blockchain: Stores immutable records of detected fake profiles and user reports.​
Smart Contracts: Automates verification and reporting mechanisms, ensuring transparency and preventing data manipulation.​
IPFS (InterPlanetary File System): Decentralized storage for profile reports, preventing unauthorized alterations.​
Machine Learning Models:​
Random Forest (RF): An ensemble learning method based on decision trees that effectively handles large datasets and captures non-linear relationships.​
Support Vector Machine (SVM): A supervised classification algorithm that identifies fake profiles based on feature analysis.​
Artificial Neural Network (ANN): A deep learning model that captures complex patterns in user profiles, improving detection accuracy over time.
​
Conclusion​:
Enhanced Detection Accuracy: Machine learning models effectively classify fake profiles with high precision.​
Improved Security & Transparency: Blockchain ensures immutable storage and prevents tampering of reported fake profiles.​
Automation & Efficiency: The integration of ML reduces human intervention, making the detection process faster and more reliable.​
Scalability: The system can handle large amounts of social media data, making it suitable for real-world applications.​
Reduction in Fraud & Misinformation: By detecting fake profiles accurately, the system helps improve the integrity of social media platforms.​
Future Scope: The project can be expanded with deep learning models and real-time detection capabilities for even better accuracy and performance.​
