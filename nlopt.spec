%define libname %mklibname nlopt
%define devname %mklibname nlopt -d
%define major 0

%define pname nlopt

Name:           nlopt
Version:        2.7.1
Release:        1
Summary:        A library for nonlinear optimization
License:        LGPL-2.0-only
Group:          Development/Libraries/C and C++
URL:            https://nlopt.readthedocs.io/en/latest/
Source0:        https://github.com/stevengj/nlopt/archive/v%{version}.tar.gz#/%{pname}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  hdf5-devel
BuildRequires:  pkgconfig

%description
NLopt is a free/open-source library for nonlinear optimization,
providing a common interface for a number of different free
optimization routines available online as well as original
implementations of various other algorithms.

%package -n %{libname}
Summary:	NLopt is a free/open-source library for nonlinear optimization,
Group:		System/Libraries

%description -n %{libname}
This package provides the shared library for NLopt.
#------------------------------------------------

%package -n %{devname}
Summary:	Development package for %{name}
Group:		Development/Libraries
Requires:	%{libname} = %{version}-%{release}

%description -n	%{devname}
Header files for development with %{name}.


%prep
%autosetup -p1 -n %{pname}-%{version}

%build
%cmake \
   -DCMAKE_SKIP_RPATH:BOOL=OFF \
   -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON \
   -DNLOPT_MATLAB=OFF \
   -DNLOPT_CXX:BOOL=ON \
   -DNLOPT_TESTS:BOOL=ON \
   -DNLOPT_PYTHON:BOOL=OFF \
   -DNLOPT_OCTAVE:BOOL=OFF \
   -DNLOPT_SWIG:BOOL=OFF
%make_build

%install
%make_install -C build

%files -n %{libname}
%{_libdir}/*.so.0*

%files -n %{devname}
%{_libdir}/libnlopt.so
%{_libdir}/cmake/
%{_includedir}/nlopt.f
%{_includedir}/nlopt.h
%{_includedir}/nlopt.hpp
%{_libdir}/pkgconfig/nlopt.pc
%{_mandir}/man3/*
