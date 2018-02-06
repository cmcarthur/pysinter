A Python 3.6 wrapper for Sinter's (https://www.sinterdata.com) API.

[![Maintainability](https://api.codeclimate.com/v1/badges/2fac6cc94e46af1edf60/maintainability)](https://codeclimate.com/github/rsmichaeldunn/pysinter/maintainability)

# Usage
```python
from pysinter import Sinter

sinter = Sinter({{account_id}}, {{api_token}})

projects = sinter.list_projects()

response = sinter.trigger_job_run({{project_id}}, {{job_id}}