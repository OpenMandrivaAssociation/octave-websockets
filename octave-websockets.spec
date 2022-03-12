%global octpkg websockets

Summary:	A Websockets package for GNU Octave, based in the sockets package.
Name:		octave-%{octpkg}
Version:	0.1.0
Release:	1
Url:		https://github.com/gnu-octave/octave-%{octpkg}
Source0:	%{url}/archive/v%{version}/%{octpkg}-%{version}.tar.gz
License:	GPLv3+
Group:		Sciences/Mathematics
BuildArch:	noarch

BuildRequires:	octave-devel >= 3.6.0
BuildRequires:	octave-sockets >= 1.2.0

Requires:	octave(api) = %{octave_api}
Requires:	octave-sockets >= 1.2.0

Requires(post): octave
Requires(postun): octave

%description
A Websockets package for GNU Octave, based in the sockets package.

%files
%license COPYING
#doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-%{version}

# remove backup files
#find . -name \*~ -delete

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

