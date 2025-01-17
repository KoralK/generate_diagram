import os

# Define the DOT content for each diagram
vpc_peering_dot = """
digraph G {
    rankdir=LR; // Left-to-right layout
    node [shape=box, style=rounded, fillcolor="#dae8fc", color="#6c8ebf"];

    VPC_A [label="VPC Network A\\nSubnet: 10.0.1.0/24"];
    VPC_B [label="VPC Network B\\nSubnet: 10.0.2.0/24"];

    VPC_A -> VPC_B [label="VPC Peering", color="#333", fontcolor="#333"];
}
"""

cloud_vpn_dot = """
digraph G {
    rankdir=LR;
    node [shape=box, style=rounded, fillcolor="#dae8fc", color="#6c8ebf"];

    VPC [label="Google Cloud VPC\\nSubnets: us-east1, us-west1"];
    OnPrem [label="On-Premises Network"];

    VPC -> OnPrem [label="IPsec VPN Tunnel", color="#333", fontcolor="#333"];
}
"""

cloud_interconnect_dot = """
digraph G {
    rankdir=LR;
    node [shape=box, style=rounded, fillcolor="#dae8fc", color="#6c8ebf"];

    GoogleCloud [label="Google Cloud"];
    OnPrem [label="On-Premises Network"];
    ColoFacility [label="Co-Location Facility"];

    GoogleCloud -> ColoFacility [label="Dedicated Interconnect", color="#333", fontcolor="#333"];
    ColoFacility -> OnPrem [label="Cross-Connect", color="#333", fontcolor="#333"];
}
"""

ha_vpn_dot = """
digraph G {
    rankdir=LR;
    node [shape=box, style=rounded, fillcolor="#dae8fc", color="#6c8ebf"];

    HA_VPN [label="HA VPN Gateway"];
    Peer1 [label="Peer Device 1"];
    Peer2 [label="Peer Device 2"];

    HA_VPN -> Peer1 [label="Tunnel 1", color="#333", fontcolor="#333"];
    HA_VPN -> Peer2 [label="Tunnel 2", color="#333", fontcolor="#333"];
}
"""

# Save the DOT content to files
def save_dot_file(filename, content):
    with open(filename, "w") as file:
        file.write(content)
    print(f"DOT file saved: {filename}")

# Generate SVG files from DOT files using Graphviz
def generate_svg(dot_filename, svg_filename):
    os.system(f"dot -Tsvg {dot_filename} -o {svg_filename}")
    print(f"SVG file generated: {svg_filename}")

# Generate the DOT and SVG files
dot_files = {
    "vpc-peering.dot": vpc_peering_dot,
    "cloud-vpn.dot": cloud_vpn_dot,
    "cloud-interconnect.dot": cloud_interconnect_dot,
    "ha-vpn.dot": ha_vpn_dot,
}

for dot_filename, content in dot_files.items():
    # Save the DOT file
    save_dot_file(dot_filename, content)

    # Generate the corresponding SVG file
    svg_filename = dot_filename.replace(".dot", ".svg")
    generate_svg(dot_filename, svg_filename)

print("All DOT and SVG files generated successfully!")