salarieDictionary = {
    "Nombre": ["Juan", "Elena", "Santiago", "Fernando", "Miriam", "Julio"],
    "Edad" : [29,27,23,35,28,30],
    "Salario" : [18000,25000,28000,10500,21000,27000],
    "Genero" : ["M","F","M","M","F","M"]
}

employeeSalaries = salarieDictionary["Salario"][:]
maxSalary = max(employeeSalaries)
minSalary = min(employeeSalaries)
salaryDifference = maxSalary - minSalary

print("El salario mas alto es: " , maxSalary,  "El salario mas bajo es: ", minSalary)
print("La diferencia entre salarios es de: ", salaryDifference)