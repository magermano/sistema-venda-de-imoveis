import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { ProprietarioService } from '../proprietario.service';
import { EstadoCivilService } from '../../shared/services/estado-civil.service';

@Component({
  selector: 'app-proprietario-novo',
  templateUrl: './proprietario-novo.component.html',
  styleUrls: ['./proprietario-novo.component.css']
})
export class ProprietarioNovoComponent implements OnInit {
  proprietarioForm: any;
  lista_estadocivil: any;
  mensagem = '';
  mensagemErro = '';

  constructor(private serviceProprietario: ProprietarioService,
              private serviceEcivil: EstadoCivilService) { }

  ngOnInit(): void {
    this.proprietarioForm = new FormGroup({
      nome: new FormControl(null, Validators.required),
      cpf: new FormControl(null, Validators.required),
      rg: new FormControl(null, Validators.required),
      data_nascimento: new FormControl(null, Validators.required),
      profissao: new FormControl(null, Validators.required),
      celular: new FormControl(null, Validators.required),
      telefone: new FormControl(null),
      email: new FormControl(null, [Validators.required, Validators.email]),
      estado_civil_id: new FormControl(1)
    });
    this.serviceEcivil.getEstadoCivil()
      .subscribe(estadoCivilData => {
        this.lista_estadocivil = estadoCivilData;
      });
  }

  onSubmit() {
    this.mensagem = '';
    this.mensagemErro = '';
    this.serviceProprietario.createProprietario(this.proprietarioForm.value)
      .subscribe(returnData => {
      console.log(returnData);
      this.mensagem = 'Proprietário adicionado com sucesso!';
    }, error => {
        this.mensagemErro = error.name;
      }
    );
    this.proprietarioForm.reset();
  }

  onClearError() {
    this.mensagem = '';
    this.mensagemErro = '';
  }
}
