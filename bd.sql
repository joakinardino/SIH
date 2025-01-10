-- Script para criação do banco de dados do Sistema de Informação Hospitalar

-- Criação do banco de dados
CREATE DATABASE SistemaHospitalar;
USE SistemaHospitalar;

-- Tabela para cadastro de pacientes
CREATE TABLE Pacientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    idade INT NOT NULL,
    genero ENUM('Masculino', 'Feminino', 'Outro') NOT NULL,
    historico_medico TEXT
);

-- Tabela para cadastro de consultas
CREATE TABLE Consultas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    paciente_id INT NOT NULL,
    data_hora DATETIME NOT NULL,
    medico VARCHAR(100) NOT NULL,
    descricao TEXT,
    status ENUM('Agendada', 'Concluída', 'Cancelada') DEFAULT 'Agendada',
    FOREIGN KEY (paciente_id) REFERENCES Pacientes(id) ON DELETE CASCADE
);

-- Tabela para registro de exames
CREATE TABLE Exames (
    id INT AUTO_INCREMENT PRIMARY KEY,
    consulta_id INT NOT NULL,
    tipo_exame VARCHAR(100) NOT NULL,
    resultados TEXT,
    imagem_exame LONGBLOB,
    FOREIGN KEY (consulta_id) REFERENCES Consultas(id) ON DELETE CASCADE
);

-- Tabela para registro de médicos
CREATE TABLE Medicos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    especialidade VARCHAR(100) NOT NULL,
    contato VARCHAR(50)
);

-- Tabela para agenda de médicos
CREATE TABLE AgendaMedica (
    id INT AUTO_INCREMENT PRIMARY KEY,
    medico_id INT NOT NULL,
    data_hora DATETIME NOT NULL,
    disponibilidade ENUM('Disponível', 'Indisponível') DEFAULT 'Disponível',
    FOREIGN KEY (medico_id) REFERENCES Medicos(id) ON DELETE CASCADE
);

-- Funcionalidades adicionais: tabela de usuários para login e permissões
CREATE TABLE Usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    senha_hash VARCHAR(255) NOT NULL,
    tipo_usuario ENUM('Admin', 'Medico', 'Recepcionista') NOT NULL
);

-- Tabela para logs de atividades
CREATE TABLE LogsAtividades (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    acao VARCHAR(255) NOT NULL,
    data_hora DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES Usuarios(id) ON DELETE SET NULL
);
