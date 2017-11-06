Name:           ros-indigo-minas-control
Version:        1.0.7
Release:        0%{?dist}
Summary:        ROS minas_control package

Group:          Development/Libraries
License:        GPLv2
URL:            http://ros.org/wiki/minas_control
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-controller-manager
Requires:       ros-indigo-diagnostic-updater
Requires:       ros-indigo-ethercat-manager
Requires:       ros-indigo-hardware-interface
Requires:       ros-indigo-joint-limits-interface
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-trajectory-msgs
Requires:       ros-indigo-transmission-interface
Requires:       tinyxml-devel
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-controller-manager
BuildRequires:  ros-indigo-diagnostic-updater
BuildRequires:  ros-indigo-ethercat-manager
BuildRequires:  ros-indigo-hardware-interface
BuildRequires:  ros-indigo-joint-limits-interface
BuildRequires:  ros-indigo-roslaunch
BuildRequires:  ros-indigo-rostest
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-soem
BuildRequires:  ros-indigo-trajectory-msgs
BuildRequires:  ros-indigo-transmission-interface
BuildRequires:  tinyxml-devel

%description
This package contains ros_control based robot controller for PANASONIC MINAS
EtherCAT Motor Driver Control System

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Nov 06 2017 Tokyo Opensource Robotics Kyokai (TORK) Developer Team <dev@opensource-robotics.tokyo.jp> - 1.0.7-0
- Autogenerated by Bloom

* Tue Sep 12 2017 Tokyo Opensource Robotics Kyokai (TORK) Developer Team <dev@opensource-robotics.tokyo.jp> - 1.0.6-0
- Autogenerated by Bloom

* Tue Sep 12 2017 Tokyo Opensource Robotics Kyokai (TORK) Developer Team <dev@opensource-robotics.tokyo.jp> - 1.0.5-0
- Autogenerated by Bloom

* Mon Sep 11 2017 Tokyo Opensource Robotics Kyokai (TORK) Developer Team <dev@opensource-robotics.tokyo.jp> - 1.0.4-0
- Autogenerated by Bloom

