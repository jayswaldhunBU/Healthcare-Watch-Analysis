# Working from the Home Environment & Well-Being Study Data
## About the Project
## 1. Project Summary
Researchers used the ecological momentary assessment approach to conduct a 6-month study to assess the physical, cognitive, and mental effects of a remote work environment, on workers’  well-being. Seventy participants were recruited for the study. Participants were given a Garmin watch to wear which “pinged” them three times a day to share information such as their current location, musculoskeletal discomfort, and  number of breaks. On Fridays, participants completed the E-Work and the Flourishing scale surveys. The computer workstation survey was completed once a month on Wednesday. Three months of data have been collected and researchers want to understand what insights can be gleaned so far as a benchmark to compare to six months of data.

## 2. About the team
Team-1 composed of-
* Vani Singhal
* Jessica Woo
* Ming-Han Hsieh
* Wei-Tse Kao

## 3. Work Done 
* Our data consists of mainly **Garmin data** for 3 and 6 months and **Survey data** (E-Work Life Scale, Flourishing Scale, Daily Breaks, Comfort Visual Analog Scale, Location, Computer Workstation Checklist). 
* We first looked at answering 5 hypothesis given by the client. For answering the hypothesis we first preprocessed the required data. We removed the NAN and 0 values. For correlation hypothesis we used pearson correlation to answer. 
* We also looked at Stress data and compared the data of 3 months and 6 months.
* Next important step was to clean the garmin data for 3 months as well as 6 months. For data types like calories, steps, floorsClimbed and intensity in Minutes we took the last value(max value) for each date as it has a increasing trend. For data type hr we replaced 0 values with resting heart rate(random number btw 60-100). For stress data we averaged the value for each day.

## 4. Repository Navigation
Here is the list of files and folders in the repository along with a brief description of what each file or folder contains:
### 1. Deliverables
  *  Deliverable 0 - Contains our 1 Weekly Scrum Report
  *  Deliverable 1 - Contains report answering 3 hypothesis (a,b,c) and analysis related to stress and Weekly Scrum Report
  *  Deliverable 2 - Contains report answering all Hypothesis (a,b,c,d,e) and recording of our early insights presentation and Weekly Scrum Report
  *  Checkpoint A -  Contains early insights presentation and Weekly Scrum Report
  *  Checkpoint B - Contains First Draft of final report and Weekly Scrum Report 
  *  Deliverable 3 - Contains Contains Second Draft of final report and Weekly Scrum Report
  *  Deliverable 4 - Contains Contains Third Draft of final report, Final presentation and link of recording of our final presentation.
  *  Final Project - Contains Final Report
### 2. Notebooks 
   - **Garmin Data Cleaning** 
      *  garmin_preprocessing.ipynb and updating_files.ipynb  - These jupyter notebooks focuses on cleaning garmin data for 3 and 6 months
   - **Hypothesis Testing**  
      *  hypothesisA.ipynb - This jupyter notebook answers Hypothesis A
      *  Team1_hypothesisB.ipynb - This jupyter notebook answers Hypothesis B
      *  Hypothesis_c.ipynb - This jupyter notebook answers Hypothesis C
      *  Team1_hypothesis_d.ipynb - This jupyter notebook answers Hypothesis D
      *  Team1_hypothesis_e.ipynb - This jupyter notebook answers Hypothesis E
      *  pressure_test_3.ipynb - This jupyter notebook focuses on analysing data for 3 months
      *  pressure_test_6.ipynb - This jupyter notebook focuses on analysing data for 6 months
   - **Garmin Data Initial Analysis**
      *  garmin_merge.ipynb - This jupyter notebook focuses on finding relationship between survey and garmin data
      *  garmin_correlationMatrix.ipynb - This jupyter notebook focuses on generating a correlation matrix for the 3 month data and the 6 month data to   look for potential relationships between the Garmin data types, which are calories, floorsClimbed, heart rate (hr), intensityMinutes, steps, and stress.
      *  garmin_homunculus.ipynb - This jupyter notebook focuses on intial analysis of homunculus pain along with garmin data
      *  garmin_Ananlysis_6_month.ipynb - This jupyter notebook focuses on intial analysis of flourishing scale along with garmin data
   - **Garmin Data Relationships**
      *  garmin_homunculus.ipynb - This jupyter notebook focuses on final analysis of homunculus pain along with garmin data
      *  GarminData_and_Flourishing_scale.ipynb - This jupyter notebook focuses on final analysis of flourishing scale along with garmin data
      *  GarminData_and_Computer_Workstation_Checklist.ipynb - This jupyter notebook focuses on final analysis of computer workstation checklist along with garmin data
      *  E Worklife scale.ipynb - This jupyter notebook focuses on final analysis of E- worklife scale survey along with garmin data

### 3. Cleaned Garmin data
  * A document having link to cleaned garmin data



