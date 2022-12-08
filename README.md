# Ayah Picker

This script has two functionalities.

### 1) Random Ayah Generation
The script looks through a database of surahs in the quran and picks a surah, then chooses a random ayah from said surah, and then opens the ayah in the default web browser. 

The user submits how many random ayahs they would like the script to open in the web browser.

### 2) Ayah Printing
The script takes an input of desired surah number and desired ayah number(s) and outputs a formatted message ready to be sent as MES Ayah of the Day.  

## Usage
Run the following prompt:
```
ayahpicker
```
The arguments are as follows:
- ```-r``` or ```--random``` enables the random ayah generation feature
- ```-p``` or ```--printer``` enables the ayah printing functionality
    - you must include one of the above for the function to run
- ```--surah``` to input desired surah number
- ```--ayah``` to input desired ayah number. Use a single number or (start_ayah)-(end_ayah).
- ```--requests``` to specify how many random ayahs you want the script to open