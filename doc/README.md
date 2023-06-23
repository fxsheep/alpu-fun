# ALPU-M reverse engineering notes

## Gathered information
 - https://neowine.com/theme/a03/ko/ALPU-MP.php
 
 Datasheet tells us the pinout and silght internals of the chip.
 
 - https://tw.mitscomponent.com/news_detail_69.htm
 
 This chip is actually called ALPU-MP (I2C interface). There is also a ALPU-M1 variant that uses onewire protocol.
 
 - https://github.com/wondermedia/wm8850/blob/master/ANDROID_3.0.8/drivers/char/wmt-alpu/s_wmt_alpu.c
 
 Some code implementing `Bypass mode` mentioned in the datasheet.

## Discovered/Implemented features
 - Bypass mode
 A mode used for communication test between host and ALPU-MP. With operation mode/sub-address 0x80, write no more than 8 bytes, then read back result of the same length. Output is input XORed with 0x01.

