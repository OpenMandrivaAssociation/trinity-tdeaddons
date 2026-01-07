%bcond clang 1
%bcond gamin 1
%bcond python 1

# BUILD WARNING:
#  Remove qt-devel and qt3-devel and any kde*-devel on your system !
#  Having KDE libraries may cause FTBFS here !

# TDE variables
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif
%define pkg_rel 3

%define tde_pkg tdeaddons
%define tde_prefix /opt/trinity


%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity


Name:		trinity-%{tde_pkg}
Summary:	Trinity Desktop Environment - Plugins
Version:	%{tde_version}
Release:	%{?!preversion:%{pkg_rel}}%{?preversion:0_%{preversion}}%{?dist}
Group:		User Interface/Desktops
URL:		http://www.trinitydesktop.org/

License:	GPLv2+


Obsoletes:	trinity-kdeaddons < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdeaddons = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	trinity-kdeaddons-extras < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdeaddons-extras = %{?epoch:%{epoch}:}%{version}-%{release}

Prefix:    %{tde_prefix}

Source0:	https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/core/%{tarball_name}-%{version}%{?preversion:~%{preversion}}.tar.xz

BuildSystem:    cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DINCLUDE_INSTALL_DIR=%{tde_prefix}/include/tde
BuildOption:    -DPKGCONFIG_INSTALL_DIR=%{tde_prefix}/%{_lib}/pkgconfig
BuildOption:    -DSYSCONF_INSTALL_DIR="%{_sysconfdir}/trinity"
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_prefix}/share
BuildOption:    -DWITH_ALL_OPTIONS=ON -DWITH_ARTS=ON -DWITH_SDL=ON
BuildOption:    -DWITH_XMMS=OFF -DWITH_TEST=OFF -DBUILD_ALL=ON
BuildOption:    -DBUILD_ATLANTIKDESIGNER=ON -DBUILD_DOC=ON
BuildOption:    -DBUILD_KADDRESSBOOK_PLUGINS=ON -DBUILD_KATE_PLUGINS=ON
BuildOption:    -DBUILD_KICKER_APPLETS=ON -DBUILD_KNEWSTICKER_SCRIPTS=ON
BuildOption:    -DBUILD_KONQ_PLUGINS=ON -DBUILD_KSIG=ON -DBUILD_NOATUN_PLUGINS=ON
BuildOption:    -DBUILD_RENAMEDLG_PLUGINS=ON -DBUILD_TDEFILE_PLUGINS=ON
BuildOption:    -DBUILD_TUTORIALS=OFF
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}
# to be removed - https://mirror.git.trinitydesktop.org/gitea/TDE/tdeaddons/issues/59
BuildOption:    -DWITH_BERKELEY_DB=OFF
  
# Trinity dependencies
BuildRequires: trinity-tdelibs-devel >= %{tde_version}
BuildRequires: trinity-tdebase-devel >= %{tde_version}
BuildRequires: trinity-tdegames-devel >= %{tde_version}
BuildRequires: trinity-tdemultimedia-devel >= %{tde_version}
BuildRequires: trinity-tdepim-devel >= %{tde_version}

BuildRequires:	trinity-tde-cmake >= %{tde_version}

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig
BuildRequires:	fdupes

# SDL support
BuildRequires:  pkgconfig(sdl)

# ALSA supportl
BuildRequires:  pkgconfig(alsa)

# OPENSSL support
BuildRequires:  pkgconfig(openssl)

# IDN support
BuildRequires:	pkgconfig(libidn)

# GAMIN support
%{?with_gamin:BuildRequires:	pkgconfig(gamin)}

# PCRE2 support
BuildRequires:  pkgconfig(libpcre2-posix)

# ACL support
BuildRequires:  pkgconfig(libacl)

# DB4/DB5 support
# to be removed - https://mirror.git.trinitydesktop.org/gitea/TDE/tdeaddons/issues/59
#{?with_db:BuildRequires:	db-devel}

BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)

# PYTHON support
%if %{with python}
%global python python3
%global __python %__python3
%endif 

