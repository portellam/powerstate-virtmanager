# Power State Virtual Machine Manager
## Status: Pre-development
Set the power state of a QEMU/KVM Virtual Machine (VM). Wake from Sleep or
Hibernation. Does what `virt-manager` doesn't. Python and GTK3 GUI application.

**[View latest release]** | **[View develop branch]**

[View latest release]: /../../releases/latest
[View develop branch]: /../../tree/develop

## Table of Contents
- [Why?](#why)
- [Related Projects](#related-projects)
- [Recommended Reading](#recommended-reading)
- [Contact](#contact)

## Contents
### Why?
The virtual machine manager application `virt-manager` does not (currently) have
the option to wake a VM from Sleep.
That is unfortunate, as a VM cannot be awaken from normal and expected means
(wake from USB keyboard or network activity).
This application fixes that issue, with a nice Frontend to boot.

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
[codeberg2]: https://github.com/portellam/deploy-VFIO
[codeberg3]: https://codeberg.org/portellam/auto-xorg
[codeberg4]: https://github.com/portellam/auto-xorg
[codeberg5]: https://codeberg.org/portellam/generate-evdev
[codeberg6]: https://github.com/portellam/generate-evdev
[github1]: https://codeberg.org/portellam/guest-machine-guide
[github2]: https://github.com/portellam/guest-machine-guide
[github3]: https://codeberg.org/portellam/libvirt-hooks
[github4]: https://github.com/portellam/libvirt-hooks
[github5]: https://codeberg.org/portellam/powerstate-virtmanager
[github6]: https://github.com/portellam/powerstate-virtmanager

### Recommended Reading
[VFIO article] | [VFIO forum] | [PCI Passthrough Guide]

[VFIO Article]: https://www.kernel.org/doc/html/latest/driver-api/vfio.html
[VFIO Forum]: https://old.reddit.com/r/VFIO
[PCI Passthrough Guide]: https://wiki.archlinux.org/title/PCI_passthrough_via_OVMF

### Contact
Did you encounter a bug? Do you need help? Please contact by [raising an issue]
with the project itself.

[raising an issue]: /../../issues

## TODO:
- [ ] create GTK3 project.
- [ ] draw GUI layout.
- [ ] gather Linux shell commands.
- [ ] create Python classes.
- [ ] add CLI commands?
- [ ] test.
- [ ] create first release.