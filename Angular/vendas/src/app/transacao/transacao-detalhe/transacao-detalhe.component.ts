import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Params, Router } from '@angular/router';
import { TransacaoService } from '../transacao.service';

@Component({
  selector: 'app-transacao-detalhe',
  templateUrl: './transacao-detalhe.component.html',
  styleUrls: ['./transacao-detalhe.component.css']
})
export class TransacaoDetalheComponent implements OnInit {
  isExclusao = false;
  transacao: any;
  id = this.route.snapshot.params['id'];
  mensagemErro = '';

  constructor(private service: TransacaoService,
              private route: ActivatedRoute,
              private router: Router) { }

  ngOnInit(): void {
  this.service.getTransacaoByID(this.id)
      .subscribe(transacao => {
        this.transacao = transacao;
      });
  this.route.params
      .subscribe((params: Params) => {
        this.id = params['id'];
        this.service.getTransacaoByID(this.id)
      .subscribe(transacao => {
        this.transacao = transacao;
      });
      });
  }

  onDelete() {
    this.mensagemErro = '';
    this.service.deleteTransacao(this.id).subscribe(transacao => {
      console.log(transacao);
      this.router.navigate(['transacoes']);
    },
      error => {
      this.mensagemErro = error.name;
      });
  }

  onEdit() {
    this.router.navigate(['transacoes', 'edit', this.id]);
  }

  onPerguntar() {
    this.isExclusao = true;
  }

  onRetornar() {
    this.isExclusao = false;
  }

  onClearError() {
    this.mensagemErro = '';
  }

}
