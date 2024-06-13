# Power State Virtual Machine Manager
Set the power state of a QEMU/KVM Virtual Machine (VM). Wake from Sleep or Hibernation. Does what `virt-manager` doesn't. Python and GTK3 GUI application.

**[View latest release]** | **[View develop branch]**

### Related Projects:
[Deploy VFIO] | [Auto X.Org]| [Generate Evdev]

[Guest Machine Guide] | [Libvirt Hooks] | **[Power State Virtual Machine Manager]**

### Other Links:
[VFIO article] | [VFIO forum] | [PCI Passthrough Guide]

## Table of Contents
- [Why?](#why)
- [Contact](#contact)

## Contents
### Why?
The virtual machine manager application `virt-manager` does not (currently) have the option to wake a VM from Sleep.
That is unfortunate, as a VM cannot be awaken from normal and expected means (wake from USB keyboard or network activity).
This application fixes that issue, with a nice Frontend to boot.

### Contact
Did you encounter a bug? Do you need help? Notice any dead links? Please contact by [raising an issue] with the project itself.

## TODO:
- [ ] create GTK3 project.
- [ ] draw GUI layout.
- [ ] gather Linux shell commands.
- [ ] create Python classes.
- [ ] add CLI commands?
- [ ] test.
- [ ] create first release.

[View latest release]: [parent]powerstate-virtmanager/releases/latest
[View develop branch]: [parent]powerstate-virtmanager/tree/develop

[Deploy VFIO]: [parent]deploy-VFIO
[Auto X.Org]: [parent]auto-xorg
[Generate Evdev]: [parent]generate-evdev
[Guest Machine Guide]: [parent]guest-machine-guide
[Libvirt Hooks]: [parent]libvirt-hooks
[Power State Virtual Machine Manager]: [parent]powerstate-virtmanager

[VFIO Article]: https://www.kernel.org/doc/html/latest/driver-api/vfio.html
[VFIO Forum]: https://old.reddit.com/r/VFIO
[PCI Passthrough Guide]: https://wiki.archlinux.org/title/PCI_passthrough_via_OVMF

[raising an issue]: [parent]powerstate-virtmanager/issues

[parent]: https://github.com/portellam/