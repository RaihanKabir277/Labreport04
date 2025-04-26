
import random
import math
import csv

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cluster = None


class KMeans:
    def __init__(self, points, clusters):
        self.points = points
        self.clusters = clusters
        self.mat = [[0 for _ in range(50)] for _ in range(50)]  # 50x50 grid
        self.fkc = []
        self.start()

    def start(self):
        self.p = []
        self.k = []
        with open('data.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Type'] == 'Point':
                    self.p.append(Point(int(row['X']), int(row['Y'])))
                elif row['Type'] == 'Center':
                    self.k.append(Point(int(row['X']), int(row['Y'])))

        count = 0
        while True:
            for i in range(self.points):
                min_dist = float('inf')
                for j in range(self.clusters):
                    d1 = abs(self.k[j].x - self.p[i].x) + abs(self.k[j].y - self.p[i].y)
                    if d1 < min_dist:
                        self.p[i].cluster = j
                        min_dist = d1

            kdup = [Point(self.k[i].x, self.k[i].y) for i in range(self.clusters)]

            for j in range(self.clusters):
                x, y, ci = 0, 0, 0
                for i in range(self.points):
                    if self.p[i].cluster == j:
                        x += self.p[i].x
                        y += self.p[i].y
                        ci += 1
                if ci != 0:
                    self.k[j].x = x // ci
                    self.k[j].y = y // ci

            err = 0
            for i in range(self.clusters):
                err += abs(self.k[i].x - kdup[i].x) + abs(self.k[i].y - kdup[i].y)

            count += 1
            if err == 0:
                break

        for p in self.p:
            self.mat[p.x][p.y] = p.cluster + 1  

        for center in self.k:
            self.mat[center.x][center.y] = 'C'

        for i in range(self.clusters):
            intra_distance = sum(
                abs(self.k[i].x - p.x) + abs(self.k[i].y - p.y)
                for p in self.p if p.cluster == i
            )
            print(f"Cluster {i + 1} Intra-distance = {intra_distance}")

        for i in range(self.clusters):
            for p in self.p:
                if p.cluster == i:
                    print(f"Point ({p.x}, {p.y}) Cluster - {p.cluster + 1}")

        for i, center in enumerate(self.k):
            print(f"Cluster {i + 1} Center - ({center.x}, {center.y})")

        print("\nMatrix Visualization:\n")
        for i in range(50):
            for j in range(50):
                if self.mat[i][j] == 0:
                    print(".", end=" ")
                elif self.mat[i][j] == 'C':
                    print("C", end=" ")
                else:
                    print(self.mat[i][j], end=" ")
            print()

def generate_data(points, clusters):
    with open('data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Type", "X", "Y"])
        for _ in range(points):
            x = random.randint(0, 49)
            y = random.randint(0, 49)
            writer.writerow(["Point", x, y])
        for _ in range(clusters):
            x = random.randint(0, 49)
            y = random.randint(0, 49)
            writer.writerow(["Center", x, y])

def main():
    points = 100
    clusters = 10
    generate_data(points, clusters)
    kmeans = KMeans(points, clusters)

if __name__ == "__main__":
    main()
