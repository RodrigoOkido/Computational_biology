# This program attend to read data from a csv file,
# and apply kmean, then output the result.

from pylab            import plot,show
from numpy            import vstack,array
from numpy.random     import rand
from scipy.cluster.vq import kmeans, vq, whiten

import csv

if __name__ == "__main__":

    # clusters
    K = 2

    data_arr = []
    meal_name_arr = []

    # Output.csv is the transpose data of the leukemia_big
    with open('output.csv', 'rb') as f:
        reader = csv.reader(f)
        # next(reader)
        for row in reader:
            data_arr.append([float(x) for x in row[1:]])
            meal_name_arr.append([row[0]])

    data = vstack( data_arr )
    meal_name = vstack(meal_name_arr)

    # normalization
    data = whiten(data)

    # computing K-Means with K (clusters)
    centroids, distortion = kmeans(data,K)
    print "distortion = " + str(distortion)

    # assign each sample to a cluster
    idx,_ = vq(data,centroids)

    # some plotting using numpy's logical indexing
    plot(data[idx==0,0], data[idx==0,1],'ob',
         data[idx==1,0], data[idx==1,1],'or',
         data[idx==2,0], data[idx==2,1],'og')

    print meal_name
    print data

    for i in range(K):
        result_names = meal_name[idx==i, 0]
        counter = len(result_names)
        print "Cluster " + str(i+1)
        for name in result_names:
            print name
        print counter


    plot(centroids[:,0],
         centroids[:,1],
         'sg',markersize=8)

    show()