Requires: trinity-atlantikdesigner = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kaddressbook-plugins = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kate-plugins = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-tdeaddons-tdefile-plugins = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kicker-applets = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-knewsticker-scripts = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-konq-plugins = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-ksig = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-noatun-plugins = %{?epoch:%{epoch}:}%{version}-%{release}


%description
A collection of TDE Addons/Plugins, including: 
* atlantikdesigner: game board designer
* konq-plugins: akregator, babelfish, domtreeviewer, imagerotation, validators, webarchiver
* kate (plugins) 
* kicker-applets: kbinaryclock, kolourpicker, ktimemon, mediacontrol
* knewsticker-scripts
* noatun-plugins

%files
%defattr(-,root,root,-)

##########

%package -n trinity-atlantikdesigner
Summary:	Game board designer for Atlantik
Group:		Applications/Games
#Requires:	trinity-atlantik
Requires:	trinity-tdegames

%description -n trinity-atlantikdesigner
Atlantik Designer is a game board designer for the game Atlantik.

Atlantik is a TDE client for playing Monopoly-like board games on the
monopd network.  It can play any board supported by the network
server, including the classic Monopoly game as well as the Atlantik
game in which the properties include several major cities in North
America and Europe.

%files -n trinity-atlantikdesigner
%defattr(-,root,root,-)
%doc README atlantikdesigner/TODO
%{tde_prefix}/bin/atlantikdesigner
%{tde_prefix}/share/apps/atlantikdesigner
%{tde_prefix}/share/applications/tde/atlantikdesigner.desktop
%{tde_prefix}/share/icons/hicolor/*/apps/atlantikdesigner.png
%{tde_prefix}/share/doc/tde/HTML/en/atlantikdesigner/
%{tde_prefix}/share/man/man1/atlantikdesigner.1*

##########

%package -n trinity-kaddressbook-plugins
Summary:	Plugins for KAddressBook, the Trinity address book
Group:		Applications/Utilities
Requires:	trinity-kaddressbook

%description -n trinity-kaddressbook-plugins
This package contains a variety of useful plugins for the KDE address
book.  These plugins can be loaded through the TDE address book settings.

Highlights include exporting postal addresses as flags in KWorldClock,
as well as importing and exporting contacts in the native format used
by the German freemail provider GMX.

%files -n trinity-kaddressbook-plugins
%defattr(-,root,root,-)
%doc README
%{tde_prefix}/%{_lib}/trinity/libkaddrbk_geo_xxport.la
%{tde_prefix}/%{_lib}/trinity/libkaddrbk_geo_xxport.so
%{tde_prefix}/%{_lib}/trinity/libkaddrbk_gmx_xxport.la
%{tde_prefix}/%{_lib}/trinity/libkaddrbk_gmx_xxport.so
%{tde_prefix}/share/apps/kaddressbook
%{tde_prefix}/share/services/kaddressbook

##########

%package -n trinity-kate-plugins
Summary:	Plugins for Kate, the TDE Advanced Text Editor
Group:		Applications/Utilities
Requires:	trinity-kate
Requires:	tidy

%description -n trinity-kate-plugins
This package contains a variety of useful plugins for Kate, the KDE
Advanced Text Editor.  These plugins can be loaded through the plugin
manager in Kate settings.

Highlights include spell checking, text filtering, HTML/XML construction
and validation, vim/emacs modeline handling, templates for new files
and text snippets, opening of C/C++ headers, extraction of C/C++ symbols,
a tab bar, a Python browser and even more.

%files -n trinity-kate-plugins
%defattr(-,root,root,-)
%doc kate/xmltools/ChangeLog kate/xmltools/README
%{tde_prefix}/%{_lib}/trinity/katecppsymbolviewerplugin.la
%{tde_prefix}/%{_lib}/trinity/katecppsymbolviewerplugin.so
%{tde_prefix}/%{_lib}/trinity/katefiletemplates.la
%{tde_prefix}/%{_lib}/trinity/katefiletemplates.so
%{tde_prefix}/%{_lib}/trinity/katefll_plugin.la
%{tde_prefix}/%{_lib}/trinity/katefll_plugin.so
%{tde_prefix}/%{_lib}/trinity/katehelloworldplugin.la
%{tde_prefix}/%{_lib}/trinity/katehelloworldplugin.so
%{tde_prefix}/%{_lib}/trinity/katehtmltoolsplugin.la
%{tde_prefix}/%{_lib}/trinity/katehtmltoolsplugin.so
%{tde_prefix}/%{_lib}/trinity/kateinsertcommandplugin.la
%{tde_prefix}/%{_lib}/trinity/kateinsertcommandplugin.so
%{tde_prefix}/%{_lib}/trinity/katemakeplugin.la
%{tde_prefix}/%{_lib}/trinity/katemakeplugin.so
%{tde_prefix}/%{_lib}/trinity/katemodelineplugin.la
%{tde_prefix}/%{_lib}/trinity/katemodelineplugin.so
%{tde_prefix}/%{_lib}/trinity/kateopenheaderplugin.la
%{tde_prefix}/%{_lib}/trinity/kateopenheaderplugin.so
%{tde_prefix}/%{_lib}/trinity/katepybrowseplugin.la
%{tde_prefix}/%{_lib}/trinity/katepybrowseplugin.so
%{tde_prefix}/%{_lib}/trinity/katesnippetsplugin.la
%{tde_prefix}/%{_lib}/trinity/katesnippetsplugin.so
%{tde_prefix}/%{_lib}/trinity/katetextfilterplugin.la
%{tde_prefix}/%{_lib}/trinity/katetextfilterplugin.so
%{tde_prefix}/%{_lib}/trinity/katexmlcheckplugin.la
%{tde_prefix}/%{_lib}/trinity/katexmlcheckplugin.so
%{tde_prefix}/%{_lib}/trinity/katexmltoolsplugin.la
%{tde_prefix}/%{_lib}/trinity/katexmltoolsplugin.so
%{tde_prefix}/%{_lib}/trinity/libkatetabbarextensionplugin.la
%{tde_prefix}/%{_lib}/trinity/libkatetabbarextensionplugin.so
%{tde_prefix}/share/applnk/.hidden/kate-plugins.desktop
%{tde_prefix}/share/applnk/.hidden/katefll.desktop
%{tde_prefix}/share/apps/kate
%{tde_prefix}/share/apps/katepart
%{tde_prefix}/share/apps/katexmltools
%{tde_prefix}/share/services/katecppsymbolviewer.desktop
%{tde_prefix}/share/services/katefiletemplates.desktop
%{tde_prefix}/share/services/katefll_plugin.desktop
%{tde_prefix}/share/services/katehelloworld.desktop
%{tde_prefix}/share/services/katehtmltools.desktop
%{tde_prefix}/share/services/kateinsertcommand.desktop
%{tde_prefix}/share/services/katemake.desktop
%{tde_prefix}/share/services/katemodeline.desktop
%{tde_prefix}/share/services/kateopenheader.desktop
%{tde_prefix}/share/services/katepybrowse.desktop
%{tde_prefix}/share/services/katesnippets.desktop
%{tde_prefix}/share/services/katetabbarextension.desktop
%{tde_prefix}/share/services/katetextfilter.desktop
%{tde_prefix}/share/services/katexmlcheck.desktop
%{tde_prefix}/share/services/katexmltools.desktop
%{tde_prefix}/share/doc/tde/HTML/en/kate-plugins/
# katesort plugin
%{tde_prefix}/%{_lib}/trinity/katesortplugin.la
%{tde_prefix}/%{_lib}/trinity/katesortplugin.so
%{tde_prefix}/share/icons/hicolor/*/actions/katesort.png
%{tde_prefix}/share/services/katesort.desktop

