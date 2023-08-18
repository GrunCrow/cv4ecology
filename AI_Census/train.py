from ultralytics import YOLO
from constants import *
# pip install comet_ml
import comet_ml

comet_ml.init()

# Create a new YOLO model from scratch
model = YOLO(MODEL_NAME)

# Load a pretrained YOLO model (recommended for training)
model = YOLO(MODEL_WEIGHTS)

# Train the model using the 'coco128.yaml' dataset for 3 epochs
results = model.train(data=DATASET_YAML, 
                      epochs = 200,                   # number of epochs to train for
                      patience = 40,                # epochs to wait for no observable improvement for early stopping of training
                      batch = 32,                   # number of images per batch (-1 for AutoBatch)
                      save = True,                  # save train checkpoints and predict results
                      device = 0,                   # device to run on, i.e. cuda device=0 or device=0,1,2,3 or device=cpu
                      #workers = 8,                  # number of worker threads for data loading (per RANK if DDP)
                      project = "AI_Census/Trainings",       # project name
                      name = "first_training",      # experiment name
                      # exist_ok = False,           # whether to overwrite existing experiment
                      pretrained = True,            # whether to use a pretrained model
                      optimizer = 'auto',           # optimizer to use, choices=[SGD, Adam, Adamax, AdamW, NAdam, RAdam, RMSProp, auto]
                      verbose = True,               # whether to print verbose output
                      seed = 42,	                # random seed for reproducibility
                      resume = RESUME,	            # resume training from last checkpoint

                      #cache = False,                # True/ram, disk or False. Use cache for data loading  
                      #deterministic = True,	        # whether to enable deterministic mode
                      #single_cls = False,	        # train multi-class data as single-class
                      #rect = False,	                # rectangular training with each batch collated for minimum padding
                      #cos_lr = False,	            # use cosine learning rate scheduler
                      #close_mosaic = 10,	        # (int) disable mosaic augmentation for final epochs (0 to disable)
                      #amp = True,	                # Automatic Mixed Precision (AMP) training, choices=[True, False]
                      #fraction = 1.0,	            # dataset fraction to train on (default is 1.0, all images in train set)
                      #profile = False,	            # profile ONNX and TensorRT speeds during training for loggers
                      #freeze = None,	            # (int or list, optional) freeze first n layers, or freeze list of layer indices during training
                      #lr0 = 0.01,	                # initial learning rate (i.e. SGD=1E-2, Adam=1E-3)
                      #lrf = 0.01,	                # final learning rate (lr0 * lrf)
                      #momentum = 0.937,	            # SGD momentum/Adam beta1
                      #weight_decay = 0.0005,	    # optimizer weight decay 5e-4
                      #warmup_epochs = 3.0,	        # warmup epochs (fractions ok)
                      #warmup_momentum = 0.8,	    # warmup initial momentum
                      #warmup_bias_lr = 0.1,	        # warmup initial bias lr
                      #box = 7.5,	                # box loss gain
                      #cls = 0.5,	                # cls loss gain (scale with pixels)
                      #dfl = 1.5,	                # dfl loss gain
                      #pose = 12.0,	                # pose loss gain (pose-only)
                      #kobj = 2.0,	                # keypoint obj loss gain (pose-only)
                      #label_smoothing = 0.0,	    # label smoothing (fraction)
                      #nbs = 64,	                    # nominal batch size
                      #overlap_mask = True,	        # masks should overlap during training (segment train only)
                      #mask_ratio = 4,	            # mask downsample ratio (segment train only)
                      #dropout = 0.0,	            # use dropout regularization (classify train only)
                      val = True	                # validate/test during training  
                      )

# Evaluate the model's performance on the validation set
results = model.val()

# Perform object detection on an image using the model
# results = model('https://ultralytics.com/images/bus.jpg')

# Export the model to ONNX format
success = model.export(format='onnx')