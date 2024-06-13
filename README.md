# Power State Virtual Machine Manager
Set the power state of a QEMU/KVM Virtual Machine (VM). Wake from Sleep or Hibernation. Does what `virt-manager` doesn't. Python and GTK3 GUI application.

**~Latest release~**

### Related Projects
[Deploy VFIO](https://github.com/portellam/deploy-VFIO) | [Auto X.Org](https://github.com/portellam/auto-xorg)** | [Generate Evdev](https://github.com/portellam/generate-evdev)

[Guest Machine Guide](https://github.com/portellam/guest-machine-guide) | [Libvirt Hooks](https://github.com/portellam/libvirt-hooks) | **[Power State Virtual Machine Manager](https://github.com/portellam/powerstate-virtmanager)**

### Other Links:
[What is VFIO?](#VFIO) | [VFIO Article](https://www.kernel.org/doc/html/latest/driver-api/vfio.html) | [VFIO Forum](https://old.reddit.com/r/VFIO) | [PCI Passthrough Guide](https://wiki.archlinux.org/title/PCI_passthrough_via_OVMF)

## Table of Contents
- [Why?](#why)
- [Contact](#contact)

## Contents
### Why?
The virtual machine manager application `virt-manager` does not (currently) have the option to wake a VM from Sleep.
That is unfortunate, as a VM cannot be awaken from normal and expected means (wake from USB keyboard or network activity).
This application fixes that issue, with a nice Frontend to boot.

## TODO:
- [ ] create GTK3 project.
- [ ] draw GUI layout.
- [ ] gather Linux shell commands.
- [ ] create Python classes.
- [ ] add CLI commands?
- [ ] test.
- [ ] create first release.

### Contact
Did you encounter a bug? Do you need help? Notice any dead links? Please contact by [raising an issue](https://github.com/portellam/powerstate-virtmanager/issues) with the project itself.
