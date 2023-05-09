# Big-data-project

This project aims to enhance the capabilities of dataset search engines by enabling users to query the contents of datasets they discover. The project proposes to develop an infrastructure that supports queries over datasets stored in a file system or scalable object storage backends Minio.

The project involves modifying Auctus’ codebase to convert datasets to Parquet files, storing them in an open-source object store, and modifying the user interface to allow users to execute SQL queries over the Parquet files stored in the S3 object store using the DuckDB Python wrapper.

To execute script please follow instructions:

step1:
```
git clone https://gitlab.com/ViDA-NYU/auctus/auctus.git
```
Follow the setup instrutions in the repository to setup the environment and data volumes in your local system

## Note:
 * We will use MinIO docker container from this repository. 

 * if follwed correctly docker should be up and start running in the backend.
          

step2:
clone the repository in to your local system
```
https://github.com/Shvejan/big-data-project.git
```
step3:
create a virtual environment with python3.9

```
python -m venv myenv
```

activate the environment you just created 

```
myenv\Scripts\activate.bat
```
Install the requirements using the following instructions.

```
pip install -r requirements.txt
```

step3:
Install the node 16 (https://nodejs.org/en/download)
 After installation move to frontend folder
```
cd frontend
```

Execute the following node command:
```
npm i
```
step4:
Change directory to backend
and run the app.py file:
```
python app.py
```

step5:
Change directory to frontend and execute the following instruction:

```
npm start
```

You should now see the Front end running at https://localhost:3000 and backend at https://localhost:8000
Now continue to the Front end URL run your queries.