##########

%package tdefile-plugins
Summary:	Trinity file dialog plugins for text files and folders
Group:		Applications/Utilities

Obsoletes:	trinity-tdeaddons-kfile-plugins < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-tdeaddons-kfile-plugins = %{?epoch:%{epoch}:}%{version}-%{release}

%description tdefile-plugins
This is a collection of plugins for the TDE file dialog.  These plugins
extend the file dialog to offer advanced meta-information for text,
HTML and desktop files, as well as for folders, Windows .lnk files,
MIME archives and X.509 certificates.

This package also includes plugins for the KDE file rename dialog,
allowing a user to more easily decide what to do when faced with a
decision regarding conflicting filenames.  Rename dialog plugins are
provided for audio and image files.

%files tdefile-plugins
%defattr(-,root,root,-)
%doc tdefile-plugins/lnk/README
%{tde_prefix}/bin/lnkforward
%{tde_prefix}/%{_lib}/trinity/tdefile_cert.la
%{tde_prefix}/%{_lib}/trinity/tdefile_cert.so
%{tde_prefix}/%{_lib}/trinity/tdefile_desktop.la
%{tde_prefix}/%{_lib}/trinity/tdefile_desktop.so
%{tde_prefix}/%{_lib}/trinity/tdefile_folder.la
%{tde_prefix}/%{_lib}/trinity/tdefile_folder.so
%{tde_prefix}/%{_lib}/trinity/tdefile_html.la
%{tde_prefix}/%{_lib}/trinity/tdefile_html.so
%{tde_prefix}/%{_lib}/trinity/tdefile_lnk.la
%{tde_prefix}/%{_lib}/trinity/tdefile_lnk.so
%{tde_prefix}/%{_lib}/trinity/tdefile_mhtml.la
%{tde_prefix}/%{_lib}/trinity/tdefile_mhtml.so
%{tde_prefix}/%{_lib}/trinity/tdefile_txt.la
%{tde_prefix}/%{_lib}/trinity/tdefile_txt.so
%{tde_prefix}/%{_lib}/trinity/librenaudioplugin.la
%{tde_prefix}/%{_lib}/trinity/librenaudioplugin.so
%{tde_prefix}/%{_lib}/trinity/librenimageplugin.la
%{tde_prefix}/%{_lib}/trinity/librenimageplugin.so
%{tde_prefix}/share/applnk/.hidden/lnkforward.desktop
%{tde_prefix}/share/mimelnk/application/x-win-lnk.desktop
%{tde_prefix}/share/services/tdefile_cert.desktop
%{tde_prefix}/share/services/tdefile_desktop.desktop
%{tde_prefix}/share/services/tdefile_folder.desktop
%{tde_prefix}/share/services/tdefile_html.desktop
%{tde_prefix}/share/services/tdefile_lnk.desktop
%{tde_prefix}/share/services/tdefile_mhtml.desktop
%{tde_prefix}/share/services/tdefile_txt.desktop
%{tde_prefix}/share/services/renaudiodlg.desktop
%{tde_prefix}/share/services/renimagedlg.desktop
%{tde_prefix}/share/man/man1/lnkforward.1*

