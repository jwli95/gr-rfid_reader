# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.14

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /home/jiawei/Jetbrains/clion/bin/cmake/linux/bin/cmake

# The command to remove a file.
RM = /home/jiawei/Jetbrains/clion/bin/cmake/linux/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/jiawei/gr-rfid_reader

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/jiawei/gr-rfid_reader/cmake-build-debug

# Include any dependencies generated for this target.
include lib/CMakeFiles/test-rfid_reader.dir/depend.make

# Include the progress variables for this target.
include lib/CMakeFiles/test-rfid_reader.dir/progress.make

# Include the compile flags for this target's objects.
include lib/CMakeFiles/test-rfid_reader.dir/flags.make

lib/CMakeFiles/test-rfid_reader.dir/test_rfid_reader.cc.o: lib/CMakeFiles/test-rfid_reader.dir/flags.make
lib/CMakeFiles/test-rfid_reader.dir/test_rfid_reader.cc.o: ../lib/test_rfid_reader.cc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/jiawei/gr-rfid_reader/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object lib/CMakeFiles/test-rfid_reader.dir/test_rfid_reader.cc.o"
	cd /home/jiawei/gr-rfid_reader/cmake-build-debug/lib && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/test-rfid_reader.dir/test_rfid_reader.cc.o -c /home/jiawei/gr-rfid_reader/lib/test_rfid_reader.cc

lib/CMakeFiles/test-rfid_reader.dir/test_rfid_reader.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/test-rfid_reader.dir/test_rfid_reader.cc.i"
	cd /home/jiawei/gr-rfid_reader/cmake-build-debug/lib && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/jiawei/gr-rfid_reader/lib/test_rfid_reader.cc > CMakeFiles/test-rfid_reader.dir/test_rfid_reader.cc.i

lib/CMakeFiles/test-rfid_reader.dir/test_rfid_reader.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/test-rfid_reader.dir/test_rfid_reader.cc.s"
	cd /home/jiawei/gr-rfid_reader/cmake-build-debug/lib && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/jiawei/gr-rfid_reader/lib/test_rfid_reader.cc -o CMakeFiles/test-rfid_reader.dir/test_rfid_reader.cc.s

lib/CMakeFiles/test-rfid_reader.dir/qa_rfid_reader.cc.o: lib/CMakeFiles/test-rfid_reader.dir/flags.make
lib/CMakeFiles/test-rfid_reader.dir/qa_rfid_reader.cc.o: ../lib/qa_rfid_reader.cc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/jiawei/gr-rfid_reader/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object lib/CMakeFiles/test-rfid_reader.dir/qa_rfid_reader.cc.o"
	cd /home/jiawei/gr-rfid_reader/cmake-build-debug/lib && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/test-rfid_reader.dir/qa_rfid_reader.cc.o -c /home/jiawei/gr-rfid_reader/lib/qa_rfid_reader.cc

lib/CMakeFiles/test-rfid_reader.dir/qa_rfid_reader.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/test-rfid_reader.dir/qa_rfid_reader.cc.i"
	cd /home/jiawei/gr-rfid_reader/cmake-build-debug/lib && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/jiawei/gr-rfid_reader/lib/qa_rfid_reader.cc > CMakeFiles/test-rfid_reader.dir/qa_rfid_reader.cc.i

lib/CMakeFiles/test-rfid_reader.dir/qa_rfid_reader.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/test-rfid_reader.dir/qa_rfid_reader.cc.s"
	cd /home/jiawei/gr-rfid_reader/cmake-build-debug/lib && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/jiawei/gr-rfid_reader/lib/qa_rfid_reader.cc -o CMakeFiles/test-rfid_reader.dir/qa_rfid_reader.cc.s

# Object files for target test-rfid_reader
test__rfid_reader_OBJECTS = \
"CMakeFiles/test-rfid_reader.dir/test_rfid_reader.cc.o" \
"CMakeFiles/test-rfid_reader.dir/qa_rfid_reader.cc.o"

# External object files for target test-rfid_reader
test__rfid_reader_EXTERNAL_OBJECTS =

lib/test-rfid_reader: lib/CMakeFiles/test-rfid_reader.dir/test_rfid_reader.cc.o
lib/test-rfid_reader: lib/CMakeFiles/test-rfid_reader.dir/qa_rfid_reader.cc.o
lib/test-rfid_reader: lib/CMakeFiles/test-rfid_reader.dir/build.make
lib/test-rfid_reader: /usr/local/lib/libgnuradio-runtime.so
lib/test-rfid_reader: /usr/local/lib/libgnuradio-pmt.so
lib/test-rfid_reader: /usr/lib/x86_64-linux-gnu/libboost_filesystem.so
lib/test-rfid_reader: /usr/lib/x86_64-linux-gnu/libboost_system.so
lib/test-rfid_reader: /usr/lib/x86_64-linux-gnu/libcppunit.so
lib/test-rfid_reader: lib/libgnuradio-rfid_reader-1.0.0git.so.0.0.0
lib/test-rfid_reader: /usr/local/lib/libgnuradio-runtime.so
lib/test-rfid_reader: /usr/local/lib/libgnuradio-pmt.so
lib/test-rfid_reader: /usr/lib/x86_64-linux-gnu/libboost_filesystem.so
lib/test-rfid_reader: /usr/lib/x86_64-linux-gnu/libboost_system.so
lib/test-rfid_reader: lib/CMakeFiles/test-rfid_reader.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/jiawei/gr-rfid_reader/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX executable test-rfid_reader"
	cd /home/jiawei/gr-rfid_reader/cmake-build-debug/lib && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/test-rfid_reader.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
lib/CMakeFiles/test-rfid_reader.dir/build: lib/test-rfid_reader

.PHONY : lib/CMakeFiles/test-rfid_reader.dir/build

lib/CMakeFiles/test-rfid_reader.dir/clean:
	cd /home/jiawei/gr-rfid_reader/cmake-build-debug/lib && $(CMAKE_COMMAND) -P CMakeFiles/test-rfid_reader.dir/cmake_clean.cmake
.PHONY : lib/CMakeFiles/test-rfid_reader.dir/clean

lib/CMakeFiles/test-rfid_reader.dir/depend:
	cd /home/jiawei/gr-rfid_reader/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/jiawei/gr-rfid_reader /home/jiawei/gr-rfid_reader/lib /home/jiawei/gr-rfid_reader/cmake-build-debug /home/jiawei/gr-rfid_reader/cmake-build-debug/lib /home/jiawei/gr-rfid_reader/cmake-build-debug/lib/CMakeFiles/test-rfid_reader.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : lib/CMakeFiles/test-rfid_reader.dir/depend

