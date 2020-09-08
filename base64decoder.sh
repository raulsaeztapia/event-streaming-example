#!/bin/bash

base64 -d base64-float.binary | od -A n --endian=big -tfF --width=52