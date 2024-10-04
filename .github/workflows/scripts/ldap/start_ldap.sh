#!/bin/bash
set -e

# Start LDAP server in docker container
docker pull bitnami/openldap:latest
docker compose -f continuous_integration/ldap/start_ldap.yml up -d
docker ps