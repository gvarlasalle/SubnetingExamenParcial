import ipaddress

def subnet_planner(ip, num_subnets, max_hosts_per_subnet):
    try:
        # Crea un objeto IPv4Network utilizando la dirección IP proporcionada
        network = ipaddress.IPv4Network(ip, strict=False)

        # Calcula la máscara de subred óptima para el número máximo de hosts necesarios
        prefix_length = 0
        while 2 ** prefix_length - 2 < max_hosts_per_subnet:
            prefix_length += 1

        # Divide la red original en subredes con la máscara de subred calculada
        subnets = list(network.subnets(new_prefix=network.prefixlen + prefix_length))

        # Verifica si el número de subredes es suficiente
        if len(subnets) < num_subnets:
            print("No se pueden crear la cantidad de subredes especificadas con la máscara de subred y dirección IP proporcionadas.")
        else:
            print(f"Red Original: {network.network_address}/{network.prefixlen}")
            print(f'Máscara de Subred: /{network.prefixlen + prefix_length}')
            print(f"Número de hosts disponibles por subred: {2 ** prefix_length - 2}")
            print("\nSubredes:")
            for i, subnet in enumerate(subnets[:num_subnets]):
                print(f"Subred {i + 1}: {subnet.network_address}/{subnet.prefixlen}")
                print(f'Número de hosts disponibles: {2 ** prefix_length - 2}')
                print('-' * 30)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    ip = input("Introduce la dirección IP (Ejemplo: 192.168.10.0/24): ")
    num_subnets = int(input("Introduce la cantidad de subredes que necesitas: "))
    max_hosts_per_subnet = int(input("Introduce la cantidad máxima de hosts necesarios por subred: "))

    subnet_planner(ip, num_subnets, max_hosts_per_subnet)
