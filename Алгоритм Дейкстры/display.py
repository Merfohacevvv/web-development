from math import isinf
from random import randint
import matplotlib.pyplot as plt
import networkx as nx


def my_draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=None,
    label_pos=0.5,
    font_size=10,
    font_color="k",
    font_family="sans-serif",
    font_weight="normal",
    alpha=None,
    bbox=None,
    horizontalalignment="center",
    verticalalignment="center",
    ax=None,
    rotate=True,
    clip_on=True,
    rad=0
):
    
    import matplotlib.pyplot as plt
    import numpy as np

    if ax is None:
        ax = plt.gca()
    if edge_labels is None:
        labels = {(u, v): d for u, v, d in G.edges(data=True)}
    else:
        labels = edge_labels
    text_items = {}
    for (n1, n2), label in labels.items():
        (x1, y1) = pos[n1]
        (x2, y2) = pos[n2]
        (x, y) = (
            x1 * label_pos + x2 * (1.0 - label_pos),
            y1 * label_pos + y2 * (1.0 - label_pos),
        )
        pos_1 = ax.transData.transform(np.array(pos[n1]))
        pos_2 = ax.transData.transform(np.array(pos[n2]))
        linear_mid = 0.5*pos_1 + 0.5*pos_2
        d_pos = pos_2 - pos_1
        rotation_matrix = np.array([(0,1), (-1,0)])
        ctrl_1 = linear_mid + rad*rotation_matrix@d_pos
        ctrl_mid_1 = 0.5*pos_1 + 0.5*ctrl_1
        ctrl_mid_2 = 0.5*pos_2 + 0.5*ctrl_1
        bezier_mid = 0.5*ctrl_mid_1 + 0.5*ctrl_mid_2
        (x, y) = ax.transData.inverted().transform(bezier_mid)

        if rotate:
            # in degrees
            angle = np.arctan2(y2 - y1, x2 - x1) / (2.0 * np.pi) * 360
            # make label orientation "right-side-up"
            if angle > 90:
                angle -= 180
            if angle < -90:
                angle += 180
            # transform data coordinate angle to screen coordinate angle
            xy = np.array((x, y))
            trans_angle = ax.transData.transform_angles(
                np.array((angle,)), xy.reshape((1, 2))
            )[0]
        else:
            trans_angle = 0.0
        # use default box of white with white border
        if bbox is None:
            bbox = dict(boxstyle="round", ec=(1.0, 1.0, 1.0), fc=(1.0, 1.0, 1.0))
        if not isinstance(label, str):
            label = str(label)  # this makes "1" and 1 labeled the same

        t = ax.text(
            x,
            y,
            label,
            size=font_size,
            color=font_color,
            family=font_family,
            weight=font_weight,
            alpha=alpha,
            horizontalalignment=horizontalalignment,
            verticalalignment=verticalalignment,
            rotation=trans_angle,
            transform=ax.transData,
            bbox=bbox,
            zorder=1,
            clip_on=clip_on,
        )
        text_items[(n1, n2)] = t

    ax.tick_params(
        axis="both",
        which="both",
        bottom=False,
        left=False,
        labelbottom=False,
        labelleft=False,
    )

    return text_items
def draw_result(S, cities_names, route):
    G = nx.DiGraph()
    options = ['#59FA6F', '#DCBAFA']
    colors = []
    color_map = []
    style = []
    width = []
    ar_size = []

    for city in range(len(cities_names)):
        G.add_node(cities_names[city], pos=(randint(0, len(cities_names)^2), city))
        if city in [route[0], route[-1]]:
            color_map.append('#8BFF8F')

        else:
            color_map.append('#e2e2ff')



    edge_list = []
    for from_city in range(len(cities_names)):
        for to_city in range(len(cities_names)):
            if (S[from_city][to_city] != 0 and not isinf(S[from_city][to_city])):
                if from_city in route and from_city != route[-1] and route[route.index(from_city)+1] == to_city:
                    colors.append(options[0])
                    style.append('-')
                    tuple1 = (cities_names[from_city], cities_names[to_city], {'w':S[from_city][to_city]})
                    edge_list.append(tuple1)
                    width.append(3)
                    ar_size.append(20)
                else:
                    colors.append(options[1])
                    style.append('--')
                    tuple2 = (cities_names[from_city], cities_names[to_city], {'w':S[from_city][to_city]})
                    edge_list.append(tuple2)
                    width.append(1.1)
                    ar_size.append(14)

    G.add_edges_from(edge_list)
    pos = nx.spring_layout(G, seed=5)

    fig, ax = plt.subplots()
    nx.draw(G, pos, ax=ax, font_weight='medium', with_labels=True, font_size = 15, node_color=color_map, edge_color=colors, arrowsize=ar_size, width=width, style = style)
    nx.draw_networkx_labels(G, pos, ax=ax, font_size = 15)
    labels = nx.get_edge_attributes(G, 'weight')
    edge_labels = dict([((u, v,), d['w'])
                        for u, v, d in G.edges(data=True)])
    nx.draw_networkx_edges(G, pos, ax=ax, edgelist=labels, edge_color=colors,  width=width)
    nx.draw_networkx_edge_labels(G, pos, ax=ax, edge_labels=edge_labels, label_pos=0.25, font_size=9)

    plt.show()
