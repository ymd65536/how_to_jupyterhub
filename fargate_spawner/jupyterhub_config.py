import os
from fargatespawner import FargateSpawner
from fargatespawner import FargateSpawnerECSRoleAuthentication
c.FargateSpawner.authentication_class = FargateSpawnerECSRoleAuthentication
c.FargateSpawner.aws_region = 'us-east-2'
c.FargateSpawner.aws_ecs_host = 'ecs.us-east-2.amazonaws.com'
c.FargateSpawner.notebook_port=8000
c.FargateSpawner.notebook_scheme='http'

c.JupyterHub.spawner_class = FargateSpawner
c.JupyterHub.base_url = '/'
c.JupyterHub.hub_ip = '0.0.0.0'
c.JupyterHub.bind_url = 'http://:8000'

c.Spawner.ip = '0.0.0.0'
# c.Spawner.hub_connect_url='http://0.0.0.0'

c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.open_browser = False

# dummy for testing. Don't use this in production!
c.JupyterHub.authenticator_class = "dummy"

c.FargateSpawner.get_run_task_args = lambda spawner: {
  'cluster': 'beta-jupyterhub-cluster',
  'taskDefinition': 'jupyterhub-notebook:1',
  'overrides': {
    'taskRoleArn': 'arn:aws:iam::{account_id}:role/JupyterHubNotebookExecTask',
    'containerOverrides': [{
      'command': ['/opt/conda/bin/jupyterhub-singleuser'] + ['--NotebookApp.notebook_dir=/home','--NotebookApp.default_url=/lab',f'--port={spawner.notebook_port}','--config=notebook_config.py'],
      'environment': [
        {
          'name': name,
          'value': value,
        } for name, value in spawner.get_env().items()
      ],
      'name': 'jupyterhub-notebook',
    }],
  },
  'count': 1,
  'launchType': 'FARGATE',
  'networkConfiguration': {
    'awsvpcConfiguration': {
      'assignPublicIp': 'ENABLED',
      'securityGroups': ['sg-XXXXX'],
      'subnets':  ['subnet-XXXXX'],
    },
  },
}

c.Spawner.default_url = '/lab'
## Timeout (in seconds) before giving up on a spawned HTTP server
c.Spawner.http_timeout = 300

## Timeout (in seconds) before giving up on starting of single-user server.
c.Spawner.start_timeout = 300

## Enable debug-logging of the single-user server
c.Spawner.debug = True

# Initializing the proxy class
# c.JupyterHub.proxy_class = 'jupyterhub.proxy.ConfigurableHTTPProxy'

# Ths is for enabling the Debug mode
# c.ConfigurableHTTPProxy.debug = True

# Whether to shutdown the proxy when the Hub shuts down.
# c.JupyterHub.cleanup_proxy = False

# This tells the hub to not stop servers when the hub restarts 
# (this is useful even if you don’t run the proxy separately)
# c.JupyterHub.cleanup_servers = False

# This tells the hub that the proxy should not be started (because you start it yourself)
# c.ConfigurableHTTPProxy.should_start = False

# Should be set to a token for authenticating communication with the proxy.
# c.ConfigurableHTTPProxy.auth_token = config['HTTP_PROXY_AUTH_TOKEN']

# Should be set to the URL which the hub uses to connect to the proxy’s API
c.ConfigurableHTTPProxy.api_url = 'http://0.0.0.0:8001'
