cmake_minimum_required(VERSION 3.6)
project(1_5_classes)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

set(SOURCE_FILES main.cpp)
add_executable(1_5_classes ${SOURCE_FILES})