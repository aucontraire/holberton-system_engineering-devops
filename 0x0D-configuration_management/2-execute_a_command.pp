# kill a process named killmenow
exec { 'kill_process':
  command  => 'pkill -9 -f killmenow',
  provider => 'shell',
  path     => ['/usr/bin', '/usr/sbin',]
}
