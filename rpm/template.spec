Name:           ros-indigo-ethercat-manager
Version:        1.0.9
Release:        0%{?dist}
Summary:        ROS ethercat_manager package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/ethercat_manager
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-roscpp
Requires:       ros-indigo-soem
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-roslaunch
BuildRequires:  ros-indigo-rostest
BuildRequires:  ros-indigo-soem

%description
ROS-Industrial support stack for facilitating communication with EtherCAT
networks. The code is mainly copied from https://github.com/ros-
industrial/robotiq/blob/jade-devel/robotiq_ethercat/src/ethercat_manager.cpp

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
* Fri Mar 02 2018 Tokyo Opensource Robotics Kyokai (TORK) Developer Team <dev@opensource-robotics.tokyo.jp> - 1.0.9-0
- Autogenerated by Bloom

* Mon Nov 06 2017 Tokyo Opensource Robotics Kyokai (TORK) Developer Team <dev@opensource-robotics.tokyo.jp> - 1.0.7-1
- Autogenerated by Bloom

* Mon Nov 06 2017 Tokyo Opensource Robotics Kyokai (TORK) Developer Team <dev@opensource-robotics.tokyo.jp> - 1.0.7-0
- Autogenerated by Bloom

* Tue Sep 12 2017 Tokyo Opensource Robotics Kyokai (TORK) Developer Team <dev@opensource-robotics.tokyo.jp> - 1.0.6-0
- Autogenerated by Bloom

* Tue Sep 12 2017 Tokyo Opensource Robotics Kyokai (TORK) Developer Team <dev@opensource-robotics.tokyo.jp> - 1.0.5-0
- Autogenerated by Bloom

* Mon Sep 11 2017 Tokyo Opensource Robotics Kyokai (TORK) Developer Team <dev@opensource-robotics.tokyo.jp> - 1.0.4-0
- Autogenerated by Bloom

