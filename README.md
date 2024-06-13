# Power State Virtual Machine Manager
Set the power state of a QEMU/KVM Virtual Machine (VM). Wake from Sleep or
Hibernation. Does what `virt-manager` doesn't. Python and GTK3 GUI application.

**[View latest release]** | **[View develop branch]**

[View latest release]: ../releases/latest
[View develop branch]: ../tree/develop

## Table of Contents
- [Related Projects](#related-projects)
- [Recommended Reading](#recommended-reading)
- [Why?](#why)
- [Contact](#contact)

## Contents
### Related Projects
| Project                                 | Codeberg   | GitHub     |
| :---                                    | :---:      | :---:      |
| Deploy VFIO                             | [link][1]  | [link][2]  |
| Auto X.Org                              | [link][3]  | [link][4]  |
| Generate Evdev                          | [link][5]  | [link][6]  |
| Guest Machine Guide                     | [link][7]  | [link][8]  |
| Libvirt Hooks                           | [link][9]  | [link][10] |
| **Power State Virtual Machine Manager** | [link][11] | [link][12] |

[1]: https://codeberg.org/portellam/deploy-VFIO
[2]: https://github.com/portellam/deploy-VFIO
[3]: https://codeberg.org/portellam/auto-xorg
[4]: https://github.com/portellam/auto-xorg
[5]: https://codeberg.org/portellam/generate-evdev
[6]: https://github.com/portellam/generate-evdev
[7]: https://codeberg.org/portellam/guest-machine-guide
[8]: https://github.com/portellam/guest-machine-guide
[9]: https://codeberg.org/portellam/libvirt-hooks
[10]: https://github.com/portellam/libvirt-hooks
[11]: https://codeberg.org/portellam/powerstate-virtmanager
[12]: https://github.com/portellam/powerstate-virtmanager

### Recommended Reading
[VFIO article] | [VFIO forum] | [PCI Passthrough Guide]

[VFIO Article]: https://www.kernel.org/doc/html/latest/driver-api/vfio.html
[VFIO Forum]: https://old.reddit.com/r/VFIO
[PCI Passthrough Guide]: https://wiki.archlinux.org/title/PCI_passthrough_via_OVMF

### Why?
The virtual machine manager application `virt-manager` does not (currently) have
the option to wake a VM from Sleep.
That is unfortunate, as a VM cannot be awaken from normal and expected means
(wake from USB keyboard or network activity).
This application fixes that issue, with a nice Frontend to boot.

### Contact
Did you encounter a bug? Do you need help? Please contact by [raising an issue]
with the project itself.

[raising an issue]: /../issues

## TODO:
- [ ] create GTK3 project.
- [ ] draw GUI layout.
- [ ] gather Linux shell commands.
- [ ] create Python classes.
- [ ] add CLI commands?
- [ ] test.
- [ ] create first release.