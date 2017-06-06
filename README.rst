Pi OpenVPN
==========

Ansible playbook to install OpenVPN on a Raspberry Pi

Quick instructions
------------------

1. Download Raspbian Jessie lite from `raspberrypi.org <https://www.raspberrypi.org/downloads/raspbian/>`_
   and install it on your Raspberry Pi

2. Clone this repository::

   $ git clone git@github.com:beenje/pi_openvpn.git

3. Update the variables in host_vars/raspberry. You should at least define::

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

4. Run the playbook::

   $ ansible-playbook -i hosts openvpn.yml

5. Get the clients configuration files from the Raspberry Pi::

   $ scp pi@raspberry:openvpn/clientside/files/*.ovpn .

6. Don't leave all the generated keys on your Pi!
   Even the CA is created with no password. Anyone accessing it could
   sign new requests! You can copy the openvpn directory to a USB stick
   before to remove it.
