# terminates a process
exec { 'killmenow':
  command => 'pkill -9 -f killmenow',
}
