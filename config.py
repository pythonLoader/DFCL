import os

def set_config(args):

    args.output_path = os.path.join(os.getcwd(),"output")

    args.sparse_comm = False 
    args.client_sparsity = 0.3
    args.server_sparsity = 0.3 

    args.model ='dfcl'
    args.base_network = 'lenet' 
    
    # adaptive learning rate
    args.lr_patience = 3
    args.lr_factor = 3
    args.lr_min = 1e-10

    # base network hyperparams
    if args.base_network == 'lenet':
        args.lr = 1e-3/3
        args.wd = 1e-4

    if 'dfcl' in args.model:
        args.wd = 1e-4
        args.lambda_l1 = 1e-3
        args.lambda_l2 = 100.
        args.lambda_mask = 0

    return args

def set_data_config(args):

    args.task_path = os.path.join(os.getcwd(),"task")
    
    # CIFAR10(0), CIFAR100(1), MNIST(2), SVHN(3),
    # F-MNIST((4), TrafficSign(5), FaceScrub(6), N-MNIST(7)
    
    # CIFAR100(0), MNIST(1), F-MNIST(2), SVHN(3), TrafficSign(4)


    if args.task in ['non_iid_50'] :
        args.datasets    = [0, 1, 2, 3, 4]
        args.num_clients = 3
        args.num_tasks   = 10 
        args.num_classes = 5
        args.frac_clients = 1.0
    
    else:
        print('no correct task was given: {}'.format(args.task))
    
    return  args
