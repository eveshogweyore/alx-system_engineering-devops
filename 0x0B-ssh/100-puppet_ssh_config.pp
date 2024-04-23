# Make changes to configuration file.

$content = file('/etc/ssh/ssh_config')

file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => "${content}PasswordAuthentication no\nIdentityFile ~/.ssh/school\n",
}
