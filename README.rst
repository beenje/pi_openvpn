Pi OpenVPN
==========

Ansible playbook to install OpenVPN on a Raspberry Pi

Quick instructions
------------------

1. Download Raspbian Jessie lite from `raspberrypi.org <https://www.raspberrypi.org/downloads/raspbian/>`_
   and install it on your Raspberry Pi

2. Clone this repository::

   $ git clone git@github.com:beenje/pi_openvpn.git

3. Build the Diffie-Hellman key::

   $ wget https://github.com/OpenVPN/easy-rsa/releases/download/3.0.1/EasyRSA-3.0.1.tgz
   $ tar xfz EasyRSA-3.0.1.tgz
   $ cd EasyRSA-3.0.1
   $ ./easyrsa init-pki
   $ ./easyrsa gen-dh

4. The generated key is *EasyRSA-3.0.1/pki/dh.pem*

5. Update the variables in host_vars/raspberry:

   .. include:: host_vars/raspberry
      :code:

6. Run the playbook::

   $ ansible-playbook -i hosts openvpn.yml

7. Get the clients configuration files from the Raspberry Pi::

   $ scp pi@raspberry:openvpn/clientside/files/*.ovpn .

8. Don't leave all the generated keys on your Pi!
   Even the CA is created with no password. Anyone accessing it could
   sign new requests! You can copy the openvpn directory to a USB stick
   before to remove it.



