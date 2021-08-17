#!/usr/bin/python3

from ipaddress import IPv4Interface


class Router:
    def __init__(self, name, max_count_of_interfaces):
        self.__name = name
        self.__count_of_interfaces = 0
        self.__max_count_of_interfaces = max_count_of_interfaces
        self.__interfaces = []
        self.__internal_routes = []
        self.__external_routes = {}  # {gateway, [interfaces of another remote router]}

    def add_interface(self, interface):
        if isinstance(interface, IPv4Interface):
            if interface not in self.__interfaces:
                if self.__count_of_interfaces < self.__max_count_of_interfaces:

                    # Add interface to list of internal interfaces
                    self.__interfaces.append(interface)
                    self.__count_of_interfaces = self.__count_of_interfaces + 1

                    # Add interface to list of internal routes
                    self.__internal_routes.append(interface)
                else:
                    print("You cannot add the interface.")
            else:
                print("This interface already exists on this router.")
        else:
            print("This object is not an object of the 'IPv4Interface' class.")

    def delete_interface(self, interface):
        if isinstance(interface, IPv4Interface):
            if interface in self.__interfaces:

                # Delete interface from the list of interfaces
                self.__interfaces.remove(interface)
                self.__count_of_interfaces = self.__count_of_interfaces - 1

                # Delete interface from the list of internal routes
                self.__internal_routes.remove(interface)

                # Delete interface from the list of external routes
                try:
                    for gateway in self.__external_routes:
                        if interface.network == gateway.network:
                            list_of_dest_to_removing = self.__external_routes[gateway]
                            for dest in list_of_dest_to_removing:
                                self.delete_route(dest, gateway)
                except RuntimeError:
                    for gateway in self.__external_routes:
                        if interface.network == gateway.network:
                            list_of_dest_to_removing = self.__external_routes[gateway]
                            for dest in list_of_dest_to_removing:
                                self.delete_route(dest, gateway)
            else:
                print("This interface is absent on this router.")
        else:
            print("This object is not an object of the 'IPv4Interface' class.")

    def print_interfaces(self):
        print("Router interfaces with IP addresses:")
        for interface in self.__interfaces:
            print("IP address of the interface -> " + interface.__str__())

    def add_route(self, remote_interface, gateway):
        if isinstance(gateway, IPv4Interface):
            if isinstance(remote_interface, IPv4Interface):
                # Throws an exception if intermediate route is absent
                # Catches this exception and prints a message when the exception was thrown
                try:
                    if self.__is_gateway_available(gateway):
                        if gateway not in self.__external_routes:
                            self.__external_routes[gateway] = [remote_interface]
                        else:
                            self.__external_routes.get(gateway).append(remote_interface)
                    else:
                        raise ValueError("No route to specified gateway.")
                except ValueError:
                    print('Exception: \n  You cannot add this route. \n  Intermediate routes are absent.')
            else:
                print("The object 'ip_v4_interface' is not the object of the 'IPv4Interface' class.")
        else:
            print("The object 'gateway' is not the object of the 'IPv4Interface' class.")

    def print_routes(self):
        print("Internal routes:")
        for internal_route in self.__internal_routes:
            print("The router has an internal route to -> network " + internal_route.network.__str__())
        print("External routes:")
        for gateway in self.__external_routes:
            for destination in self.__external_routes[gateway]:
                print("Gateway " + gateway.__str__() +
                      " provides an access to -> network " + destination.network.__str__())

    def delete_route(self, remote_interface, gateway):
        if isinstance(gateway, IPv4Interface) and isinstance(remote_interface, IPv4Interface):
            if gateway in self.__external_routes and remote_interface in self.__external_routes[gateway]:
                self.__external_routes[gateway].remove(remote_interface)
                if len(self.__external_routes[gateway]) == 0:
                    self.__external_routes.pop(gateway)
                self.__delete_linked_routes(remote_interface)
            else:
                print("The specified route is absent in the table")
        else:
            print("'ip_v4_interface' or 'gateway' is not an object of the class IPv4Interface")

    def __delete_linked_routes(self, remote_interface):
        try:
            for gate_key in self.__external_routes:
                if remote_interface.network == gate_key.network:
                    self.__external_routes.pop(gate_key, None)
        except RuntimeError:
            for gate_key in self.__external_routes:
                if remote_interface.network == gate_key.network:
                    self.__external_routes.pop(gate_key, None)

    def __is_gateway_available(self, gateway):
        for element_int in self.__internal_routes:
            if gateway.network == element_int.network:
                return True
        for list_of_routes in self.__external_routes.values():
            for element_ext in list_of_routes:
                if gateway.network == element_ext.network:
                    return True
        return False


print("========================= Starting the program ======================================================")
print("========================= Saving objects ============================================================")

router1 = Router("router1", 4)
router1.add_interface(IPv4Interface("192.168.5.14/24"))
router1.add_route(IPv4Interface("172.16.0.0/16"), IPv4Interface("192.168.5.1/24"))  # ok
router1.add_route(IPv4Interface("172.24.0.0/16"), IPv4Interface("192.168.8.1/24"))  # exception
router1.add_route(IPv4Interface("172.24.0.0/16"), IPv4Interface("172.16.8.1/16"))  # ok

print("========================= Objects are saved =========================================================")
print("========================= Checking: saving objects ==================================================")

router1.print_interfaces()
router1.print_routes()

print("========================= Deleting objects ==========================================================")

router1.delete_interface(IPv4Interface("192.168.5.14/24"))
# router1.delete_route(IPv4Interface("172.24.0.0/16"), IPv4Interface("172.16.8.1/16"))
# router1.delete_route(IPv4Interface("172.16.0.0/16"), IPv4Interface("192.168.5.1/24"))

print("========================= Objects are deleted =======================================================")
print("========================= Check: deleting objects ===================================================")

router1.print_interfaces()
router1.print_routes()
