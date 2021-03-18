import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';
import { EstadoCivilService } from '../../shared/services/estado-civil.service';
import { ActivatedRoute } from '@angular/router';
import { Observable } from 'rxjs';
import { tap } from 'rxjs/operators';
import { ProprietarioService } from '../proprietario.service';

@Component({
  selector: 'app-proprietario-edit',
  templateUrl: './proprietario-edit.component.html',
  styleUrls: ['./proprietario-edit.component.css']
})
export class ProprietarioEditComponent implements OnInit {
  editForm: any;
  lista_estadocivil: any;
  mensagem = '';
  mensagemErro = '';
  proprietario: Observable<any>;
  id = this.route.snapshot.params['id'];

  constructor(private serviceProprietario: ProprietarioService,
              private serviceEcivil: EstadoCivilService,
              private route: ActivatedRoute) {
    this.proprietario = new Observable();
  }

  ngOnInit(): void {
    this.editForm = new FormGroup({
      nome: new FormControl(),
      cpf: new FormControl(),
      rg: new FormControl(),
      data_nascimento: new FormControl(),
      profissao: new FormControl(),
      celular: new FormControl(),
      telefone: new FormControl(),
      email: new FormControl(),
      estado_civil_id: new FormControl()
    });
    this.proprietario = this.serviceProprietario.getProprietarioByID(this.id)
      .pipe(tap(proprietario => this.editForm.patchValue(proprietario)));
    this.serviceEcivil.getEstadoCivil()
      .subscribe(estadoCivilData => {
        this.lista_estadocivil = estadoCivilData;
      });
  }
  onSubmit() {
    this.mensagem = '';
    this.mensagemErro = '';
    this.serviceProprietario.editProprietario(this.id, this.editForm.value)
      .subscribe(returnData => {
      console.log(returnData);
      this.mensagem = 'Proprietário editado com sucesso!';
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
