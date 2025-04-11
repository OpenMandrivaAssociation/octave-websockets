%global octpkg websockets

Summary:	Simple implementation of the Websockets protocol for GNU Octave
Name:		octave-websockets
Version:	0.1.0
Release:	3
License:	GPLv3+
Group:		Sciences/Mathematics
#Url:		https://packages.octave.org/websockets/
Url:		https://github.com/gnu-octave/octave-websockets/
Source0:	https://github.com/gnu-octave/octave-websockets/archive/v%{version}/websockets-%{version}.tar.gz

BuildRequires:  octave-devel >= 3.2.0
BuildRequires:  octave-sockets >= 1.2.0

Requires:	octave(api) = %{octave_api}
Requires:  	octave-sockets >= 1.2.0

Requires(post): octave
Requires(postun): octave

BuildArch:	noarch

%description
Simple implementation of the Websockets protocol for GNU Octave.

%files
%license COPYING
#doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

