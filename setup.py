import setuptools

with open('README.md', 'r', encoding='utf8') as f:
    long_description = f.read()


REPO_NAME  = 'CreditWatchdog'
AUTHER_USER_NAME = 'codedestructed007'
SRC_REPO = 'mlproject'
AUTHER_EMAIL = 'codexistslonglastingnotfog@gmail.com'

setuptools.setup(
    name=SRC_REPO,
    author=AUTHER_USER_NAME,
    license='MIT',
    classifiers=[
    
    'Development Status :: 5 - Production/Stable',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',

    # Pick your license as you wish (should match "license" above)
    'License :: OSI Approved :: MIT License'

],
    project_urls={
    'Similar Project(On architecture)': 'https://github.com/codedestructed007/Wine_Quality_prediction',
   
},
    author_email=AUTHER_USER_NAME,
    description= "A small python package for machine learning app",
    long_description=long_description,
    url=f"https://github.com/{AUTHER_USER_NAME}/{REPO_NAME}",
    packages = setuptools.find_packages(where='src'),

)

found_packages = setuptools.find_packages(where='src')
print("Found packages:")
for package in found_packages:
    print(package)
