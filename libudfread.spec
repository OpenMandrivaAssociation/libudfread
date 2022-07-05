%define         major 0
%define         libname %mklibname udfread %{major}
%define         devel %mklibname udfread -d

Name:           libudfread
Version:        1.1.2
Release:        1
Summary:        UDF reader from VideoLAN
Group:          System/Libraries
License:        LGPLv2+
URL:            https://code.videolan.org/videolan/libudfread
Source0:        https://code.videolan.org/videolan/libudfread/-/archive/%{version}/%{name}-%{version}.tar.bz2


%description
UDF reader made by developers from VideoLAN project.

%package        -n %{libname}
Summary:        Library files for %{name}

%description    -n %{libname}
Libraries for %{name}.

%package        -n %{devel}
Summary:        Development files for %{name}
Requires:       %{libname} = %{version}-%{release}

%description    -n %{devel}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1

%build
autoreconf -vfi
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -delete

%files -n %{libname}
%license COPYING
%{_libdir}/*udfread*.so.%{major}{,.*}

%files -n %{devel}
%doc examples/*
%{_includedir}/*
%{_libdir}/*udfread*.so
%{_libdir}/pkgconfig/udfread.pc
