export interface Proprietario {
  nome?: string;
  cpf?: string;
  rg?: string;
  data_nascimento?: string;
  profissao?: string;
  celular?: string;
  telefone?: string;
  email?: string;
  estado_civil_id?: number;
  estado_civil?: string
  id?: number;
  enderecos?: [];
  imoveis?: [];
}
