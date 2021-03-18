import { Component, OnInit } from '@angular/core';
import { TransacaoService } from '../transacao.service';

@Component({
  selector: 'app-transacao-lista',
  templateUrl: './transacao-lista.component.html',
  styleUrls: ['./transacao-lista.component.css']
})
export class TransacaoListaComponent implements OnInit {
  listaTransacoes: any;

  constructor(private service: TransacaoService) { }

  ngOnInit(): void {
    this.service.getTransacoes()
      .subscribe(transacoes => {
        this.listaTransacoes = transacoes;
    });
  }
  onAtualizaTransacao() {
    this.service.getTransacoes()
      .subscribe(transacoes => {
        this.listaTransacoes = transacoes;
    });
  }

}
