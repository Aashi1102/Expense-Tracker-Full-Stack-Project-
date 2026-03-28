-- Create and use database
CREATE DATABASE IF NOT EXISTS expense_manager;
USE expense_manager;

-- Create expenses table
CREATE TABLE IF NOT EXISTS expenses (
id INT AUTO_INCREMENT PRIMARY KEY,
expense_date DATE NOT NULL,
amount DECIMAL(10,2) NOT NULL,
category VARCHAR(50) NOT NULL,
notes VARCHAR(255),
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Index for faster queries
CREATE INDEX idx_expense_date ON expenses(expense_date);
