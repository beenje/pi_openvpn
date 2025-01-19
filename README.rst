Pi OpenVPN
==========

Ansible playbook to install OpenVPN on a Raspberry Pi

Quick instructions
------------------

1. Download Raspbian bookworm lite from `raspberrypi.org <https://www.raspberrypi.org/downloads/raspbian/>`_
   and install it on your Raspberry Pi

1. Clone this repository::

   $ git clone git@github.com:beenje/pi_openvpn.git

1. Build the Diffie-Hellman key::

   $ wget https://github.com/OpenVPN/easy-rsa/releases/download/v3.2.1/EasyRSA-3.2.1.tgz
   $ tar xfz EasyRSA-3.2.1.tgz
   $ cd EasyRSA-3.2.1
   $ ./easyrsa init-pki
   $ ./easyrsa gen-dh

1. The generated key is *EasyRSA-3.2.1/pki/dh.pem*

1. Update the variables in host_vars/raspberry. You should at least define::

    # Static Internet hostname
    openvpn_server: my.raspberry.example.org
    # List of client configurations to create
    openvpn_clients:
      - client1
      - client2
    # List of subnets behind the server you want to access
    # You probably want to put your internal LAN
    private_subnets:
      - 192.168.10.0 255.255.255.0
    # Full path of the Diffie-Hellman key generated locally
    openvpn_dh: /path/to/dh.pem

1. Run the playbook::

   $ ansible-playbook -i hosts openvpn.yml

1. Get the clients configuration files from the Raspberry Pi::

   $ scp pi@raspberry:openvpn/clientside/files/*.ovpn .

1. Don't leave all the generated keys on your Pi!
   Even the CA is created with no password. Anyone accessing it could
   sign new requests! You can copy the openvpn directory to a USB stick
   before to remove it.
