# Potabl. - Water Quality Analysis Tool
---
Access to clean and safe drinking water is a fundamental requirement for human health and well-being. However, contamination from industrial discharge, agricultural runoff, and aging infrastructure continues to threaten water quality in both rural and urban areas. Traditional laboratory-based testing methods, though accurate, are often time-consuming, expensive, and inaccessible to communities with limited resources.

This project introduces a Water Quality Analysis Tool—a digital platform designed to evaluate drinking water quality quickly, accurately, and in a user-friendly manner. The system enables users to input measured water parameters such as pH, turbidity, total dissolved solids (TDS), hardness, chloride content, fluoride levels, and microbial indicators, among others. These inputs are compared against the permissible limits defined by the World Health Organization (WHO) and the Bureau of Indian Standards (BIS). The tool then classifies water as Safe, Marginal, or Unsafe for drinking, providing parameter-specific alerts and recommendations for corrective measures.

Developed using Streamlit for an interactive and responsive web interface, the tool supports bilingual operation (English and Tamil) to ensure accessibility for diverse user groups. Its backend logic is powered by a rule-based evaluation engine, allowing for easy scalability and integration of additional parameters in the future. The solution is designed to work on desktops and mobile devices, making it usable by field workers, local authorities, NGOs, and community members.

By combining scientific standards with an intuitive design, the Water Quality Analysis Tool bridges the gap between laboratory precision and on-site usability. It has the potential to improve public awareness, support timely interventions, and contribute to long-term water safety monitoring strategies. Future enhancements could include sensor integration for real-time data collection, automated reporting to authorities, and AI-based anomaly detection to predict contamination trends.

Tools and Technology
---
- Python - Backend logic and parameter evalutaion
- Streamlit - For interactive and user-friendly interface
- Pandas - CSV exporting and handling 
- JSON - Language translation operations

References
---
1.	World Health Organization (WHO) – Guidelines for drinking-water quality: fourth edition incorporating the first and second addenda. World Health Organization, Geneva, 2022. https://www.who.int/publications/i/item/9789240045064
2.	Bureau of Indian Standards (BIS) – IS 10500: 2012 – Drinking Water Specification. Bureau of Indian Standards, New Delhi, 2012. https://cpcb.nic.in/wqm/BIS_Drinking_Water_Specification.pdf
3.	Streamlit Documentation – Streamlit: The fastest way to build data apps in Python. https://docs.streamlit.io/
4.	Pandas Documentation – Python Data Analysis Library. https://pandas.pydata.org/docs/
5.	Python Software Foundation – Python Programming Language. https://www.python.org/


This project was done under 1M1B - Green Internship Batch-4