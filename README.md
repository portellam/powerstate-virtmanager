# Power State Virtual Machine Manager
Set the power state of a QEMU/KVM Virtual Machine (VM). Wake from Sleep or Hibernation. Python and GTK3 GUI application.

**[View master branch...](https://github.com/portellam/pwrstat-virtman/tree/master)**

#### Related Projects:
**[Auto Xorg](https://github.com/portellam/auto-Xorg) | [Deploy VFIO](https://github.com/portellam/deploy-vfio) | [Generate Evdev](https://github.com/portellam/generate-evdev) | [Guest Machine Guide](https://github.com/portellam/guest-machine-guide) | | [Libvirt Hooks](https://github.com/portellam/libvirt-hooks)**

## Table of Contents
- [Why?](#why)

## Contents

# Why?
The virtual machine manager application *virt-manager* does not (currently) have the option to wake a VM from S3 sleep.
That is unfortunate, as a VM cannot be awaken from normal and expected means (wake from USB keyboard or network activity).
This application fixes that issue, with a nice Frontend.

## TODO:
- [ ] create GTK3 project.
- [ ] draw GUI layout.
- [ ] gather Linux shell commands.
- [ ] create Python classes.
- [ ] Test.
