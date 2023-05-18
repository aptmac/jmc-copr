# Version
%global major 8
%global minor 3
%global patchlevel 0

# Revision
%global revnum 1
%global releasestr %{revnum}

%global release_name %{major}.%{minor}.%{patchlevel}
%global tarball_name org.openjdk.jmc-%{release_name}-linux.gtk.x86_64

# Install jmc in /usr/lib/jmc (arch-specific and multilib exempt)
%global _jmcdir %{_prefix}/lib/%{name}

%global debug_package %{nil}

# Don't export Eclipse libraries
%global __provides_exclude_from ^%{_jmcdir}/plugins/org.eclipse.*$
%global __requires_exclude_from ^%{_jmcdir}/plugins/org.eclipse.*$

%global __requires_exclude ^osgi\\((javax|org\\.apache|org\\.eclipse|org\\.sat4j).*$
%global __provides_exclude ^osgi\\((com|javax|org\\.apache|org\\.glassfish|org\\.kxml2|org\\.sat4j|org\\.tukaani|org\\.w3c|org\\.xmlpull).*$

Name:       jmc
Version:    %{major}.%{minor}.%{patchlevel}
Release:    %{releasestr}
Summary:    JDK Mission Control is a production time profiling and diagnostics tools suite. 

License:    UPL
URL:        https://openjdk.java.net/projects/jmc/

Source0:    https://github.com/adoptium/jmc-build/releases/download/%{release_name}/%{tarball_name}.tar.gz
Source1:    %{name}.desktop
Source2:    %{name}.1
Source3:    jmc.appdata.xml

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires:   java-11-openjdk-devel

%description
JDK Mission Control is a powerful profiler for HotSpot JVMs and has an
advanced set of tools that enables efficient and detailed analysis of the
extensive data collected by Flight Recorder. The tool chain enables
developers and administrators to collect and analyze data from Java
applications running locally or deployed in production environments.

%prep
%setup -q -n 'JDK Mission Control'

%build
# Nothing to build, thank you Adoptium.

%install

# change jmc.ini to use system java (remove -vm option line)
sed -i '/^-vm$/d' %{_builddir}/'JDK Mission Control'/%{name}.ini
sed -i '/^..\/..\/bin\/$/d' %{_builddir}/'JDK Mission Control'/%{name}.ini

# delete unnecessary files (e.g., p2)
rm -r %{_builddir}/JDK\ Mission\ Control/p2/

# move contents of 'JDK Mission Control' and 'legal' folders to /usr/lib/jmc/
install -d -m 755 %{buildroot}%{_jmcdir}
cp -p -r %{_builddir}/JDK\ Mission\ Control/* %{buildroot}%{_jmcdir}/
cp -p -r %{_builddir}/legal/ %{buildroot}%{_jmcdir}/

# move jmc.ini to /etc/jmc.ini
install -d -m 755 %{buildroot}%{_sysconfdir}
mv %{buildroot}%{_jmcdir}/%{name}.ini %{buildroot}%{_sysconfdir}/%{name}.ini
ln -s %{_sysconfdir}/%{name}.ini %{buildroot}%{_jmcdir}/%{name}.ini

# create symlink to jmc in /usr/bin/
install -d -m 755 %{buildroot}%{_bindir}
ln -s %{_jmcdir}/%{name} %{buildroot}%{_bindir}/%{name}

# create application launcher in desktop menu
install -d -m 755 %{buildroot}%{_datadir}/pixmaps
mv %{buildroot}%{_jmcdir}/icon.xpm %{buildroot}%{_datadir}/pixmaps/%{name}.xpm
chmod 644 %{buildroot}%{_datadir}/pixmaps/%{name}.xpm
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

# install appstream metadata
install -D -m 644 %{SOURCE3} %{buildroot}%{_metainfodir}/jmc.appdata.xml
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/jmc.appdata.xml

# install manpage and insert location of config file
install -D -m 644 %{SOURCE2} %{buildroot}%{_mandir}/man1/%{name}.1
sed -i "/.SH FILES/a .I %{_sysconfdir}/%{name}.ini" %{buildroot}%{_mandir}/man1/%{name}.1

%files
%license %{_jmcdir}/legal/LICENSE.txt
%license %{_jmcdir}/legal/THIRDPARTYREADME.txt
%config(noreplace) %{_sysconfdir}/%{name}.ini
%{_jmcdir}
%{_mandir}/man1/%{name}.1*
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/applications/%{name}.desktop
%{_metainfodir}/jmc.appdata.xml

%changelog
* Wed May 17 2023 Alex Macdonald <almacdon@redhat.com> - 8.3.0-1
- Update to version 8.3.0-ga

* Wed Jun 16 2021 Alex Macdonald <almacdon@redhat.com> - 8.1.0-1.SNAPSHOT.20210607613
- Initial copr packaging of AdoptOpenJDK binaries
