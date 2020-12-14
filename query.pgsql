SELECT employees.name, projects.proj_name, employees_projects.role
FROM employees
JOIN employees_projects
ON employees.id = employees_projects.emp_id
JOIN projects
ON projects.proj_code = employees_projects.proj_code;