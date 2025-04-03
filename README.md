# Power State Virtual Machine Manager
### v1.0.0
Set the power state of a QEMU/KVM Virtual Machine (VM). Wake from Sleep or
Hibernation. Does what `virt-manager` doesn't.

## [Download](#5-download)
#### View this repository on [Codeberg][01] or [GitHub][02].
[01]: https://codeberg.org/portellam/powerstate-virtmanager
[02]: https://github.com/portellam/powerstate-virtmanager
##

## Table of Contents
- [1. Why?](#1-why)
- [2. Related Projects](#2-related-projects)
- [3. Documentation](#3-documentation)
- [4. Host Requirements](#4-host-requirements)
    - [4.1. Operating System](#41-operating-system)
    - [4.2. Software](#42-software)
    - [4.3. Hardware](#43-hardware)
- [5. Download](#5-download)
- [6. Usage](#6-usage)
    - [6.1. Install](#61-install)
    - [6.2. Run](#62-run)
- [7. Contact](#7-contact)
- [8. References](#8-references)

## Contents
### 1. Why?
The virtual machine manager application `virt-manager` does not (currently) have
the option to wake a VM from Sleep. In other words, as a VM cannot be awaken by
an input device, unfortunately. For example, a physical or virtual "power on",
button, keyboard input, or network activity. This application includes the
ability to wake from Sleep and Hibernation, and the other related features from
`virt-manager`.

### 2. Related Projects
To view other relevant projects, visit [Codeberg][21]
or [GitHub][22].

[21]: https://codeberg.org/portellam/vfio-collection
[22]: https://github.com/portellam/vfio-collection

### 3. Documentation
- What is VFIO?[<sup>[2]</sup>](#2)
- VFIO Discussion and Support[<sup>[3]</sup>](#3)
- Hardware-Passthrough Guide[<sup>[1]</sup>](#1)
- Virtual Machine XML Format Guide[<sup>[4]</sup>](#4)

### 4. Host Requirements
#### 4.1. Operating System
Linux.

#### 4.2. Software
- `QEMU` and `Libvirt` for Virtual Machines.

#### 4.3. Hardware
The following firmware options are supported and enabled (motherboard and CPU):
- System Power State S3 (Sleep).
- System Power State S4 (Hibernation).

### 5. Download
- Download the Latest Release:&ensp;[Codeberg][51] or [GitHub][52]

- Download the `.zip` file:
    1. Viewing from the top of the repository's (current) webpage, click the
        drop-down icon:
        - `···` on Codeberg.
        - `<> Code ` on GitHub.
    2. Click `Download ZIP` and save.
    3. Open the `.zip` file, then extract its contents.

- Clone the repository:
    1. Open a Command Line Interface (CLI) or Terminal.
        - Open a console emulator (for Debian systems: Konsole).
        - **Linux only:** Open an existing console: press `CTRL` + `ALT` + `F2`,
        `F3`, `F4`, `F5`, or `F6`.
            - **To return to the desktop,** press `CTRL` + `ALT` + `F7`.
            - `F1` is reserved for debug output of the Linux kernel.
            - `F7` is reserved for video output of the desktop environment.
            - `F8` and above are unused.
    2. Change your directory to your home folder or anywhere safe:
        - `cd ~`
    3. Clone the repository:
        - `git clone https://www.codeberg.org/portellam/powerstate-virtmanager`
        - `git clone https://www.github.com/portellam/powerstate-virtmanager`

[51]: https://codeberg.org/portellam/powerstate-virtmanager/releases/latest
[52]: https://github.com/portellam/powerstate-virtmanager/releases/latest

### 6. Usage
#### 6.1. Install
```bash
sudo bash installer.sh
```

#### 6.2. Run
Installer will copy required files to `/usr/bin/local/`. You may run executable
from any directory.
```bash
sudo powerstate-virtmanager
```

### 7. Contact
Do you need help? Please visit the [Issues][71] page.

[71]: https://github.com/portellam/powerstate-virtmanager/issues

### 8. References
#### 1.
&nbsp;&nbsp;**PCI passthrough via OVMF**. ArchWiki. Accessed June 14, 2024.

&nbsp;&nbsp;&nbsp;&nbsp;<sup>https://wiki.archlinux.org/title/PCI_passthrough_via_OVMF.</sup>

#### 2.
&nbsp;&nbsp;**VFIO - ‘Virtual Function I/O’ - The Linux Kernel Documentation**.
The linux kernel. Accessed June 14, 2024.

&nbsp;&nbsp;&nbsp;&nbsp;<sup>https://www.kernel.org/doc/html/latest/driver-api/vfio.html.</sup>

#### 3.
&nbsp;&nbsp;**VFIO Discussion and Support**. Reddit. Accessed June 14, 2024.

&nbsp;&nbsp;&nbsp;&nbsp;<sup>https://www.reddit.com/r/VFIO/.</sup>
##

#### Click [here](#auto-xorg) to return to the top of this document.