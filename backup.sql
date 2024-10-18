drop schema if exists talentotech;
create schema talentotech;
DROP TABLE IF EXISTS `usuarios`;
CREATE TABLE `usuarios` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `edad` bigint(20) DEFAULT NULL,
  `estado` tinyint(4) NOT NULL DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE = InnoDB AUTO_INCREMENT = 4 DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_uca1400_ai_ci;
INSERT INTO `usuarios` (`id`, `Nombre`, `email`, `edad`, `estado`)
VALUES (1, 'Andres', 'andres@test.com', 24, 0),
  (2, 'Juan', 'juan@test.co', 25, 1),
  (3, 'Felipe', 'felipe@test.co', 23, 1);