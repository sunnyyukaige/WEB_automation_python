# WEB_automation_python
Automation framework of web page(light framework)with BDD
# jmeter installation
###install JDK environment
###download jmeter latest version 
###install tool management and install useful plugin

#soapUI installation 
###download latest version 

#UI automation install
###install python https://www.python.org/downloads/release/python-351/
###set system environment path add PATH=install folder(check with python --version)
###install pip
###pip install *selenium python -m pip install selenium*
###pip install browser driver 
 -------------------------------华丽分界线------------------------------------------------------  
**Base**
   - action
   - elements
   - utility
   - config
   - wait
   - assert
   
**Page**
   - BasePage.js (add some hook and define some comment method and property for all other funciton page)
   - LoginPage.js (will be many page like this provide for test cases using)  
 
**TestCases**
   - BaseCase.js (define some hook method and commen method used by multiple test cases)
   - LoginCase.js (one login case as exp)
