import os


dirs=[
     "data_given",
     os.path.join("data", "raw") ,
     os.path.join("data", "processed"),
     "report",
     "notebook",
     "saved_models",
     "src"
     ]

for dir in dirs:
    os.makedirs(dir,exist_ok=True)
    with open(os.path.join(dir,".gitkeep"),"w") as f:
        pass
    
files=[
      "dvc.yaml",
      "params.yaml",
      ".gitignore",
      os.path.join("src","__init__.py")
      ]

for file in files:
    if not (os.path.exists(file)):        
        with open(file,"w") as f:
            pass
    else:
        print(f"{file} is present")