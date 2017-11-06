Name:           ros-indigo-tra1-bringup
Version:        1.0.7
Release:        1%{?dist}
Summary:        ROS tra1_bringup package

Group:          Development/Libraries
License:        GPLv2
URL:            http://ros.org/wiki/tra1_bringup
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-controller-manager
Requires:       ros-indigo-joint-state-controller
Requires:       ros-indigo-joint-trajectory-controller
Requires:       ros-indigo-minas-control
Requires:       ros-indigo-position-controllers
Requires:       ros-indigo-robot-state-publisher
Requires:       ros-indigo-tf
Requires:       ros-indigo-tra1-description
Requires:       ros-indigo-tra1-moveit-config
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-roslaunch
BuildRequires:  ros-indigo-rostest

%description
Package contains bringup scripts/config/tools for tra1 robto

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

