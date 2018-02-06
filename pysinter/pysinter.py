import requests
import json


class Sinter(object):
	"""
	Class for interacting with the Sinter API

	* :py:meth:`list_projects` - lists all projects under the account specified when instantiating the Sinter object
	* :py:meth:`get_project' - returns details of a single project id
	* :py:meth:`list_job_definitions` - lists all job definitions for the specified project id
	* :py:meth:`get_job_definition` - (not implemented) returns details of a single job definition
	* :py:meth:`list_job_runs` - (not implemented) lists all job runs for the specified job id
	* :py:meth:`get_job_run` - (not implemented) returns details of a single job run
	* :py:meth:`trigger_job_run` - triggers an execution of a job definition
	"""

	def __init__(self, account_id, api_token):
		self.account_id = account_id
		self.api_token = api_token
		self.api_base = 'https://app.sinterdata.com/api/v1'

	def _build_request(self, url_suffix):
		return {
			"url": self.api_base + url_suffix,
			"headers": {
					"Authorization": "Token %s" % self.api_token
				}
			}
	@staticmethod
	def _validated_response(response, expected_status_codes):
		if response.status_code not in expected_status_codes:
			raise RuntimeError(response.content)
		return json.loads(response.content)

	def _get(self, url_suffix):
		return self._validated_response(requests.get(**self._build_request(url_suffix)), [200])

	def _post(self, url_suffix):
		return self._validated_response(requests.post(**self._build_request(url_suffix)), [201])

	def list_projects(self):
		return self._get('/accounts/%s/projects/' % self.account_id)['data']

	def get_project(self, project_id):
		return self._get('/accounts/%s/projects/%s/' % (self.account_id, project_id))['data']

	def list_job_definitions(self, project_id):
		return self._get('/accounts/%s/projects/%s/definitions/' % (self.account_id, project_id))

	def get_job_definition(self, project_id, job_id):
		raise NotImplementedError
		# return self._get('/accounts/%s/projects/%s/definitions/%s/' % (self.account_id, project_id, job_id))

	def list_job_runs(self, project_id, job_id):
		raise NotImplementedError
		# return self._get('/accounts/%s/projects/%s/definitions/%s/runs/' % (self.account_id, project_id, job_id))

	def get_job_run(self, project_id, job_id, job_run_id):
		raise NotImplementedError
		# return self._get('/accounts/%s/projects/%s/definitions/%s/runs/%s/' % (self.account_id, project_id, job_id, job_run_id))

	def trigger_job_run(self, project_id, job_id):
		return self._post('/accounts/%s/projects/%s/definitions/%s/runs/' % (self.account_id, project_id, job_id))