%define name valheim
%define version 0.0.7
%define release 1
%define user_home /valheim

%global debug_package %{nil}

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Valheim game server


License:	MIT
URL:		https://github.com/bostrt/valheim-server
Source0:    https://github.com/bostrt/valheim-server/archive/%{name}-%{version}-%{release}.tar.gz

BuildArch: x86_64

BuildRequires: systemd-rpm-macros

# Deps for steamcmd
Requires:       glibc(x86-32) libstdc++(x86-32)


%description
Valheim dedicated game server.


%pre
if [ "$1" = 1 ]; then
  # install
  mkdir -p /valheim/Game
  useradd -d /valheim valheim
  chown -R valheim:valheim /valheim
  semanage fcontext -a -t usr_t '/valheim(/.*)?'
fi


%preun
%systemd_preun valheim-backup.timer
%systemd_preun valheim.service


%prep
%setup -q -n %{name}-server-%{version}


%install
rm -rf $RPM_BUILD_ROOT
install -p -D -m 644 valheim.service %{buildroot}%{_unitdir}/valheim.service
install -p -D -m 644 valheim-backup.service  %{buildroot}%{_unitdir}/valheim-backup.service
install -p -D -m 644 valheim-backup.timer  %{buildroot}%{_unitdir}/valheim-backup.timer
install -p -D -m 644 valheim-backup.timer  %{buildroot}%{_unitdir}/valheim-backup.timer
install -p -D -m 644 50-valheim.preset  %{buildroot}%{_presetdir}/50-valheim.preset
install -p -D -m 644 valheim-sysconfig %{buildroot}%{_sysconfdir}/valheim

install -p -D -m 744 start_valheim.sh %{buildroot}/valheim/Game/start_valheim.sh
install -p -D -m 744 backup.sh %{buildroot}/valheim/backup.sh
install -p -D -m 744 update.sh %{buildroot}/valheim/update.sh


%post
%systemd_post valheim-backup.timer
if [ "$1" = 1 ]; then
  # install
  restorecon -RF /valheim/
  echo 'Installing Valheim via steamcmd. This will take a few moments...' > /proc/$PPID/fd/1
  sudo -u valheim /valheim/update.sh
  systemctl start valheim-backup.timer
fi


%postun
if [ "$1" = 0 ]; then
  # uninstall
  userdel valheim
  semanage fcontext -d -t usr_t '/valheim(/.*)?'
fi


%files
%defattr(-,root,root)
%doc README.md
%{_unitdir}/valheim.service
%{_unitdir}/valheim-backup.service
%{_unitdir}/valheim-backup.timer
%{_presetdir}/50-valheim.preset
%{_sysconfdir}/valheim
%attr(-,valheim,valheim) %{user_home}/backup.sh
%attr(-,valheim,valheim) %{user_home}/update.sh
%attr(-,valheim,valheim) %{user_home}/Game
%attr(-,valheim,valheim) %{user_home}/Game/start_valheim.sh


%changelog
* Thu Feb 25 2021 Robert Bost <rbost@redhat.com> 0.0.7-1
- new package built with tito
