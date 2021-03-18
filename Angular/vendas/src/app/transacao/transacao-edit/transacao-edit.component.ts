import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { TransacaoService } from '../transacao.service';
import { ProprietarioService } from '../../proprietario/proprietario.service';
import { ClienteService } from '../../cliente/cliente.service';
import { ImovelService } from '../../imovel/imovel.service';
import { BancoService } from '../../shared/services/banco.service';
import { ActivatedRoute } from '@angular/router';
import { Observable } from 'rxjs';
import { tap } from 'rxjs/operators';

@Component({
  selector: 'app-transacao-edit',
  templateUrl: './transacao-edit.component.html',
  styleUrls: ['./transacao-edit.component.css']
})
export class TransacaoEditComponent implements OnInit {
  editForm: any;
  lista_proprietario: any;
  lista_cliente: any;
  lista_imovel: any;
  lista_banco: any;
  lista_financiamento = ['À Vista', 'Financiado'];
  mensagem = '';
  mensagemErro = '';
  transacao: Observable<any>;
  id = this.route.snapshot.params['id'];

  constructor(private serviceTransacao: TransacaoService,
              private serviceProprietario: ProprietarioService,
              private serviceCliente: ClienteService,
              private serviceImovel: ImovelService,
              private serviceBanco: BancoService,
              private route: ActivatedRoute) {
    this.transacao = new Observable();
  }

  ngOnInit(): void {
    this.editForm = new FormGroup({
      valor: new FormControl(null),
      financiamento: new FormControl(null),
      proprietario: new FormControl(null),
      cliente: new FormControl(null),
      banco: new FormControl(null),
      imovel: new FormControl(null),
      data_transacao: new FormControl(null),
    });
    this.transacao = this.serviceTransacao.getTransacaoByID(this.id)
      .pipe(tap(transacao => this.editForm.patchValue(transacao)));
    this.serviceProprietario.getProprietarios()
      .subscribe(proprietarioData => {
        this.lista_proprietario = proprietarioData;
      });
    this.serviceCliente.getClientes()
      .subscribe(clienteData => {
        this.lista_cliente = clienteData;
      });
    this.serviceImovel.getAll()
      .subscribe(imovelData => {
        this.lista_imovel = imovelData;
      });
    this.serviceBanco.getBancos()
      .subscribe(bancoData => {
        this.lista_banco = bancoData;
      });
  }

  onSubmit() {
    this.mensagem = '';
    this.mensagemErro = '';
    this.serviceTransacao.editTransacao(this.id, this.editForm.value)
      .subscribe(returnData => {
      console.log(returnData);
      this.mensagem = 'Transação editada com sucesso!';
    }, error => {
        this.mensagemErro = error.name;
      }
    );
  }

  onClearError() {
    this.mensagem = '';
    this.mensagemErro = '';
  }
}
