cmake_minimum_required(VERSION 3.16)
project(vksample)

set(CMAKE_CXX_STANDARD 17)

set(SOURCE_FILES src/main.cpp)

add_executable(vksample ${SOURCE_FILES})

include_directories(include)

find_library(vulkan vulkan)
find_library(glfw glfw)
find_library(X11 X11)
find_library(Xxf86vm Xxf86vm)
find_library(Xrandr Xrandr)
find_library(Xi Xi)
find_library(m m)
find_library(pthread pthread)

target_link_libraries(vksample LINK_PUBLIC vulkan X11 Xxf86vm Xrandr Xi m pthread glfw ${CMAKE_DL_LIBS})
add_custom_command(TARGET vksample POST_BUILD COMMAND ${CMAKE_COMMAND} -E copy_directory ${CMAKE_SOURCE_DIR}/res $<TARGET_FILE_DIR:vksample>)
