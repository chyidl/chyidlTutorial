#!/bin/bash
#----------------------------------------------
# INTERACTIVE REMOTE DATABASE DUMP SCRIPT
#----------------------------------------------
SCRIPT=${0##*/}
IFS=$'\n'
HISTFILE="$HOME/.remotedump.history"

# Use colors, but only if connected to a terminal, and that terminal supports them.
# tpu, reset - initialize a terminal or query terminfo database
if which tput >/dev/null 2>&1; then
  ncolors=$(tput colors)
fi

if [ -t 1 ] && [ -n "$ncolors" ] && [ "$ncolors" -ge 8 ]; then
  RED="$(tput setaf 1)"
  GREEN="$(tput setaf 2)"
  YELLOW="$(tput setaf 3)"
  BLUE="$(tput setaf 4)"
  BOLD="$(tput bold)"
  NORMAL="$(tput sgr0)"
else
  RED=""
  GREEN=""
  YELLOW=""
  BLUE=""
  BOLD=""
  NORMAL=""
fi

# Case-insensitive for regex matching
shopt -s nocasematch

# Prepare history mode
set -i
history -c
history -r

# Input method text
get_input()
{
  read -e -p "${BLUE}$1${NORMAL}" "$2"
  history -s "${!2}"
}

# Input method password
get_input_pw()
{
  read -s -p "${BLUE}$1${NORMAL}" "$2"
  history -s "${!2}"
}

# Echo in bold
echo_b()
{
  if [ "$1" = "-e" ]; then
    echo -e "${BOLD}$2${NORMAL}"
  else
    echo "${BOLD}$1${NORMAL}"
  fi
}

# Echo in colour
echo_c()
{
  case "$1" in
    red | r | -red | -r | --red | --r ) echo "${RED}$2${NORMAL}" ;;
    green | g | -green | -g | --green | --g ) echo "${GREEN}$2${NORMAL}" ;;
    blue | b | -blue | -b | --blue | --b ) echo "${BLUE}$2${NORMAL}" ;;
    yellow | y | -yellow | -y | --yellow | --y ) echo "${YELLOW}$2${NORMAL}" ;;
    * ) echo "$(BOLD)$2$(RESET)" ;;
  esac
}

# Get input data and save to history
save_input()
{
  if [[ ! -n "$local_dir" ]]; then
    while get_input "Local DB Directory > " local_dir; do
      case ${local_dir%% *} in
        * )
            if [ -n "$local_dir" ]; then
              break
            else
              continue
            fi
        ;;
      esac
    done
  fi
  if [[ ! -n "$remote_user" ]]; then
    while get_input "SSH Username > " remote_user; do
      case ${remote_user%% *} in
        * )
            if [ -n "$remote_user" ]; then
              break
            else
              continue
            fi
        ;;
      esac
    done
  fi
  if [[ ! -n "$remote_ip" ]]; then
    while get_input "SSH Aliases/IP-address > " remote_ip; do
      case ${remote_ip%% *} in
        * )
            if [ -n "$remote_ip" ]; then
              break
            else
              continue
            fi
        ;;
      esac
    done
  fi
  if [[ ! -n "$remote_dir" ]]; then
    while get_input "Remote Backup Directory > " local_dir; do
      case ${remote_dir%% *} in
        * )
            if [ -n "$remote_dir" ]; then
              break
            else
              continue
            fi
        ;;
      esac
    done
  fi
  if [[ ! -n "$db_user" ]]; then
    while get_input "DB Username > " local_dir; do
      case ${db_user%% *} in
        * )
            if [ -n "$db_user" ]; then
              break
            else
              continue
            fi
        ;;
      esac
    done
  fi
  if [[ ! -n "$db_password" ]]; then
    while get_input_pw "DB Password > " local_dir; do
      case ${db_password%% *} in
        * )
            if [ -n "$db_password" ]; then
              break
            else
              continue
            fi
        ;;
      esac
    done
  fi
  if [[ ! -n "$db_name" ]]; then
    while get_input "DB Name > " local_dir; do
      case ${db_name%% *} in
        * )
            if [ -n "$db_name" ]; then
              break
            else
              continue
            fi
        ;;
      esac
    done
  fi
}

change_pwd_rsync()
{
  ## CD INTO LOCAL WORKING DIRECTORY
  ## this is where I keep my local dump SQL files.
  ## the most recent one is always named dump.sql
  cd "$local_dir"
  
  ## RSYNC LATEST DUMP.SQL FILE TO REMOTE SERVER
  rsync -avzP dump.sql $remote_user@$remote_ip:$remote_dir
  wait
}

remote_dump()
{
  ## SSH INTO SERVER
  ssh $remote_user@$remote_ip /bin/bash << EOF
    echo "**************************";
    echo "** Connected to remote. **"
    echo "**************************";
    echo "";

    ## CD INTO REMOTE WORKING NON-PUBLIC DIRECTORY
    ## where the dump.sql file was rsynced to
    cd "$remote_dir"
    wait
    sleep 1
    
    ## RUN MYSQLDUMP COMMAND
    ## save the SQL with date stamp
    mysqldump --host=localhost --user=$db_user --password=$db_password $db_name > `date +%Y-%m-%d`.sql;
    echo "***************************************";
    echo "** `date +%Y-%m-%d`.SQL has been imported. **"
    echo "***************************************";
    echo "";
    wait
    sleep 1

    ## IMPORT DUMP.SQL COMMAND
    mysql --host=localhost --user=$db_user --password=$db_password $db_name < dump.sql;
    echo "*********************************";
    echo "** DUMP.SQL has been imported. **"
    echo "*********************************";
    echo "";
    wait
    sleep 1

    ## REMOVE DUMP.SQL FILE
    rm dump.sql
    echo "********************************";
    echo "** DUMP.SQL has been removed. **"
    echo "********************************";
    exit
  EOF
}

main()
{
  save_input
  change_pwd_rsync
  remote_dump
}

main