# MPU 6050

Using the MPU 6050  Gyroscope / Accelerator sensor board with a rasperry pi using i2c.


## Pins

| Raspberry Pi | MPU 6050 |
|--------------|----------|
| Pin 1 (3.3V) | VCC      |
| Pin 3 (SDA)  | SDA      |
| Pin 5 (SCL)  | SCL      |
| Pin 6 (GND)  | GND      |

## Modules

Ensure these modules are loaded:


* i2c-bcm2708
* i2c-dev

Install i2c-tools 

```
$ sudo apt-get install i2c-tools
```

## i2cdetect 

```
thys@navio:~ $ sudo i2cdetect -y 1
[sudo] password for thys: 
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- -- 
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
60: -- -- -- -- -- -- -- -- 68 -- -- -- -- -- -- -- 
70: -- -- -- -- -- -- -- --                         

```

# mpu-650.py

```
{
    "gyro": {
        "y": -211, 
        "x": -592, 
        "z": -147
    }, 
    "rotation": {
        "y": 18.58245664915674, 
        "x": 12.841702233893653
    }, 
    "accelleration": {
        "z_scaled": 0.8330078125, 
        "y_scaled": 0.200927734375, 
        "y": 3292, 
        "x": -4720, 
        "z": 13648, 
        "x_scaled": -0.2880859375
    }
}
{
    "gyro": {
        "y": -247, 
        "x": -622, 
        "z": -111
    }, 
    "rotation": {
        "y": 18.86977712270345, 
        "x": 12.861078737945162
    }, 
    "accelleration": {
        "z_scaled": 0.826171875, 
        "y_scaled": 0.199951171875, 
        "y": 3276, 
        "x": -4760, 
        "z": 13536, 
        "x_scaled": -0.29052734375
    }
}
```
