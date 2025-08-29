# Cradle-Care
Final Bachelor Project - Biomedical Engineering - Bio Electric - Cradle care with Raspberry Pi 5


## Tree of Project

Cradle-Care/
│
├── local_media/
│   ├── images/
│   ├── gif/
│   └── video/
│
├── sensor/
│   ├── __init__.py
│   ├── microphone.py
│   ├── dht22.py
│   ├── mlx90614.py
│   └── camera.py
│
├── config/
│   ├── sensors.yaml
│   ├── paths.yaml
│   └── system.yaml
│
├── logs/
│   ├── main/
│   │   └── main.log
│   ├── setup/
│   │   └── setup.log
│   ├── microphone/
│   │   └── microphone.log
│   ├── dht22/
│   │   └── dht22.log
│   ├── mlx90614/
│   │   └── mlx90614.log
│   └── camera/
│       └── camera.log
│
├── data/
│   ├── audio/
│   ├── camera/
│   ├── dht22/
│   ├── mlx90614/
│   └── fusion/
│
├── AI/
│   ├── audio_processing/
│   ├── camera_processing/
│   ├── dht22_processing/
│   ├── mlx90614_processing/
│   ├── fusion/
│   └── utils/
│
├── tests/
│   ├── test_main.py
│   ├── test_setup.py
│   ├── test_microphone.py
│   ├── test_dht22.py
│   ├── test_mlx90614.py
│   └── test_camera.py
│
├── main.py
├── requirements.txt
├── README.md
├── LICENSE
├── TODO.md
└── setup.sh

