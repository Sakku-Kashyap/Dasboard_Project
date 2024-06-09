import streamlit as st


col1,col2,col3=st.columns(3)
with col1:
    st.write("""Hi Everyone:wave:""")
    st.subheader("""I am Saket Kumar, a Data Analyst
    """
    )
    st.write("""I am working for NTT DATA and its been 4.8 years now.
    """)

with col2:
    st.write('')
with col3:
    st.image('saket.jpg')

st.write('___')
st.subheader('Objective')
st.write("""
         I’m eager to harness my proficiency in analytics, data science, computing, and development to enrich and refine my
         knowledge within a stimulating and challenging professional arena. My objective is to contribute meaningfully to
         projects while also cultivating a motivating work environment. By leveraging my skills, I’m drawn to environments
         that encourage growth and innovation, where I can apply my talents to tackle complex problems and drive impactful
          outcomes.""")

st.write('___')
st.markdown("""
### Education
- BabaSaheb BhimRao Ambedkar University Lucknow
Bachelor of Technology - Computer Science, Grade: A+ Aug 2014 - June 2018
- Delhi Jain Public School Palam,New delhi
HSC (PCM): A+ Mar 2013 - Nov 2014

""")
st.write('___')
st.markdown("""
### Skills
- **Technical Skills**: SQL, Python, server and SFTP/FTP management, HEAT tool for patch management.

- **Libraries**:  Pandas, Numpy, Matplotlib, Seaborn,Streamlit.
- **Data Tools**:  Power-BI Jira, Jupyter, Advance Excel, Tableau, MySQL/SQL Server, ServiceNow
- **Scheduling Tools**:  Control-M (Scheduling/Monitoring), Ivanti HEAT Patching ) ,CA 7, ActiveBatch
- **Core Concepts**:  Advanced Data Analytics, DSA, Statistics.
- **Business Analysis**:  Documentation of business requirements, process flow diagrams, incident logs.
- **Client Support**:  Production/UAT support, issue resolution, automated reporting 
- **Security Management**:  Patch installation, server security, vulnerability prevention.
- **Soft Skills**:  Strong Communication, Analytical, Decision making Problem-solving skills
""")
st.write('---')
st.markdown("""
### Hobies
- Engaging myself in social activities like working for mankind and to work for people.
- Working as an active volunteer for RobinHood Army,Bhumi and Zariaa few NGO’s.
- Playing cricket and running keeps me engage and physically fit.
""")

