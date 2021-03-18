import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Transacao } from '../shared/transacao.model';

@Injectable({
  providedIn: 'root'
})
export class TransacaoService {
  private url = 'http://127.0.0.1:5000/Transacoes/';

  constructor(private http: HttpClient) { }

  getTransacoes() {
    return this.http.get<Transacao>(this.url);
  }

  getTransacaoByID(id: number) {
    return this.http.get(this.url + id);
  }

  createTransacao(transacaoData: Transacao) {
    return this.http.post(this.url, transacaoData);
  }

  editTransacao(id: number, transacaoData: Transacao) {
    return this.http.patch(this.url + id, transacaoData);
  }

  deleteTransacao(id: number) {
    return this.http.delete(this.url + id);
  }
}
