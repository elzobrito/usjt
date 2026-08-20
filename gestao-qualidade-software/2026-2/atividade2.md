Atividade 2 — Caça ao defeito: quem encontra o bug que passou pelo teste?
Situação

Vocês fazem parte da equipe de qualidade responsável por liberar uma pequena página para produção.
'''
<!DOCTYPE html>
<html>
<head>
  <style>
    h1.titulo { color: #0b6e4f; }
    label + select { width: 280px; }
    #periodo { color: #0b6e4f; }
  </style>
</head>
<body>
  <h1 class="Titulo">Consulta de escolas</h1>

  <label for="regional">Núcleo Regional</label>
  <span>
    <select id="regional">
      <option>Escolha</option>
    </select>
  </span>

  <label for="periodo">Período</label>
  <select id="período">
    <option>Escolha</option>
  </select>
</body>
</html>
