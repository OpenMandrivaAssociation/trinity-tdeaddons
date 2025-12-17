%bcond clang 1
%bcond gamin 1
%bcond db 0
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
%define tde_bindir %{tde_prefix}/bin
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_mandir %{tde_datadir}/man
%define tde_tdeappdir %{tde_datadir}/applications/tde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

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

#Vendor:		Trinity Project
#Packager:	Francois Andriot <francois.andriot@free.fr>

Obsoletes:	trinity-kdeaddons < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdeaddons = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	trinity-kdeaddons-extras < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdeaddons-extras = %{?epoch:%{epoch}:}%{version}-%{release}

Prefix:    %{tde_prefix}

Source0:	https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/core/%{tarball_name}-%{version}%{?preversion:~%{preversion}}.tar.xz

BuildSystem:    cmake
BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_SKIP_RPATH=OFF
BuildOption:    -DCMAKE_SKIP_INSTALL_RPATH=OFF
BuildOption:    -DCMAKE_BUILD_WITH_INSTALL_RPATH=ON
BuildOption:    -DCMAKE_INSTALL_RPATH="%{tde_libdir}"
BuildOption:    -DCMAKE_INSTALL_PREFIX="%{tde_prefix}"
BuildOption:    -DBIN_INSTALL_DIR="%{tde_bindir}"
BuildOption:    -DDOC_INSTALL_DIR="%{tde_docdir}"
BuildOption:    -DINCLUDE_INSTALL_DIR="%{tde_tdeincludedir}"
BuildOption:    -DLIB_INSTALL_DIR="%{tde_libdir}"
BuildOption:    -DPKGCONFIG_INSTALL_DIR="%{tde_libdir}/pkgconfig"
BuildOption:    -DSYSCONF_INSTALL_DIR="%{_sysconfdir}/trinity"
BuildOption:    -DSHARE_INSTALL_PREFIX="%{tde_datadir}"
BuildOption:    -DWITH_ALL_OPTIONS=ON -DWITH_ARTS=ON -DWITH_SDL=ON
BuildOption:    -DWITH_XMMS=OFF -DWITH_TEST=OFF -DBUILD_ALL=ON
BuildOption:    -DBUILD_ATLANTIKDESIGNER=ON -DBUILD_DOC=ON
BuildOption:    -DBUILD_KADDRESSBOOK_PLUGINS=ON -DBUILD_KATE_PLUGINS=ON
BuildOption:    -DBUILD_KICKER_APPLETS=ON -DBUILD_KNEWSTICKER_SCRIPTS=ON
BuildOption:    -DBUILD_KONQ_PLUGINS=ON -DBUILD_KSIG=ON -DBUILD_NOATUN_PLUGINS=ON
BuildOption:    -DBUILD_RENAMEDLG_PLUGINS=ON -DBUILD_TDEFILE_PLUGINS=ON
BuildOption:    -DBUILD_TUTORIALS=OFF
%{!?with_db:BuildOption:    -DWITH_BERKELEY_DB=OFF}
  
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
%{?with_db:BuildRequires:	db-devel}

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
%{tde_bindir}/atlantikdesigner
%{tde_datadir}/apps/atlantikdesigner
%{tde_tdeappdir}/atlantikdesigner.desktop
%{tde_datadir}/icons/hicolor/*/apps/atlantikdesigner.png
%{tde_tdedocdir}/HTML/en/atlantikdesigner/
%{tde_mandir}/man1/atlantikdesigner.1*

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
%{tde_tdelibdir}/libkaddrbk_geo_xxport.la
%{tde_tdelibdir}/libkaddrbk_geo_xxport.so
%{tde_tdelibdir}/libkaddrbk_gmx_xxport.la
%{tde_tdelibdir}/libkaddrbk_gmx_xxport.so
%{tde_datadir}/apps/kaddressbook
%{tde_datadir}/services/kaddressbook

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
%{tde_tdelibdir}/katecppsymbolviewerplugin.la
%{tde_tdelibdir}/katecppsymbolviewerplugin.so
%{tde_tdelibdir}/katefiletemplates.la
%{tde_tdelibdir}/katefiletemplates.so
%{tde_tdelibdir}/katefll_plugin.la
%{tde_tdelibdir}/katefll_plugin.so
%{tde_tdelibdir}/katehelloworldplugin.la
%{tde_tdelibdir}/katehelloworldplugin.so
%{tde_tdelibdir}/katehtmltoolsplugin.la
%{tde_tdelibdir}/katehtmltoolsplugin.so
%{tde_tdelibdir}/kateinsertcommandplugin.la
%{tde_tdelibdir}/kateinsertcommandplugin.so
%{tde_tdelibdir}/katemakeplugin.la
%{tde_tdelibdir}/katemakeplugin.so
%{tde_tdelibdir}/katemodelineplugin.la
%{tde_tdelibdir}/katemodelineplugin.so
%{tde_tdelibdir}/kateopenheaderplugin.la
%{tde_tdelibdir}/kateopenheaderplugin.so
%{tde_tdelibdir}/katepybrowseplugin.la
%{tde_tdelibdir}/katepybrowseplugin.so
%{tde_tdelibdir}/katesnippetsplugin.la
%{tde_tdelibdir}/katesnippetsplugin.so
%{tde_tdelibdir}/katetextfilterplugin.la
%{tde_tdelibdir}/katetextfilterplugin.so
%{tde_tdelibdir}/katexmlcheckplugin.la
%{tde_tdelibdir}/katexmlcheckplugin.so
%{tde_tdelibdir}/katexmltoolsplugin.la
%{tde_tdelibdir}/katexmltoolsplugin.so
%{tde_tdelibdir}/libkatetabbarextensionplugin.la
%{tde_tdelibdir}/libkatetabbarextensionplugin.so
%{tde_datadir}/applnk/.hidden/kate-plugins.desktop
%{tde_datadir}/applnk/.hidden/katefll.desktop
%{tde_datadir}/apps/kate
%{tde_datadir}/apps/katepart
%{tde_datadir}/apps/katexmltools
%{tde_datadir}/services/katecppsymbolviewer.desktop
%{tde_datadir}/services/katefiletemplates.desktop
%{tde_datadir}/services/katefll_plugin.desktop
%{tde_datadir}/services/katehelloworld.desktop
%{tde_datadir}/services/katehtmltools.desktop
%{tde_datadir}/services/kateinsertcommand.desktop
%{tde_datadir}/services/katemake.desktop
%{tde_datadir}/services/katemodeline.desktop
%{tde_datadir}/services/kateopenheader.desktop
%{tde_datadir}/services/katepybrowse.desktop
%{tde_datadir}/services/katesnippets.desktop
%{tde_datadir}/services/katetabbarextension.desktop
%{tde_datadir}/services/katetextfilter.desktop
%{tde_datadir}/services/katexmlcheck.desktop
%{tde_datadir}/services/katexmltools.desktop
%{tde_tdedocdir}/HTML/en/kate-plugins/
# katesort plugin
%{tde_tdelibdir}/katesortplugin.la
%{tde_tdelibdir}/katesortplugin.so
%{tde_datadir}/icons/hicolor/*/actions/katesort.png
%{tde_datadir}/services/katesort.desktop

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
%{tde_bindir}/lnkforward
%{tde_tdelibdir}/tdefile_cert.la
%{tde_tdelibdir}/tdefile_cert.so
%{tde_tdelibdir}/tdefile_desktop.la
%{tde_tdelibdir}/tdefile_desktop.so
%{tde_tdelibdir}/tdefile_folder.la
%{tde_tdelibdir}/tdefile_folder.so
%{tde_tdelibdir}/tdefile_html.la
%{tde_tdelibdir}/tdefile_html.so
%{tde_tdelibdir}/tdefile_lnk.la
%{tde_tdelibdir}/tdefile_lnk.so
%{tde_tdelibdir}/tdefile_mhtml.la
%{tde_tdelibdir}/tdefile_mhtml.so
%{tde_tdelibdir}/tdefile_txt.la
%{tde_tdelibdir}/tdefile_txt.so
%{tde_tdelibdir}/librenaudioplugin.la
%{tde_tdelibdir}/librenaudioplugin.so
%{tde_tdelibdir}/librenimageplugin.la
%{tde_tdelibdir}/librenimageplugin.so
%{tde_datadir}/applnk/.hidden/lnkforward.desktop
%{tde_datadir}/mimelnk/application/x-win-lnk.desktop
%{tde_datadir}/services/tdefile_cert.desktop
%{tde_datadir}/services/tdefile_desktop.desktop
%{tde_datadir}/services/tdefile_folder.desktop
%{tde_datadir}/services/tdefile_html.desktop
%{tde_datadir}/services/tdefile_lnk.desktop
%{tde_datadir}/services/tdefile_mhtml.desktop
%{tde_datadir}/services/tdefile_txt.desktop
%{tde_datadir}/services/renaudiodlg.desktop
%{tde_datadir}/services/renimagedlg.desktop
%{tde_mandir}/man1/lnkforward.1*

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
%{tde_tdelibdir}/kolourpicker_panelapplet.la
%{tde_tdelibdir}/kolourpicker_panelapplet.so
%{tde_tdelibdir}/ktimemon_panelapplet.la
%{tde_tdelibdir}/ktimemon_panelapplet.so
%{tde_tdelibdir}/math_panelapplet.la
%{tde_tdelibdir}/math_panelapplet.so
%{tde_tdelibdir}/mediacontrol_panelapplet.la
%{tde_tdelibdir}/mediacontrol_panelapplet.so
%{tde_tdelibdir}/kbinaryclock_panelapplet.la
%{tde_tdelibdir}/kbinaryclock_panelapplet.so
%{tde_datadir}/apps/kicker/applets
%{tde_datadir}/apps/mediacontrol
%{tde_datadir}/config.kcfg/kbinaryclock.kcfg
%{tde_datadir}/icons/locolor/*/apps/ktimemon.png
%{tde_datadir}/icons/crystalsvg/*/apps/ktimemon.png
%{tde_tdedocdir}/HTML/en/kicker-applets/

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
%{tde_datadir}/apps/knewsticker/

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
%{tde_bindir}/fsview
%{tde_bindir}/jpegorient
%{tde_tdelibdir}/konq_sidebarnews.la
%{tde_tdelibdir}/konq_sidebarnews.so
%{tde_tdelibdir}/konqsidebar_delicious.la
%{tde_tdelibdir}/konqsidebar_delicious.so
%{tde_tdelibdir}/konqsidebar_mediaplayer.la
%{tde_tdelibdir}/konqsidebar_mediaplayer.so
%{tde_tdelibdir}/konqsidebar_metabar.la
%{tde_tdelibdir}/konqsidebar_metabar.so
%{tde_tdelibdir}/libakregatorkonqfeedicon.la
%{tde_tdelibdir}/libakregatorkonqfeedicon.so
%{tde_tdelibdir}/libakregatorkonqplugin.la
%{tde_tdelibdir}/libakregatorkonqplugin.so
%{tde_tdelibdir}/libarkplugin.la
%{tde_tdelibdir}/libarkplugin.so
%{tde_tdelibdir}/libautorefresh.la
%{tde_tdelibdir}/libautorefresh.so
%{tde_tdelibdir}/libbabelfishplugin.la
%{tde_tdelibdir}/libbabelfishplugin.so
%{tde_tdelibdir}/libcrashesplugin.la
%{tde_tdelibdir}/libcrashesplugin.so
%{tde_tdelibdir}/libdirfilterplugin.la
%{tde_tdelibdir}/libdirfilterplugin.so
%{tde_tdelibdir}/librsyncplugin.la
%{tde_tdelibdir}/librsyncplugin.so
%{tde_tdelibdir}/libdomtreeviewerplugin.la
%{tde_tdelibdir}/libdomtreeviewerplugin.so
%{tde_tdelibdir}/libfsviewpart.la
%{tde_tdelibdir}/libfsviewpart.so
%{tde_tdelibdir}/libtdehtmlsettingsplugin.la
%{tde_tdelibdir}/libtdehtmlsettingsplugin.so
%{tde_tdelibdir}/kcm_kuick.la
%{tde_tdelibdir}/kcm_kuick.so
%{tde_tdelibdir}/libkimgallery.la
%{tde_tdelibdir}/libkimgallery.so
%{tde_tdelibdir}/libkuickplugin.la
%{tde_tdelibdir}/libkuickplugin.so
%{tde_tdelibdir}/libmfkonqmficon.la
%{tde_tdelibdir}/libmfkonqmficon.so
%{tde_tdelibdir}/libminitoolsplugin.la
%{tde_tdelibdir}/libminitoolsplugin.so
%{tde_tdelibdir}/librellinksplugin.la
%{tde_tdelibdir}/librellinksplugin.so
%{tde_tdelibdir}/libsearchbarplugin.la
%{tde_tdelibdir}/libsearchbarplugin.so
%{tde_tdelibdir}/libuachangerplugin.la
%{tde_tdelibdir}/libuachangerplugin.so
%{tde_tdelibdir}/libvalidatorsplugin.la
%{tde_tdelibdir}/libvalidatorsplugin.so
%{tde_tdelibdir}/libwebarchiverplugin.la
%{tde_tdelibdir}/libwebarchiverplugin.so
%{tde_tdelibdir}/webarchivethumbnail.la
%{tde_tdelibdir}/webarchivethumbnail.so
%{tde_datadir}/applnk/.hidden/arkplugin.desktop
%{tde_datadir}/applnk/.hidden/kcmkuick.desktop
%{tde_datadir}/applnk/.hidden/kuickplugin.desktop
%{tde_datadir}/applnk/.hidden/mediaplayerplugin.desktop
%{tde_datadir}/applnk/.hidden/crashesplugin.desktop
%{tde_datadir}/applnk/.hidden/dirfilterplugin.desktop
%{tde_datadir}/applnk/.hidden/rsyncplugin.desktop
%{tde_datadir}/applnk/.hidden/fsview.desktop
%{tde_datadir}/applnk/.hidden/tdehtmlsettingsplugin.desktop
%{tde_datadir}/applnk/.hidden/kimgalleryplugin.desktop
%{tde_datadir}/applnk/.hidden/plugin_babelfish.desktop
%{tde_datadir}/applnk/.hidden/plugin_domtreeviewer.desktop
%{tde_datadir}/applnk/.hidden/plugin_validators.desktop
%{tde_datadir}/applnk/.hidden/plugin_webarchiver.desktop
%{tde_datadir}/applnk/.hidden/uachangerplugin.desktop
%{tde_datadir}/apps/akregator
%{tde_datadir}/apps/domtreeviewer
%{tde_datadir}/apps/fsview
%{tde_datadir}/apps/imagerotation/
%{tde_datadir}/apps/tdehtml/kpartplugins
%{tde_datadir}/apps/konqiconview
%{tde_datadir}/apps/konqlistview
%{tde_datadir}/apps/konqsidebartng
%{tde_datadir}/apps/konqueror/icons
%{tde_datadir}/apps/konqueror/kpartplugins
%{tde_datadir}/apps/konqueror/servicemenus
%{tde_datadir}/apps/metabar/
%{tde_datadir}/apps/microformat/
%{tde_datadir}/config.kcfg/konq_sidebarnews.kcfg
%{tde_datadir}/icons/crystalsvg/*/actions/babelfish.png
%{tde_datadir}/icons/crystalsvg/*/actions/cssvalidator.png
%{tde_datadir}/icons/crystalsvg/*/actions/domtreeviewer.png
%{tde_datadir}/icons/crystalsvg/*/actions/htmlvalidator.png
%{tde_datadir}/icons/crystalsvg/*/actions/imagegallery.png
%{tde_datadir}/icons/crystalsvg/*/actions/remotesync.png
%{tde_datadir}/icons/crystalsvg/*/actions/remotesyncconfig.png
%{tde_datadir}/icons/crystalsvg/*/actions/minitools.png
%{tde_datadir}/icons/crystalsvg/*/actions/validators.png
%{tde_datadir}/icons/crystalsvg/*/actions/webarchiver.png
%{tde_datadir}/icons/crystalsvg/*/apps/konqsidebar_delicious.png
%{tde_datadir}/icons/crystalsvg/*/apps/konqsidebar_mediaplayer.png
%{tde_datadir}/icons/crystalsvg/*/apps/konqsidebar_news.png
%{tde_datadir}/icons/hicolor/*/apps/metabar.png
%{tde_datadir}/icons/hicolor/*/apps/fsview.png
%{tde_datadir}/icons/hicolor/scalable/apps/metabar.svgz
%{tde_datadir}/icons/locolor/*/apps/autorefresh.png
%{tde_datadir}/icons/locolor/*/apps/konqsidebar_mediaplayer.png
%{tde_datadir}/services/akregator_konqplugin.desktop
%{tde_datadir}/services/ark_plugin.desktop
%{tde_datadir}/services/fsview_part.desktop
%{tde_datadir}/services/kuick_plugin.desktop
%{tde_datadir}/services/webarchivethumbnail.desktop
%{tde_tdelibdir}/libadblock.la
%{tde_tdelibdir}/libadblock.so
%{tde_tdedocdir}/HTML/en/konq-plugins/
%{tde_mandir}/man1/exif.py.1*
%{tde_mandir}/man1/fsview.1*
%{tde_mandir}/man1/jpegorient.1*
%{tde_mandir}/man1/orient.py.1*

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
%{tde_bindir}/ksig
%{tde_tdeappdir}/ksig.desktop
%{tde_datadir}/apps/ksig/
%{tde_datadir}/icons/hicolor/*/apps/ksig.png
%{tde_tdedocdir}/HTML/en/ksig/
%{tde_mandir}/man1/ksig.1*

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
%{tde_bindir}/noatunsynaescope.bin
%{tde_bindir}/noatuntippecanoe.bin
%{tde_bindir}/noatuntyler.bin
%{tde_tdelibdir}/noatunalsaplayer.la
%{tde_tdelibdir}/noatunalsaplayer.so
%{tde_tdelibdir}/noatunblurscope.la
%{tde_tdelibdir}/noatunblurscope.so
%{tde_tdelibdir}/noatuncharlatan.la
%{tde_tdelibdir}/noatuncharlatan.so
%{tde_tdelibdir}/noatundub.la
%{tde_tdelibdir}/noatundub.so
%{tde_tdelibdir}/noatun_ffrs.la
%{tde_tdelibdir}/noatun_ffrs.so
%{tde_tdelibdir}/noatunluckytag.la
%{tde_tdelibdir}/noatunluckytag.so
%{tde_tdelibdir}/noatunlyrics.la
%{tde_tdelibdir}/noatunlyrics.so
%{tde_tdelibdir}/noatunmadness.la
%{tde_tdelibdir}/noatunmadness.so
%if %{with db}
%{tde_tdelibdir}/noatun_oblique.la
%{tde_tdelibdir}/noatun_oblique.so
%endif
%{tde_tdelibdir}/noatunpitchablespeed.la
%{tde_tdelibdir}/noatunpitchablespeed.so
%{tde_tdelibdir}/noatunsynaescope.la
%{tde_tdelibdir}/noatunsynaescope.so
%{tde_tdelibdir}/noatuntippecanoe.la
%{tde_tdelibdir}/noatuntippecanoe.so
%{tde_tdelibdir}/noatuntyler.la
%{tde_tdelibdir}/noatuntyler.so
%{tde_tdelibdir}/noatunwakeup.la
%{tde_tdelibdir}/noatunwakeup.so
%{tde_tdelibdir}/noatunwavecapture.la
%{tde_tdelibdir}/noatunwavecapture.so
%{tde_datadir}/apps/noatun/*
%{tde_datadir}/icons/crystalsvg/16x16/apps/synaescope.png
%{tde_mandir}/man1/noatunsynaescope.bin.1*
%{tde_mandir}/man1/noatuntippecanoe.bin.1*
%{tde_mandir}/man1/noatuntyler.bin.1*


%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig:${PKG_CONFIG_PATH}"

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
%__rm -rf %{?buildroot}%{tde_tdedocdir}/HTML/en/khelpcenter

