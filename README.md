# AI4Bio 
Note: this is only a user experience survey repo. Core funcationalities are not accessible here.

## Prerequisite (St.Jude user specific minimum)
1. OnDemand related:
    - know how to start a VSCode session with GPU environment 
    - know how to upload/download files to/from St.Jude HPC through OnDemand
2. VSCode related:
    - know where to start a terminal session
    - know how to click to find and open the right file in a specific folder through VSCode interface
    - know how to select the right environment kernel on jupyter notebook
3. Terminal command line related:
    - know the common command line such as ```cd```,```ls``` to the required directory level
    - know how to copy-paste command to terminal and hit run

## Installation (St.Jude user specific)
1. Go to [St.Jude OnDemand](https://svlpondemand02.stjude.org/pun/sys/dashboard) and start a VSCode session with GPU access

2. Clone the repository by copy the following command to your terminal and hit enter
```sh
git clone https://github.com/mb-group/ai4bio_experience_test.git
```
and get inside the folder by
```sh
cd ai4bio_experience_test
```

3. Load conda utility by 
```sh
module load conda3/202402
```

4. Create the environment by
```sh
conda env create -f environment.yaml
```

5. Activate the environment by
```sh
conda activate ai4bio_test
```

## Train a model
Assuming you have finished model design through AI4Bio web portal, the following code is automatically generated for you. Copy to terminal in activated environment
```sh
python ai4bio/train_model.py --project_name="project_name_x" --my_data_ready_dir="my_data_i" --seed=666 --training_inference_mode="training" --lr=99
```

## Examine trained results
See what new files are generated under ```Experiment_RUNS_BY_Projects/```

## Post-analysis
