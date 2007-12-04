Name:		ethemes
Version:	1.1
Release:	 %mkrel 12
License:	GPL
Summary:	Themes for Enlightenment
Group:		Graphical desktop/Enlightenment

Source:		ethemes-%{version}.tar.bz2

Icon:		ethemes-logo.xpm
BuildRoot:	%_tmppath/%name-%version-%release-root
Requires:	enlightenment >= 0.16
BuildArchitectures: noarch
URL:		http://e.themes.org/
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


