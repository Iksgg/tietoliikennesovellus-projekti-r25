import numpy as np
import matplotlib.pyplot as plt
import pathlib
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

k= 6
max_iteration= 1000
tol= 1.0e-4
filepath = pathlib.Path(__file__).with_name("cleaned_data.csv")

try:
    X = np.loadtxt(filepath, delimiter=";")
    print(X[:5])
except FileNotFoundError:
    print("File not found")
    
'''
# Generates 6 random clusters of data will be change to use actual data
centers = np.array([
    [1200,1500,1500],
    [1800,1500,1500],
    [1500,1200,1500],
    [1500,1800,1500],
    [1500,1500,1200],
    [1500,1500,1800]
])

X, label = make_blobs(n_samples=1000, n_features=3, centers=centers, cluster_std=20, random_state=23)

x= X[:,0]
y= X[:,1]
z= X[:,2]
'''

#Starting points for cluster centers 
kmeans = KMeans(n_clusters=k, init='k-means++', 
                n_init=10)
kmeans.fit(X)
init_centers = kmeans.cluster_centers_


clusters={}
for i in range(k):
    clusters[i] = {'center':init_centers[i], 'points':[]}

#functions for calculating k means
def distance(p1,p2):
    return np.sqrt(np.sum((p1-p2)**2))

def assigne_clusters(X, clusters):
    for i in range(k):
        clusters[i]['points'] = []

    for idx in range(X.shape[0]):
        dist = [distance(X[idx], clusters[i]['center']) for i in range(k)]
        curr_cluster = np.argmin(dist)
        clusters[curr_cluster]['points'].append(X[idx])
    return(clusters)

def update_clusters(X, clusters):
    for i in range(k):
        points = np.array(clusters[i]['points'])
        if points.shape[0]>0:
            new_center = points.mean(axis=0)
            clusters[i]['center'] = new_center
            clusters[i]['points'] = []
    return(clusters)

def predict_cluster(X, clusters):
    pred= np.zeros(X.shape[0], dtype=int)
    for i in range(X.shape[0]):
        dist=[]
        for j in range(k):
            dist.append(distance(X[i],clusters[j]['center']))
        pred[i]= np.argmin(dist)
    return pred

def centers_changed(old_center, new_center, tol):
    movement = np.linalg.norm(new_center - old_center, axis=1)
    return np.any(movement > tol)


#Calculation of the centter point for clusters
for iteration in range(max_iteration):
    old_center = np.array([clusters[i]['center'] for i in range(k)])
    clusters = assigne_clusters(X,clusters)
    clusters = update_clusters(X,clusters)
    new_center = np.array([clusters[i]['center'] for i in range(k)])

    if iteration > 0 and not centers_changed(old_center, new_center, tol):
        print(f"Stoped at iteration {iteration}")
        print(f"Shape: {new_center.shape}")
        print(f"Centers:\n {new_center} ")
        break

pred = predict_cluster(X,clusters)

# Plots the generated clusters in xyz grid and coloring each cluster
fig = plt.figure(0)
ax = fig.add_subplot(projection="3d")

#Coloration for cluster
color = {
    0: "#0033cc",  
    1: "#66aaff",  
    2: "#008800",  
    3: "#66ff66",  
    4: "#cc0000",  
    5: "#ff6666"   
}

#Plotting of data points
for c_id in range(k):
    pts = X[pred == c_id]
    ax.scatter(pts[:,0],
               pts[:,1],
               pts[:,2],
                c=color[c_id])
                
#Plotting of cluster centers    
for i in clusters:
    center = clusters[i]['center']
    ax.scatter(center[0],center[1],center[2],marker ='*', c='y', s=200)

#Lines from center to data points
for idx in range(X.shape[0]):
    c_id = pred[idx]
    center = clusters[c_id]['center']
    ax.plot([X[idx,0],center[0]],
            [X[idx,1],center[1]],
            [X[idx,2],center[2]],
            c='gray', linestyle='--', alpha=0.5)


ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.grid(True)

plt.show()


#Saves center to .h file
max_x = np.argmax(new_center[:,0])
min_x = np.argmin(new_center[:,0])
max_y = np.argmax(new_center[:,1])
min_y = np.argmin(new_center[:,1])
max_z = np.argmax(new_center[:,2])
min_z = np.argmin(new_center[:,2])

file = open("keskipisteet.h","a")
file.write("int keskipisteet[6][3] = {\n")
file.write(f"{{{new_center[max_x][0]:.0f}, {new_center[max_x][1]:.0f}, {new_center[max_x][2]:.0f}}},\n")
file.write(f"{{{new_center[min_x][0]:.0f}, {new_center[min_x][1]:.0f}, {new_center[min_x][2]:.0f}}},\n")
file.write(f"{{{new_center[max_y][0]:.0f}, {new_center[max_y][1]:.0f}, {new_center[max_y][2]:.0f}}},\n")
file.write(f"{{{new_center[min_y][0]:.0f}, {new_center[min_y][1]:.0f}, {new_center[min_y][2]:.0f}}},\n")
file.write(f"{{{new_center[max_z][0]:.0f}, {new_center[max_z][1]:.0f}, {new_center[max_z][2]:.0f}}},\n")
file.write(f"{{{new_center[min_z][0]:.0f}, {new_center[min_z][1]:.0f}, {new_center[min_z][2]:.0f}}}\n")
file.write("};\n")
file.close()

