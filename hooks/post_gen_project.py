import subprocess


project_slug = "{{ cookiecutter.project_slug }}"

MESSAGE_COLOR = "\x1b[35m"
RESET_ALL = "\x1b[0m"

print(f"{MESSAGE_COLOR}Almost done!")

print(f"{MESSAGE_COLOR}Installing environment...{RESET_ALL}")
subprocess.call(['mamba', 'env', 'create','--file','environment.yml'])
subprocess.call(['mamba', 'activate', project_slug])
subprocess.call(['mamba', 'list'])

print(f"{MESSAGE_COLOR}Initializing a git repository...{RESET_ALL}")

subprocess.call(["git","init"])
subprocess.call(["git","add","*"])
subprocess.call(["git","commit","-m","Initial commit"])
#The call function from the subprocess library inputs in the terminal the strings within the parenthesis.

print(f"{MESSAGE_COLOR}The beginning of your destiny is defined now! Create and have fun")