##########

%package -n trinity-kicker-applets
Summary:	Applets for Kicker, the Trinity panel
Group:		Applications/Utilities
Requires:	trinity-kicker

%description -n trinity-kicker-applets
This package contains a variety of applets for Kicker, the KDE panel.
These applets will appear in the panel's Add--Applet menu.

Included are a system monitor, a colour picker, a media player controller,
a mathematical evaluator and a binary clock.

The media control applet does not support XMMS, as this would force all
kicker-applets users to install XMMS. If you want a kicker applet that
controls XMMS, install the xmms-kde-trinity package.

%files -n trinity-kicker-applets
%defattr(-,root,root,-)
%doc README 
%{tde_prefix}/%{_lib}/trinity/kolourpicker_panelapplet.la
%{tde_prefix}/%{_lib}/trinity/kolourpicker_panelapplet.so
%{tde_prefix}/%{_lib}/trinity/ktimemon_panelapplet.la
%{tde_prefix}/%{_lib}/trinity/ktimemon_panelapplet.so
%{tde_prefix}/%{_lib}/trinity/math_panelapplet.la
%{tde_prefix}/%{_lib}/trinity/math_panelapplet.so
%{tde_prefix}/%{_lib}/trinity/mediacontrol_panelapplet.la
%{tde_prefix}/%{_lib}/trinity/mediacontrol_panelapplet.so
%{tde_prefix}/%{_lib}/trinity/kbinaryclock_panelapplet.la
%{tde_prefix}/%{_lib}/trinity/kbinaryclock_panelapplet.so
%{tde_prefix}/share/apps/kicker/applets
%{tde_prefix}/share/apps/mediacontrol
%{tde_prefix}/share/config.kcfg/kbinaryclock.kcfg
%{tde_prefix}/share/icons/locolor/*/apps/ktimemon.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/ktimemon.png
%{tde_prefix}/share/doc/tde/HTML/en/kicker-applets/

##########

%package -n trinity-knewsticker-scripts
Summary: scripts for KNewsTicker, the Trinity news ticker
Group:		Applications/Utilities
Requires:	perl
%if %{with python}
Requires:	%{python}
%endif
#Requires:	libfinance-quote-perl
#Requires:	libmime-perl
#Requires:	libnews-nntpclient-perl
Requires:	perl-libwww-perl
Requires:	trinity-knewsticker

%description -n trinity-knewsticker-scripts
This package contains a variety of scripts that provide additional news
sources for KNewsTicker, the news ticker applet for the TDE panel.

Highlights include newsgroup handling, stock data retrieval, sports scores
and various local news sources.

%files -n trinity-knewsticker-scripts
%defattr(-,root,root,-)
%doc README
%{tde_prefix}/share/apps/knewsticker/

##########

%package -n trinity-konq-plugins
Summary:	plugins for Konqueror, the Trinity file/web/doc browser
Group:		Applications/Utilities
Requires:	%{_lib}jpeg8
%if %{with python}
Requires:	%{python}
%endif
Requires:	rsync
#Requires:	unison
Requires:	trinity-konqueror

%description -n trinity-konq-plugins
This package contains a variety of useful plugins for Konqueror, the
file manager, web browser and document viewer for TDE.  Many of these
plugins will appear in Konqueror's Tools menu.

Highlights for web browsing include web page translation, web page archiving,
auto-refreshing, HTML and CSS structural analysis, a search toolbar, a
sidebar news ticker, fast access to common options, bookmarklets, a crash
monitor, a microformat availability indicator, a del.icio.us bookmarks
sidebar, and integration with the aKregator RSS feed reader.

Highlights for directory browsing include directory filters, image gallery
creation, archive compression and extraction, quick copy/move, a sidebar
media player, a file information metabar/sidebar, a media folder helper, a
graphical disk usage viewer and image conversions and transformations.

%files -n trinity-konq-plugins
%defattr(-,root,root,-)
%doc konq-plugins/README
%{_sysconfdir}/trinity/translaterc
%{tde_prefix}/bin/fsview
%{tde_prefix}/bin/jpegorient
%{tde_prefix}/%{_lib}/trinity/konq_sidebarnews.la
%{tde_prefix}/%{_lib}/trinity/konq_sidebarnews.so
%{tde_prefix}/%{_lib}/trinity/konqsidebar_delicious.la
%{tde_prefix}/%{_lib}/trinity/konqsidebar_delicious.so
%{tde_prefix}/%{_lib}/trinity/konqsidebar_mediaplayer.la
%{tde_prefix}/%{_lib}/trinity/konqsidebar_mediaplayer.so
%{tde_prefix}/%{_lib}/trinity/konqsidebar_metabar.la
%{tde_prefix}/%{_lib}/trinity/konqsidebar_metabar.so
%{tde_prefix}/%{_lib}/trinity/libakregatorkonqfeedicon.la
%{tde_prefix}/%{_lib}/trinity/libakregatorkonqfeedicon.so
%{tde_prefix}/%{_lib}/trinity/libakregatorkonqplugin.la
%{tde_prefix}/%{_lib}/trinity/libakregatorkonqplugin.so
%{tde_prefix}/%{_lib}/trinity/libarkplugin.la
%{tde_prefix}/%{_lib}/trinity/libarkplugin.so
%{tde_prefix}/%{_lib}/trinity/libautorefresh.la
%{tde_prefix}/%{_lib}/trinity/libautorefresh.so
%{tde_prefix}/%{_lib}/trinity/libbabelfishplugin.la
%{tde_prefix}/%{_lib}/trinity/libbabelfishplugin.so
%{tde_prefix}/%{_lib}/trinity/libcrashesplugin.la
%{tde_prefix}/%{_lib}/trinity/libcrashesplugin.so
%{tde_prefix}/%{_lib}/trinity/libdirfilterplugin.la
%{tde_prefix}/%{_lib}/trinity/libdirfilterplugin.so
%{tde_prefix}/%{_lib}/trinity/librsyncplugin.la
%{tde_prefix}/%{_lib}/trinity/librsyncplugin.so
%{tde_prefix}/%{_lib}/trinity/libdomtreeviewerplugin.la
%{tde_prefix}/%{_lib}/trinity/libdomtreeviewerplugin.so
%{tde_prefix}/%{_lib}/trinity/libfsviewpart.la
%{tde_prefix}/%{_lib}/trinity/libfsviewpart.so
%{tde_prefix}/%{_lib}/trinity/libtdehtmlsettingsplugin.la
%{tde_prefix}/%{_lib}/trinity/libtdehtmlsettingsplugin.so
%{tde_prefix}/%{_lib}/trinity/kcm_kuick.la
%{tde_prefix}/%{_lib}/trinity/kcm_kuick.so
%{tde_prefix}/%{_lib}/trinity/libkimgallery.la
%{tde_prefix}/%{_lib}/trinity/libkimgallery.so
%{tde_prefix}/%{_lib}/trinity/libkuickplugin.la
%{tde_prefix}/%{_lib}/trinity/libkuickplugin.so
%{tde_prefix}/%{_lib}/trinity/libmfkonqmficon.la
%{tde_prefix}/%{_lib}/trinity/libmfkonqmficon.so
%{tde_prefix}/%{_lib}/trinity/libminitoolsplugin.la
%{tde_prefix}/%{_lib}/trinity/libminitoolsplugin.so
%{tde_prefix}/%{_lib}/trinity/librellinksplugin.la
%{tde_prefix}/%{_lib}/trinity/librellinksplugin.so
%{tde_prefix}/%{_lib}/trinity/libsearchbarplugin.la
%{tde_prefix}/%{_lib}/trinity/libsearchbarplugin.so
%{tde_prefix}/%{_lib}/trinity/libuachangerplugin.la
%{tde_prefix}/%{_lib}/trinity/libuachangerplugin.so
%{tde_prefix}/%{_lib}/trinity/libvalidatorsplugin.la
%{tde_prefix}/%{_lib}/trinity/libvalidatorsplugin.so
%{tde_prefix}/%{_lib}/trinity/libwebarchiverplugin.la
%{tde_prefix}/%{_lib}/trinity/libwebarchiverplugin.so
%{tde_prefix}/%{_lib}/trinity/webarchivethumbnail.la
%{tde_prefix}/%{_lib}/trinity/webarchivethumbnail.so
%{tde_prefix}/share/applnk/.hidden/arkplugin.desktop
%{tde_prefix}/share/applnk/.hidden/kcmkuick.desktop
%{tde_prefix}/share/applnk/.hidden/kuickplugin.desktop
%{tde_prefix}/share/applnk/.hidden/mediaplayerplugin.desktop
%{tde_prefix}/share/applnk/.hidden/crashesplugin.desktop
%{tde_prefix}/share/applnk/.hidden/dirfilterplugin.desktop
%{tde_prefix}/share/applnk/.hidden/rsyncplugin.desktop
%{tde_prefix}/share/applnk/.hidden/fsview.desktop
%{tde_prefix}/share/applnk/.hidden/tdehtmlsettingsplugin.desktop
%{tde_prefix}/share/applnk/.hidden/kimgalleryplugin.desktop
%{tde_prefix}/share/applnk/.hidden/plugin_babelfish.desktop
%{tde_prefix}/share/applnk/.hidden/plugin_domtreeviewer.desktop
%{tde_prefix}/share/applnk/.hidden/plugin_validators.desktop
%{tde_prefix}/share/applnk/.hidden/plugin_webarchiver.desktop
%{tde_prefix}/share/applnk/.hidden/uachangerplugin.desktop
%{tde_prefix}/share/apps/akregator
%{tde_prefix}/share/apps/domtreeviewer
%{tde_prefix}/share/apps/fsview
%{tde_prefix}/share/apps/imagerotation/
%{tde_prefix}/share/apps/tdehtml/kpartplugins
%{tde_prefix}/share/apps/konqiconview
%{tde_prefix}/share/apps/konqlistview
%{tde_prefix}/share/apps/konqsidebartng
%{tde_prefix}/share/apps/konqueror/icons
%{tde_prefix}/share/apps/konqueror/kpartplugins
%{tde_prefix}/share/apps/konqueror/servicemenus
%{tde_prefix}/share/apps/metabar/
%{tde_prefix}/share/apps/microformat/
%{tde_prefix}/share/config.kcfg/konq_sidebarnews.kcfg
%{tde_prefix}/share/icons/crystalsvg/*/actions/babelfish.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/cssvalidator.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/domtreeviewer.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/htmlvalidator.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/imagegallery.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/remotesync.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/remotesyncconfig.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/minitools.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/validators.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/webarchiver.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/konqsidebar_delicious.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/konqsidebar_mediaplayer.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/konqsidebar_news.png
%{tde_prefix}/share/icons/hicolor/*/apps/metabar.png
%{tde_prefix}/share/icons/hicolor/*/apps/fsview.png
%{tde_prefix}/share/icons/hicolor/scalable/apps/metabar.svgz
%{tde_prefix}/share/icons/locolor/*/apps/autorefresh.png
%{tde_prefix}/share/icons/locolor/*/apps/konqsidebar_mediaplayer.png
%{tde_prefix}/share/services/akregator_konqplugin.desktop
%{tde_prefix}/share/services/ark_plugin.desktop
%{tde_prefix}/share/services/fsview_part.desktop
%{tde_prefix}/share/services/kuick_plugin.desktop
%{tde_prefix}/share/services/webarchivethumbnail.desktop
%{tde_prefix}/%{_lib}/trinity/libadblock.la
%{tde_prefix}/%{_lib}/trinity/libadblock.so
%{tde_prefix}/share/doc/tde/HTML/en/konq-plugins/
%{tde_prefix}/share/man/man1/exif.py.1*
%{tde_prefix}/share/man/man1/fsview.1*
%{tde_prefix}/share/man/man1/jpegorient.1*
%{tde_prefix}/share/man/man1/orient.py.1*

