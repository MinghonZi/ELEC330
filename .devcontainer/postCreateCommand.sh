sudo apt update && sudo apt install --yes --no-install-recommends curl wget git
NONINTERACTIVE=1 /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
echo '# Set PATH, MANPATH, etc., for Homebrew.' >> ~/.bashrc
echo 'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"' >> ~/.bashrc
eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"
brew install lazygit llvm gdb
catkin_make --directory /home/elec330/catkin_ws -DPYTHON_EXECUTABLE=/usr/bin/python3.8 -DCMAKE_EXPORT_COMPILE_COMMANDS=1