
### Basic Conversion
#   jupyter nbconvert my_notebook.ipynb --to html

### Exclude Input
#   jupyter nbconvert my_notebook.ipynb --to html --TemplateExporter.exclude_input=True

### Exclude Output
#   jupyter nbconvert my_notebook.ipynb --to html --TemplateExporter.exclude_output=True

### Use a Custom Template
#   jupyter nbconvert my_notebook.ipynb --to html --template lab


### Output to Specific File
#   jupyter nbconvert my_notebook.ipynb --to html --output custom_output_name.html


import os, json, time 
import pandas as pd

# Step 1: List all .ipynb files in the current directory
ipynb_files = [f for f in os.listdir('.') if f.endswith('.ipynb')]

# Step 2: Save filenames to a JSON file as array of objects
notebook_data = [{"filename": fname} for fname in ipynb_files]
with open(f'./Cache/notebooks-{str(time.asctime())}.json', 'w') as f:
    json.dump(notebook_data, f, indent=4)

# Step 3 & 4: Convert to HTML and delete .ipynb files
for file in ipynb_files:
    os.system(f'jupyter nbconvert "{file}" --to html')
    os.remove(file)


# Step 1: List all .pdf files in the current directory
pdf_files = [f for f in os.listdir('.') if f.endswith('.pdf')]

# Step 2: Save filenames to a JSON file as array of objects
pdf_data = [{"filename": fname} for fname in pdf_files]

with open(f'./Cache/pdfs-{str(time.asctime())}.json', 'w') as f:
    json.dump(pdf_data, f, indent=4)


# Step 2: delete .pdf files
for file in pdf_files:
    os.remove(file)


# Step 1: Find all .xlsx and .csv files
table_files = [f for f in os.listdir('.') if f.endswith(('.xlsx', '.csv'))]

# Step 2: Save file list to tables.json
table_data = [{"filename": fname} for fname in table_files]

with open(f'./Cache/tables-{str(time.asctime())}.json', 'w') as f:
    json.dump(table_data, f, indent=4)

# Step 3: Convert to .json and delete original files
for file in table_files:
    if file.endswith('.csv'):
        df = pd.read_csv(file)
    elif file.endswith('.xlsx'):
        df = pd.read_excel(file)

    json_filename = file.rsplit('.', 1)[0] + '.json'
    df.to_json(json_filename, orient='records', indent=4)

    os.remove(file)

time.sleep(2.5)
text=str(input("\n\tEnter the git commit words : \n\t"))
os.system("git add .")
os.system(f"git commit -m '{text}'")
os.system("git push origin ui_format")