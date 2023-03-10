# Introduction

onboarding_fill.exe is a user interface that prepares the three Optimize onboarding files.  You only have to enter the information once in 
the GUI (mainly client names), and all three onboarding agreement files are placed in the current folder.

You do have to copy and rename the three onboarding files from Optimize as described below, and you can enter the default financial planner and portfolio manager names in one of them.


# Installation

1. Install pdftk from [pdf labs](https://www.pdflabs.com/).  This is a program
that can, among other things, fill PDF forms.
1.  Put the onboarding_fill.exe program in a folder, and [put it in  your path](https://www.c-sharpcorner.com/article/how-to-addedit-path-environment-variable-in-windows-11/).  You can use the same folder as where you are instructed to place o1.pdf below.  something like `c:\Users\yourname\ob`  
1.  Anywhere you like in your file system, create a folder for your three Optimize client onboarding files. Download the PDFs from Optimize.    Rename them o1.pdf, o2.pdf, and o3.pdf (keep the same number as the original name).  This is required to make the tool work.  
1.  Create a windows environment variable 'OPTIMIZE_ONBOARDING_TEMPLATE_DIR' with the path to the folder where o1.pdf, o2.pdf, and o3.pdf are.
1.  Open o2.pdf in your PDF program and set any defaults for the fields.  You normally would set "Optimize Relationship Manager" and "Licensed Portfolio Manger/Optimize Representative Name".  Save.  This will be used by this new_onboarding_docs to prepopulate all 3 forms. 
1.  Open a  terminal in the folder (use the file explore context menu) you want to create the client onboarding files ready to sign.
1.  Run the new_onboarding_docs program like this:
`new_onboarding_docs`.   This will pop up a form for your to edit the information (the information you saved in o2.pdf should appear in the form), and all three PDFs will populated with the info.  Open each one up to make sure they are correct.  



# Developer Instructions
1. Checkout the source from github.
2. install locally, which gets required python tools.
`pip install -e .[dev]`/   
This will also produce a script for testing in Scripts, but this is not the script to distribute.
3.  Build the distributed program.
`pyinstaller .\optimize_onboarding\onboarding_fill.py`.
The distributable exe will be `dist/onboarding_fill/onboarding_fill.exe`

