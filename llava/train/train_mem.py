# from llava.train.train import train
from train_full_finetuning import train

if __name__ == "__main__":
    # train(attn_implementation="flash_attention_2")
    train()
