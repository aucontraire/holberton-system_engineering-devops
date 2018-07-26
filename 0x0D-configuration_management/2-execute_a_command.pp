# kill a process named killmenow
exec { 'kill_process':
  command  => 'pkill -f killmenow',
  provider => 'shell',
  path     => ['/usr/bin', '/usr/sbin',]
}
