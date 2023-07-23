# Token extracter for r/Place2023

# Make sure to install the requirements from `requirements.txt`
- also have the latest version of python installed!
```
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
irm get.scoop.sh | iex
scoop install git python wget unzip
git clone https://github.com/r-Bangladesh/token-extracter-r-place.git
cd token-extracter-r-place
pip install -r ./requirement.txt
wget https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/115.0.5790.102/win64/chrome-win64.zip
unzip ./chrome-win64.zip
```
to get this bot with all dependencies

and to run it 
```
python -u ./main.py
```
