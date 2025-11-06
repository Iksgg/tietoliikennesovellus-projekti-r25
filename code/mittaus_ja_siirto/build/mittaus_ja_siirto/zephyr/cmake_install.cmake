# Install script for directory: C:/ncs/v3.1.1/zephyr

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "C:/Program Files (x86)/Zephyr-Kernel")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "TRUE")
endif()

# Set default install directory permissions.
if(NOT DEFINED CMAKE_OBJDUMP)
  set(CMAKE_OBJDUMP "C:/ncs/toolchains/c1a76fddb2/opt/zephyr-sdk/arm-zephyr-eabi/bin/arm-zephyr-eabi-objdump.exe")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/tietoliikennesovellus-projekti-r25/code/mittaus_ja_siirto/build/mittaus_ja_siirto/zephyr/arch/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/tietoliikennesovellus-projekti-r25/code/mittaus_ja_siirto/build/mittaus_ja_siirto/zephyr/lib/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/tietoliikennesovellus-projekti-r25/code/mittaus_ja_siirto/build/mittaus_ja_siirto/zephyr/soc/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/tietoliikennesovellus-projekti-r25/code/mittaus_ja_siirto/build/mittaus_ja_siirto/zephyr/boards/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/tietoliikennesovellus-projekti-r25/code/mittaus_ja_siirto/build/mittaus_ja_siirto/zephyr/subsys/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/tietoliikennesovellus-projekti-r25/code/mittaus_ja_siirto/build/mittaus_ja_siirto/zephyr/drivers/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/tietoliikennesovellus-projekti-r25/code/mittaus_ja_siirto/build/mittaus_ja_siirto/modules/nrf/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/tietoliikennesovellus-projekti-r25/code/mittaus_ja_siirto/build/mittaus_ja_siirto/modules/hostap/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/tietoliikennesovellus-projekti-r25/code/mittaus_ja_siirto/build/mittaus_ja_siirto/modules/mcuboot/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/tietoliikennesovellus-projekti-r25/code/mittaus_ja_siirto/build/mittaus_ja_siirto/modules/mbedtls/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/tietoliikennesovellus-projekti-r25/code/mittaus_ja_siirto/build/mittaus_ja_siirto/modules/trusted-firmware-m/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/tietoliikennesovellus-projekti-r25/code/mittaus_ja_siirto/build/mittaus_ja_siirto/modules/cjson/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/tietoliikennesovellus-projekti-r25/code/mittaus_ja_siirto/build/mittaus_ja_siirto/modules/azure-sdk-for-c/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/tietoliikennesovellus-projekti-r25/code/mittaus_ja_siirto/build/mittaus_ja_siirto/modules/cirrus-logic/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/tietoliikennesovellus-projekti-r25/code/mittaus_ja_siirto/build/mittaus_ja_siirto/modules/openthread/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/tietoliikennesovellus-projekti-r25/code/mittaus_ja_siirto/build/mittaus_ja_siirto/modules/memfault-firmware-sdk/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/tietoliikennesovellus-projekti-r25/code/mittaus_ja_siirto/build/mittaus_ja_siirto/modules/canopennode/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/tietoliikennesovellus-projekti-r25/code/mittaus_ja_siirto/build/mittaus_ja_siirto/modules/chre/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/tietoliikennesovellus-projekti-r25/code/mittaus_ja_siirto/build/mittaus_ja_siirto/modules/lz4/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/tietoliikennesovellus-projekti-r25/code/mittaus_ja_siirto/build/mittaus_ja_siirto/modules/nanopb/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/tietoliikennesovellus-projekti-r25/code/mittaus_ja_siirto/build/mittaus_ja_siirto/modules/zscilib/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/tietoliikennesovellus-projekti-r25/code/mittaus_ja_siirto/build/mittaus_ja_siirto/modules/cmsis/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/tietoliikennesovellus-projekti-r25/code/mittaus_ja_siirto/build/mittaus_ja_siirto/modules/cmsis-dsp/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/tietoliikennesovellus-projekti-r25/code/mittaus_ja_siirto/build/mittaus_ja_siirto/modules/cmsis-nn/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/tietoliikennesovellus-projekti-r25/code/mittaus_ja_siirto/build/mittaus_ja_siirto/modules/cmsis_6/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/tietoliikennesovellus-projekti-r25/code/mittaus_ja_siirto/build/mittaus_ja_siirto/modules/fatfs/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/tietoliikennesovellus-projekti-r25/code/mittaus_ja_siirto/build/mittaus_ja_siirto/modules/hal_nordic/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/tietoliikennesovellus-projekti-r25/code/mittaus_ja_siirto/build/mittaus_ja_siirto/modules/hal_st/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/tietoliikennesovellus-projekti-r25/code/mittaus_ja_siirto/build/mittaus_ja_siirto/modules/hal_tdk/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/tietoliikennesovellus-projekti-r25/code/mittaus_ja_siirto/build/mittaus_ja_siirto/modules/hal_wurthelektronik/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/tietoliikennesovellus-projekti-r25/code/mittaus_ja_siirto/build/mittaus_ja_siirto/modules/liblc3/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/tietoliikennesovellus-projekti-r25/code/mittaus_ja_siirto/build/mittaus_ja_siirto/modules/libmetal/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/tietoliikennesovellus-projekti-r25/code/mittaus_ja_siirto/build/mittaus_ja_siirto/modules/littlefs/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/tietoliikennesovellus-projekti-r25/code/mittaus_ja_siirto/build/mittaus_ja_siirto/modules/loramac-node/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/tietoliikennesovellus-projekti-r25/code/mittaus_ja_siirto/build/mittaus_ja_siirto/modules/lvgl/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/tietoliikennesovellus-projekti-r25/code/mittaus_ja_siirto/build/mittaus_ja_siirto/modules/mipi-sys-t/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/tietoliikennesovellus-projekti-r25/code/mittaus_ja_siirto/build/mittaus_ja_siirto/modules/nrf_wifi/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/tietoliikennesovellus-projekti-r25/code/mittaus_ja_siirto/build/mittaus_ja_siirto/modules/open-amp/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/tietoliikennesovellus-projekti-r25/code/mittaus_ja_siirto/build/mittaus_ja_siirto/modules/percepio/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/tietoliikennesovellus-projekti-r25/code/mittaus_ja_siirto/build/mittaus_ja_siirto/modules/picolibc/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/tietoliikennesovellus-projekti-r25/code/mittaus_ja_siirto/build/mittaus_ja_siirto/modules/segger/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/tietoliikennesovellus-projekti-r25/code/mittaus_ja_siirto/build/mittaus_ja_siirto/modules/tinycrypt/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/tietoliikennesovellus-projekti-r25/code/mittaus_ja_siirto/build/mittaus_ja_siirto/modules/uoscore-uedhoc/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/tietoliikennesovellus-projekti-r25/code/mittaus_ja_siirto/build/mittaus_ja_siirto/modules/zcbor/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/tietoliikennesovellus-projekti-r25/code/mittaus_ja_siirto/build/mittaus_ja_siirto/modules/nrfxlib/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/tietoliikennesovellus-projekti-r25/code/mittaus_ja_siirto/build/mittaus_ja_siirto/modules/nrf_hw_models/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/tietoliikennesovellus-projekti-r25/code/mittaus_ja_siirto/build/mittaus_ja_siirto/modules/connectedhomeip/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/tietoliikennesovellus-projekti-r25/code/mittaus_ja_siirto/build/mittaus_ja_siirto/zephyr/kernel/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/tietoliikennesovellus-projekti-r25/code/mittaus_ja_siirto/build/mittaus_ja_siirto/zephyr/cmake/flash/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/tietoliikennesovellus-projekti-r25/code/mittaus_ja_siirto/build/mittaus_ja_siirto/zephyr/cmake/usage/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/tietoliikennesovellus-projekti-r25/code/mittaus_ja_siirto/build/mittaus_ja_siirto/zephyr/cmake/reports/cmake_install.cmake")
endif()

