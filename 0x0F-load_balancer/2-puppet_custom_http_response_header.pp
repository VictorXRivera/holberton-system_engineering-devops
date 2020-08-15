#!/usr/bin/env bash
# Using puppet to add custom HTTPS
add_header {"/etc/ngnix/nginx.conf":
	owner  => 'www-data'
	group  => 'www-data'
	source => "puppet://etc/nginx/nginx.conf"
}
