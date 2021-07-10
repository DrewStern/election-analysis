# Found at: https://python-poetry.org/docs/#windows-powershell-install-instructions
#The installer installs the poetry tool to Poetry’s bin directory. On Unix it is located at $HOME/.poetry/bin and on Windows at %USERPROFILE%\.poetry\bin.
#This directory will be automatically added to your $PATH environment variable, by appending a statement to your $HOME/.profile configuration (or equivalent files).
#If you do not feel comfortable with this, please pass the --no-modify-path flag to the installer and manually add the Poetry’s bin directory to your path.
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -