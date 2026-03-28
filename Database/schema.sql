-- Use your existing database
CREATE DATABASE IF NOT EXISTS expense_manager;
USE expense_manager;

-- Create expenses table (same as your current structure)
CREATE TABLE IF NOT EXISTS expenses (
id INT AUTO_INCREMENT PRIMARY KEY,
expense_date DATE NOT NULL,
amount INT NOT NULL,
category VARCHAR(50) NOT NULL,
notes VARCHAR(255)
);

-- Index for faster date filtering
CREATE INDEX idx_expense_date ON expenses(expense_date);
