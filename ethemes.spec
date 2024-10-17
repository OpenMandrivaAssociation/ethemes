Name:		ethemes
Version:	1.1
Release:	 17
License:	GPL
Summary:	Themes for Enlightenment
Group:		Graphical desktop/Enlightenment

Source:		ethemes-%{version}.tar.bz2

BuildRoot:	%_tmppath/%name-%version-%release-root
Requires:	enlightenment >= 0.16
BuildArchitectures: noarch
URL:		https://e.themes.org/
Prefix:		%{_prefix}

%description
This package contains some nice themes for Enlightenment.

%description -l fr
Ce package contient des thèmes pour Enlightenment.

%prep
%setup -q -n  %{name} 

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{prefix}/X11R6/share/enlightenment/themes/
cp -a * $RPM_BUILD_ROOT%{prefix}/X11R6/share/enlightenment/themes/
cd $RPM_BUILD_ROOT%{prefix}/X11R6/share/enlightenment/themes/Absolute_E/sound/samples
for sample in *.wav;
 do ln -sf %{prefix}/X11R6/share/enlightenment/themes/BrushedMetal-Tigert/sound/samples/$sample .;
done
find $RPM_BUILD_ROOT -type d -a -name .xvpics | xargs rm -rf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root)
%{prefix}/X11R6/share/enlightenment/themes/Absolute_E
%{prefix}/X11R6/share/enlightenment/themes/Aliens
%{prefix}/X11R6/share/enlightenment/themes/minEguE
%{prefix}/X11R6/share/enlightenment/themes/GTK+




%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1-16mdv2011.0
+ Revision: 618240
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 1.1-15mdv2010.0
+ Revision: 428630
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.1-14mdv2009.0
+ Revision: 244960
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Dec 14 2007 Thierry Vignaud <tv@mandriva.org> 1.1-12mdv2008.1
+ Revision: 120120
- kill Icon tag
- use %%mkrel
- import ethemes



* Tue May 04 2004 Michael Scherer <misc@mandrake.org> 1.1-12mdk
- fix #3465, by removing .xvpics directory
 
* Fri Jul 18 2003 David BAUDENS <baudens@mandrakesoft.com> 1.1-11mdk
- Rebuild

* Thu May 16 2002 David BAUDENS <baudens@mandrakesoft.com> 1.1-10mdk
- Remove Jedi, ApplePlatiniumn, BeOS and Blue_OS

* Wed Apr 11 2001 Götz Waschk <waschk@linux-mandrake.com> 1.1-9mdk
- fixed dead symlinks in Absolute-E theme

* Sun Apr 08 2001 David BAUDENS <baudens@mandrakesoft.com> 1.1-8mdk
- Move in /usr/X11R6

* Thu Aug  3 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 1.1-7mdk
- BM + macroszification

* Mon Apr 10 2000 Daouda Lo <daouda@mandrakesoft.com> 1.1-6mdk
- add some themes (the Jedi one is amazing)
- fix group

* Wed Nov 10 1999 Alexandre Dussart <adussart@mandrakesoft.com>
- Updated Absolute_E(DR0.16, 10/23/99) 
- Removed Aztekr
- Updated ApplePlatinum(DR0.15, 08/08/99)
- Updated BeOS(DR0.15, 08/12/99)
- Added Aliens(DR0.15, 10/03/99)
- Added Blue_OS theme(DR0.16, 10/19/99) 
- Added minEguE theme(DR0.16, 10/20/99)
- Added GTK+ theme(DR0.16, 10/13/99) 
- Added URL.

* Fri Jul 30 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- put -l fr in the french description.
- added an icon.

* Fri Apr 30 1999 Alexandre Dussart <adussart@mandrakesoft.com>
- First packaging.
