Name:           ros-kinetic-tra1-moveit-config
Version:        1.0.10
Release:        0%{?dist}
Summary:        ROS tra1_moveit_config package

Group:          Development/Libraries
License:        BSD
URL:            http://moveit.ros.org/
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-joint-state-publisher
Requires:       ros-kinetic-joy
Requires:       ros-kinetic-moveit-fake-controller-manager
Requires:       ros-kinetic-moveit-kinematics
Requires:       ros-kinetic-moveit-planners-ompl
Requires:       ros-kinetic-moveit-ros-move-group
Requires:       ros-kinetic-moveit-ros-visualization
Requires:       ros-kinetic-moveit-ros-warehouse
Requires:       ros-kinetic-moveit-simple-controller-manager
Requires:       ros-kinetic-robot-state-publisher
Requires:       ros-kinetic-rviz
Requires:       ros-kinetic-tra1-description
Requires:       ros-kinetic-warehouse-ros
Requires:       ros-kinetic-xacro
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-roslaunch
BuildRequires:  ros-kinetic-rostest

%description
An automatically generated package with all the configuration and launch files
for using the tra1 with the MoveIt! Motion Planning Framework

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Sat Apr 28 2018 Ryosuke Tajima <ryosuke.tajima@opensource-robotics.tokyo.jp> - 1.0.10-0
- Autogenerated by Bloom

* Fri Mar 02 2018 Ryosuke Tajima <ryosuke.tajima@opensource-robotics.tokyo.jp> - 1.0.9-0
- Autogenerated by Bloom

* Mon Nov 06 2017 Ryosuke Tajima <ryosuke.tajima@opensource-robotics.tokyo.jp> - 1.0.7-1
- Autogenerated by Bloom

* Mon Nov 06 2017 Ryosuke Tajima <ryosuke.tajima@opensource-robotics.tokyo.jp> - 1.0.7-0
- Autogenerated by Bloom

* Wed Sep 20 2017 Ryosuke Tajima <ryosuke.tajima@opensource-robotics.tokyo.jp> - 1.0.6-0
- Autogenerated by Bloom

