# This program cleans and standardizes user names.
# Given list of names
names = [" Alice ", "bob", " CHARLIE "]
# Empty list to store cleaned names
cleaned_names = []
# Clean each name
for name in names:
    cleaned_name = name.strip().lower()  # remove spaces and convert to lowercase
    cleaned_names.append(cleaned_name)
    
# Print cleaned list
print("Original Names:", names)
print("Cleaned Names:", cleaned_names)