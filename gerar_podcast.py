from gtts import gTTS

# Texto do podcast
podcast_text = """
[Introdução]

Olá, bem-vindos ao podcast "Futuro IoT: Inovações Conectadas". Eu sou [Seu Nome], e hoje vamos explorar as incríveis inovações que a Internet das Coisas, ou IoT, está trazendo para nossos lares. A IoT está transformando nossos ambientes residenciais em espaços mais inteligentes, eficientes e conectados. Vamos descobrir como isso acontece!

[Inovações em Iluminação Inteligente]

Um dos avanços mais populares da IoT são as lâmpadas inteligentes. Com elas, você pode controlar a iluminação da sua casa diretamente do seu smartphone ou até mesmo com comandos de voz. Imagine poder ajustar a iluminação do seu quarto sem sair da cama!

[Termostatos Inteligentes]

Outra inovação revolucionária são os termostatos inteligentes. Eles permitem que você ajuste a temperatura da sua casa de forma automática e remota, economizando energia e aumentando o conforto. Pense em chegar em casa num dia frio e encontrar o ambiente já aquecido!

[Segurança Residencial Inteligente]

Os sistemas de segurança inteligentes são outra aplicação fantástica da IoT. Câmeras, sensores de movimento e fechaduras inteligentes podem ser monitorados e controlados remotamente, aumentando a segurança da sua casa. É como ter uma vigilância 24/7 ao alcance do seu telefone.

[Eletrodomésticos Inteligentes]

Eletrodomésticos como geladeiras, máquinas de lavar e aspiradores de pó estão ficando mais inteligentes. Eles podem ser controlados remotamente, oferecendo conveniência e eficiência no uso diário. Imagine poder iniciar a máquina de lavar enquanto você ainda está no trabalho!

[Assistentes Virtuais]

Por último, mas não menos importante, temos os assistentes virtuais como Alexa, Google Assistant e Siri. Eles se conectam a vários dispositivos IoT da sua casa, permitindo que você os controle com comandos de voz simples. Você pode pedir para ligar as luzes, ajustar a temperatura ou até mesmo tocar sua música favorita, tudo com um simples comando de voz.

[Conclusão]

E isso é tudo por hoje no "Futuro IoT: Inovações Conectadas". Esperamos que você tenha gostado de aprender sobre as principais inovações da IoT em nossos lares e como elas estão facilitando nossas vidas. Se você quer ver exemplos de como isso tudo funciona em termos de código, visite nosso site [ou blog/repositório GitHub] onde postamos todos os detalhes técnicos. Fique ligado para mais episódios sobre como a tecnologia está moldando nosso futuro. Até a próxima!
"""

# Gerar o áudio do podcast
tts = gTTS(podcast_text, lang='pt')
tts.save("../Audios/futuro_iot_podcast.mp3")

print("Arquivo MP3 gerado com sucesso: futuro_iot_podcast.mp3")
