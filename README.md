# big-data-project

This project aims to enhance the capabilities of dataset search engines by enabling users to query the contents of datasets they discover. The project proposes to develop an infrastructure that supports queries over datasets stored in a file system or scalable object storage backends Minio.

The project involves modifying Auctus’ codebase to convert datasets to Parquet files, storing them in an open-source object store, and modifying the user interface to allow users to execute SQL queries over the Parquet files stored in the S3 object store using the DuckDB Python wrapper.
