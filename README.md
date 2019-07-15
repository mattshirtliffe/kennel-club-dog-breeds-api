# Install

virtualenv env -p python3.7

source env/bin/activate

pip install -r requirements.txt

# Run

python program.py

export FLASK_APP=program.py

flask run --host=0.0.0.0 --port 5001