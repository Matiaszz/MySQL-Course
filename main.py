'''
CREATE TABLE base_de_dados.users (
    id INT UNSIGNED auto_increment NOT NULL,
    first_name varchar(100) NOT NULL,
    last_name varchar(100) NULL,
    email varchar(255) NOT NULL,
    password_hash varchar(255) NOT NULL,
    CONSTRAINT users_pk PRIMARY KEY (id),
    CONSTRAINT users_un_email UNIQUE KEY (email),
    CONSTRAINT users_un_password_hash UNIQUE KEY (password_hash)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_unicode_ci;

esse é o codigo gerado para a tabela users que eu criei manualmente


CONSTRAINT = Restrições
'''
