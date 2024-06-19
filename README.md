# Power State Virtual Machine Manager
### Status: Pre-development
Set the power state of a QEMU/KVM Virtual Machine (VM). Wake from Sleep or
Hibernation. Does what `virt-manager` doesn't.

**Download the Latest Release:**&ensp;[Codeberg][codeberg-releases],
[GitHub][github-releases]

[codeberg-releases]: https://codeberg.org/portellam/powerstate-virtmanager/releases/latest
[github-releases]:   https://github.com/portellam/powerstate-virtmanager/releases/latest

## Table of Contents
- [Why?](#why)
- [Related Projects](#related-projects)
- [Documentation](#documentation)
- [Contact](#contact)
- [References](#references)

## Contents
### Why?
The virtual machine manager application `virt-manager` does not (currently) have
the option to wake a VM from Sleep. That is unfortunate, as a VM cannot be
awaken from normal and expected means. For example, wake from keyboard or
network activity. This application fixes that issue, with a nice Frontend to
boot.

### Related Projects
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

### Documentation
- [What is VFIO?](#3)
- [VFIO Forum](#2)
- [Hardware-Passthrough Guide](#1)
- [Virtual Machine XML Format Guide](#4)

### Contact
Did you encounter a bug? Do you need help? Please visit the
**Issues page** ([Codeberg][codeberg-issues], [GitHub][github-issues]).

[codeberg-issues]: https://codeberg.org/portellam/powerstate-virtmanager/issues
[github-issues]:   https://github.com/portellam/powerstate-virtmanager/issues

### References
#### 1.
**PCI passthrough via OVMF**. ArchWiki. Accessed June 14, 2024.
<sup>https://wiki.archlinux.org/title/PCI_passthrough_via_OVMF.</sup>

#### 2.
**r/VFIO**. Accessed June 14, 2024.
<sup>https://www.reddit.com/r/VFIO/.</sup>

#### 3.
**VFIO - ‘Virtual Function I/O’ - The Linux Kernel Documentation**.
The linux kernel. Accessed June 14, 2024.
<sup>https://www.kernel.org/doc/html/latest/driver-api/vfio.html.</sup>

#### 4.
**libvirt/libvirt - XML Design Format** GitHub. Accessed June 18, 2024.
<sup>https://github.com/libvirt/libvirt/blob/master/docs/formatdomain.rst.</sup>