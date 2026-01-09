# These and other macros are documented in ../droid-configs-device/droid-configs.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device RMX3852
%define vendor realme

%define vendor_pretty Realme
%define device_pretty GT Neo 6
%define dcd_path ./

# We assume most devices will
%define have_modem 1
%define android_version_major 16

# Device-specific usb-moded configuration
Provides: usb-moded-configs

# Device-specific ofono configuration
Provides: ofono-configs
Conflicts: ofono-configs-binder
Obsoletes: ofono-configs-mer

Obsoletes: qt5-qpa-surfaceflinger-plugin

# Community HW adaptations need this
%define community_adaptation 1

# Pixel ratio 1.0 was originally jolla phone with 245ppi, and the devices
# should roughly have their ppi compared to that. Large displays can use
# bigger ratio if seen fit. Values are with 0.25 increments.
%define pixel_ratio 1.0

%include droid-configs-device/droid-configs.inc
%include patterns/patterns-sailfish-device-adaptation-hammerhead.inc
%include patterns/patterns-sailfish-device-configuration-hammerhead.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

