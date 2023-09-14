# Streamlit Tutorial
## Live Site Example
https://lnmpredictor.streamlit.app/
## Essential Files
These three files are essential to to deploy:
<ol>
  <li> Model File -- Typically a ".sav" file, can use more than one, just make sure to modify the main python script. </li>
  <li> requirements.txt -- Make sure this is lowercase and spelled correctly, it specifies dependencies and their versions needed by the app and model.</li>
  <li> streamlit_app.py -- Streamlit needs a Python script to run, it doesn't have to be this name, but the file name has to match the name entered when creating app on the share.streamlit.io webpage. </li>
</ol>

## Minimum Steps to Deployment
<ol>
  <li> Fork this repo.</li>
  <li> Add model to repo (.sav file) and make sure that its name matches in the streamlit-app.py file. </li>
  <li> Update the streamlit input components in the streamlit-app.py file. </li>
  <li> Go to https://share.streamlit.io/ and grant streamlit github authorization permission. </li> 
</ol>

<details> 
<summary> Important Note About Granting Streamlit Github Authorization Permissions </summary>
This will give streamlit permission to view ALL files in ALL repos that your account and any organization your account is connected to. If you don't want to have that happen and still want to use streamlit, then I'd recommend forking the project from the second account and then adding your primary account as a collaborator.
</details>

<ol start="5">
  <li> Once authorized, the webpage displays your apps. Create a new app using the updated forked repo. </li>
  <li> Streamlit servers will build the app using the environment details listed in the requirements.txt file. </li>
</ol>

## Benefits of Streamlit
<ol>
  <li> Fast easy setup. </li>
  <li> Free unlimited web hosting. </li>
  <li> Only need one language -- Python. </li>
  <li> Model is loaded directly onto user's computer so potentially confidential form data is not sent over internet/stored anywhere. </li>
  <li> Link permissions are modifiable - can change whether model is publicly accesible or if authentication is needed.  </li>
</ol>

## Troubleshooting Tips
<ol>
  <li>Make sure requirements.txt is spelled correctly and not in a subfolder. </li>
  <li>Scikit-Learn has In streamlit_app.py import sklearn, but in requirements.txt use scikit-learn. </li>
  <li>If there still are errors, inspect the console on the live link, find the specific error message, copy it and put it surrounded by quotes in a search engine and hopefully there will be forumn posts that can help you resolve the issue. For Example: "ValueError: node array from the pickle has an incompatible dtype" lead us to reading that the scikit-learn version needed to be fixed in requirments.txt from this blog post: https://discuss.streamlit.io/t/valueerror-node-array-from-the-pickle-has-an-incompatible-dtype/46682</li>
</ol>
