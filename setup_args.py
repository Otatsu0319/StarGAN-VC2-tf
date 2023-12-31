import datetime
class Args:
    def __init__(self):
        self.mixed_precision = True
        self.use_tpu = False
        self.num_workers = 8

        self.dataset_t_length = 256
        self.dataset_hop_size = 64
        self.mcep_size = 36
        self.code_size = 4
        self.frame_period = 5.0 # ms
        self.fft_size = 1024
        self.crop_size = 256 # = dataset_t_length
        self.target_sr = 22050

        # self.using_jvs_id_m = ["jvs009", "jvs020", "jvs028", "jvs041"]
        self.using_jvs_id_m = ["jvs009", "jvs020"]
        # self.using_jvs_id_f = ["jvs002", "jvs010", "jvs058", "jvs036"]
        self.using_jvs_id_f = ["jvs002", "jvs010"]
        self.train_data_ratio = 0.70
        self.preset_datafile_ratio = 0.5
        self.remake_datasets = True
        self.shuffle_buffer_Size = 100

        self.repeat_num = 1
        self.iterations = 3*(10**5) // self.repeat_num
        self.train_batch_size = 8
        self.test_batch_size = 16
        self.logging_interval = 1000 // self.repeat_num
        self.sample_interval = 5000 // self.repeat_num
        self.checkpoint_interval = 1000 // self.repeat_num
        self.print_log = False

        self.g_learn_rate = 0.0002
        self.d_learn_rate = 0.0001
        self.momentum = 0.5

        self.lambda_cyc = 10.0
        self.lambda_id = 5.0
        self.lambda_cls = 1.0
        self.id_rate = 10**4 // self.repeat_num

        self.model_name = "stargan_vc2"

        self.tensorboard_log_dir = "logs"
        self.save_profile = True

        self.restore_bool = False
        if self.restore_bool:
            self.start_iteration = 13000
            self.datetime = "20221121-093359"
            
            if self.id_rate <= self.start_iteration:
                self.lambda_id = 0.0
                print("change lambda id")
        else:
            self.start_iteration = 0
            now = datetime.datetime.utcnow() + datetime.timedelta(hours=9)
            self.datetime = now.strftime("%Y%m%d-%H%M%S")

        self.set_seed = True
        self.seed = 2050

if __name__ == "__main__":
    args = Args()
    print(args.__dict__)