CREATE TABLE Person(
	Email VARCHAR(30),
    Named VARCHAR(25),
    Dob DATE,
    Phone VARCHAR(10),
    Address VARCHAR(30),
    PRIMARY KEY(Email));

CREATE TABLE Customer(
	CustomerID INT,
    Username VARCHAR(20),
    Userpass VARCHAR(20),
    PRIMARY KEY(CustomerID));
    
CREATE TABLE Employee(
	EmployeeID INT,
    DateJoined DATE,
    PRIMARY KEY(EmployeeID),
    FOREIGN KEY(Supervisor) REFERENCES Employee(EmployeeID));
                
CREATE TABLE Item(
	ItemID INT,
	Price DEC(6,2),
	ItemType VARCHAR(15),
	Seller VARCHAR(15),
	PRIMARY KEY(ItemID),
	FOREIGN KEY(Inventory) REFERENCES Inventory(ItemType));

CREATE TABLE Inventory(
	Named VARCHAR(15),
	Quantity INT,
	Seller VARCHAR(15),
	ItemType VARCHAR(15),
	PRIMARY KEY(ItemType));

CREATE TABLE ShoppingCart(
	PRIMARY KEY(CustomerID, ItemID),
	FOREIGN KEY(CustomerID) REFERENCES Customer(CustomerID),
	FOREIGN KEY(ItemID) REFERENCES Item(ItemID));

CREATE TABLE WishList(
	PRIMARY KEY(CustomerID, ItemID),
	FOREIGN KEY(CustomerID) REFERENCES Customer(CustomerID),
	FOREIGN KEY(ItemID) REFERENCES Item(ItemID));
                                      
CREATE TABLE Orders(
	OrderNum INT,
    OrderDate DATE,
    Completed CHAR(1),
    PRIMARY KEY(OrderNum),
    CHECK (Completed IN('Y', 'N')));
    
CREATE TABLE REVIEWS(
	Ratings INT,
	PRIMARY KEY(OrderID),
	FOREIGN KEY(CustomerID) REFERENCES Customer(CustomerID),
	FOREIGN KEY(OrderID) REFERENCES Orders(OrderNum));