# macOS PostgreSQL installation with Homebrew

## 1.0 Options

See the PostgreSQL [Downloads](https://www.postgresql.org/ftp/source/) page for acquiring and
installing platform-friendly PostgreSQL packages.

## 2.0 macOS Homebrew install

I do my development work on a Mac. I use [Homebrew](https://brew.sh/), a macOS package manager, to
acquire and maintain a number of software packages that I use on a daily basis, including
PostgreSQL and Python.

Before choosing the Homebrew route review the Homebrew installation
[requirements and options](https://docs.brew.sh/Installation). Quite likely, you will need to first
install the Command Line Tools (CLT) for Xcode.

## 3.0 Install Xcode</a>
[Xcode](https://developer.apple.com/xcode/) is Apple's integrated development environment (IDE).
Homebrew requires access to Xcode's developer tools.  First, open your Terminal and check if Xcode
is already installed:

```commandline
xcode-select -p
/Library/Developer/CommandLineTools
```

If no path value is returned, install Apple's Xcode package:

```commandline
xcode-select --install
```

Click your way through the confirmation screens and allow Xcode time to install (it's a large install).

:bulb: You can also obtain Xcode from the Apple App store (it's free).

## 4.0 Install Homebrew

Install Homebrew.

```commandline
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Confirm that the install was successful:

```commandline
brew --version
```

## 5.0 PATH environment variable

Homebrew stores its executables in `/usr/local/bin`. You _must_ add this path to your environment's
`PATH` variable in the _first_ position so that Homebrew package installs are called in place of
packages that come pre-installed with macOS like the easy-to-use command line interface (CLI)
[nano](https://www.nano-editor.org/) version 2.0.6 which is wildly out-of-date (latest nano version
is 5.7).

If you are using the Z shell (zsh) use nano to open the `.zshrc` file in your home directory:

```commandline
nano ~/.zshrc
```

:bulb: If you are still using the BASH shell (now retired in favor of zsh) edit the `.bash_profile`
file in your home directory:

```commandline
nano ~/.bash_profile
```

Add the following line to the bottom of the `.zshrc` (or `.bash_profile`) file:

```commandline\
# Homebrew executables directory listed first
export PATH=/usr/local/bin:$PATH
```

Save the updated file: `CTRL + letter 0`, then exit nano: `CTRL + letter X`.

Then use the `source` command to reload your environment variables:

```commandline
source ~/.zshrc
```

or

```commandline
source ~/.bash_profile
```

:bulb: You can confirm the `PATH` order of precedence with the `env` command:

```commandline
env
```

### 6.0 Install wget and nano packages (optional)

Prior to installing PostgreSQL I recommend installing the [wget](https://www.gnu.org/software/wget/)
package in order to exercise Homebrew. wget provides command line interface (CLI) file retrieval
using HTTP, HTTPS, FTP, and FTPS protocols.

```commandline
brew install wget
cd ~/Documents
wget https://www.pg4e.com/tools/sql/library.csv
```

:bulb: You can confirm location of wget using the `which` command:

```commandline
which wget

/usr/local/bin/wget
```

Although macOS comes pre-installed with [nano](https://www.nano-editor.org/), an easy to use command
line interface (CLI) text editor, I prefer to install and maintain it using Homebrew.

```commandline
brew install nano
```

:bulb: there are number of nano tutorial articles and videos available online. nano is a great CLI
text editor and I encourage you to get to know it.

You can check the "health" of your Homebrew install with the `doctor` command:

```commandline
brew doctor

Your system is ready to brew.
```

### 7.0 Install PostgreSQL

Now install PostgreSQL server and the command line console `psql`:

```commandline
brew install postgresql
```

Then execute the following command to run the server as a service:

```commandline
brew services start postgresql
```

:bulb: You can stop PostgreSQL with the following command:

```commandline
brew services stop postgresql
```

:bulb: Alternatively, you can create a `LaunchAgent` and `plist` to launch PostgreSQL on startup.
See the following [tutorial](https://chartio.com/resources/tutorials/how-to-start-postgresql-server-on-mac-os-x/)
or [gist](https://gist.github.com/ibraheem4/ce5ccd3e4d7a65589ce84f2a3b7c23a3) for instructions on
how to create PostgreSQL `LaunchAgents`.

### 8.0 Run psql

Local connection:

```commandline
psql postgres
```

pg.pg4e.com connection:

```commandline
psql -h pg.pg4e.com -p 5432 -U < username > < database >
```

:bulb: type "exit" and hit the return key to terminate `psql`.

Congratulations, you have installed PostgreSQL succesfully.

### 9.0 Install pgadmin4 and/or dbeaver-community (optional)

There is also a Homebrew cask [formula](https://formulae.brew.sh/cask/pgadmin4) available for
installing and maintaining `pgadmin4`:

```commandline
brew install --cask pgadmin4
```

There is also a Homeebrew cask [formula](https://formulae.brew.sh/cask/dbeaver-community) available
for [DBeaver](https://dbeaver.io/) community edition:

```commandline
brew install --cask dbeaver-community
```

## 10.0 Additional Homebrew commands

### 10.1 Return a list of installed packages

Run `brew list` to return a list of installed packages. Add the `--version` option to include the
versions installed:

```commandline
brew list --versions
```

### 10.2 Update formulas and upgrade packages

Run the following commands periodically (I do so every other day) in order to update formulas,
upgrade packages, confirm installs, and delete outdated packages.

```commandline
brew update
brew upgrade
brew doctor
brew cleanup
```

## 10.3 Additional info

Get to know Homebrew by having a look at the official [Homebrew Documentation](https://docs.brew.sh/).
Andr&eacute; Mar&eacute;'s [Homebrew - Basic Commands and Cheatsheet](https://dev.to/code2bits/homebrew---basics--cheatsheet-3a3n)
is also a useful read.

Run `brew help` in the terminal to retrieve a complete list of Homebrew commands:

```commandline
brew help

Example usage:
  brew search TEXT|/REGEX/
  brew info [FORMULA|CASK...]
  brew install FORMULA|CASK...
  brew update
  brew upgrade [FORMULA|CASK...]
  brew uninstall FORMULA|CASK...
  brew list [FORMULA|CASK...]

Troubleshooting:
  brew config
  brew doctor
  brew install --verbose --debug FORMULA|CASK

Contributing:
  brew create URL [--no-fetch]
  brew edit [FORMULA|CASK...]

Further help:
  brew commands
  brew help [COMMAND]
  man brew
  https://docs.brew.sh
```
