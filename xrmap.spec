Summary:	xrmap
Name:		xrmap
Version:	2.10
Release:	0.1
License:	GPL v2 + others - see README for details
Group:		X11/Applications/Science
Source0:	ftp://ftp.ac-grenoble.fr/ge/geosciences/%{name}/%{name}-%{version}.tgz
# Source0-md5:	e18247abf044e8e00616ef67f6126678
Source1:	ftp://ftp.ac-grenoble.fr/ge/geosciences/CIA_WDB2.jpd.gz
# Source1-md5:	534818ffb498322b64373f66ae042596
URL:		http://frmas.free.fr/li_1.htm
BuildRequires:	XFree86-devel
BuildRequires:	imake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define _prefix	/usr
%define _bindir %{_prefix}/X11R6/bin
%define _mandir %{_prefix}/X11R6/man

%description
The Xrmap program provides a user-friendly X client for generating
images of the Earth and manipulating the CIA World data bank II global
vector information (a huge geodata set of about 45 MB). Available
features include coastlines and islands, political boundaries, major
and minor rivers, glaciers, lakes, canals, reefs, etc. The images can
be accurately zoomed in, up to a factor of 100 or more. The package
also contains a rather comprehensive data set of world cities and
locations - about 20000 cities are listed.

%prep
%setup -q -n %{name}-%{version}

%build
xmkmf
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT/%{_prefix}
cp %{SOURCE1} $RPM_BUILD_ROOT/%{_datadir}/rmap

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README TODO WARNING
%attr(755,root,root) %{_bindir}/*
%{_datadir}/rmap/*
%{_mandir}/man1/*
