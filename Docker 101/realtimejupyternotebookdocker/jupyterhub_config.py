c.Authenticator.allowed_users = {'user1', 'user2'}
c.LocalAuthenticator.create_system_users = True
c.Spawner.env.update({'LD_LIBRARY_PATH': '/usr/local/nvidia/bin:/usr/local/cuda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'})
c.Spawner.env_keep = ['PATH', 'PYTHONPATH', 'CONDA_ROOT', 'CONDA_DEFAULT_ENV', 'VIRTUAL_ENV', 'LANG', 'LC_ALL', 'JUPYTERHUB_SINGLEUSER_APP','LD_LIBRARY_PATH']