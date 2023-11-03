Name:       firmware-pine64-pinetab2
Summary:    Firmware blobs for Pinetab 2
Version:    1.0
Release:    1
Group:      System/Firmware
License:    Redistributable
URL:        https://github.com/sailfish-on-dontbeevil/firmware-pine64-pinetab2
Source0:     %{name}-%{version}.tar.bz2
Source1:    bes2600_factory.txt
Source2:    best2002_fw_boot_sdio.bin
Source3:    best2002_fw_sdio_btrf.bin
Source4:    best2002_fw_sdio_nosignal.bin
Source5:    best2002_fw_sdio.bin

%description
This package contains firmware for the Pinephone Pro

%prep
ls -lhR .
%setup -q -n %{name}-%{version}

%build
ls -lR .

%install
pwd
ls -lR .
mkdir -p $RPM_BUILD_ROOT/lib/firmware/bes2600
cp %{SOURCE1} $RPM_BUILD_ROOT/lib/firmware/bes2600/
cp %{SOURCE2} $RPM_BUILD_ROOT/lib/firmware/bes2600/
cp %{SOURCE3} $RPM_BUILD_ROOT/lib/firmware/bes2600/
cp %{SOURCE4} $RPM_BUILD_ROOT/lib/firmware/bes2600/
cp %{SOURCE5} $RPM_BUILD_ROOT/lib/firmware/bes2600/

%files
/lib/firmware/
