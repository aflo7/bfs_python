from createGraph import create_graph_and_run_bfs


def main():
    create_graph_and_run_bfs(1, 25, 50)
    create_graph_and_run_bfs(2, 50, 200)
    create_graph_and_run_bfs(3, 100, 800)
    create_graph_and_run_bfs(4, 200, 3200)


if __name__ == "__main__":
    main()
