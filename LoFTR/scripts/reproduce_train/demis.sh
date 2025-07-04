#!/bin/bash -l

# DEMIS training execution script.
# 
# Project: Deep Electron Microscopy Image Stitching (DEMIS)
# Author: Petr Šilling
# Year: 2023

SCRIPTPATH=$(dirname $(readlink -f "$0"))
PROJECT_DIR="${SCRIPTPATH}/../../"

# conda activate demis
export PYTHONPATH=$PROJECT_DIR:$PYTHONPATH
cd $PROJECT_DIR

data_cfg_path="configs/data/demis_trainval.py"
main_cfg_path="configs/loftr/demis/loftr_demis_dense.py"
ckpt_path="weights/outdoor_ds.ckpt"

n_nodes=1
n_gpus_per_node=2
torch_num_workers=8
batch_size=2
pin_memory=true
exp_name="demis-bs=$(($n_gpus_per_node * $n_nodes * $batch_size))"

python -u ./train.py \
    ${data_cfg_path} \
    ${main_cfg_path} \
    --exp_name=${exp_name} \
    --gpus=${n_gpus_per_node} --num_nodes=${n_nodes} --accelerator="ddp" \
    --batch_size=${batch_size} --num_workers=${torch_num_workers} --pin_memory=${pin_memory} \
    --ckpt_path ${ckpt_path} \
    --check_val_every_n_epoch=1 \
    --log_every_n_steps=1 \
    --flush_logs_every_n_steps=1 \
    --limit_val_batches=1. \
    --num_sanity_val_steps=10 \
    --benchmark=True \
    --max_epochs=10
