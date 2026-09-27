{ pkgs }: {
  deps = [
    pkgs.python310
    pkgs.libxcrypt
    pkgs.python310Packages.pip
  ];
}
