import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {HomeComponent} from './home/home.component';
import {ClienteComponent} from './cliente/cliente.component';
import {ProprietarioComponent} from './proprietario/proprietario.component';
import {ImovelComponent} from './imovel/imovel.component';
import {TransacaoComponent} from './transacao/transacao.component';
import {PageNotFoundComponent} from './page-not-found/page-not-found.component';
import {ClienteDetalheComponent} from './cliente/cliente-detalhe/cliente-detalhe.component';
import {ClienteNovoComponent} from './cliente/cliente-novo/cliente-novo.component';
import {ClienteEditComponent} from './cliente/cliente-edit/cliente-edit.component';
import {ProprietarioNovoComponent} from './proprietario/proprietario-novo/proprietario-novo.component';
import {ProprietarioEditComponent} from './proprietario/proprietario-edit/proprietario-edit.component';
import {ProprietarioDetalheComponent} from './proprietario/proprietario-detalhe/proprietario-detalhe.component';
import {ImovelNovoComponent} from './imovel/imovel-novo/imovel-novo.component';
import {ImovelEditComponent} from './imovel/imovel-edit/imovel-edit.component';
import {ImovelDetalheComponent} from './imovel/imovel-detalhe/imovel-detalhe.component';
import {TransacaoNovoComponent} from "./transacao/transacao-novo/transacao-novo.component";
import {TransacaoEditComponent} from "./transacao/transacao-edit/transacao-edit.component";
import {TransacaoDetalheComponent} from "./transacao/transacao-detalhe/transacao-detalhe.component";

const routes: Routes = [
  { path: '', component: HomeComponent},
  { path: 'clientes', component: ClienteComponent, children: [
    { path: 'novo', component: ClienteNovoComponent},
    { path: 'edit/:id', component: ClienteEditComponent},
    { path: ':id', component: ClienteDetalheComponent}
    ]},
  { path: 'proprietarios', component: ProprietarioComponent, children: [
    { path: 'novo', component: ProprietarioNovoComponent},
    { path: 'edit/:id', component: ProprietarioEditComponent},
    { path: ':id', component: ProprietarioDetalheComponent}
    ]},
  { path: 'imoveis', component: ImovelComponent, children: [
    { path: 'novo', component: ImovelNovoComponent},
    { path: 'edit/:id', component: ImovelEditComponent},
    { path: ':id', component: ImovelDetalheComponent}
    ]},
  { path: 'transacoes', component: TransacaoComponent, children: [
    { path: 'novo', component: TransacaoNovoComponent},
    { path: 'edit/:id', component: TransacaoEditComponent},
    { path: ':id', component: TransacaoDetalheComponent}
    ]},
  { path: '**', component: PageNotFoundComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
