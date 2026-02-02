module.exports = {
  apps: [{
    name: 'nado-bot',
    interpreter: '/home/user/nado-volume/packages/nado/venv/bin/python',
    script: 'main.py',
    cwd: '/home/user/nado-volume/packages/nado',
    autorestart: true,
    max_restarts: 10,
    min_uptime: '10s',
    restart_delay: 5000,
    log_date_format: 'YYYY-MM-DD HH:mm:ss Z',
    error_file: 'logs/nado-error.log',
    out_file: 'logs/nado-out.log',
    merge_logs: true,
    max_memory_restart: '500M',
    watch: false,
    ignore_watch: ['logs', 'node_modules', '__pycache__', '.git', 'docs']
  }]
};
