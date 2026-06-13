#!/bin/bash
echo "Iniciando atualização..."
cd /home/ondance_public/backend && git pull && sudo systemctl restart ondance
cd /home/ondance_public/frontend && git pull && npm install && npx quasar build && sudo cp -r dist/spa/* /etc/icontainer/apps/openresty/openresty/www/sites/ondance-frontend.ddns.net/index/ && sudo docker exec ic-openresty-00VZ nginx -s reload
echo "Atualização concluída com sucesso!"