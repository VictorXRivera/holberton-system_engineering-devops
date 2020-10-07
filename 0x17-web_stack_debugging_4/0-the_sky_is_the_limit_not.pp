# Sky is the limit, let's bring that limit higher

exec { 'Update /etc/default/nginx':
  path    => '/bin:/usr/bin:/sbin:/usr/sbin',
  command => 'sed -i "/ULIMIT=/c\ULIMIT=\'-n 20000\'" /etc/default/nginx; sudo service nginx restart',
}
