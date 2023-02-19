# build_files.sh
MYDIR="$(dirname "$(realpath "$0")")"
pip install -r MYDIR+requirements.txt
python3.9 manage.py collectstatic