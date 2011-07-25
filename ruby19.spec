%define rubyver         1.9.2
%define rubyminorver    p290

Name:           ruby
Version:        %{rubyver}%{rubyminorver}
Release:        1%{?dist}
License:        Ruby License/GPL - see COPYING
URL:            http://www.ruby-lang.org/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  readline readline-devel ncurses ncurses-devel gdbm gdbm-devel glibc-devel tcl-devel gcc unzip openssl-devel db4-devel byacc make
Source0:        ftp://ftp.ruby-lang.org/pub/ruby/ruby-%{rubyver}-%{rubyminorver}.tar.gz
Summary:        An interpreter of object-oriented scripting language
Group:          Development/Languages
Requires: openssl, openssl-devel, zlib, zlib-devel
Provides: ruby(abi) = 1.9
Provides: ruby-irb
Provides: ruby-rdoc
Provides: ruby-libs
Provides: ruby-devel
Obsoletes: ruby
Obsoletes: ruby-libs
Obsoletes: ruby-irb
Obsoletes: ruby-rdoc
Obsoletes: ruby-devel

%description
Ruby is the interpreted scripting language for quick and easy
object-oriented programming.  It has many features to process text
files and to do system management tasks (as in Perl).  It is simple,
straight-forward, and extensible.

%prep
%setup -n ruby-%{rubyver}-%{rubyminorver}

%build
export CFLAGS="$RPM_OPT_FLAGS -Wall -fno-strict-aliasing"

%configure \
  --enable-shared \
  --disable-rpath \
  --without-X11 \
  --without-tk \
  --without-tcl \
  --includedir=%{_includedir}/ruby \
  --libdir=%{_libdir} \
  --with-openssl-include=/usr/include/openssl \
  --with-openssl-lib=/usr/lib64/openssl/engines \
  --with-zlib-include=/usr/include \
  --with-zlib-lib=/usr/lib64

make %{?_smp_mflags}

%install
# installing binaries ...
make install DESTDIR=$RPM_BUILD_ROOT

#we don't want to keep the src directory
rm -rf $RPM_BUILD_ROOT/usr/src

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%{_bindir}
%{_includedir}
%{_datadir}
%{_libdir}

%changelog
* Sun Jul 24 2011 Matt Albright <mattalbright@gmail.com> - 1.9.2-p290-1
- Update ruby version to 1.9.2-p290

* Tue Jul 05 2011 Neal Brown <neal@spiceworks.com> - 1.9.2-p180-3
- Added openssl and zlib support

* Sat Jun 25 2011 Ian Meyer <ianmmeyer@gmail.com> - 1.9.2-p180-2
- Remove non-existant --sitearchdir and --vedorarchdir from %configure
- Replace --sitedir --vendordir with simpler --libdir
- Change %{_prefix}/share to %{_datadir}

* Tue Mar 7 2011 Robert Duncan <robert@robduncan.co.uk> - 1.9.2-p180-1
- Update prerequisites to include make
- Update ruby version to 1.9.2-p180
- Install /usr/share documentation
- (Hopefully!?) platform agnostic

* Sun Jan 2 2011 Ian Meyer <ianmmeyer@gmail.com> - 1.9.2-p136-1
- Initial spec to replace system ruby with 1.9.2-p136
