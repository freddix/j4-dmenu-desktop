Summary:	A replacement for i3-dmenu-desktop
Name:		j4-dmenu-desktop
Version:	2.4
Release:	1
License:	GPL v3
Group:		Applications
Source0:	https://github.com/enkore/j4-dmenu-desktop/archive/r%{version}.tar.gz
# Source0-md5:	f03c72f8595e20e291e27f21ebbbf073
BuildRequires:	cmake
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
j4-dmenu-desktop is a replacement for i3-dmenu-desktop. It's purpose
is to find .desktop files and offer you a menu to start an application
using dmenu.

%prep
%setup -qn %{name}-r%{version}
%{__sed} -i "s/-Wpedantic//" CMakeLists.txt

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_CXX_FLAGS="%{rpmcxxflags}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/j4-dmenu-desktop

