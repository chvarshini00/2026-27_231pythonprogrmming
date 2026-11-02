# Tuple-Based Route Distance Analysis

## 1. Problem Statement

Develop a Python program to perform route distance analysis using tuples. Store the geographical coordinates (latitude and longitude) of multiple locations as tuples.

The program should calculate the distance between successive geographical points using the supplied Euclidean distance formula and identify the longest route segment.

The program must perform the following operations:

1. Store geographical coordinates as tuples.
2. Accept the number of geographical locations.
3. Read the latitude and longitude of each location.
4. Calculate the distance between successive locations.
5. Use the Euclidean distance formula:

\\[ d=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2} \\]

6. Identify the longest distance between successive locations.
7. Display all route segments and their distances.
8. Display the longest route segment.

Note: This program uses Euclidean distance on the supplied coordinate values, not actual road distance or geographical distance in kilometres.

## 2. Algorithm

1. Start the program.
2. Import the `math` module.
3. Read the number of geographical locations.
4. Initialize an empty list to store coordinate tuples.
5. Read the latitude and longitude of each location.
6. Store each coordinate as a tuple `(latitude, longitude)`.
7. Initialize the maximum distance to zero.
8. Repeat for every pair of successive locations:
   - Extract the coordinates of the current location.
   - Extract the coordinates of the next location.
   - Calculate the distance using the Euclidean distance formula.
   - Display the distance between the two locations.
   - Compare the calculated distance with the maximum distance.
   - Update the maximum distance if necessary.
9. Display the longest route segment and its distance.
10. Stop the program.


## 5. Sample Input

```
===== ROUTE DISTANCE ANALYSIS =====

Enter number of locations: 5

Enter coordinates for Location 1
Enter latitude: 10
Enter longitude: 20

Enter coordinates for Location 2
Enter latitude: 13
Enter longitude: 24

Enter coordinates for Location 3
Enter latitude: 16
Enter longitude: 28

Enter coordinates for Location 4
Enter latitude: 20
Enter longitude: 30

Enter coordinates for Location 5
Enter latitude: 25
Enter longitude: 35
```

## 6. Sample Output

```
===== ROUTE DISTANCE ANALYSIS =====

========== ROUTE SEGMENT DISTANCES ==========

Location 1 to Location 2 : 5.0
Location 2 to Location 3 : 5.0
Location 3 to Location 4 : 4.47
Location 4 to Location 5 : 7.07

Stored Coordinate Tuples:

Location 1 : (10.0, 20.0)
Location 2 : (13.0, 24.0)
Location 3 : (16.0, 28.0)
Location 4 : (20.0, 30.0)
Location 5 : (25.0, 35.0)

========== LONGEST ROUTE SEGMENT ==========

Longest Segment: Location 4 to Location 5
Maximum Distance: 7.07

Route analysis completed.
```

## 7. Calculation

The Euclidean distance formula is:

\\[ d=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2} \\]

Example: Location 1 to Location 2

Coordinates:

- Location 1 = (10, 20)
- Location 2 = (13, 24)

Substituting the values:

\\[ d=\sqrt{(13-10)^2+(24-20)^2} \\]

\\[ d=\sqrt{3^2+4^2} \\]

\\[ d=\sqrt{9+16} \\]

\\[ d=\sqrt{25}=5 \\]

Therefore, the distance is 5.00 units.

| Route segment           | Distance |
| ----------------------- | -------- |
| Location 1 → Location 2 | 5.00     |
| Location 2 → Location 3 | 5.00     |
| Location 3 → Location 4 | 4.47     |
| Location 4 → Location 5 | 7.07     |



Longest segment

&#x20;Location 4 → Location 5 = 7.07 units



## 8. Mermaid Flowchart Code
``` mermaid

flowchart TD
    A([Start]) --> B[Import math module]
    B --> C[/Enter number of locations/]
    C --> D[Initialize empty coordinate list]
    D --> E[/Input latitude and longitude/]
    E --> F[Store coordinates as tuple]
    F --> G{More locations?}

    G -- Yes --> E
    G -- No --> H{Number of locations >= 2?}

    H -- No --> I[Display insufficient locations]
    I --> Z([Stop])

    H -- Yes --> J[Initialize maximum distance = 0]
    J --> K[Select two successive coordinate tuples]
    K --> L[Extract latitude and longitude]
    L --> M[Calculate Euclidean distance]
    M --> N[Display segment distance]
    N --> O{Distance > maximum distance?}

    O -- Yes --> P[Update maximum distance and segment]
    O -- No --> Q{More route segments?}
    P --> Q

    Q -- Yes --> K
    Q -- No --> R[Display all coordinate tuples]
    R --> S[Display longest route segment]
    S --> T[Display maximum distance]
    T --> U[Display completion message]
    U --> Z
mermaid


```



## 9. Result

The Python program successfully stores geographical coordinates using tuples, calculates distances between successive locations using the Euclidean distance formula, and identifies the longest route segment.

In the given sample, the longest route segment is Location 4 to Location 5, with a distance of 7.07 units.
