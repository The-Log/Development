
cmake_minimum_required(VERSION 2.8)
project( cubeProjection )
find_package( OpenCV REQUIRED )
add_executable(cubeProjection cubeProjection.cpp )
target_link_libraries( cubeProjection ${OpenCV_LIBS} )
set(CMAKE_BUILD_TYPE Debug)
set(CMAKE_BUILD_TYPE RelWithDebInfo)
