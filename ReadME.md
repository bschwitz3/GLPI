# GLPI Scripts

This repository contains scripts for automating GLPI tasks.

## Requirements

1. Check if you have Python installed by running `python --version` or `python3 --version`.

   If not, download and install Python from the official website: <https://www.python.org/downloads/>.

2. Check if you have pip installed by running `pip --version` or `pip3 --version`.

   If not, follow the official instructions to install pip: <https://pip.pypa.io/en/stable/installing/>.

## Configuration

1. Clone the Git repository by running:
    ```powershell
    git clone https://github.com/bschwitz3/GLPI.git GLPI_Scripts
    ```

2. Navigate to the project directory and install the dependencies by running:
   ```powershell
   cd GLPI_Scripts
   pip install -r requirements.txt
   ```
3. Environment Variables

   Create a copy of the `.env.exemple` file and fill the `.env` file with your personnal informations:
   ```powershell
   cp .env.exemple .env
   ```

4. Custom Scripts
   
   - To customize the scripts, open them and modify the dates, paths, and file names as desired where indicated.

5. Power BI and Task Scheduler

   - Customize Power BI to update data from your file

   - Set up automatic tasks in Task Scheduler and specify the Python executable and your script path.