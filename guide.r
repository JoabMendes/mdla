##Attribution
a <- 2 #Evything is a vector

is.vector(a) #verifies id a is a vector TRUE

#Joining two vectors

x <- 2
z <- 4

a <- c(x, z) # a = [2, 4]

#Range

rang <- 1:50

#Data frames, matrices and lists

#Dataframes are like tables, with coluns and rows.
#R has some ready data frames for testing
#They are like matrices but with mixed data type (numerical, factor [multivalored], string)

#Matrices are like data frames but only accept one data type. If we convert iris to a matrix
#it will convert all data frames elements to a strings.
#Iris is a native data frame for testing
as.matrix(iris)

#List are are arrays of ordered objects

list.ex <- list(name="Alice", age=40, children.at=c(22,24,25))
list.ex #Givinf the list object
$name #Accessing elements of a list many times in console
#[1] "Alice"
$age
#[1] 40
$children.at
#[1] 22 24 25
list.ex[[3]] #Also workds as list.ex$children.at

#Accessing and extracting data

#Accessing Dataframes clumns names:
colnames(iris)
#rows
rownames(iris)

#Can be accessed by indexes

iris[1,1]

#Indexes and column names

iris[1,"Sepal.Length"]
iris["fleur d ✬ iris n. 1","Sepal.Length"]
iris$Sepal.Length[1]

#Packages/Libraries
#http://cran.r-project.org/src/contrib/PACKAGES.html

install.packages("package_name")

#Column binding
a <- cbind(1,2,4)
b <- cbind(3, 5, 6)
#Row binding
c <- rbind(a,b)

#table(iris$Species) #Count the occurence for every specie on the dataframw
#apply()

install.packages("RColorBrewer") #applies color to plots
install.packages("TraMineR") #Downloads the library
