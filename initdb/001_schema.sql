-- Exemplo de script inicial
CREATE TABLE IF NOT EXISTS public.example (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  created_at TIMESTAMPTZ DEFAULT now()
);
