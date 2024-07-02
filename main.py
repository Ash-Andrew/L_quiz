import random
import tkinter as tk
from tkinter import messagebox


# All the questions from the provided list
questions = [
    {
        "type": "multiple_choice",
        "question": "A new server needs to be installed to host services for a period of several years. Throughout this time, the server should receive important security updates from its Linux distribution. Which of the following Linux distributions meet these requirements? (Choose two.)",
        "choices": ["Ubuntu Linux LTS", "Fedora Linux", "Debian GNU/Linux Unstable", "Ubuntu Linux non-LTS", "Red Hat Enterprise Linux"],
        "answer": "AE"
    },
    {
        "type": "multiple_choice",
        "question": "What happens to a file residing outside the home directory when the file owner's account is deleted? (Choose two.)",
        "choices": ["During a file system check, the file is moved to /lost +found.", "The file is removed from the file system.", "The UID of the former owner is shown when listing the file's details.", "The user root is set as the new owner of the file.", "Ownership and permissions of the file remain unchanged."],
        "answer": "CE"
    },
    {
        "type": "multiple_choice",
        "question": "Which of the following programs are web servers? (Choose two.)",
        "choices": ["Apache HTTPD", "Postfix", "Curl", "Dovecot", "NGINX"],
        "answer": "AE"
    },
    {
        "type": "multiple_choice",
        "question": "Reverse DNS assigns hostnames to IP addresses. How is the name of the IP address 198.51.100.165 stored on a DNS server?",
        "choices": ["In the A record for 165.100.51.198.ipv4.arpa.", "In the PTR record for 165.100.51.198.in-addr.arpa.", "In the RNAME record for 198-51-100-165.rev.arpa.", "In the ARPA record for 165.100.51.198.rev.", "In the REV record for arpa.in-addr.198.51.100.165."],
        "answer": "B"
    },
    {
        "type": "multiple_choice",
        "question": "Members of a team already have experience using Red Hat Enterprise Linux. For a small hobby project, the team wants to set up a Linux server without paying for a subscription. Which of the following Linux distributions allows the team members to apply as much of their Red Hat Enterprise Linux knowledge as possible?",
        "choices": ["Ubuntu Linux LTS", "Raspbian", "Debian GNU/Linux", "CentOS", "openSUSE"],
        "answer": "D"
    },
    {
        "type": "fill_in_the_blank",
        "question": "Which of the following outputs comes from the command free?\nA. total used free shared buff/cached available\nB. total used free shared buff/cached available",
        "answer": "total used free shared buff/cached available"
    },
    {
        "type": "multiple_choice",
        "question": "Which of the following outputs could stem from the command last?",
        "choices": ["1 ls 2 cat text.txt 3 logout", "Password for user last changed at Sat Mar 31 16:38:57 EST 2018", "Last login: Fri Mar 23 10:56:39 2018 from server.example.com", "EXT4-fs (dm-7): mounted filesystem with ordered data mode. Opts: (null)", "root tty2 Wed May 17 21:11 - 21:11 (00:00)"],
        "answer": "E"
    },
    {
        "type": "multiple_choice",
        "question": "What is the UID of the user root?",
        "choices": ["1", "-1", "255", "65536", "0"],
        "answer": "E"
    },
    {
        "type": "multiple_choice",
        "question": "What is true about the owner of a file?",
        "choices": ["Each file is owned by exactly one user and one group.", "The owner of a file always has full permissions when accessing the file.", "The user owning a file must be a member of the file's group.", "When a user is deleted, all files owned by the user disappear.", "The owner of a file cannot be changed once it is assigned to an owner."],
        "answer": "A"
    },
    {
        "type": "multiple_choice",
        "question": "What information is stored in /etc/passwd? (Choose three.)",
        "choices": ["The user's storage space limit", "The numerical user ID", "The username", "The encrypted password", "The user's default shell"],
        "answer": "BCE"
    },
    {
        "type": "multiple_choice",
        "question": "Which package management tool is used in Red Hat-based Linux Systems?",
        "choices": ["portage", "rpm", "apt-get", "dpkg", "packagectl"],
        "answer": "B"
    },
    {
        "type": "multiple_choice",
        "question": "Which of the following programs is a graphical editor for vector graphics?",
        "choices": ["Python", "NGINX", "Samba", "Inkscape", "MySQL"],
        "answer": "D"
    },
    {
        "type": "multiple_choice",
        "question": "What is true about a recursive directory listing?",
        "choices": ["It includes the content of sub-directories.", "It includes the permissions of the directory listed.", "It includes details of file system internals, such as inodes.", "It includes ownership information for the files.", "It includes a preview of content for each file in the directory."],
        "answer": "A"
    },
    {
        "type": "multiple_choice",
        "question": "Running the command rm Downloads leads to the following error: rm: cannot remove 'Downloads/': Is a directory. Which of the following commands can be used instead to remove Downloads, assuming Downloads is empty? (Choose two.)",
        "choices": ["undir Downloads", "rmdir Downloads", "dir -r Downloads", "rem Downloads", "rm -r Downloads"],
        "answer": "BE"
    },
    {
        "type": "multiple_choice",
        "question": "A user is currently in the directory /home/user/Downloads/ and runs the command ls ../Documents/. Assuming it exists, which directory's content is displayed?",
        "choices": ["/home/user/Documents/", "/home/user/Documents/Downloads/", "/home/user/Downloads/Documents/", "/Documents/", "/home/Documents"],
        "answer": "D"
    },
    {
        "type": "multiple_choice",
        "question": "A directory contains the following three files: texts 1.txt, texts 2.txt, texts 3.csv. Which command copies the two files ending in .txt to the /tmp/ directory?",
        "choices": ["cp ??.txt /tmp/", "cp *.txt /tmp/", "cp. \.txt /tmp/", "cp ?.txt /tmp/", "cp $?.txt /tmp/"],
        "answer": "B"
    },
    {
        "type": "multiple_choice",
        "question": "Which of the following is a protocol used for automatic IP address configuration?",
        "choices": ["NFS", "LDAP", "SMTP", "DNS", "DHCP"],
        "answer": "E"
    },
    {
        "type": "multiple_choice",
        "question": "Which command displays file names only and no additional information?",
        "choices": ["ls -a", "ls -lh", "ls -l", "ls -alh", "ls -nl"],
        "answer": "A"
    },
    {
        "type": "multiple_choice",
        "question": "Which of the following examples shows the general structure of a for loop in a shell script?",
        "choices": ["for *.txt as file => echo $file", "for *.txt ( echo $i )", "for file in *.txt do echo $i done", "for ls *.txt exec {} \;", "foreach @{file} { echo $i }"],
        "answer": "C"
    },
    {
        "type": "multiple_choice",
        "question": "What is the return value of a shell script after successful execution?",
        "choices": ["1", "0", "-1", "-255", "255"],
        "answer": "B"
    },
    {
        "type": "multiple_choice",
        "question": "Which of the following types of bus can connect hard disk drives with the motherboard?",
        "choices": ["The RAM bus", "The NUMA bus", "The CPU bus", "The SATA bus", "The Auto bus"],
        "answer": "D"
    },
    {
        "type": "multiple_choice",
        "question": "What information can be displayed by top?",
        "choices": ["Existing files, ordered by their size.", "Running processes, ordered by CPU or RAM consumption.", "User accounts, ordered by the number of logins.", "User groups, ordered by the number of members.", "User accounts, ordered by the number of files."],
        "answer": "B"
    },
    {
        "type": "multiple_choice",
        "question": "Which of the following commands can be used to resolve a DNS name to an IP address?",
        "choices": ["dnsname", "dns", "query", "host", "iplookup"],
        "answer": "D"
    },
    {
        "type": "multiple_choice",
        "question": "What is true about the dmesg command? (Choose two.)",
        "choices": ["It traces the execution of a command and shows each step the program carries out.", "It sends messages to the command lines of all current user sessions.", "It displays the content of the Linux kernel's ring buffer.", "It immediately outputs all new messages written to the system journal.", "It might not display older information because it was overwritten by newer information."],
        "answer": "CE"
    },
    {
        "type": "multiple_choice",
        "question": "Which permissions are set on a regular file once the permissions have been modified with the command chmod 654 file.txt?",
        "choices": ["drw-r-xr--", "drwxr-x--", "wrxr-x--x", "rwxrw---x", "-rw-r-xr--"],
        "answer": "E"
    },
    {
        "type": "multiple_choice",
        "question": "Which of the following permissions are set on the /tmp/ directory?",
        "choices": ["rwxrwxrwt", "------rwX", "rwSrw-rw-", "rwxrwS---", "r-xr-X--t"],
        "answer": "A"
    },
    {
        "type": "multiple_choice",
        "question": "Which command adds the new user tux and creates the user's home directory with default configuration files?",
        "choices": ["defaultuser tux", "useradd -m tux", "usercreate tux", "useradd -o default tux", "passwd -a tux"],
        "answer": "B"
    },
    {
        "type": "multiple_choice",
        "question": "Which of the following tar options handle compression? (Choose two.)",
        "choices": ["-bz", "-z", "-g", "-j", "-z2"],
        "answer": "BD"
    },
    {
        "type": "fill_in_the_blank",
        "question": "What keyword is used in a shell script to begin a loop? (Specify one keyword only, without any additional information.)",
        "answer": "for"
    },
    {
        "type": "multiple_choice",
        "question": "Which of the following commands creates an archive file work.tar from the contents of the directory ./work/?",
        "choices": ["tar --new work.tar ./work/", "tar -cf work.tar ./work/", "tar --create work.tgz --content ./work/", "tar work.tar < ./work/", "tar work > work.tar"],
        "answer": "B"
    },
    {
        "type": "multiple_choice",
        "question": "Which of the following keys can be pressed to exit less?",
        "choices": ["l", "x", "e", "q", "!"],
        "answer": "D"
    },
    {
        "type": "multiple_choice",
        "question": "The current directory contains the following file: -rwxr-xr-x 1 root root 859688 Feb 7 08:15 test.sh. Given that the file is a valid shell script, how can this script be executed? (Choose two.)",
        "choices": ["run test.sh", "${test.sh}", "cmd ./test.sh", "./test.sh", "bash test.sh"],
        "answer": "DE"
    },
    {
        "type": "multiple_choice",
        "question": "Which of the following commands sorts the output of the command export-logs?",
        "choices": ["export-logs < sort", "export-logs > sort", "export-logs & sort", "export-logs | sort", "export-logs <> sort"],
        "answer": "B"
    },
    {
        "type": "multiple_choice",
        "question": "A directory contains the following files: a.txt, b.txt, c.csv. What would be the output of the following shell script?\nfor file in *.txt\ndo\necho $file\ndone",
        "choices": ["*.txt", "a b", "c.cav", "a.txt", "a.txt b.txt"],
        "answer": "E"
    },
    {
        "type": "multiple_choice",
        "question": "Which of the following commands will search for the file foo.txt under the directory /home?",
        "choices": ["search /home --file foo.txt", "search /home foo.txt", "find /home --file foo.txt", "find /home name foo.txt", "find /home foo.txt"],
        "answer": "D"
    },
    {
        "type": "multiple_choice",
        "question": "The current directory contains the following file: -rw-r--r-- 1 root exec 24551 Apr 2 12:36 test.sh. The file contains a valid shell script, but executing this file using ./test.sh leads to this error: bash: ./test.sh: Permission denied. What should be done in order to successfully execute the script?",
        "choices": ["The file's extension should be changed from .sh to .bin.", "The execute bit should be set in the file's permissions.", "The user executing the script should be added to the exec group.", "The SetUID bit should be set in the file's permissions", "The script should be run using #!./test.sh instead of ./test.sh."],
        "answer": "B"
    },
    {
        "type": "multiple_choice",
        "question": "What is a Linux distribution?",
        "choices": ["The Linux file system as seen from the root account after mounting all file systems.", "A bundling of the Linux kernel, system utilities and other software.", "The set of rules which governs the distribution of Linux kernel source code.", "An operating system based on Linux but incompatible to the regular Linux kernel.", "A set of changes to Linux which enable Linux to run on another processor architecture."],
        "answer": "B"
    },
    {
        "type": "multiple_choice",
        "question": "Where is the operating system of a Raspberry Pi stored?",
        "choices": ["On the master device attached to the Raspberry Pi's IDE bus.", "On a read only partition on the Raspberry Pi's firmware, next to the BIOS.", "On a removable SD card which is put into the Raspberry Pi.", "On a Linux extension module connected to the Raspberry Pi's GPIO pins.", "On rewritable flash storage which is built into the Raspberry Pi."],
        "answer": "C"
    },
    {
        "type": "multiple_choice",
        "question": "What is defined by a Free Software license?",
        "choices": ["Details of the technical documentation each contributor has to provide.", "The programming languages which may be used to extend the licensed program.", "A complete list of libraries required to compile the licensed software.", "Limits on the purposes for which the licensed software may be used.", "Conditions for modifying and distributing the licensed software."],
        "answer": "E"
    },
    {
        "type": "multiple_choice",
        "question": "Why are web browser cookies considered dangerous?",
        "choices": ["Cookies support identification and tracking of users.", "Cookies are always public and accessible to anyone on the internet.", "Cookies consume significant amounts of storage and can exhaust disk space.", "Cookies store critical data which is lost when a cookie is deleted.", "Cookies can contain and execute viruses and malware."],
        "answer": "A"
    },
    {
        "type": "multiple_choice",
        "question": "Which of the following are typical services offered by public cloud providers? (Choose three.)",
        "choices": ["Platform as a Service (PaaS)", "Infrastructure as a Service (IaaS)", "Internet as a Service (IaaS)", "Graphics as a Service (GaaS)", "Software as a Service (SaaS)"],
        "answer": "ABE"
    },
    {
        "type": "multiple_choice",
        "question": "Which of the following characters in a shell prompt indicates the shell is running with root privileges?",
        "choices": ["!", "#", "*", "&", "$"],
        "answer": "B"
    },
    {
        "type": "multiple_choice",
        "question": "Which of the following commands are used to get information on the proper use of ls? (Choose two.)",
        "choices": ["option ls", "usage ls", "manual ls", "man ls", "info ls"],
        "answer": "DE"
    },
    {
        "type": "multiple_choice",
        "question": "Which of the following directories contains information, documentation and example configuration files for installed software packages?",
        "choices": ["/usr/share/doc/", "/etc/defaults/", "/var/info/", "/doc/", "/usr/examples/"],
        "answer": "A"
    },
    {
        "type": "multiple_choice",
        "question": "Which of the following commands adds the directory /new/dir/ to the PATH environment variable?",
        "choices": ["$PATH=/new/dir: $PATH", "PATH=/new/dir: PATH", "export PATH=/new/dir: PATH", "export $PATH=/new/dir: $PATH", "export PATH=/new/dir: $PATH"],
        "answer": "E"
    },
    {
        "type": "fill_in_the_blank",
        "question": "When typing a long command line at the shell, what single character can be used to split a command across multiple lines?",
        "answer": "\\"
    },
    {
        "type": "multiple_choice",
        "question": "Which of the following DNS record types hold an IP address? (Choose two.)",
        "choices": ["NS", "AAAA", "MX", "A", "CNAME"],
        "answer": "BD"
    },
    {
        "type": "multiple_choice",
        "question": "Which of the following values could be a process ID on Linux?",
        "choices": ["/bin/bash", "60b503cd-019e-4300-a7be-922f074ef5ce", "/sys/pid/9a14", "fff3", "21398"],
        "answer": "E"
    },
    {
        "type": "multiple_choice",
        "question": "Which of the following devices represents a hard disk partition?",
        "choices": ["/dev/ttyS0", "/dev/sata0", "/dev/part0", "/dev/sda2", "/dev/sda/p2"],
        "answer": "D"
    },
    {
        "type": "multiple_choice",
        "question": "Which of the following statements regarding Linux hardware drivers is correct?",
        "choices": ["Drivers are regular Linux programs which have to be run by the user who wants to use a device.", "Drivers are not used by Linux because the BIOS handles all access to hardware on behalf of Linux.", "Drivers are stored on their devices and are copied by the Linux kernel when a new device is attached", "Drivers are downloaded from the vendor's driver repository when a new device is attached.", "Drivers are either compiled into the Linux kernel or are loaded as kernel modules."],
        "answer": "E"
    },
    {
        "type": "multiple_choice",
        "question": "What can be found in the /proc/ directory?",
        "choices": ["One directory per installed program.", "One device file per hardware device.", "One file per existing user account.", "One directory per running process.", "One log file per running service."],
        "answer": "D"
    },
    {
        "type": "multiple_choice",
        "question": "Which of the following directories must be mounted with read and write access if it resides on its own dedicated file system?",
        "choices": ["/opt", "/lib", "/etc", "/var", "/usr"],
        "answer": "D"
    },
    {
        "type": "multiple_choice",
        "question": "The ownership of the file doku.odt should be changed. The new owner is named tux. Which command accomplishes this change?",
        "choices": ["chmod u=tux doku.odt", "newuser doku.odt tux", "chown tux doku.odt", "transfer tux: doku.odt", "passwd doku.odt:tux"],
        "answer": "C"
    },
    {
        "type": "multiple_choice",
        "question": "Which statements about the directory /etc/skel are correct? (Choose two.)",
        "choices": ["The personal user settings of root are stored in this directory.", "The files from the directory are copied to the home directory of the new user when starting the system.", "The files from the directory are copied to the home directory of a new user when the account is created.", "The directory contains a default set of configuration files used by the useradd command.", "The directory contains the global settings for the Linux system."],
        "answer": "CD"
    },
    {
        "type": "multiple_choice",
        "question": "What is true about links in a Linux file system?",
        "choices": ["A symbolic link can only point to a file and not to a directory.", "A hard link can only point to a directory and never to a file.", "When the target of the symbolic link is moved, the link is automatically updated.", "A symbolic link can point to a file on another file system.", "Only the root user can create hard links."],
        "answer": "D"
    },
    {
        "type": "multiple_choice",
        "question": "Which files are the source of the information in the following output? (Choose two.)\nuid=1000 (bob) gid=1000 (bob) groups=1000 (bob), 10 (wheel), 150 (wireshark), 989 (docker), 1001 (libvirt)",
        "choices": ["/etc/id", "/etc/passwd", "/etc/group", "/home/index", "/var/db/users"],
        "answer": "BC"
    },
    {
        "type": "multiple_choice",
        "question": "Which of the following tasks can the command passwd accomplish? (Choose two.)",
        "choices": ["Change a user's username.", "Change a user's password.", "Create a new user account.", "Create a new user group.", "Lock a user account."],
        "answer": "BE"
    },
    {
        "type": "multiple_choice",
        "question": "What is true about the su command?",
        "choices": ["It is the default shell of the root account.", "It can only be used by the user root.", "It runs a shell or command as another user.", "It changes the name of the main administrator account.", "It locks the root account in specific time frames."],
        "answer": "C"
    },
    {
        "type": "fill_in_the_blank",
        "question": "What parameter of ls prints a recursive listing of a directory's content? (Specify ONLY the option name without any values or parameters.)",
        "answer": "ls-R"
    },
    {
        "type": "multiple_choice",
        "question": "Most commands on Linux can display information on their usage. How can this information typically be displayed?",
        "choices": ["By running the command with the option /? or /??.", "By running the command with the option ?! or ?=!.","By running the command with the option /doc or /documentation.", "By running the command with the option -h or --help.", "By running the command with the option -m or --manpage."],
        "answer": "D"
    },
    {
        "type": "multiple_choice",
        "question": "Which of the following commands shows the absolute path to the current working directory?",
        "choices": ["who", "cd ..", "pwd", "ls -l", "cd ~/home"],
        "answer": "C"
    },
    {
        "type": "multiple_choice",
        "question": "Which of the following commands output the content of the file Texts 2.txt? (Choose two.)",
        "choices": ["cat 'Texts 2.txt'", "cat -- Texts 2.txt", "cat |Texts 2.txt|", "cat 'Texts\\ 2.txt'", "cat Texts\\ 2.txt"],
        "answer": "AE"
    },
    {
        "type": "multiple_choice",
        "question": "What is the purpose of the PATH environment variable?",
        "choices": ["It allows the execution of commands without the need to know the location of the executable.", "It increases security by preventing commands from running in certain locations.", "It specifies the location of a user's home directory.", "It indicates the location of the default shell to be used when a user logs in.", "It contains the absolute path to the current directory."],
        "answer": "A"
    },
    {
        "type": "multiple_choice",
        "question": "Which of the following commands sets the variable USERNAME to the value bob?",
        "choices": ["set USERNAME bob", "$USERNAME==bob", "var USERNAME=bob", "USERNAME<=bob", "USERNAME=bob"],
        "answer": "E"
    },
    {
        "type": "fill_in_the_blank",
        "question": "What command displays manual pages? (Specify ONLY the command without any path or parameters.)",
        "answer": "man"
    },
    {
        "type": "multiple_choice",
        "question": "Which command copies the contents of the directory /etc/, including all sub-directories, to /root/?",
        "choices": ["copy /etc /root", "cp -r /etc/* /root", "cp -v /etc/* /root", "rcp /etc/* /root", "cp -R /etc/. /root"],
        "answer": "B"
    },
    {
        "type": "multiple_choice",
        "question": "Which of the following commands puts the lines of the file data.csv into alphabetical order?",
        "choices": ["a..z data.csv", "sort data.csv", "abc data.csv", "wc -s data.csv", "grep --sort data.csv"],
        "answer": "B"
    },
    {
        "type": "multiple_choice",
        "question": "Which operator in a regular expression matches the preceding character either zero or one time?",
        "choices": ["?", "*", "+", "%", "$"],
        "answer": "B"
    },
    {
        "type": "multiple_choice",
        "question": "The file script.sh in the current directory contains the following content:\n#!/bin/bash\necho $MYVAR\nThe following commands are used to execute this script:\nMYVAR=value ./script.sh\nThe result is an empty line instead of the content of the variable MYVAR. How should MYVAR be set in order to make script.sh display the content of MYVAR?",
        "choices": ["!MYVAR=value", "env MYVAR=value", "MYVAR=value", "$MYVAR=value", "export MYVAR=value"],
        "answer": "E"
    },
    {
        "type": "multiple_choice",
        "question": "Which of the following commands creates the ZIP archive poems.zip containing all files in the current directory whose names end in .txt?",
        "choices": ["zip *.txt > poems.zip", "zcat *.txt poems.zip", "zip poems.zip *.txt", "zip cfz poems.zip *.txt", "cat *.txt | zip poems.zip"],
        "answer": "C"
    },
    {
        "type": "multiple_choice",
        "question": "Which of the following statements are true regarding a typical shell script? (Choose two.)",
        "choices": ["It has the executable permission bit set.", "It starts with the two character sequence #!.", "It is located in /usr/local/scripts/.", "It is located in /etc/bash/scripts/.", "It is compiled into a binary file compatible with the current machine architecture."],
        "answer": "AB"
    },
    {
        "type": "multiple_choice",
        "question": "Which of the following commands extracts the contents of the compressed archive file1.tar.gz?",
        "choices": ["tar -czf file1.tar.gz", "ztar file1.tar.gz", "tar -xzf file1.tar.gz", "tar --extract file1.tar.gz", "detar file1.tar.gz"],
        "answer": "C"
    },
    {
        "type": "multiple_choice",
        "question": "Which of the following commands finds all lines in the file operating-systems.txt which contain the term linux, regardless of the case?",
        "choices": ["igrep linux operating-systems.txt", "less -i linux operating-systems.txt", "grep -i linux operating-systems.txt", "cut linux operating-systems.txt", "cut [Ll] [Ii] [Nn] [Uu] [Xx] operating-systems.txt"],
        "answer": "C"
    },
    {
        "type": "multiple_choice",
        "question": "Which one of the following statements concerning Linux passwords is true?",
        "choices": ["All passwords can be decrypted using the system administrator's master password.", "Passwords may never start with a non-letter.", "Users cannot change their password once it has been set.", "Passwords are only stored in hashed form.", "Passwords may be at most six characters long."],
        "answer": "D"
    },
    {
        "type": "multiple_choice",
        "question": "Which of the following Linux Distributions is derived from Red Hat Enterprise Linux?",
        "choices": ["Raspbian", "openSUSE", "Debian", "Ubuntu", "CentOS"],
        "answer": "E"
    },
    {
        "type": "multiple_choice",
        "question": "Which of the following statements is true about Free Software?",
        "choices": ["It is developed by volunteers only.", "It may be modified by anyone using it.", "It must always be available free of charge.", "It only runs on Linux.", "It is only distributed as a compiled binary."],
        "answer": "B"
    },
    {
        "type": "multiple_choice",
        "question": "How is a new Linux computing instance provisioned in an IaaS cloud?",
        "choices": ["The standard Linux installer has to be run through a remote console.", "After buying a Linux distribution, its vendor delivers it to a cloud instance.", "The installation has to be prepared in a local virtual machine which is then copied to the cloud.", "The cloud hosting organization provides a set of pre-prepared images of popular Linux distributions.", "A provider-specific configuration file describing the desired installation is uploaded to the cloud provider."],
        "answer": "D"
    },
    {
        "type": "multiple_choice",
        "question": "What are the differences between a private web browser window and a regular web browser window? (Choose three.)",
        "choices": ["Private web browser windows do not allow printing or storing websites.", "Private web browser windows do not store cookies persistently.", "Private web browser windows do not support logins into websites.", "Private web browser windows do not keep records in the browser history.", "Private web browser windows do not send regular stored cookies."],
        "answer": "BDE"
    },
    {
        "type": "multiple_choice",
        "question": "What is the preferred source for the installation of new applications in a Linux based operating system?",
        "choices": ["The vendor's version management system", "A CD-ROM disk", "The distribution's package repository", "The vendor's website", "A retail store"],
        "answer": "C"
    },
]

