import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { TransacaoService } from '../transacao.service';
import { ProprietarioService } from '../../proprietario/proprietario.service';
import { ClienteService } from '../../cliente/cliente.service';
import { ImovelService } from '../../imovel/imovel.service';
import { BancoService } from '../../shared/services/banco.service';

@Component({
  selector: 'app-transacao-novo',
  templateUrl: './transacao-novo.component.html',
  styleUrls: ['./transacao-novo.component.css']
})
export class TransacaoNovoComponent implements OnInit {
  transacaoForm: any;
  mensagem = '';
  mensagemErro = '';
  lista_proprietario: any;
  lista_cliente: any;
  lista_imovel: any;
  lista_banco: any;
  lista_financiamento = ['À Vista', 'Financiado'];

  constructor(private serviceTransacao: TransacaoService,
              private serviceProprietario: ProprietarioService,
              private serviceCliente: ClienteService,
              private serviceImovel: ImovelService,
              private serviceBanco: BancoService) { }

  ngOnInit(): void {
    this.transacaoForm = new FormGroup({
      valor: new FormControl(null, Validators.required),
      financiamento: new FormControl(null, Validators.required),
      proprietario: new FormControl(null, Validators.required),
      cliente: new FormControl(null, Validators.required),
      banco: new FormControl(null),
      imovel: new FormControl(null, Validators.required),
      data_transacao: new FormControl(null),
    });
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
    this.serviceTransacao.createTransacao(this.transacaoForm.value)
      .subscribe(returnData => {
      console.log(returnData);
      this.mensagem = 'Transação adicionada com sucesso!';
    }, error => {
        this.mensagemErro = error.name;
      }
    );
    this.transacaoForm.reset();
  }

  onClearError() {
    this.mensagem = '';
    this.mensagemErro = '';
  }
}
