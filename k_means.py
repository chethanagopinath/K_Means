import math  

centroids_changed = True

def clustering_datapoints(data_points, centroids, k):
    # Initiate empty clusters and set keys in range of k
    clusters = {}
    for i in range(k):
        clusters[i] = []

    for data in data_points:
        # Set up list of euclidian distance and iterate through
        euclidean_dist = []
        for j in range(k):
            centroid = centroids[j]
            dist = math.sqrt((data[0] - centroid[0]) ** 2 + (data[1] - centroid[1]) ** 2)
            euclidean_dist.append(dist)
        # Find min euclidean distance index cluster and append the data point to the right cluster
        clusters[euclidean_dist.index(min(euclidean_dist))].append(data)
    # Displaying clusters
    for i in range(0, k):
        print("Cluster ", centroids[i] ," : ", clusters[i])
    return clusters  

def recalculate_centroids(centroids, clusters, k):
    global centroids_changed
    centroids_changed = False
    for i in range(k):
        x, y = 0, 0
        element = []
        # Finds the average of the cluster at given index
        for point in clusters[i]:
            x += point[0]
            y += point[1]
        element.append(x / len(clusters[i]))
        element.append(y / len(clusters[i]))
        # Extracting old mean and checking both old x and old y coordinates with the new x and new y coordinates
        old_mean = centroids[i]
        if old_mean != element:
            centroids_changed = True
        centroids[i] = element
    # Displaying centroids
    for i in range(0, k):
        print("Centroids for cluster ", (i + 1), " : ", centroids[i])
    return centroids

def sum_of_squares_error(centroids, k, clusters):
    dist = 0
    for key, values in clusters.items():
        for value in values:
            centroid = centroids[key]
            dist += (value[0] - centroid[0]) ** 2 + (value[1] - centroid[1]) ** 2
    #print("Sum of Squared Error : ", dist)
    return dist

def k_means(data_points, means, k, centroids = {} ):
    for i in range(k):
        # Setting up centroids with given initial centroids based on number of clusters
        centroids[i] = means[i]
    count = 1 
    # iterate until centroids do not change
    while centroids_changed:  
        print("\nIteration count : ", count)  
        # Clustering data points    
        clusters = clustering_datapoints(data_points, centroids, k)

        # Recalculating means/centroids 
        centroids = recalculate_centroids(centroids, clusters, k)

        # Computing sum of squares error
        sum_squares_error = sum_of_squares_error(centroids, k , clusters)
        
        #Displaying sum of squares errors
        print("Sum of Squared Error : ", sum_squares_error)
        count += 1

if __name__ == '__main__':
    k = 3
    means = [[2, 3], [3, 3], [5, 4]]
    print("-" * 45)
    print("K Means implementation for given 2D dataset")
    print("-" * 45)

    data_points = [[1,1],
        [1,2],
        [2,1],
        [2,3],
        [3,3],
        [4,5],
        [5,4],
        [6,5]]
    k_means(data_points, means, k)