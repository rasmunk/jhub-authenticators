"""A simple jupyter config file for testing the authenticator."""
c = get_config()

c.JupyterHub.ip = "0.0.0.0"
c.JupyterHub.hub_ip = "0.0.0.0"
c.JupyterHub.authenticator_class = "jhubauthenticators.DataRemoteUserAuthenticator"
c.DataRemoteUserAuthenticator.data_headers = ["Mount"]
