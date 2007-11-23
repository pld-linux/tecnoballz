# TODO:
# - pl descryption and summary
# - desktop and icon
Summary:	A breakout clone with 50 levels of game and 11 special levels
Name:		tecnoballz
Version:	0.92
Release:	1
License:	GPL v3
Group:		X11/Applications/Games
Source0:	http://linux.tlk.fr/games/TecnoballZ/download/%{name}-%{version}.tgz
# Source0-md5:	111022212bc77b7dfcb453eaa5eac751
URL:		http://linux.tlk.fr/games/TecnoballZ/
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	libmikmod-devel
BuildRequires:	smpeg-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A exciting Brick Breaker with 50 levels of game and 11 special levels,
distributed on the 2 modes of game to give the player a sophisticated
system of attack weapons with an enormous power of fire that can be
build by gaining bonuses. Numerous decors, musics and sounds complete
this great game. This game was ported from the Commodore Amiga.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# FIX: add missing files
cp -fr src/TecnoballZ/levels-data.xml src/TecnoballZ/texts $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES NEWS README
%attr(2755,root,games) %{_prefix}/games/%{name}
%{_datadir}/%{name}
%attr(2775,root,games) %dir /var/games/tecnoballz
%attr(664,root,games) %config(noreplace) %verify(not md5 mtime size) /var/games/tecnoballz/tecnoballz.hi
%{_mandir}/man6/*
