#== importacoes
import asyncio
import time
import httpx
#django
from django.http import HttpResponse, JsonResponse

#== funcoes
def api(requisicao):
    #espera
    time.sleep(1)
    #resposta http
    conteudo = {'mensagem': 'Ola mundo!'}
    #validacao se possui tarefas
    if 'id_tarefa' in requisicao.GET:
        conteudo['id_tarefa'] = requisicao.GET['id_tarefa']
    #retorno
    return JsonResponse(conteudo)

def chamada_http_sinc():
    #loop
    for i in range(1,6):
        #espera por 1 segundo
        time.sleep(1)
        print(i)
    #espera resposta web
    r = httpx.get('https://httpbin.org')
    print(r)
        
def visao_sinc(requisicao):
    #executa uma tarefa
    chamada_http_sinc()
    #retorno
    return HttpResponse('Chamada HTTP bloqueante!')

#assincronos
async def chamada_http_asinc():
    #loop
    for i in range(1,6):
        #espera por 1 segundo assincronicamente
        await asyncio.sleep(1)
        print(i)
    #cria cliente assincrono do httpx
    async with httpx.AsyncClient() as cliente:
        #espera resposta web
        r = await cliente.get('https://httpbin.org')
        print(r)
        
async def visao_asinc(requisicao):
    #cria um manipulador de evento assincronos
    loop = asyncio.get_event_loop()
    #executa uma tarefa
    loop.create_task(chamada_http_asinc())
    #retorno
    return HttpResponse('Chamada HTTP nao-bloqueante!')