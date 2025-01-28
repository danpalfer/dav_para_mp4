# Conversor de Arquivos DAV para MP4

Este projeto é um aplicativo simples desenvolvido em Python que converte arquivos de vídeo no formato `.DAV` (geralmente utilizados em sistemas de câmeras de segurança) para o formato `.MP4`, que é amplamente compatível com a maioria dos dispositivos e players de vídeo.

## Funcionalidades

- Permite selecionar o arquivo `.DAV` a ser convertido.
- Permite escolher o local de salvamento do arquivo `.MP4` convertido.
- Interface gráfica simples e amigável usando `tkinter`.
- Integração com a biblioteca VLC para realizar a conversão.
- Mensagens claras de erro e sucesso.
- O botão de conversão exibe o estado durante o processo.

## Pré-requisitos

Antes de executar o script, certifique-se de que os seguintes requisitos estão atendidos:

1. **Python 3.6 ou superior** instalado no sistema.
2. **Bibliotecas Python necessárias**:
   - `vlc`
   - `tkinter` (já incluso no Python por padrão)
3. **VLC Media Player** instalado no computador:
   - Certifique-se de que o VLC está corretamente configurado e que a biblioteca `python-vlc` pode acessá-lo.

### Instalando as dependências

Para instalar as dependências necessárias, use o seguinte comando:

```bash
pip install python-vlc