##########

%package -n trinity-ksig
Summary:	Graphical tool for managing multiple email signatures
Group:		Applications/Utilities
Requires:	trinity-kmail

%description -n trinity-ksig
KSig is a graphical tool for keeping track of many different email
signatures.  The signatures themselves can be edited through KSig's
graphical user interface.  A command-line interface is then available
for generating random or daily signatures from this list.

The command-line interface makes a suitable plugin for generating
signatures in external mail clients such as KMail.

%files -n trinity-ksig
%defattr(-,root,root,-)
%doc README
%{tde_prefix}/bin/ksig
%{tde_prefix}/share/applications/tde/ksig.desktop
%{tde_prefix}/share/apps/ksig/
%{tde_prefix}/share/icons/hicolor/*/apps/ksig.png
%{tde_prefix}/share/doc/tde/HTML/en/ksig/
%{tde_prefix}/share/man/man1/ksig.1*

##########

%package -n trinity-noatun-plugins
Summary:	plugins for Noatun, the Trinity media player
Group:		Applications/Utilities
Requires:	trinity-noatun

%description -n trinity-noatun-plugins
This package contains a variety of useful plugins for Noatun, the audio and
video media player for TDE. These plugins can be loaded through the plugin
manager in Noatun settings.

Highlights include an alarm clock, guessing tags from filenames, adjustable
playback speed, capture to wave file and displaying lyrics, plus a variety
of user interfaces, playlists and visualisation plugins.

%files -n trinity-noatun-plugins
%defattr(-,root,root,-)
%doc README
%{tde_prefix}/bin/noatunsynaescope.bin
%{tde_prefix}/bin/noatuntippecanoe.bin
%{tde_prefix}/bin/noatuntyler.bin
%{tde_prefix}/%{_lib}/trinity/noatunalsaplayer.la
%{tde_prefix}/%{_lib}/trinity/noatunalsaplayer.so
%{tde_prefix}/%{_lib}/trinity/noatunblurscope.la
%{tde_prefix}/%{_lib}/trinity/noatunblurscope.so
%{tde_prefix}/%{_lib}/trinity/noatuncharlatan.la
%{tde_prefix}/%{_lib}/trinity/noatuncharlatan.so
%{tde_prefix}/%{_lib}/trinity/noatundub.la
%{tde_prefix}/%{_lib}/trinity/noatundub.so
%{tde_prefix}/%{_lib}/trinity/noatun_ffrs.la
%{tde_prefix}/%{_lib}/trinity/noatun_ffrs.so
%{tde_prefix}/%{_lib}/trinity/noatunluckytag.la
%{tde_prefix}/%{_lib}/trinity/noatunluckytag.so
%{tde_prefix}/%{_lib}/trinity/noatunlyrics.la
%{tde_prefix}/%{_lib}/trinity/noatunlyrics.so
%{tde_prefix}/%{_lib}/trinity/noatunmadness.la
%{tde_prefix}/%{_lib}/trinity/noatunmadness.so
%if %{with db}
%{tde_prefix}/%{_lib}/trinity/noatun_oblique.la
%{tde_prefix}/%{_lib}/trinity/noatun_oblique.so
%endif
%{tde_prefix}/%{_lib}/trinity/noatunpitchablespeed.la
%{tde_prefix}/%{_lib}/trinity/noatunpitchablespeed.so
%{tde_prefix}/%{_lib}/trinity/noatunsynaescope.la
%{tde_prefix}/%{_lib}/trinity/noatunsynaescope.so
%{tde_prefix}/%{_lib}/trinity/noatuntippecanoe.la
%{tde_prefix}/%{_lib}/trinity/noatuntippecanoe.so
%{tde_prefix}/%{_lib}/trinity/noatuntyler.la
%{tde_prefix}/%{_lib}/trinity/noatuntyler.so
%{tde_prefix}/%{_lib}/trinity/noatunwakeup.la
%{tde_prefix}/%{_lib}/trinity/noatunwakeup.so
%{tde_prefix}/%{_lib}/trinity/noatunwavecapture.la
%{tde_prefix}/%{_lib}/trinity/noatunwavecapture.so
%{tde_prefix}/share/apps/noatun/*
%{tde_prefix}/share/icons/crystalsvg/16x16/apps/synaescope.png
%{tde_prefix}/share/man/man1/noatunsynaescope.bin.1*
%{tde_prefix}/share/man/man1/noatuntippecanoe.bin.1*
%{tde_prefix}/share/man/man1/noatuntyler.bin.1*


%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_prefix}/bin:${PATH}"
export PKG_CONFIG_PATH="%{tde_prefix}/%{_lib}/pkgconfig:${PKG_CONFIG_PATH}"

%if %{with db}
# Help cmake to find DB headers ...
if [ -d "/usr/include/db53" ]; then
  export CMAKE_INCLUDE_PATH="/usr/include/db53"
fi
if [ -d "/usr/include/db4" ]; then
  export CMAKE_INCLUDE_PATH="/usr/include/db4"
fi
%endif


%install -a
# Temporary
%__rm -rf %{?buildroot}%{tde_prefix}/share/doc/tde/HTML/en/khelpcenter

