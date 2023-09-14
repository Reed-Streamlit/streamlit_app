# Streamlit Tutorial
## Minimum to Deployment
<ol>
  <li> Fork this repo</li>
  <li> Add model to repo (.sav file) and make sure that its name matches in the streamlit-app.py file. </li>
  <li> Update the streamlit input components in the streamlit-app.py file. </li>
  <li> Go to https://share.streamlit.io/ and grant streamlit github authorization permission. </li> 
</ol>
<!-- Not sure why the formatting isn't working here -- see https://github.com/orgs/community/discussions/16925 -->
<!-- Also add picture here -->
<details> 
<summary> Important Note </summary>
This will give streamlit permission to view ALL files in ALL repos that your account and any organization your account is connected to. If you don't want to have that happen and still want to use streamlit, then I'd recommend following [these instructions](#setting-up-a-second-account)
</details>


<ol start="5">
  <!-- add pictures here -->
  
  <li> Once authorized, the webpage displays your apps. Create a new app using the updated forked repo. </li>
  <li> Streamlit servers will build the app using the environment details listed in the requirements.txt file </li>
</ol>

## Benefits of Streamlit
<ol>
  <li> Fast easy setup </li>
  <li> Only need one language -- Python </li>
  <li> Model is loaded directly onto user's computer so potentially confidential form data is not sent over internet/stored anywhere. </li>
  <li> Link permissions are modifiable - can change whether model is publicly accesible or if authentication is needed  </li>
  <li> Free web hosting </li>
</ol>

## Getting Started
First thing that you'll need to do is make a github account so that you can fork the repo (essentially making your own separate copy).
Secondly you will want to fork the repo.

## Setting Up A Second Account
Streamlit cloud makes it very easy to create a publicly accessible website, however to do that
it requires you to link your GitHub account, giving it permission to read all public and private repos as well
as repos of any organizations your GitHub is linked to.

So if you would like to avoid that, I would recommend creating another
github account, which you will need another email for.

<details>
<summary>Tip for gmail users</summary>
<br>
Google will ignore text between the + and @ sign, for instance
user@gmail.com and user+all-text-here-is-ignored@gmail.com will both be treated
as user@gmail.com by google but will be treated differently by github, meaning you can
make different acdounts with those email addresses even though emails sent to either will
end up in the same inbox.
</details>


After setting up the second account, you want to fork the repo while logged in as the second account,
making the second account the owner of the repo.
Once that is done, you can add your original github account
as a collaborator, enabling that account to make changes to the repo.
https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-access-to-your-personal-repositories/inviting-collaborators-to-a-personal-repository#

While still logged in as this second account, go to
https://share.streamlit.io/
and give streamlit access to this account.

Then you are free to log off and login to your main account
to accept the collaborator invitation and
start making changes.


## Updating Model and App Files
You technically can just change files via the
web platform on github and then open the share streamlit
website to see your changes, however it can take
some time for streamlit to access the repo via github,
download those files and build it again.

If you would like to be able to see changes more quickly
I would recommend running streamlit locally, though it will take a few steps to setup.

First you will want to setup an ssh key on your computer for github.
Then you'll want to clone the repo onto your computer.
After you will want to ensure that you are able to make changes via the add, commit, push
Then you are set with github, so next we have to set up the python environment

If using a newer computer I believe pip and python default to using
Python3, though if you are using an older computer they default to Python2,
so youll want to use pip3 and python3.

Follow streamlits instructions for setting up a virtual environment

Now you should be able to run streamlit locally!


## Troubleshooting
When first running this test project we ran into some errors
with the sklearn vs scikit-learn package and versions. By copying the error
and searching google with it, (usually in ""s to narrow the search to exact matches)
we found some streamlit forum posts where others ran into the same issue and were able to fix it.

