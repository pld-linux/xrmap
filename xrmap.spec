Summary:	xrmap - generate maps of the Earth with an amazing accuracy
Summary(pl):	xrmap - generowanie map Ziemi z zadziwiaj�c� dok�adno�ci�
Name:		xrmap
Version:	2.10
Release:	0.1
License:	GPL v2 + others - see README for details
Group:		X11/Applications/Science
Source0:	ftp://ftp.ac-grenoble.fr/ge/geosciences/xrmap/%{name}-%{version}.tgz
# Source0-md5:	e18247abf044e8e00616ef67f6126678
Source1:	ftp://ftp.ac-grenoble.fr/ge/geosciences/CIA_WDB2.jpd.gz
# Source1-md5:	534818ffb498322b64373f66ae042596
URL:		http://frmas.free.fr/li_1.htm
BuildRequires:	XFree86-devel
BuildRequires:	imake
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Xrmap program provides a user-friendly X client for generating
images of the Earth and manipulating the CIA World data bank II global
vector information (a huge geodata set of about 45 MB). Available
features include coastlines and islands, political boundaries, major
and minor rivers, glaciers, lakes, canals, reefs, etc. The images can
be accurately zoomed in, up to a factor of 100 or more. The package
also contains a rather comprehensive data set of world cities and
locations - about 20000 cities are listed.

%description -l pl
Program Xrmap dostarcza przyjaznego dla u�ytkownika klienta X do
generowania obraz�w Ziemi i przetwarzania og�lno�wiatowych informacji
wektorowych z CIA World Data Bank (du�ego zbioru informacji
geograficznych o obj�to�ci oko�o 45MB). Mo�liwo�ci obejmuj� linie
wybrze�y i wyspy, granice polityczne, wi�ksze i mniejsze rzeki,
lodowce, jeziora, kana�y, rafy itp. Obrazy mog� by� szczeg�owo
powi�kszane a� do wsp�czynnika 100 lub wi�cej. Pakiet zawiera tak�e
do�� obszerny zbi�r danych o miastach z ca�ego �wiata i po�o�eniach -
dost�pna jest lista oko�o 20000 miast.

%prep
%setup -q

sed -i -e 's/-O //' Imakefile

%build
xmkmf
%{__make} \
	CDEBUGFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

# originally DESTDIR was meant as prefix, but we can abuse it
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=%{_bindir} \
	MANDIR=%{_mandir}/man1 \
	SHAREDIR=%{_datadir}/rmap

install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/rmap

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README TODO WARNING
%attr(755,root,root) %{_bindir}/*
%{_datadir}/rmap
%{_mandir}/man1/*
