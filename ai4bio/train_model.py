import os
import json
import argparse
from datetime import datetime 



def set_flags_description(desc):
    parser = argparse.ArgumentParser(desc)
    parser.add_argument('--project_name',type=str)
    parser.add_argument('--my_data_ready_dir', type=str)
    parser.add_argument('--seed',type=int)
    parser.add_argument('--training_inference_mode',type=str)
    parser.add_argument('--debug_mode',action='store_true')

    partial_args, _ = parser.parse_known_args()
    if partial_args.training_inference_mode =='training':
        config_training_path = 'ai4bio/config.json'
        parser = add_args_from_config(parser,config_training_path)


    return parser

def all_setup(args):
    args.experiment_dir='Experiment_RUNS_BY_Projects'
    args.experiment_dir_by_project = os.path.join(args.experiment_dir,args.project_name)
    timestamp_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    run_id=f'run_timestamp_{timestamp_str}'
    args = folder_setup(run_id,args)
    return args


def folder_setup(run_id,args):
    # Create the necessary directories for the experiment
    print('setting folder')
    ckpt_folder=os.path.join(args.experiment_dir_by_project,'CHECKPOINTS')
    
    checkpoint_dir= os.path.join(ckpt_folder,run_id)
    args.data_path='DATA'
    args.data_path_by_choice = os.path.join('DATA',  args.my_data_ready_dir)
    args.checkpoint_dir = checkpoint_dir

    folders =[ args.experiment_dir, 
            args.experiment_dir_by_project, 
            ckpt_folder,checkpoint_dir,
            args.data_path,
            args.data_path_by_choice]
    for p in folders:
        if os.path.exists( p) ==False:
            os.mkdir(p)       

    return args

def add_args_from_config(parser, config_path):
    """ 
    Adds command line arguments to the parser based on a configuration file.
    """

    type_map = {
                "str": str,
                "int": int,
                "float": float,
                "bool": bool
            }
    with open(config_path) as f:
        config_dict = json.load(f)

    for arg, options in config_dict.items():
        kwargs = {}

        if "action" in options:
            kwargs["action"] = options["action"]
        else:
            kwargs["type"] = type_map[options["type"]]

        if "choices" in options:
            kwargs["choices"] = options["choices"]
        if "help" in options:
            kwargs["help"] = options["help"]
        if "default" in options:
            kwargs["default"] = options["default"]

        parser.add_argument(f'--{arg}', **kwargs)

    return parser



def main():
    parser=set_flags_description("unit-test-config-system")
    args = parser.parse_args()
    args = all_setup(args)
    # save config by run
    path_to_save_args=os.path.join(args.checkpoint_dir,'args_logs.json')
    with open(path_to_save_args,'w') as f:
        json.dump(vars(args), f, indent=2)

if __name__=='__main__':
    main()