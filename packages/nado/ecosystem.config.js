module.exports = {
  apps: [
    {
      name: 'nado-bot',
      script: 'python',
      args: 'main.py',
      cwd: '/home/user/lighter-volume/packages/nado',
      interpreter: 'none',
      env: {
        PYTHONPATH: '/home/user/lighter-volume/packages/nado'
      },
      // Restart policy
      autorestart: true,
      max_restarts: 10,
      min_uptime: '10s',
      restart_delay: 5000,

      // Logging
      log_date_format: 'YYYY-MM-DD HH:mm:ss Z',
      error_file: 'logs/nado-error.log',
      out_file: 'logs/nado-out.log',
      merge_logs: true,

      // Resource limits
      max_memory_restart: '500M',

      // Watch for changes (disable in production)
      watch: false,
      ignore_watch: ['logs', 'node_modules', '__pycache__', '.git', 'docs']
    }
  ]
};
