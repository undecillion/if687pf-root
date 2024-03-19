import torch
import os
from TTS.api import TTS


def get_script_directory():
    return os.path.dirname(os.path.realpath(__file__))


def create_tuples_from_file(file_name):
    file_path = os.path.join(get_script_directory(), file_name)

    with open(file_path, "r") as file:
        lines = file.readlines()

    tuples = [(line.strip(), f"voice_line_{i}_") for i, line in enumerate(lines)]
    return tuples


current_scene = 8

file_name_in = "cena" + str(current_scene) + ".txt"

curr_folder = get_script_directory()
os.makedirs(
    os.path.join(curr_folder, "voiceout", "cena" + str(current_scene)), exist_ok=True
)

tuples = create_tuples_from_file(file_name_in)


def write_tuples_to_file(tuples, file_name):
    file_path = os.path.join(
        get_script_directory(),
        "voiceout",
        "cena" + str(current_scene),
        file_name_in + "_tuples.txt",
    )

    with open(file_path, "w") as file:
        for line, file_name in tuples:
            file.write(f"{line}\t{file_name}\n")


def convert_tuples_to_voice(tuples):
    tts = TTS(
        model_name="tts_models/multilingual/multi-dataset/xtts_v2", progress_bar=True
    ).to("cuda")
    for line, file_name in tuples:
        tts.tts_to_file(
            line,
            speaker_wav=f"{curr_folder}/voicein/sim1009.ogg",
            language="pt",
            file_path=f"{curr_folder}/voiceout/cena{current_scene}/{file_name}cena{current_scene}.wav",
        )

write_tuples_to_file(tuples, file_name_in)
convert_tuples_to_voice(tuples)
