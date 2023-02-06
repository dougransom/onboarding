PS C:\Users\doug\code\onboarding> pdftk .\o1.pdf dump_data_fields           ---

# Installation

1. Install pdftk from [pdf labs](https://www.pdflabs.com/).  This is a program
that can, among other things, fill PDF forms.
1.  Put the onboarding_fill.exe program in a folder, and put it in  your path.  You can use the same folder as where you are instructed to place o1.pdf below.  something like `c:\Users\yourname\ob`  
1.  Anywhere you like in your file system, create a folder for your three Optimize client onboarding files. Download the PDFs from Optimize.    Rename them o1.pdf, o2.pdf, and o3.pdf (keep the same number as the original name).  This is required to make the tool work.  
1.  Create a windows environment variable 'OPTIMIZE_ONBOARDING_TEMPLATE_DIR' with the path to the folder where o1.pdf, o2.pdf, and o3.pdf are.
1.  Open a powershell or terminal in the folder you want to create the client onboarding files ready to sign.
1.  Run the new_onboarding_docs program like this:
`new_onboarding_docs`.   This will pop up a form for your to edit the information, and all three PDFs will populated with the info.  Open each one up to make sure they are correct.  



# Developer Instructions
1. Checkout the source from github.
2. install locally, which gets required python tools.
`pip install -e .[dev]`/   
This will also produce a script for testing in Scripts, but this is not the script to distribute.
3.  Build the distributed program.
`pyinstaller .\optimize_onboarding\onboarding_fill.py`.
The distributable exe will be `dist/onboarding_fill/onboarding_fill.exe`

