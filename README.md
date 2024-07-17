# Power State Virtual Machine Manager
### v1.0.0-alpha
Set the power state of a Virtual Machine (VM). Does what `virt-manager` doesn't;
includes missing features like sleep, hibernate, and wake. Includes a TUI and
GUI applications.

**[Latest release](https://github.com/portellam/powerstate-virtmanager/releases/latest)**

## Table of Contents
- [1. Why?](#1-why)
- [2. Related Projects](#2-related-projects)
- [3. Documentation](#3-documentation)
- [4. Host Requirements](#4-host-requirements)
    - [4.1. Operating System](#41-operating-system)
    - [4.2. Software](#42-software)
- [5. Download](#5-download)
- [6. Usage](#6-usage)
    - [6.1. Install](#61-install)
    - [6.2. Terminal User Interface](#62-terminal-user-interface)
    - [6.3. Graphics User Interface](#63-graphics-user-interface)
- [7. Contact](#7-contact)
- [8. References](#8-references)

## Contents
### 1. Why?
The Virtual Machine (VM) manager application `virt-manager` does not (currently)
support resume and suspend of power states (S3 and above) such as sleep,
hibernate, hybrid sleep.

Normally, a bare-metal machine may resume from or suspend to sleep by a power
button or input device activity.

The Command Line Interface (CLI) tool `virsh` does support the aforementioned
power states.

The Terminal and Graphics UI (TUI and GUI) applications provided utilize `virsh`
to simulate power button activity.

### 2. Related Projects
| Project                                 | Codeberg          | GitHub          |
| :---                                    | :---:             | :---:           |
| Deploy VFIO                             | [link][codeberg1] | [link][github1] |
| Auto X.Org                              | [link][codeberg2] | [link][github2] |
| Generate Evdev                          | [link][codeberg3] | [link][github3] |
| Guest Machine Guide                     | [link][codeberg4] | [link][github4] |
| Libvirt Hooks                           | [link][codeberg5] | [link][github5] |
| **Power State Virtual Machine Manager** | [link][codeberg6] | [link][github6] |

[codeberg1]: https://codeberg.org/portellam/deploy-VFIO
[github1]:   https://github.com/portellam/deploy-VFIO
[codeberg2]: https://codeberg.org/portellam/auto-xorg
[github2]:   https://github.com/portellam/auto-xorg
[codeberg3]: https://codeberg.org/portellam/generate-evdev
[github3]:   https://github.com/portellam/generate-evdev
[codeberg4]: https://codeberg.org/portellam/guest-machine-guide
[github4]:   https://github.com/portellam/guest-machine-guide
[codeberg5]: https://codeberg.org/portellam/libvirt-hooks
[github5]:   https://github.com/portellam/libvirt-hooks
[codeberg6]: https://codeberg.org/portellam/powerstate-virtmanager
[github6]:   https://github.com/portellam/powerstate-virtmanager

### 3. Documentation
- [What is VFIO?](#2)
- [VFIO Discussion and Support](#3)
- [Hardware-Passthrough Guide](#1)
- [Virtual Machine XML Format Guide](#4)

### 4. Host Requirements
#### 4.1. Operating System
Linux.

#### 4.2. Software
- `virsh`, the Command Line Interface (CLI) tool which manages Virtual Machines,
regardless of virtualization hypervisor (`QEMU`, `KVM`, etc.).

### 5. Download
- Download the Latest Release:&ensp;[Codeberg][codeberg-releases],
[GitHub][github-releases]

- Download the `.zip` file:
    1. Viewing from the top of the repository's (current) webpage, click the
        drop-down icon:
        - `···` on Codeberg.
        - `<> Code ` on GitHub.
    2. Click `Download ZIP` and save.
    3. Open the `.zip` file, then extract its contents.

- Clone the repository:
    1. Open a Command Line Interface (CLI).
        - Open a console emulator (for Debian systems: Konsole).
        - Open a existing console: press `CTRL` + `ALT` + `F2`, `F3`, `F4`, `F5`,  or
        `F6`.
            - **To return to the desktop,** press `CTRL` + `ALT` + `F7`.
            - `F1` is reserved for debug output of the Linux kernel.
            - `F7` is reserved for video output of the desktop environment.
            - `F8` and above are unused.
    2. Change your directory to your home folder or anywhere safe:
        - `cd ~`
    3. Clone the repository:
        - `git clone https://www.codeberg.org/portellam/powerstate-virtmanager`
        - `git clone https://www.github.com/portellam/powerstate-virtmanager`

[codeberg-releases]: https://codeberg.org/portellam/powerstate-virtmanager/releases/latest
[github-releases]:   https://github.com/portellam/powerstate-virtmanager/releases/latest

### 6. Usage
#### 6.1. Install
Installer will copy required files to `/usr/bin/local/`. You may run the
executable(s) from any directory.

```bash
sudo bash installer.sh
```

#### 6.2. Terminal User Interface
```bash
sudo powerstate-virtmanager
```

#### 6.3. Graphics User Interface
- Quickly navigate using arrow keys and macros with the top toolbar.
- Set a power setting with the left vertical toolbar.
- Sort Virtual Machine(s) within the right view port.

![GUI Main Window](/images/gui-main-window.png)

### 7. Contact
Did you encounter a bug? Do you need help? Please visit the
**Issues page** ([Codeberg][codeberg-issues], [GitHub][github-issues]).

[codeberg-issues]: https://codeberg.org/portellam/powerstate-virtmanager/issues
[github-issues]:   https://github.com/portellam/powerstate-virtmanager/issues

### 8. References
#### 1.
**PCI passthrough via OVMF**. ArchWiki. Accessed June 14, 2024.
<sup>https://wiki.archlinux.org/title/PCI_passthrough_via_OVMF.</sup>

#### 2.
**VFIO - ‘Virtual Function I/O’ - The Linux Kernel Documentation**.
The linux kernel. Accessed June 14, 2024.
<sup>https://www.kernel.org/doc/html/latest/driver-api/vfio.html.</sup>

#### 3.
**VFIO Discussion and Support**. Reddit. Accessed June 14, 2024.
<sup>https://www.reddit.com/r/VFIO/.</sup>

#### 4.
**XML Design Format** GitHub - libvirt/libvirt. Accessed June 18, 2024.
<sup>https://github.com/libvirt/libvirt/blob/master/docs/formatdomain.rst.</sup>