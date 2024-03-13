## Requirements

1. Check if you have python `python --version`
To install python :  https://www.python.org/downloads/

2. Check if you have pip `pip --version`
To install pip : https://pip.pypa.io/en/stable/installing/

## Configuration

1. Clone the repo :
`git clone https://github.com/bschwitz3/GLPI.git GLPI_Scripts`

2. In the repo, install depedencies
`cd GLPI_Scripts`
`pip install -r requirements.txt`

3. Environement Variables
- copy .env.exemple file and fill the .env file it with your data
`cp .env.exemple .env`

4. Custom scripts
- To custom scripts, open them and modify dates, path and file name like you want where it is indicate.

5. Power BI and Task Scheduler
- Custom Power BI to update data from your file.
- Set automatic tasks in Task Scheduler and specify python executable and your script path.

