cmake_minimum_required(VERSION 3.5)
project(phantomx_description)

find_package(ament_cmake REQUIRED)
find_package(urdf REQUIRED)
find_package(xacro REQUIRED)

install(DIRECTORY meshes urdf launch
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
