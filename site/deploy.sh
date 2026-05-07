#!/bin/bash
set -e
echo "=== Deploying Sentinel Ops landing page ==="
docker compose up -d --force-recreate
echo ""
echo "Container status:"
docker compose ps
echo ""
echo "=== To enable nginx reverse proxy: ==="
echo "  cp deploy/nginx-sentinel-ops /etc/nginx/sites-available/sentinel-ops"
echo "  ln -sf /etc/nginx/sites-available/sentinel-ops /etc/nginx/sites-enabled/sentinel-ops"
echo "  nginx -t && systemctl reload nginx"
echo ""
echo "=== Done. Open http://127.0.0.1:8080 to verify ==="