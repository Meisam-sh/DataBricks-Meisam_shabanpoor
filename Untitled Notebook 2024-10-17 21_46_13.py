# Databricks notebook source
# MAGIC %md
# MAGIC # we have 4 types of utilities:
# MAGIC ### File system utilities
# MAGIC ### Secrets utilities
# MAGIC ### widget utilities

# COMMAND ----------

# MAGIC %md
# MAGIC ## File System utilities

# COMMAND ----------

# MAGIC %md
# MAGIC ### On this notebook we review some scripts about file system utilities.
# MAGIC - we should remember we can use file system utilities on python , Scala and R, but not in SQL

# COMMAND ----------

# fs refers to file system utility
%fs
ls

# COMMAND ----------

# MAGIC %fs
# MAGIC ls /databricks-datasets

# COMMAND ----------

#if we want to see all utility files  we can use dbutil.fs.ls command.
# here we checked utility files of root folder of databricks
dbutils.fs.ls('/')

# COMMAND ----------

# the directories above contains few datasets that we can use. for example we enter into Covid folder
dbutils.fs.ls('/databricks-datasets/COVID')

# COMMAND ----------

for files in dbutils.fs.ls('/databricks-datasets/COVID'):
    print(files)

# COMMAND ----------

for files in dbutils.fs.ls('/databricks-datasets/COVID'):
    if files.name.endswith('/'):
        print(files.name)

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

dbutils.fs.help('ls')

# COMMAND ----------


