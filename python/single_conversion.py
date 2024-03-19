import torch
import os
from TTS.api import TTS

curr_folder = os.path.dirname(os.path.realpath(__file__))

tts = TTS(
        model_name="tts_models/multilingual/multi-dataset/xtts_v2", progress_bar=True
    ).to("cuda")

tts.tts_to_file(
            "Essa conexão permite o acesso a diversos recursos, como artigos científicos e bases de dados que normalmente requerem uma subscrição. Também é possível fazer upload de arquivos para seu espaço de hospedagem web usando uma conexão SFTP segura. Para imprimir documentos nos laboratórios do CIn de seu computador pessoal, você também precisará estar conectado à VPN.",
            speaker_wav=f"{curr_folder}/voicein/sim1009.ogg",
            language="pt",
            file_path=f"{curr_folder}/voiceout/_cenaw7.wav")