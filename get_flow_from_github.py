from prefect import flow,task

@task
def task1():
  return "from task1"

@flow(log_prints=True)
def github_flow():
   result=task1()
   print(result)
