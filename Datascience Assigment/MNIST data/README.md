# MNIST to MNIST-M

The `Blobs-DANN.ipynb` shows some basic experiments on a very simple dataset. The `MNIST-DANN.ipynb` recreates the MNIST experiment from the papers on a synthetic dataset. Instructions to generate the synthetic dataset are below.

Requires TensorFlow>=1.0 and tested with Python 2.7 and Python 3.4.


## MNIST Experiments

The `MNIST-DANN.ipynb` notebook implements the MNIST experiments for the paper with the same model and optimization parameters, including the learning rate and adaptation parameter schedules. Rough results are below (more training would likely improve results - # epochs are not reported in the paper).

| Method | Target acc (paper) | Target acc (this repo w/ 10 epochs) |
| ------ | ------------------ | ----------------------------------- |
| Source Only | 0.5225 | 0.4801 |
| DANN | 0.7666 | 0.7189 |


### Build MNIST-M dataset

The MNIST-M dataset consists of MNIST digits blended with random color patches from the [BSDS500](http://www.eecs.berkeley.edu/Research/Projects/CS/vision/grouping/resources.html#bsds500) dataset. To generate a MNIST-M dataset, first download the BSDS500 dataset and run the `create_mnistm.py` script:

```bash
curl -L -O http://www.eecs.berkeley.edu/Research/Projects/CS/vision/grouping/BSR/BSR_bsds500.tgz
python create_mnistm.py
```

This may take a couple minutes and should result in a `mnistm_data.pkl` file containing generated images.


