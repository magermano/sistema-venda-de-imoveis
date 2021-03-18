import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { ClienteComponent } from './cliente/cliente.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { CategoriaComponent } from './categoria/categoria.component';
import { ClienteListaComponent } from './cliente/cliente-lista/cliente-lista.component';
import { ClienteDetalheComponent } from './cliente/cliente-detalhe/cliente-detalhe.component';
import { ProprietarioComponent } from './proprietario/proprietario.component';
import { ProprietarioListaComponent } from './proprietario/proprietario-lista/proprietario-lista.component';
import { ProprietarioDetalheComponent } from './proprietario/proprietario-detalhe/proprietario-detalhe.component';
import { ImovelComponent } from './imovel/imovel.component';
import { ImovelListaComponent } from './imovel/imovel-lista/imovel-lista.component';
import { ImovelDetalheComponent } from './imovel/imovel-detalhe/imovel-detalhe.component';
import { HomeComponent } from './home/home.component';
import { TransacaoComponent } from './transacao/transacao.component';
import { TransacaoListaComponent } from './transacao/transacao-lista/transacao-lista.component';
import { TransacaoDetalheComponent } from './transacao/transacao-detalhe/transacao-detalhe.component';
import { PageNotFoundComponent } from './page-not-found/page-not-found.component';
import { AppRoutingModule } from './app-routing.module';
import { ClienteNovoComponent } from './cliente/cliente-novo/cliente-novo.component';
import { EnderecoComponent } from './endereco/endereco.component';
import { ClienteEditComponent } from './cliente/cliente-edit/cliente-edit.component';
import { ProprietarioEditComponent } from './proprietario/proprietario-edit/proprietario-edit.component';
import { ProprietarioNovoComponent } from './proprietario/proprietario-novo/proprietario-novo.component';
import { ImovelNovoComponent } from './imovel/imovel-novo/imovel-novo.component';
import { ImovelEditComponent } from './imovel/imovel-edit/imovel-edit.component';
import { TransacaoNovoComponent } from './transacao/transacao-novo/transacao-novo.component';
import { TransacaoEditComponent } from './transacao/transacao-edit/transacao-edit.component';

@NgModule({
  declarations: [
    AppComponent,
    ClienteComponent,
    CategoriaComponent,
    ClienteListaComponent,
    ClienteDetalheComponent,
    ProprietarioComponent,
    ProprietarioListaComponent,
    ProprietarioDetalheComponent,
    ImovelComponent,
    ImovelListaComponent,
    ImovelDetalheComponent,
    HomeComponent,
    TransacaoComponent,
    TransacaoListaComponent,
    TransacaoDetalheComponent,
    PageNotFoundComponent,
    ClienteNovoComponent,
    EnderecoComponent,
    ClienteEditComponent,
    ProprietarioEditComponent,
    ProprietarioNovoComponent,
    ImovelNovoComponent,
    ImovelEditComponent,
    TransacaoNovoComponent,
    TransacaoEditComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,
    ReactiveFormsModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
