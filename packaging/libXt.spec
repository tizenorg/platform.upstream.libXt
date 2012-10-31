Name:           libXt
Version:        1.1.2
Release:        2
License:        MIT
Summary:        X
Url:            http://www.x.org
Group:          System Environment/Libraries

Source:         %{name}-%{version}.tar.bz2

BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xproto)

%description
X.Org X11 libXt runtime library

%package devel
Summary:        X
Group:          Development/Libraries
Requires:       %{name} = %{version}
Provides:       libxt-devel

%description devel
X.Org X11 libXt development package

%prep
%setup -q

%build
# FIXME: Work around pointer aliasing warnings from compiler for now
export CFLAGS="${CFLAGS} %{optflags} -fno-strict-aliasing"
%configure --disable-static \
           --with-appdefaultdir=/etc/X11/app-defaults \
           --with-xfile-search-path="/usr/lib/X11/%L/%T/%N%S:/usr/lib/X11/%l/%T/%N%S:/usr/lib/X11/%T/%N%S:/etc/X11/%L/%T/%N%C%S:/etc/X11/%l/%T/%N%C%S:/etc/X11/%T/%N%C%S:/etc/X11/%L/%T/%N%S:/etc/X11/%l/%T/%N%S:/etc/X11/%T/%N%S"

make %{?_smp_mflags}

%install
%make_install
mkdir -p -m 0755 %{buildroot}%{_datadir}/X11/app-defaults

%remove_docs

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING 
%{_libdir}/libXt.so.6
%{_libdir}/libXt.so.6.0.0
%dir %{_datadir}/X11/app-defaults

%files devel
%defattr(-,root,root,-)
#%{_datadir}/doc/%{name}
%{_includedir}/X11/CallbackI.h
%{_includedir}/X11/Composite.h
%{_includedir}/X11/CompositeP.h
%{_includedir}/X11/ConstrainP.h
%{_includedir}/X11/Constraint.h
%{_includedir}/X11/ConvertI.h
%{_includedir}/X11/Core.h
%{_includedir}/X11/CoreP.h
%{_includedir}/X11/CreateI.h
%{_includedir}/X11/EventI.h
%{_includedir}/X11/HookObjI.h
%{_includedir}/X11/InitialI.h
%{_includedir}/X11/Intrinsic.h
%{_includedir}/X11/IntrinsicI.h
%{_includedir}/X11/IntrinsicP.h
%{_includedir}/X11/Object.h
%{_includedir}/X11/ObjectP.h
%{_includedir}/X11/PassivGraI.h
%{_includedir}/X11/RectObj.h
%{_includedir}/X11/RectObjP.h
%{_includedir}/X11/ResConfigP.h
%{_includedir}/X11/ResourceI.h
%{_includedir}/X11/SelectionI.h
%{_includedir}/X11/Shell.h
%{_includedir}/X11/ShellI.h
%{_includedir}/X11/ShellP.h
%{_includedir}/X11/StringDefs.h
%{_includedir}/X11/ThreadsI.h
%{_includedir}/X11/TranslateI.h
%{_includedir}/X11/VarargsI.h
%{_includedir}/X11/Vendor.h
%{_includedir}/X11/VendorP.h
%{_includedir}/X11/Xtos.h
%{_libdir}/libXt.so
%{_libdir}/pkgconfig/xt.pc
#%{_mandir}/man3/*.3*
