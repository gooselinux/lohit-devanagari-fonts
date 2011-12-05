%global fontname lohit-devanagari
%global fontconf 66-%{fontname}.conf

Name:           %{fontname}-fonts
Version:        2.4.3
Release:        6%{?dist}
Summary:        Free Devanagari Script Font

Group:          User Interface/X
License:        GPLv2 with exceptions
URL:            https://fedorahosted.org/lohit/
Source0:        https://fedorahosted.org/releases/l/o/lohit/%{fontname}-%{version}.tar.gz
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:      noarch
BuildRequires: fontforge >= 20080429
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem
Patch1: bug-578034.patch
# remove provides in f15
Provides: lohit-marathi-fonts = %{version}-%{release}
Provides: lohit-hindi-fonts = %{version}-%{release}
Provides: lohit-konkani-fonts = %{version}-%{release}
Provides: lohit-nepali-fonts = %{version}-%{release}
Provides: lohit-maithili-fonts = %{version}-%{release}
Provides: lohit-kashmiri-fonts = %{version}-%{release}
Provides: lohit-sindhi-fonts = %{version}-%{release}

Obsoletes: lohit-marathi-fonts < 2.4.3-4
Obsoletes: lohit-hindi-fonts < 2.4.3-4
Obsoletes: lohit-konkani-fonts < 2.4.3-4
Obsoletes: lohit-nepali-fonts < 2.4.3-4
Obsoletes: lohit-maithili-fonts < 2.4.3-4
Obsoletes: lohit-kashmiri-fonts < 2.4.3-4
Obsoletes: lohit-sindhi-fonts < 2.4.3-4


%description
This package provides a free Devanagari Script TrueType/OpenType font.


%prep
%setup -q -n %{fontname}-%{version} 
%patch1 -p1 -b .1-fix-font-conf

%build
make

%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{fontconf} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}


%clean
rm -fr %{buildroot}


%_font_pkg -f %{fontconf} *.ttf

%doc ChangeLog COPYRIGHT COPYING AUTHORS README ChangeLog.old


%changelog
* Tue May 04 2010 Pravin Satpute <psatpute@redhat.com> - 2.4.3-6
- Resolves: bug 586858

* Thu Feb 04 2010 Pravin Satpute <psatpute@redhat.com> - 2.4.3-5
- done changes as per review comments bug 559936 

* Fri Jan 29 2010 Pravin Satpute <psatpute@redhat.com> - 2.4.3-4
- first release
- decided to keep only one font for all languages using devanagari script
