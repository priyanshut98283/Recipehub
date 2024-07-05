# Use a specific Python version if needed
PYTHON=$(which python3)
PIP=$(which pip3)

# Install Python dependencies
$PIP install -r requirements.txt

# Collect static files
$PYTHON manage.py collectstatic --noinput