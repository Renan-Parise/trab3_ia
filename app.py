import networkx as nx
import matplotlib.pyplot as plt

points_of_interest = {
    "Ginásio": (0, 0),
    "Refeitório": (10, 20),
    "Cantina": (15, 30),
    "Guarita": (25, 40),
    "Biblioteca e Pedagógico": (35, 50),
    "Auditório": (45, 15),
    "Laboratórios": (55, 30),
    "Galpão de Máquinas": (65, 5),
    "Salas de Aula": (75, 60),
    "Administrativo": (85, 20),
    "Estacionamento Descoberto": (95, 40),
    "Garagem Coberta Aberta": (105, 60),
    "Subestação": (115, 30)
}

campus_graph = nx.Graph()

for poi, coord in points_of_interest.items():
    campus_graph.add_node(poi, pos=coord)

edges_with_distances = [
    ("Refeitório", "Ginásio", 20), ("Cantina", "Ginásio", 30), ("Guarita", "Ginásio", 40), 
    ("Biblioteca e Pedagógico", "Ginásio", 50), ("Auditório", "Ginásio", 60), 
    ("Laboratórios", "Ginásio", 30), ("Galpão de Máquinas", "Ginásio", 40), 
    ("Salas de Aula", "Ginásio", 60), ("Administrativo", "Ginásio", 25), 
    ("Estacionamento Descoberto", "Ginásio", 40), ("Garagem Coberta Aberta", "Ginásio", 50), 
    ("Subestação", "Ginásio", 40), ("Cantina", "Refeitório", 10), ("Guarita", "Refeitório", 30),
    ("Biblioteca e Pedagógico", "Refeitório", 25), ("Auditório", "Refeitório", 20), 
    ("Laboratórios", "Refeitório", 25), ("Galpão de Máquinas", "Refeitório", 40),
    ("Salas de Aula", "Refeitório", 30), ("Administrativo", "Refeitório", 20), 
    ("Estacionamento Descoberto", "Refeitório", 50), ("Garagem Coberta Aberta", "Refeitório", 55), 
    ("Subestação", "Refeitório", 60), ("Guarita", "Cantina", 35), ("Biblioteca e Pedagógico", "Cantina", 40),
    ("Auditório", "Cantina", 15), ("Laboratórios", "Cantina", 20), ("Galpão de Máquinas", "Cantina", 45),
    ("Salas de Aula", "Cantina", 35), ("Administrativo", "Cantina", 25), 
    ("Estacionamento Descoberto", "Cantina", 50), ("Garagem Coberta Aberta", "Cantina", 55), 
    ("Subestação", "Cantina", 60), ("Biblioteca e Pedagógico", "Guarita", 30), 
    ("Auditório", "Guarita", 40), ("Laboratórios", "Guarita", 25), ("Galpão de Máquinas", "Guarita", 40),
    ("Salas de Aula", "Guarita", 50), ("Administrativo", "Guarita", 20), 
    ("Estacionamento Descoberto", "Guarita", 60), ("Garagem Coberta Aberta", "Guarita", 70),
    ("Subestação", "Guarita", 40), ("Auditório", "Biblioteca e Pedagógico", 10), 
    ("Laboratórios", "Biblioteca e Pedagógico", 15), ("Galpão de Máquinas", "Biblioteca e Pedagógico", 35),
    ("Salas de Aula", "Biblioteca e Pedagógico", 20), ("Administrativo", "Biblioteca e Pedagógico", 15), 
    ("Estacionamento Descoberto", "Biblioteca e Pedagógico", 40), ("Garagem Coberta Aberta", "Biblioteca e Pedagógico", 50), 
    ("Subestação", "Biblioteca e Pedagógico", 45), ("Laboratórios", "Auditório", 25), 
    ("Galpão de Máquinas", "Auditório", 40), ("Salas de Aula", "Auditório", 30), 
    ("Administrativo", "Auditório", 20), ("Estacionamento Descoberto", "Auditório", 50), 
    ("Garagem Coberta Aberta", "Auditório", 55), ("Subestação", "Auditório", 40), 
    ("Galpão de Máquinas", "Laboratórios", 40), ("Salas de Aula", "Laboratórios", 30), 
    ("Administrativo", "Laboratórios", 20), ("Estacionamento Descoberto", "Laboratórios", 50), 
    ("Garagem Coberta Aberta", "Laboratórios", 60), ("Subestação", "Laboratórios", 50), 
    ("Salas de Aula", "Galpão de Máquinas", 40), ("Administrativo", "Galpão de Máquinas", 30), 
    ("Estacionamento Descoberto", "Galpão de Máquinas", 50), ("Garagem Coberta Aberta", "Galpão de Máquinas", 60), 
    ("Subestação", "Galpão de Máquinas", 55), ("Administrativo", "Salas de Aula", 30), 
    ("Estacionamento Descoberto", "Salas de Aula", 50), ("Garagem Coberta Aberta", "Salas de Aula", 60), 
    ("Subestação", "Salas de Aula", 55), ("Estacionamento Descoberto", "Administrativo", 40), 
    ("Garagem Coberta Aberta", "Administrativo", 50), ("Subestação", "Administrativo", 45), 
    ("Garagem Coberta Aberta", "Estacionamento Descoberto", 20), 
    ("Subestação", "Estacionamento Descoberto", 30), ("Subestação", "Garagem Coberta Aberta", 25)
]

for edge in edges_with_distances:
    campus_graph.add_edge(edge[0], edge[1], weight=edge[2])

def find_shortest_path(graph, start, end):
    try:
        shortest_path = nx.dijkstra_path(graph, start, end, weight='weight')
        path_length = nx.dijkstra_path_length(graph, start, end, weight='weight')
        print(f"Caminho mais curto entre {start} e {end}: {shortest_path}")
        print(f"Distância total: {path_length} unidades")
        return shortest_path
    except nx.NetworkXNoPath:
        print(f"Não existe caminho entre {start} e {end}.")
        return []

print("Lista de pontos de interesse: ")
for poi in points_of_interest:
    print(poi)

partida = input("Digite o ponto de partida: ")
chegada = input("Digite o ponto de chegada: ")

caminho_mais_curto = find_shortest_path(campus_graph, partida, chegada)

plt.figure(figsize=(14, 10))

node_colors = ['lightgreen' if 'Estacionamento' in node or 'Garagem' in node else 'lightblue' for node in campus_graph.nodes]

pos = nx.get_node_attributes(campus_graph, 'pos')
weights = nx.get_edge_attributes(campus_graph, 'weight')

nx.draw(
    campus_graph,
    pos,
    with_labels=True,
    node_size=4000,
    node_color=node_colors,
    font_size=9,
    font_weight="bold",
    edge_color="gray",
    width=1,
)

path_edges = list(zip(caminho_mais_curto, caminho_mais_curto[1:]))
nx.draw_networkx_edges(campus_graph, pos, edgelist=path_edges, edge_color="red", width=4)

nx.draw_networkx_edge_labels(campus_graph, pos, edge_labels=weights, font_size=9)

plt.title("Mapa do Campus IFC Videira - Todos os Caminhos Possíveis e o Mais Curto", fontsize=15, fontweight="bold")
plt.show()