def split_questions(questions):
    random.shuffle(questions)
    half = len(questions) // 2
    return questions[:half], questions[half:]

class QuizApp:
    def __init__(self, root, questions, test_id, missed_questions_collector):
        self.root = root
        self.questions = questions
        self.test_id = test_id
        self.root.title(f"Linux Quiz Test {test_id}")
        self.root.geometry("600x400")
        self.root.configure(bg="#2E2E2E")  # Set background color
        
        self.score = 0
        self.current_question_index = -1
        self.missed_questions = []
        self.missed_questions_collector = missed_questions_collector

        # Custom font settings
        self.font = ("Helvetica", 14)
        self.font_bold = ("Helvetica", 14, "bold")
        
        self.question_label = tk.Label(root, text="", wraplength=500, justify="left", bg="#2E2E2E", fg="white", font=self.font)
        self.question_label.pack(pady=20)

        self.answer_var = tk.StringVar()
        self.answer_entry = tk.Entry(root, textvariable=self.answer_var, font=self.font)
        self.answer_entry.pack(pady=10)
        self.answer_entry.bind("<Return>", self.submit_answer)  # Bind the Enter key

        self.submit_button = tk.Button(root, text="Submit", command=self.submit_answer, bg="#4CAF50", fg="white", font=self.font_bold)
        self.submit_button.pack(pady=10)

        self.next_question()

    def display_question(self, question):
        self.question_label.config(text=question["question"])
        if question["type"] == "multiple_choice":
            choices_text = "\n".join([f"{chr(65+i)}. {choice}" for i, choice in enumerate(question["choices"])])
            self.question_label.config(text=f"{question['question']}\n\n{choices_text}")
        self.answer_var.set("")

    def next_question(self):
        self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            self.display_question(self.questions[self.current_question_index])
        else:
            self.end_quiz()

    def submit_answer(self, event=None):
        current_question = self.questions[self.current_question_index]
        user_answer = self.answer_var.get().strip().upper()
        if current_question["type"] == "multiple_choice":
            correct = user_answer == current_question["answer"]
        elif current_question["type"] == "fill_in_the_blank":
            correct = user_answer.lower() == current_question["answer"].lower()
        
        if correct:
            self.score += 1
            messagebox.showinfo("Result", "Correct!")
        else:
            self.missed_questions.append(current_question)
            messagebox.showinfo("Result", f"Wrong! The correct answer is: {current_question['answer']}")
        
        self.next_question()

    def end_quiz(self):
        self.question_label.config(text=f"Quiz over! Your final score is: {self.score}/{len(self.questions)}")
        self.answer_entry.pack_forget()
        self.submit_button.pack_forget()
        self.answer_entry.unbind("<Return>")  # Unbind the Enter key
        self.missed_questions_collector.extend(self.missed_questions)
        if self.missed_questions:
            missed_text = "\n\n".join([q["question"] for q in self.missed_questions])  # Add extra newlines for spacing
            messagebox.showinfo("Missed Questions", f"You missed the following questions:\n\n{missed_text}")
            # Save missed questions to a file or display them in some other way
            with open(f"missed_questions_test_{self.test_id}.txt", "w") as f:
                f.write(missed_text)
        self.root.destroy()
        if self.test_id == 2:
            # Start the third test with missed questions
            root3 = tk.Tk()
            app3 = QuizApp(root3, self.missed_questions_collector, 3, [])
            root3.mainloop()
        elif self.test_id == 3:
            # End the program after the third test
            self.root.quit()

if __name__ == "__main__":
    questions_set_1, questions_set_2 = split_questions(questions)
    missed_questions_collector = []

    # Test 1
    root1 = tk.Tk()
    app1 = QuizApp(root1, questions_set_1, 1, missed_questions_collector)
    root1.mainloop()

    # Test 2
    root2 = tk.Tk()
    app2 = QuizApp(root2,questions_set_2, 2, missed_questions_collector)
    root2.mainloop()

                   
